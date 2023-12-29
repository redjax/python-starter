from __future__ import annotations

import platform
import sys

sys.path.append(".")


def get_os_type() -> str:
    return platform.system()


def py_ver() -> str:
    return platform.python_version()


def get_processor() -> str:
    return platform.machine()
