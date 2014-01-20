# -*- coding: utf-8 -*-
"""Dump all django settings.

If names are passed through the command line, limit the output to those that match.
The match is case insensitive.
"""
import re
import pprint

from django.core.management.color import color_style
from django.core.management.base import BaseCommand, CommandError


def settings():
    from django.conf import settings

    for name in dir(settings):
        if not name.isupper():
            continue
        yield name, getattr(settings, name)


def settings_limited_to(values):
    regex = re.compile('|'.join(values), re.IGNORECASE)
    for name, value in settings():
        if regex.match(name):
            yield name, value


def list_settings(limit_to=None):
    _settings = settings() if limit_to is None else settings_limited_to(limit_to)
    for name, value in _settings:
        yield name, value


class Command(BaseCommand):
    args = '<setting-name-regex ...>'
    help = __doc__

    def handle(self, *args, **options):
        style = color_style()

        for name, value in list_settings(limit_to=args):
            self.stdout.write(style.NOTICE("\n{} =>\n".format(name)))
            self.stdout.write(style.SQL_FIELD("{}\n".format(pprint.pformat(value))))
