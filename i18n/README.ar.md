<p align="center">
  <img src="b4n1net_presentation.png" alt="B4N1 Net — Sovereign transport. Sealed frames. Zero trust." width="100%" />
</p>

<div align="center">

# 📦 b4n1-net

** النقل السيادي. إطارات UDP مختومة مع HMAC وAEAD وإقرارات الإقرار - مركز أساسي واحد وستة أغلفة SDK. لا يوجد وسيط خارجي، لا يوجد اعتماد على السحابة، لا يوجد قياس عن بعد.**

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

## 📦 التثبيت — 6 سجلات، 1 نواة

| التسجيل | لغة | طَرد | يأمر |
|----------|----------|---------|---------|
| **بايبي** | بايثون 3.10+ | `b4n1-net` | `pip install b4n1-net` |
| **نبم** | Node.js | `b4n1-net` | `npm install b4n1-net` |
| ** نوجيت ** | صافي / سي # | `B4n1Net` | `dotnet add package B4n1Net` |
| **جواهر الياقوت** | روبي | `b4n1net` | `gem install b4n1net` |
| **باكاجيست** | بي إتش بي 8.1+ | `b4n1/b4n1-net` | `composer require b4n1/b4n1-net` |
| **يذهب** | الذهاب 1.21+ | `b4n1-net/sdks/go` | `go get github.com/B4N1-com/b4n1-net/sdks/go` |

جميع الحزم الست تشحن ** نفس النواة الأصلية ** (مترجمة مسبقًا، لا حاجة إلى مترجم). إن حزم SDK عبارة عن أغلفة رفيعة تنتج الملف الثنائي المجمع.

---

## 🚀 بداية سريعة

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

## ⚙️ التكوين

يقوم SDK بحل الملف الثنائي الأصلي تلقائيًا. التجاوز باستخدام متغير البيئة:

```bash
export B4N1NET_BIN_PATH=/path/to/b4n1net-linux-amd64
```

---

## 🖥 دعم المنصة

| منصة | أبنية |
|----------|---------------|
| **لينكس** | x86_64 |

يتم تعقب الثنائيات المجمعة مسبقًا لمنصات إضافية (macOS وWindows) كمتابعة.

---

## 📄 الترخيص

ترخيص مصدر الأعمال 1.1 - راجع [الترخيص](LICENSE) و[EULA.txt](EULA.txt).