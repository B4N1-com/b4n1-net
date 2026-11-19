# b4n1-net Python SDK

Sovereign Network Layer — thin Python wrapper around the b4n1-net binary.

## Install

```bash
pip install b4n1-net
```

## Quick start

```python
from b4n1net import NetClient

client = NetClient()
print(client.version())
print(client.status())
print(client.demo())
```

## CLI

```bash
python -m b4n1net --help
python -m b4n1net install
```

## License

Business Source License 1.1 (BUSL-1.1). See LICENSE and EULA.txt.