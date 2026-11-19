"""Binary resolution for the b4n1-net SDK."""

import os
import platform
import subprocess
import sys
from pathlib import Path
from typing import Optional

_PLATFORM_BINARIES = {
    ("linux", "x86_64"): "b4n1net-linux-amd64",
    ("linux", "aarch64"): "b4n1net-linux-arm64",
    ("linux", "x86"): "b4n1net-linux-ia32",
    ("linux", "i686"): "b4n1net-linux-ia32",
    ("darwin", "x86_64"): "b4n1net-macos-x64",
    ("darwin", "arm64"): "b4n1net-macos-arm64",
    ("windows", "AMD64"): "b4n1net-windows-amd64.exe",
}


def _get_platform_binary_name() -> Optional[str]:
    key = (sys.platform, platform.machine())
    return _PLATFORM_BINARIES.get(key)


def get_b4n1net_binary() -> Optional[str]:
    """Resolve the b4n1-net binary path.

    Resolution order:
    1. B4N1NET_BIN_PATH env var (exact path, wins)
    2. Bundled binary in bin/ (matches current platform)
    3. B4N1NET_BINARY env var
    4. Common install locations + PATH
    """
    if "B4N1NET_BIN_PATH" in os.environ:
        env_path = os.environ["B4N1NET_BIN_PATH"]
        if os.path.exists(env_path) and os.access(env_path, os.X_OK):
            return env_path

    bin_name = _get_platform_binary_name()
    if bin_name:
        bundled = Path(__file__).parent / "bin" / bin_name
        if bundled.exists() and os.access(bundled, os.X_OK):
            return str(bundled)

    env_binary = os.getenv("B4N1NET_BINARY")
    if env_binary and os.path.isfile(env_binary) and os.access(env_binary, os.X_OK):
        return env_binary

    possible = [
        str(Path.home() / ".local/bin/b4n1net"),
        str(Path.home() / ".b4n1net/bin/b4n1net"),
        "/usr/local/bin/b4n1net",
        "/usr/bin/b4n1net",
    ]
    for d in os.environ.get("PATH", "").split(":"):
        possible.append(os.path.join(d, "b4n1net"))

    for loc in possible:
        if os.path.isfile(loc) and os.access(loc, os.X_OK):
            return loc

    return None


def get_b4n1net_version() -> Optional[str]:
    """Get the version of the resolved b4n1-net binary."""
    binary = get_b4n1net_binary()
    if not binary:
        return None
    try:
        result = subprocess.run(
            [binary, "--version"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        return result.stdout.strip() or result.stderr.strip()
    except Exception:
        return None


def run(*args, **kwargs):
    """Run the b4n1-net binary with the given arguments.

    Returns a subprocess.CompletedProcess. Raises RuntimeError if the
    binary cannot be resolved.
    """
    binary = get_b4n1net_binary()
    if not binary:
        raise RuntimeError(
            "b4n1-net binary not found. Set B4N1NET_BIN_PATH or install "
            "the binary. See: https://github.com/B4N1-com/b4n1-net"
        )
    return subprocess.run([binary] + list(args), **kwargs)