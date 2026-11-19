"""b4n1-net SDK — Sovereign Network Layer.

Thin Python wrapper around the b4n1-net binary. The wheel bundles the engine
for the supported platforms and resolves the matching one at import time.

Overrides:
    B4N1NET_BIN_PATH=/path/to/b4n1net   exact binary, wins over the bundle
    B4N1NET_BINARY=/path/to/b4n1net     same, kept for older callers

Quick start:
    from b4n1net import NetClient

    client = NetClient()
    print(client.version())
    print(client.status())

CLI usage:
    python -m b4n1net --help
    python -m b4n1net install
"""

from .binary import (
    get_b4n1net_binary,
    get_b4n1net_version,
    run,
)

SDK_VERSION = "0.4.2"

__version__ = SDK_VERSION
__author__ = "Bani Montoya"
__email__ = "banimontoya@gmail.com"

__all__ = [
    "get_b4n1net_binary",
    "get_b4n1net_version",
    "run",
    "NetClient",
]


class NetClient:
    """High-level client wrapping the b4n1-net binary."""

    def __init__(self, binary_path: str = None):
        self._binary = binary_path or get_b4n1net_binary()
        if not self._binary:
            raise RuntimeError(
                "b4n1-net binary not found. Set B4N1NET_BIN_PATH or install "
                "the binary."
            )

    def _run(self, *args, capture=True, timeout=30):
        import subprocess

        result = subprocess.run(
            [self._binary] + list(args),
            capture_output=capture,
            text=True,
            timeout=timeout,
        )
        return result

    def version(self) -> str:
        r = self._run("--version")
        return (r.stdout or r.stderr).strip()

    def status(self, json_output=False) -> str:
        args = ["status"]
        if json_output:
            args.append("--json")
        r = self._run(*args)
        return (r.stdout or r.stderr).strip()

    def demo(self, json_output=False) -> str:
        args = ["demo"]
        if json_output:
            args.append("--json")
        r = self._run(*args)
        return (r.stdout or r.stderr).strip()

    def docs(self, section=None, list_sections=False) -> str:
        args = ["docs"]
        if list_sections:
            args.append("--list")
        elif section:
            args.extend(["--section", section])
        r = self._run(*args)
        return (r.stdout or r.stderr).strip()

    def licenses(self) -> str:
        r = self._run("licenses")
        return (r.stdout or r.stderr).strip()

    def help(self) -> str:
        r = self._run("help")
        return (r.stdout or r.stderr).strip()

    def serve(self, addr="127.0.0.1:0", secret=None, vault=None, secret_key=None, json_output=False):
        args = ["serve", "--addr", addr]
        if secret:
            args.extend(["--secret", secret])
        if vault:
            args.extend(["--vault", vault])
        if secret_key:
            args.extend(["--secret-key", secret_key])
        if json_output:
            args.append("--json")
        return self._run(*args)

    def send(self, addr, secret=None, vault=None, secret_key=None, message=None, json_output=False):
        args = ["send", "--addr", addr]
        if secret:
            args.extend(["--secret", secret])
        if vault:
            args.extend(["--vault", vault])
        if secret_key:
            args.extend(["--secret-key", secret_key])
        if message:
            args.extend(["--message", message])
        if json_output:
            args.append("--json")
        return self._run(*args)

    def start(self, addr="127.0.0.1:0", secret=None, vault=None, secret_key=None, json_output=False):
        args = ["start"]
        if addr:
            args.extend(["--addr", addr])
        if secret:
            args.extend(["--secret", secret])
        if vault:
            args.extend(["--vault", vault])
        if secret_key:
            args.extend(["--secret-key", secret_key])
        if json_output:
            args.append("--json")
        return self._run(*args)

    def stop(self, json_output=False):
        args = ["stop"]
        if json_output:
            args.append("--json")
        return self._run(*args)