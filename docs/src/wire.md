# Wire format

A frame is a **33-byte header** followed by a payload of up to 65535 bytes.

| Offset | Size | Field |
|---|---|---|
| 0 | 4 | magic `0xB44E3100` |
| 4 | 1 | version (`1`, the only accepted one) |
| 5 | 1 | frame type |
| 6 | 2 | payload length (little endian, u16) |
| 8 | 16 | session id |
| 24 | 4 | sequence number (little endian, u32) |
| 28 | 1 | flags |
| 29 | 4 | header HMAC (first 4 bytes of SHA-256) |

## Flags

| Flag | Value | Meaning |
|---|---|---|
| `FLAG_ACK` | `0x01` | the frame acknowledges another sequence |
| `FLAG_ENCRYPTED` | `0x02` | payload is `[u64 counter][ciphertext][16B tag]` |
| `FLAG_COMPRESSED` | `0x04` | payload is `[u32 original_len][deflate]` |

## Limits, and why they are loud

- A payload larger than 65535 bytes **panics** instead of being truncated: the
  length field is a `u16` and a truncated length desynchronises every receiver.
- A frame sealed with AEAD that would exceed the wire limit is refused, never
  split silently.
- A compressed frame is inflated only when asked: `from_bytes` keeps
  payload == wire bytes so a relay can forward a frame it cannot read.

## Encryption

`FLAG_ENCRYPTED` means the payload is
`[u64 little-endian counter][ciphertext][16-byte Poly1305 tag]`, produced with
ChaCha20-Poly1305 (RFC 8439).

- The nonce is derived from the magic, the sequence number and the counter;
  it never travels on the wire.
- The counter must advance by one per frame: a repeated or rolled-back counter
  is a **replay** and is refused.
- The authenticated data is the 29-byte routing header. Changing the session
  id, the type, the sequence or the flags after sealing breaks the tag, so
  routing itself is authenticated.
- The 4-byte header HMAC is a cheap routing check, not the security boundary.

## Control and bulk

Frames are scheduled in three lanes: control, data and bulk. Control frames
(handshake, ACK, heartbeat, downgrade) always take the control lane regardless
of size, so an ACK never waits behind a bulk backlog. `b4n1-net demo` measures
this on your machine instead of quoting a number.

## Credit

The receiver owns the credit: it grants bytes, the sender reserves them before
transmitting, and an ACK releases them. Over-sending fails with an explicit
backpressure error rather than queueing without bound.
