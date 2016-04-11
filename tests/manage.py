#!/usr/bin/env python
import os
import sys

BASE_PATH = os.path.abspath(__file__)
for i in range(2):
    BASE_PATH = os.path.dirname(BASE_PATH)
sys.path.insert(0, os.path.join(BASE_PATH, 'links'))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
