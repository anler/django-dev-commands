import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

py_version = sys.version_info[:2]

here = os.path.abspath(os.path.dirname(__file__))

PROJECT_NAME = "django-dev-commands"
PROJECT_URL = "https://github.com/ikame/django-dev-commands"
PROJECT_VERSION = "1.0.0"
PROJECT_DESCRIPTION = "Useful commands for developing Django applications."

AUTHOR = "ikame"
AUTHOR_EMAIL = "anler86@gmail.com"

try:
    README = open(os.path.join(here, "README.rst")).read()
    README += open(os.path.join(here, "HISTORY.rst")).read()
except IOError:
    README = PROJECT_URL

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(name=PROJECT_NAME,
      version=PROJECT_VERSION,
      description=PROJECT_DESCRIPTION,
      long_description=README,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=PROJECT_URL,
      license="MIT",
      install_requires=["six"],
      tests_require=["pytest", "mock"],
      cmdclass={"test": PyTest},
      keywords="django development dev tools utilities",
      classifiers=[
          "Environment :: Plugins",
          "Environment :: Console",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "Intended Audience :: Financial and Insurance Industry",
          "Framework :: Django",
          "Topic :: Database :: Front-Ends",
          "Topic :: Documentation",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
          "Topic :: Internet :: WWW/HTTP :: Site Management",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Topic :: Software Development :: Libraries :: Python Modules"])
