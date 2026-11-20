<p align="center">
  <img src="b4n1net_presentation.png" alt="B4N1 Net — Sovereign transport. Sealed frames. Zero trust." width="100%" />
</p>

<div align="center">

# 📦 b4n1-net

**Hoheitstransport. Versiegelte UDP-Frames mit HMAC, AEAD und Bestätigungen – ein nativer Kern, sechs SDK-Wrapper. Kein Drittanbieter-Broker, keine Cloud-Abhängigkeit, keine Telemetrie.**

[![License](https://img.shields.io/badge/license-BUSL--1.1-blue.svg)](LICENSE)
[![PyPI](https://badge.fury.io/py/b4n1-net.svg)](https://pypi.org/project/b4n1-net/)
[![npm](https://img.shields.io/npm/v/b4n1-net.svg)](https://www.npmjs.com/package/b4n1-net)
[![NuGet](https://img.shields.io/nuget/v/B4n1Net.svg)](https://www.nuget.org/packages/B4n1Net)
[![RubyGems](https://img.shields.io/gem/v/b4n1net.svg)](https://rubygems.org/gems/b4n1net)
[![Packagist](https://img.shields.io/packagist/v/b4n1/b4n1-net.svg)](https://packagist.org/packages/b4n1/b4n1-net)
[![Go Reference](https://pkg.go.dev/badge/github.com/B4N1-com/b4n1-net/sdks/go.svg)](https://pkg.go.dev/github.com/B4N1-com/b4n1-net/sdks/go)
[![Tests](https://img.shields.io/badge/tests-51%20passing-brightgreen)](https://github.com/B4N1-com/b4n1-net)

</div>

---

## 📦 Installation – 6 Register, 1 Kern

| Registrierung | Sprache | Paket | Befehl |
|----------|----------|---------|---------|
| **PyPI** | Python 3.10+ | `b4n1-net` | `pip install b4n1-net` |
| **npm** | Node.js | `b4n1-net` | `npm install b4n1-net` |
| **NuGet** | .NET / C# | `B4n1Net` | `dotnet add package B4n1Net` |
| **RubyGems** | Rubin | `b4n1net` | `gem install b4n1net` |
| **Verpacker** | PHP 8.1+ | `b4n1/b4n1-net` | `composer require b4n1/b4n1-net` |
| **Gehen** | Gehen Sie 1.21+ | `b4n1-net/sdks/go` | `go get github.com/B4N1-com/b4n1-net/sdks/go` |

Alle sechs Pakete liefern den **gleichen nativen Kern** (vorkompiliert, kein Compiler erforderlich). Die SDKs sind Thin Wrapper, die die gebündelte Binärdatei erzeugen.

---

## 🚀 Schnellstart

```python
# Python
from b4n1net import B4n1Net
net = B4n1Net()
print(net.info())
```

```javascript
// Node.js
const { B4n1Net } = require('b4n1-net');
const net = new B4n1Net();
console.log(net.info());
```

```csharp
// .NET / C#
using B4n1Net;
var net = new B4n1NetClient();
Console.WriteLine(net.Info());
```

```ruby
# Ruby
require 'b4n1net'
net = B4n1Net.new
puts net.info
```

```php
// PHP
$net = new \B4n1Net\Client();
echo $net->info();
```

```go
// Go
import b4n1net "github.com/B4N1-com/b4n1-net/sdks/go"
net := b4n1net.New()
fmt.Println(net.Info())
```

---

## ⚙️ Konfiguration

Das SDK löst die native Binärdatei automatisch auf. Mit einer Umgebungsvariablen überschreiben:

```bash
export B4N1NET_BIN_PATH=/path/to/b4n1net-linux-amd64
```

---

## 🖥 Plattformunterstützung

| Plattform | Architekturen |
|----------|---------------|
| **Linux** | x86_64 |

Als Folgemaßnahme werden vorkompilierte Binärdateien für weitere Plattformen (macOS, Windows) verfolgt.

---

## 📄 Lizenz

Business Source-Lizenz 1.1 – siehe [LIZENZ](LICENSE) und [EULA.txt](EULA.txt).