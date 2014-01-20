# -*- coding: utf-8 -*-
"""List commands of the specified applications.

By passing command line arguments that represents regexs of app names you can list the commands of
those apps only.
"""
import re

from django.core.management import get_commands, execute_from_command_line
from django.core.management.base import BaseCommand, CommandError
from django.core.management.color import color_style
from django.utils import six


def get_filtered_commands(*filters):
    filters_re = re.compile("|".join(filters))
    for command, app in six.iteritems(get_commands()):
        if filters_re.search(app):
            yield app, command


class Command(BaseCommand):
    args = '<app-name-regex ...>'
    help = __doc__

    def handle(self, *filters, **options):
        if filters:
            style = color_style()
            output = set()
            for app, command in get_filtered_commands(*filters):
                if app not in output:
                    self.stdout.write(style.NOTICE("\n[{}]\n".format(app)))
                    output.add(app)
                self.stdout.write("{}\n".format(command))
        else:
            execute_from_command_line(["manage.py"])
