# -*- coding: utf-8 -*-
"""Run a python file within your Django app environment."""
import runpy
from os import path

from django.core.management.base import BaseCommand, CommandError


def run_files(*filenames):
    for filename in filenames:
        run(filename)


def run(filename):
    runpy.run_path(filename, globals(), run_name="__main__")


class Command(BaseCommand):
    args = '<filename ...>'
    help = __doc__

    def handle(self, *args, **options):
        if not args:
            raise CommandError("You must specify at least a python file path to execute.")
        for filename in args:
            if not path.isfile(filename):
                raise CommandError("{!r} is not a valid file path.".format(filename))

        run_files(*args)
