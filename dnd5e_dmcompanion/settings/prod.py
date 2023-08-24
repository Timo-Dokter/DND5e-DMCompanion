# flake8: noqa
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

import dnd5e_dmcompanion

from .base import *

# ==============================================================================
# CORE SETTINGS
# ==============================================================================


# ==============================================================================
# SECURITY SETTINGS
# ==============================================================================

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = []


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 465
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

sentry_sdk.init(
    dsn=config("SENTRY_DSN", default=""),
    environment=SIMPLE_ENVIRONMENT,
    release="dnd5e_dmcompanion@%s" % dnd5e_dmcompanion.__version__,
    integrations=[DjangoIntegration()],
)
