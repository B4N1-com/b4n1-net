# b4n1-net PHP SDK

Sovereign transport — thin PHP wrapper around the bundled `b4n1net` engine.

## Install

```bash
composer require b4n1/b4n1-net
```

## Quick start

```php
<?php
require __DIR__ . '/vendor/autoload.php';

use B4n1Net\Client;

$client = new Client();
echo $client->version(), PHP_EOL;
echo $client->demo(), PHP_EOL;   // real sealed round trip over loopback
```

## What you get

| Call | Purpose |
|---|---|
| `version()` | Engine banner |
| `status($json)` | Running state; "not running" is a valid answer |
| `demo()` | Offline demonstration with live numbers |
| `docs($section)` | Bundled manual, no network |
| `licenses()` | Full license text, no key required |
| `serve / send / start / stop` | The transport verbs |

## Override the engine

```bash
B4N1NET_BIN_PATH=/opt/b4n1net php app.php
```

## License

Business Source License 1.1 (BUSL-1.1) for this wrapper. Engine binaries are
covered by `EULA.txt`.
