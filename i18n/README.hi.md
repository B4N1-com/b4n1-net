<p align="center">
  <img src="b4n1net_presentation.png" alt="B4N1 Net — Sovereign transport. Sealed frames. Zero trust." width="100%" />
</p>

<div align="center">

# 📦 b4n1-net

**संप्रभु परिवहन। एचएमएसी, एईएडी और पावती के साथ सीलबंद यूडीपी फ्रेम - एक देशी कोर, छह एसडीके रैपर। कोई तृतीय-पक्ष ब्रोकर नहीं, कोई क्लाउड निर्भरता नहीं, कोई टेलीमेट्री नहीं।**

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

## 📦 इंस्टालेशन - 6 रजिस्ट्रियां, 1 कोर

| रजिस्ट्री | भाषा | पैकेट | आज्ञा |
|----------|----------|---------|---------|
| **पीईपीआई** | पायथन 3.10+ | `b4n1-net` | `pip install b4n1-net` |
| **एनपीएम** | नोड.जे.एस | `b4n1-net` | `npm install b4n1-net` |
| **न्यूगेट** | .नेट/सी# | `B4n1Net` | `dotnet add package B4n1Net` |
| **रूबीजेम्स** | रूबी | `b4n1net` | `gem install b4n1net` |
| **पैकेजिस्ट** | पीएचपी 8.1+ | `b4n1/b4n1-net` | `composer require b4n1/b4n1-net` |
| **जाना** | 1.21+ जाओ | `b4n1-net/sdks/go` | `go get github.com/B4N1-com/b4n1-net/sdks/go` |

सभी छह पैकेज **समान मूल कोर** (पूर्व-संकलित, किसी कंपाइलर की आवश्यकता नहीं) शिप करते हैं। एसडीके पतले रैपर होते हैं जो बंडल बाइनरी को उत्पन्न करते हैं।

---

## 🚀 त्वरित शुरुआत

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

## ⚙️विन्यास

SDK मूल बाइनरी को स्वचालित रूप से हल करता है। पर्यावरण चर के साथ ओवरराइड करें:

```bash
export B4N1NET_BIN_PATH=/path/to/b4n1net-linux-amd64
```

---

## 🖥 प्लेटफार्म समर्थन

| प्लैटफ़ॉर्म | वास्तुकला |
|----------|---------------|
| **लिनक्स** | x86_64 |

अतिरिक्त प्लेटफ़ॉर्म (macOS, Windows) के लिए पूर्व-संकलित बायनेरिज़ को अनुवर्ती के रूप में ट्रैक किया जाता है।

---

## 📄लाइसेंस

बिजनेस सोर्स लाइसेंस 1.1 - देखें [लाइसेंस](LICENSE) और [EULA.txt](EULA.txt).