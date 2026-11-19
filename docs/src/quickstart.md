# Quickstart

Every command below works offline. No account, no network, no setup.

## Prove the protocol on this machine

```bash
b4n1-net demo
```

Three sealed frames round-trip over UDP loopback. The report shows the
measured round-trip time, the real wire cost of a frame, where a control frame
is transmitted from behind a 512-frame backlog, and how many bytes of credit
the window reserved. Nothing is quoted from a specification.

## Connect two points

Point A listens:

```bash
b4n1-net serve --addr 127.0.0.1:9460 --secret s3cret
```

Point B sends:

```bash
b4n1-net send --addr 127.0.0.1:9460 --secret s3cret --message "hola"
```

`send` seals each frame, transmits it and waits for the peer's ACK. On success
it prints the round-trip time; when no ACK arrives it prints
`urn:b4n1:error:net:no-ack` and the two causes that actually produce it (peer
not running, secret mismatch).

Both ends must use the **same** secret. It is used for the header HMAC, the
AEAD key and the session id — nothing secret travels on the wire.

## Run it as a daemon

```bash
b4n1-net start --addr 127.0.0.1:9460 --secret s3cret
b4n1-net status
b4n1-net stop
```

`start` binds first and publishes the **resolved** address, so `--addr
127.0.0.1:0` reports the port the kernel actually assigned. Use port 0 when
you do not care which port it is.

Prefer the environment over the flag for the secret, so it never appears in
`ps`:

```bash
export B4N1_NET_SECRET=s3cret
b4n1-net start --addr 127.0.0.1:9460
```

## Read the manual from the binary

```bash
b4n1-net docs --list
b4n1-net docs --section wire
```
