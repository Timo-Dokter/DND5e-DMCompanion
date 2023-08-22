# flake8: noqa

from .base import *

import platform

current_os = platform.system()


INSTALLED_APPS += [
    "debug_toolbar",
]
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# ==============================================================================
# CORE SETTINGS
# ==============================================================================
if current_os == "Windows":
    NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
