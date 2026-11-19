# Daemon

`b4n1-net start` launches `b4n1-net serve` detached, with stdin closed and
stdout/stderr appended to a log file.

## State file

The child binds first and then writes a small JSON record:

```json
{ "pid": 12345, "addr": "127.0.0.1:9460", "started_at": 1763318400 }
```

`start` waits for that record before reporting success, so the address it
prints is the one the kernel assigned — including when you passed port `0`.
The file is replaced atomically (write, then rename).

- Missing file: the daemon is not running.
- Record present but the pid is gone: the record is **stale**, reported as such
  and cleaned up by the next `start` or `stop`.
- `status` always exits `0`: "not running" is a state, not an error.

## Environment

| Variable | Purpose | Default |
|---|---|---|
| `B4N1_NET_SECRET` | session secret, so it stays out of `ps` and shell history | — |
| `B4N1_NET_STATE_FILE` | state file path | temp dir |
| `B4N1_NET_LOG_FILE` | daemon log path | temp dir |

## Signals

`stop` sends SIGTERM, waits for the process to disappear, escalates to SIGKILL
only if needed, and **fails loudly** if the pid survives both. Stopping a
daemon that is not running is success: the verb is idempotent.

`stop` never assumes that `kill -0` answering means the endpoint works: a
crashed-but-not-reaped process still answers. The port is the only honest
liveness signal, which is why `start` reports the address the endpoint itself
published.

## Ports

The default is `127.0.0.1:9460`. Nothing else in the ecosystem uses it. Bind
to a specific interface when the endpoint must be reachable from another
machine:

```bash
b4n1-net start --addr 0.0.0.0:9460 --secret s3cret
```

A busy port is a loud failure (`urn:b4n1:error:net:start-failed`), not a
silent switch to another port.
