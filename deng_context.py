from __future__ import annotations

import json
import os
from dotenv import load_dotenv

load_dotenv()

CONFIG_KEY = "config"


class DengConfig:
    def __init__(self):
        self.primary_profile = os.getenv("AWS_PROFILE")
        self.primary_region = os.getenv("AWS_REGION")
        self.config_dir = os.getenv("DENG_CFG_DIR")

    def prettyprint(self):
        j = json.dumps(self.__dict__, indent=3)
        print(j)

    def set_context(self, ctx):
        ctx.ensure_object(dict)
        ctx.obj[CONFIG_KEY] = self

    @classmethod
    def from_context(cls, ctx) -> DengConfig:
        cfg = ctx.obj[CONFIG_KEY]
        return cfg

