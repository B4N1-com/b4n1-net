# Introduction

b4n1-net is the connectivity layer of the B4N1 ecosystem. It moves **binary
frames** instead of HTTP requests: a 33-byte header, an optional AEAD payload,
receiver-driven credit and a priority scheduler that keeps the control plane
out of the bulk queue.

## What it is

- A **library** (`rlib`) that other components link at compile time: the P2P
  transport, the browser bridge and generated code all sit on top of it.
- A **binary** (this one) that exposes the same stack as an executable: it can
  be the receiving point of a link, the transmitting point, or a daemon.
- **Offline-first**: the frame codec, the crypto and the scheduler never touch
  the network, so every property is testable without a peer.

## What it is not

- It is not a replacement for HTTP on the public internet. It is the protocol
  used between B4N1 components that already trust each other's identity.
- It is not a VPN and it does not traverse NAT by itself: STUN discovery and
  the relay fallback live one layer above, in the P2P transport.

## The three surfaces

| Surface | Status | What it gives you |
|---|---|---|
| Library (rlib) | available | compile-time types, zero runtime coupling |
| Binary | available | endpoints, daemon, demo, embedded manual |
| SDK wrappers | not shipped yet | thin bindings over the binary, one per language |
| Suite plugin | not shipped yet | in-process transport subscribed to the host event bus |

This manual documents the surface you are holding. Nothing here describes a
future artifact as if it already existed.
