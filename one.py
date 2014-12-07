"""This is for interactive debugging with, e.g., iPython."""

import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "one.settings"
django.setup ()
