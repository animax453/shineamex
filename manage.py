#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    test_settings = 'shineamex.settings.test'
    settings = test_settings if 'test' in sys.argv else 'shineamex.settings.main'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

