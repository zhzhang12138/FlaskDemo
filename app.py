# -*- coding: utf-8 -*-
__author__ = "zt"

import os
import logging
from settings import Config
from factory import create_app

logging.basicConfig(format='%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s',
                    level=os.getenv("LOG_LEVEL", 'DEBUG'))

app = create_app()

if __name__ == '__main__':
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
