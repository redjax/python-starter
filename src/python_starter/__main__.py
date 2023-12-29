from __future__ import annotations

from dataclasses import asdict

from python_starter import say_hi
from python_starter.core import AppSettings

if __name__ == "__main__":
    print(say_hi())

    settings: AppSettings = AppSettings()

    print(f"Settings: {settings}")
