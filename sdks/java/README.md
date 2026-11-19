# b4n1-net Java SDK

Sovereign transport — thin Java wrapper around the bundled `b4n1net` engine.

## Install

```xml
<dependency>
  <groupId>com.b4n1</groupId>
  <artifactId>b4n1-net</artifactId>
  <version>0.4.0</version>
</dependency>
```

## Quick start

```java
import com.b4n1.net.NetClient;

public class App {
    public static void main(String[] args) {
        NetClient client = new NetClient();
        System.out.println(client.version());
        System.out.println(client.demo());   // real sealed round trip over loopback
    }
}
```

## What you get

| Call | Purpose |
|---|---|
| `version()` | Engine banner |
| `status(boolean json)` | Running state; "not running" is a valid answer |
| `demo()` | Offline demonstration with live numbers |
| `docs(String section)` | Bundled manual, no network |
| `licenses()` | Full license text, no key required |
| `serve / send / start / stop` | The transport verbs |

## Override the engine

```bash
B4N1NET_BIN_PATH=/opt/b4n1net java -jar app.jar
```

## License

Business Source License 1.1 (BUSL-1.1) for this wrapper. Engine binaries are
covered by `EULA.txt`.
