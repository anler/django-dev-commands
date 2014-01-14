# -*- coding: utf-8 -*-
"""Run other Django commands temporarily overriding the specified settings."""
import sys
import subprocess
import shlex
from optparse import make_option

from django.core.management.base import BaseCommand, CommandError
from django.core.management import execute_from_command_line
from django.conf import settings


def expand_shell(cmd):
    return shlex.split(subprocess.check_output('bash -c "echo {}"'.format(cmd), shell=True))


def set_settings(raw_settings):
    exec(u"\n".join(raw_settings), settings._wrapped.__dict__)


class Command(BaseCommand):
    args = '<setting=value ...>'
    option_list = BaseCommand.option_list + (
        make_option('--exec', default=False, help='Command to run with these settings.'),
    )
    help = __doc__

    def handle(self, *settings, **options):
        cmd = options.get('exec')
        if not cmd:
            raise CommandError('You have to specify a command to run with these settings.')
        set_settings(settings)
        cmd = sys.argv[:1] + expand_shell(cmd)
        execute_from_command_line(cmd)
