# b4n1-net .NET SDK

Sovereign transport — thin .NET wrapper around the bundled `b4n1net` engine.

## Install

```bash
dotnet add package B4n1Net
```

## Quick start

```csharp
using B4n1Net;

var client = new NetClient();
Console.WriteLine(client.Version());
Console.WriteLine(client.Demo());   // real sealed round trip over loopback
```

## What you get

| Call | Purpose |
|---|---|
| `Version()` | Engine banner |
| `Status(json)` | Running state; "not running" is a valid answer |
| `Demo()` | Offline demonstration with live numbers |
| `Docs(section)` | Bundled manual, no network |
| `Licenses()` | Full license text, no key required |
| `Serve / Send / Start / Stop` | The transport verbs |

## Override the engine

```bash
B4N1NET_BIN_PATH=/opt/b4n1net dotnet run
```

## License

Business Source License 1.1 (BUSL-1.1) for this wrapper. Engine binaries are
covered by `EULA.txt`.
