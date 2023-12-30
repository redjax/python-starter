from __future__ import annotations

from dataclasses import dataclass, field

from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    environments=True,
    settings_files=["settings.toml", ".secrets.toml"],
)


@dataclass
class AppSettings:
    env: str = field(default=settings.get("ENV", "prod"))
    container_env: bool = field(default=settings.get("CONTAINER_ENV", None))
    log_level: str = field(default=settings.get("LOG_LEVEL", "INFO"))

    test_secret: str = field(default=settings.get("TEST_SECRET", None))
