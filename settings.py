# -*- coding: utf-8 -*-
__author__ = "zt"

import os

env = os.getenv("AceEnv", "develop")
print(f"AceEnv is running under environment: {env}")

if env == "develop":
    from config.develop import Config
elif env == "production":
    from config.production import Config
else:
    from config.develop import Config
