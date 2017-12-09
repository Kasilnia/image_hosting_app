from django.core.exceptions import ImproperlyConfigured


try:
    from .local import *
except ImportError:
    from .default import *
