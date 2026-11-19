# b4n1-net Ruby SDK

Sovereign transport — thin Ruby wrapper around the bundled `b4n1net` engine.

## Install

```bash
gem install b4n1net
```

## Quick start

```ruby
require "b4n1net"

client = B4n1Net::Client.new
puts client.version
puts client.demo     # real sealed round trip over loopback
```

## What you get

| Call | Purpose |
|---|---|
| `version` | Engine banner |
| `status(json: true)` | Running state; "not running" is a valid answer |
| `demo` | Offline demonstration with live numbers |
| `docs(section:)` | Bundled manual, no network |
| `licenses` | Full license text, no key required |
| `serve / send / start / stop` | The transport verbs |

## Override the engine

```bash
B4N1NET_BIN_PATH=/opt/b4n1net ruby app.rb
```

## License

Business Source License 1.1 (BUSL-1.1) for this wrapper. Engine binaries are
covered by `EULA.txt`.
