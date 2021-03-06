#!/usr/bin/env python
import os
import sys
from os import environ
from os.path import dirname, abspath
import sys
from django.core.management import execute_from_command_line
from web import lisa, googlespeech, plugins, interface

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.lisa.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
