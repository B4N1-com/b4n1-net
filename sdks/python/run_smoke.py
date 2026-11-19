"""Run the Python SDK smoke tests without pytest.

The other six SDKs ship a single self-contained smoke script; Python shipped
pytest-style functions, which made its leg depend on pytest being installed.
This runner discovers the ``test_*`` functions and executes them directly, so
the leg runs on a bare interpreter (no network, no toolchain, no venv).
"""

import importlib.util
import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
MODULE = os.path.join(HERE, "b4n1net", "tests", "test_basic.py")


def load(path):
    spec = importlib.util.spec_from_file_location("b4n1net_smoke", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    sys.path.insert(0, HERE)
    module = load(MODULE)
    names = sorted(name for name in dir(module) if name.startswith("test_"))
    failed = 0
    for name in names:
        try:
            getattr(module, name)()
            print(f"  \u2713 {name}")
        except Exception:
            failed += 1
            print(f"  \u2717 {name}")
            traceback.print_exc()
    print(f"\npython SDK: {len(names) - failed} passed, {failed} failed")
    return 1 if failed or not names else 0


if __name__ == "__main__":
    sys.exit(main())
