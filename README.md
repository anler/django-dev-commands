django-dev-commands
===================

Useful commands for developing Django applications.

## `conf` ##

### List all loaded settings ###

    python manage.py conf

### Filter by setting name ###

The search is case insensitive and is treated as a regular expression.

    python manage.py conf "debug$"
