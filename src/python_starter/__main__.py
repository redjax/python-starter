from __future__ import annotations

from python_starter import say_hi
from python_starter.core import AppSettings
from python_starter.system_info import get_os_type, get_processor, py_ver
from python_starter.utils.ex_utils import join_lists

import snoop

@snoop(depth=2)
def demo():
    print(say_hi())

    settings: AppSettings = AppSettings()

    print(f"Settings: {settings}")

    print(f"OS type: {get_os_type()}")
    print(f"Processor: {get_processor()}")
    print(f"Python version: {py_ver()}")

    print(
        f"Joined list: {join_lists(['test', 'test2', 'test3'], ['test4', 5, 'test6'])}"
    )


if __name__ == "__main__":
    demo()
