# -*- coding: utf-8 -*-
"""Call a function and print its result."""
import importlib

from django.core.management.base import BaseCommand, CommandError


def call_function(function_path):
    parts = function_path.split(".")
    function_name, module_name = parts[-1], ".".join(parts[:-1])
    module = importlib.import_module(module_name)
    function = getattr(module, function_name)

    return function()


def call_functions(*function_paths):
    for function_path in function_paths:
        yield call_function(function_path)


class Command(BaseCommand):
    help = __doc__

    def handle(self, *functions, **options):
        for result in call_functions(*functions):
            self.stdout.write("{}\n".format(result))
