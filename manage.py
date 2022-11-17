#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from data.firebase_settings import *
from decision_tree.classify import *
import decision_tree.constants as consts

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'natalnet.settings')
    try:
        consts.const_decision_tree = train_decision_tree()
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
