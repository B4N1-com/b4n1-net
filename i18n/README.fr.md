<p align="center">
  <img src="b4n1net_presentation.png" alt="B4N1 Net — Sovereign transport. Sealed frames. Zero trust." width="100%" />
</p>

<div align="center">

# 📦 b4n1-net

**Transport souverain. Cadres UDP scellés avec HMAC, AEAD et accusés de réception : un cœur natif, six wrappers SDK. Pas de courtier tiers, pas de dépendance au cloud, pas de télémétrie.**

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

## 📦 Installation — 6 registres, 1 cœur

| Enregistrement | Langue | Emballer | Commande |
|----------|----------|---------|---------|
| **PyPI** | Python3.10+ | `b4n1-net` | `pip install b4n1-net` |
| **npm** | Noeud.js | `b4n1-net` | `npm install b4n1-net` |
| **NuGet** | .NET/C# | `B4n1Net` | `dotnet add package B4n1Net` |
| **RubisGemmes** | Rubis | `b4n1net` | `gem install b4n1net` |
| **Emballeur** | PHP8.1+ | `b4n1/b4n1-net` | `composer require b4n1/b4n1-net` |
| **Aller** | Allez 1.21+ | `b4n1-net/sdks/go` | `go get github.com/B4N1-com/b4n1-net/sdks/go` |

Les six packages sont livrés avec le **même noyau natif** (précompilé, aucun compilateur n'est nécessaire). Les SDK sont des wrappers minces qui génèrent le binaire fourni.

---

## 🚀 Démarrage rapide

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

## ⚙️Configuration

Le SDK résout automatiquement le binaire natif. Remplacer par une variable d'environnement :

```bash
export B4N1NET_BIN_PATH=/path/to/b4n1net-linux-amd64
```

---

## 🖥 Prise en charge de la plateforme

| Plate-forme | Architectures |
|----------|---------------|
| **Linux** | x86_64 |

Les binaires précompilés pour des plates-formes supplémentaires (macOS, Windows) sont suivis à titre de suivi.

---

## 📄 Licence

Licence Business Source 1.1 — voir [LICENCE](LICENSE) et [CLUF.txt](EULA.txt).