django-dev-commands
===================

Useful commands for developing Django applications.

## `conf` ##

### List all loaded settings ###

    python manage.py conf

### Filter by setting name ###

The search is case insensitive and is treated as a regular expression.

    python manage.py conf "debug$"

## `run` ##

### Run a python file ###

Run a python file within your Django environment:

    python manage.py run path/to/my/script.py

### Run multiple files ###

    python manage.py run path/to/my/script_1.py path/to/my/script_2.py

### Interrupt execution ###

You can raise within a `CommandError` exception within your script anytime you want to interrupt the execution. Is not necessary that you import such an exception since it is available automatically in the execution environment:

```python
from django.conf import settings

if settings.DEBUG:
    raise CommandError("Can't run if DEBUG is True!")
```
