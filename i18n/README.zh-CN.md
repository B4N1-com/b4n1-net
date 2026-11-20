<p align="center">
  <img src="b4n1net_presentation.png" alt="B4N1 Net — Sovereign transport. Sealed frames. Zero trust." width="100%" />
</p>

<div align="center">

# 📦 b4n1-net

**主权运输。带有 HMAC、AEAD 和确认的密封 UDP 帧 — 一个本机核心、六个 SDK 包装器。没有第三方代理，没有云依赖，没有遥测。**

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

## 📦 安装 — 6 个注册表，1 个核心

| 登记处 | 语言 | 包裹 | 命令 |
|----------|----------|---------|---------|
| **PyPI** | Python 3.10+ | `b4n1-net` | `pip install b4n1-net` |
| **npm** | Node.js | `b4n1-net` | `npm install b4n1-net` |
| **NuGet** | .NET / C# | `B4n1Net` | `dotnet add package B4n1Net` |
| **红宝石** | 红宝石 | `b4n1net` | `gem install b4n1net` |
| **包装师** | PHP 8.1+ | `b4n1/b4n1-net` | `composer require b4n1/b4n1-net` |
| **去** | 去1.21+ | `b4n1-net/sdks/go` | `go get github.com/B4N1-com/b4n1-net/sdks/go` |

所有六个软件包都提供**相同的本机核心**（预编译，无需编译器）。 SDK 是生成捆绑二进制文件的薄包装器。

---

## 🚀 快速入门

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

## ⚙️配置

SDK 自动解析本机二进制文件。使用环境变量覆盖：

```bash
export B4N1NET_BIN_PATH=/path/to/b4n1net-linux-amd64
```

---

## 🖥 平台支持

| 平台 | 架构 |
|----------|---------------|
| **Linux** | x86_64 |

其他平台（macOS、Windows）的预编译二进制文件将作为后续跟踪。

---

## 📄 许可证

商业源许可证 1.1 — 请参阅 [许可证](LICENSE) 和 [EULA.txt](EULA.txt)。