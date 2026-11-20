<p align="center">
  <img src="b4n1net_presentation.png" alt="B4N1 Net — Sovereign transport. Sealed frames. Zero trust." width="100%" />
</p>

<div align="center">

# 📦 b4n1-net

**주권 운송. HMAC, AEAD 및 승인이 포함된 봉인된 UDP 프레임 - 기본 코어 1개, SDK 래퍼 6개. 타사 브로커, 클라우드 종속성, 원격 측정이 없습니다.**

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

## 📦 설치 — 레지스트리 6개, 코어 1개

| 기재 | 언어 | 패키지 | 명령 |
|----------|----------|---------|---------|
| **PyPI** | 파이썬 3.10+ | `b4n1-net` | `pip install b4n1-net` |
| **npm** | Node.js | `b4n1-net` | `npm install b4n1-net` |
| **누겟** | .NET/C# | `B4n1Net` | `dotnet add package B4n1Net` |
| **RubyGems** | 루비 | `b4n1net` | `gem install b4n1net` |
| **패키지 담당자** | PHP 8.1+ | `b4n1/b4n1-net` | `composer require b4n1/b4n1-net` |
| **가다** | 1.21+로 이동 | `b4n1-net/sdks/go` | `go get github.com/B4N1-com/b4n1-net/sdks/go` |

6개 패키지 모두 **동일한 기본 코어**를 제공합니다(사전 컴파일되어 컴파일러가 필요하지 않음). SDK는 번들 바이너리를 생성하는 씬 래퍼입니다.

---

## 🚀 빠른 시작

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

## ⚙️ 구성

SDK는 기본 바이너리를 자동으로 확인합니다. 환경 변수로 재정의합니다.

```bash
export B4N1NET_BIN_PATH=/path/to/b4n1net-linux-amd64
```

---

## 🖥 플랫폼 지원

| 플랫폼 | 아키텍처 |
|----------|---------------|
| **리눅스** | x86_64 |

추가 플랫폼(macOS, Windows)용으로 미리 컴파일된 바이너리는 후속 조치로 추적됩니다.

---

## 📄 라이선스

비즈니스 소스 라이선스 1.1 - [LICENSE] 참조](LICENSE) 그리고 [EULA.txt](EULA.txt).