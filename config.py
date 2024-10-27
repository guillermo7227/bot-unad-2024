#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "bb454822-7dbc-4ce8-ad62-2eb3b788344c")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
