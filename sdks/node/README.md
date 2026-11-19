# b4n1-net Node SDK

Sovereign transport — thin Node wrapper around the bundled `b4n1net` engine.

## Install

```bash
npm install b4n1-net
```

## Quick start

```js
const { NetClient } = require('b4n1-net');

const client = new NetClient();
console.log(client.version());
console.log(client.demo());     // real sealed round trip over loopback
```

## What you get

| Call | Purpose |
|---|---|
| `version()` | Engine banner |
| `status(json)` | Running state; "not running" is a valid answer |
| `demo()` | Offline demonstration with live numbers |
| `docs(section)` | Bundled manual, no network |
| `licenses()` | Full license text, no key required |
| `serve / send / start / stop` | The transport verbs |

## Override the engine

```bash
B4N1NET_BIN_PATH=/opt/b4n1net node app.js
```

## License

Business Source License 1.1 (BUSL-1.1) for this wrapper. Engine binaries are
covered by `EULA.txt`.
