# Verbs

```bash
b4n1-net <verb> [flags]
```

| Verb | What it does | Needs |
|---|---|---|
| `serve` | Foreground endpoint: bind, verify, unseal, ACK | `--secret` |
| `send` | Seal frames to a peer and wait for its ACKs | `--addr`, `--secret` |
| `start` | Detached daemon (idempotent) | `--secret` |
| `stop` | Stop the daemon (idempotent) | — |
| `status` | Report pid, address and uptime | — |
| `demo` | Offline demo with live measurements | — |
| `docs` | Manual inside the binary (`--list`, `--section`) | — |
| `licenses` | Full license text | — |
| `help` | Usage | — |

`build` and `test` are project verbs, not binary verbs: a binary cannot
compile or test itself, so it does not pretend to. Use
`bash cli.sh net build` and `bash cli.sh net test`.

## Flags

| Flag | Meaning | Default |
|---|---|---|
| `--addr <ip:port>` | Endpoint address | `127.0.0.1:9460` (`send` requires it) |
| `--secret <text>` | Session secret shared by both ends | `B4N1_NET_SECRET` |
| `--vault <dir>` | Read the secret from a `b4n1-secrets` vault | `B4N1_NET_VAULT` |
| `--secret-key <id>` | Vault key holding the secret (`app/KEY`) | `B4N1_NET_SECRET_KEY` |
| `--message <text>` | Payload sent by `send` | `b4n1-net` |
| `--count <n>` | Frames sent by `send` (1..1000) | `1` |
| `--state-file <path>` | Override the daemon state file | temp dir |
| `--section <name>` | Manual section to print | — |
| `--list` | List the manual sections | — |
| `--json` | Pure JSON on stdout | off |

## Where the secret comes from

Three sources, checked in this order:

1. `--secret <text>` — a literal value.
2. `B4N1_NET_SECRET` — the same value from the environment.
3. A vault: `--vault <dir> --secret-key <app/KEY>` (or the two env vars).

```bash
b4n1-secrets init ~/.b4n1/vault            # once per machine
b4n1-secrets unlock ~/.b4n1/vault          # passphrase on stdin, key stays in RAM
b4n1-secrets set ~/.b4n1/vault b4n1-net/shared --value '<the shared secret>'

b4n1-net start --vault ~/.b4n1/vault --secret-key b4n1-net/shared
b4n1-net send  --addr 127.0.0.1:9460 --vault ~/.b4n1/vault --secret-key b4n1-net/shared
```

With a vault the daemon is handed the **key name**, not the value, and asks
the vault itself: the plaintext never enters argv, the log, or the daemon's
environment. Two sources at once is refused (`conflicting-secret-sources`)
rather than silently ranked — two answers to one question is how a link ends
up with the wrong key.

A vault source requires an unlocked vault: `vault-locked` (exit 1) means
`b4n1-secrets unlock` has not been run on this machine, and
`vault-key-missing` means the key does not exist or has expired.

## Output contract

- stdout carries the result; it is pure JSON when `--json` is passed.
- stderr carries diagnostics, notes and errors.
- Nothing depends on a terminal: `NO_COLOR=1` removes colour and decorative
  glyphs.

## Exit codes

| Code | Meaning | Example |
|---|---|---|
| `0` | Done | `demo`, `status` of a stopped daemon |
| `1` | Runtime failure | port busy, no ACK, spawn failed |
| `4` | Usage error | unknown verb or flag, missing `--secret`, bad `--addr` |

Every non-zero exit prints a typed code:

```
✗ unknown verb: frobnicate
  code: urn:b4n1:error:net:unknown-verb
  hint: run 'b4n1-net help' for the verb list
```

An unknown verb is **not** guessed at: it never silently becomes `help`. A
command that does not exist must fail, not answer something else.
