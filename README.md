django-dev-commands
===================

Useful commands for developing Django applications.

## Available commands ##

* `conf` - Show the value of loaded settings.
* `run` - Run a python file within your Django project environment.
* `settings` - Run other Django commands temporarily overriding some project settings.
* `commands` - List only commands of the specified apps.
* `call` - Call the given functions and print their results.

## Getting help ##

Run: `python manage.py <command> -h` for getting help of a command.

## Examples ##

### `conf` ###

#### List all loaded settings ####

    python manage.py conf

#### Filter by setting name ####

The search is case insensitive and is treated as a regular expression.

    python manage.py conf "debug$" "use_tz"

### `run` ###

#### Run a python file ####

Run a python file within your Django environment:

    python manage.py run path/to/my/script.py

#### Run multiple files ####

    python manage.py run path/to/my/script_1.py path/to/my/script_2.py

#### Interrupting execution within the running file ####

You can raise within a `CommandError` exception within your script anytime you want to interrupt the execution. Is not necessary that you import such an exception since it is available automatically in the execution environment:

Let's say you have the following `main.py` script:

```python
from django.conf import settings

if settings.DEBUG:
    raise CommandError("Can't run if DEBUG is True!")
```

### `settings` ###

#### Temporarily override a setting while running a command ####


Let's say you have the following `main.py` script:

```python
from django.conf import settings

if settings.DEBUG:
    raise CommandError("Can't run if DEBUG is True!")
```

You can turn **DEBUG** off while running the `run` command with:

    python manage.py settings DEBUG=False --exec "run path/to/main.py"

Very useful when running celery in my dev environment and I don't want any memory leak:

    python manage.py settings DEBUG=False --exec "celeryd"

#### You can pass any valid python code as a setting####

    python manage.py settings "DATABASES['default']['engine'] = 'django.db.backends.sqlite3'" --exec "runserver"

### `commands` ###

List the available commands of only **auth** and **staticfiles**:

    python manage.py commands auth staticfiles

### `call` ###

*TODO: Add support for passing argument and keyword arguments via the command line.*

#### Call a function a print its results ####

    python manage.py call django.core.management.get_commands
