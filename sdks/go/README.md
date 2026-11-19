# b4n1-net Go SDK

Sovereign transport — thin Go wrapper around the bundled `b4n1net` engine.

## Install

```bash
go get github.com/B4N1-com/b4n1-net/sdks/go
```

## Quick start

```go
package main

import (
	"fmt"
	"log"

	net "github.com/B4N1-com/b4n1-net/sdks/go"
)

func main() {
	client, err := net.New()
	if err != nil {
		log.Fatal(err)
	}
	version, _ := client.Version()
	fmt.Println(version)

	demo, _ := client.Demo(false) // real sealed round trip over loopback
	fmt.Println(demo)
}
```

## What you get

| Call | Purpose |
|---|---|
| `Version()` | Engine banner |
| `Status(json bool)` | Running state; "not running" is a valid answer |
| `Demo()` | Offline demonstration with live numbers |
| `Docs(section)` | Bundled manual, no network |
| `Licenses()` | Full license text, no key required |
| `Serve / Send / Start / Stop` | The transport verbs |

## Override the engine

```bash
B4N1NET_BIN_PATH=/opt/b4n1net go run .
```

## License

Business Source License 1.1 (BUSL-1.1) for this wrapper. Engine binaries are
covered by `EULA.txt`.
