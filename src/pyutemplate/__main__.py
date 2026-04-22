from __future__ import annotations

import sys
from pathlib import Path
from typing import TYPE_CHECKING

import tomllib

from pyutemplate.generated.ksy.msg import Msg

if TYPE_CHECKING:
    from pyutemplate.generated.schemas.config import Config

with Path.open(sys.argv[1]) as f:
    config: Config = tomllib.load(f)
    m = Msg()
