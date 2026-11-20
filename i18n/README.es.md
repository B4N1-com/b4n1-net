<p align="center">
  <img src="b4n1net_presentation.png" alt="B4N1 Net — Sovereign transport. Sealed frames. Zero trust." width="100%" />
</p>

<div align="center">

# 📦 b4n1-net

**Transporte soberano. Marcos UDP sellados con HMAC, AEAD y reconocimientos: un núcleo nativo, seis contenedores SDK. Sin intermediarios externos, sin dependencia de la nube, sin telemetría.**

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

## 📦 Instalación: 6 registros, 1 núcleo

| Registro | Idioma | Paquete | Dominio |
|----------|----------|---------|---------|
| **PyPI** | Pitón 3.10+ | `b4n1-net` | `pip install b4n1-net` |
| **npm** | Nodo.js | `b4n1-net` | `npm install b4n1-net` |
| **NuGet** | .NET/C# | `B4n1Net` | `dotnet add package B4n1Net` |
| **RubíGemas** | Rubí | `b4n1net` | `gem install b4n1net` |
| **Empaquetador** | PHP 8.1+ | `b4n1/b4n1-net` | `composer require b4n1/b4n1-net` |
| **Ir** | Ir 1.21+ | `b4n1-net/sdks/go` | `go get github.com/B4N1-com/b4n1-net/sdks/go` |

Los seis paquetes incluyen el **mismo núcleo nativo** (precompilado, no se necesita compilador). Los SDK son envoltorios finos que generan el binario incluido.

---

## 🚀 Inicio rápido

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

## ⚙️ Configuración

El SDK resuelve el binario nativo automáticamente. Anular con una variable de entorno:

```bash
export B4N1NET_BIN_PATH=/path/to/b4n1net-linux-amd64
```

---

## 🖥 Soporte de plataforma

| Plataforma | Arquitecturas |
|----------|---------------|
| **Linux** | x86_64 |

Los binarios precompilados para plataformas adicionales (macOS, Windows) se rastrean como seguimiento.

---

## 📄 Licencia

Licencia de origen empresarial 1.1: consulte [LICENCIA](LICENSE) y [CLUF.txt](EULA.txt).