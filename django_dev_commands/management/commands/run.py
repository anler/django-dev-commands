# -*- coding: utf-8 -*-
"""Run a python file within your Django app environment.

Example:
    python manage.py run script.py

You can also pass arguments to the file using the following syntax:
    python manage.py run script.py:"some_argument --another-argument=something"
"""
import runpy
import sys
import operator
from os import path

from django.core.management.base import BaseCommand, CommandError


def run(filename, args):
    if hasattr(args, "split"):
        args = args.split()
    sys.argv = [filename] + args
    runpy.run_path(filename, globals(), run_name="__main__")


class Command(BaseCommand):
    args = '<filename:"arg ..." ...>'
    help = __doc__

    def handle(self, *args, **options):
        if not args:
            raise CommandError("You must specify at least a python file path to execute.")
        args = map(operator.methodcaller("split", ":"), args)
        for arg in args:
            try:
                filename, filename_args = arg
            except ValueError:
                filename, = arg
                filename_args = ""
            if not path.isfile(filename):
                raise CommandError("{!r} is not a valid file path.".format(filename))
            run(filename, filename_args)
