=================
pytest-mousecolor
=================

.. image:: https://img.shields.io/pypi/v/pytest-mousecolor.svg
    :target: https://pypi.org/project/pytest-mousecolor
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-mousecolor.svg
    :target: https://pypi.org/project/pytest-mousecolor
    :alt: Python versions

.. image:: https://travis-ci.org/bigbird/pytest-mousecolor.svg?branch=master
    :target: https://travis-ci.org/bigbird/pytest-mousecolor
    :alt: See Build Status on Travis CI

.. image:: https://ci.appveyor.com/api/projects/status/github/bigbird/pytest-mousecolor?branch=master
    :target: https://ci.appveyor.com/project/bigbird/pytest-mousecolor/branch/master
    :alt: See Build Status on AppVeyor

Show the test status on the color of your RGB mouse

**WARNING: Logitech RGB mouse (or RGB keyboard) is needed!!!**

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


Features
--------

When initializing then the mouse color change to yellow,
meaning that no test was executed.
When the first test pass then the mouse color will be green.
When any of the tests fail then mouse will be red, and
it will stay red.
So during test run, you will see immediately what the
overall result of your test is.

Options are:

--mousecolor_wait
    At the end of the test it will pause and wait
    for user confirmation with the Enter key.
    Useful for long tests, keeping the result indication.

--mousecolor_nowait
    Quit at the end immediately. Not blocking, but
    unfortunately mouse color will revert to the
    default color. This is a limitation in the SDK.

Note: using this plugin adds 1+1 sec wait to your
test execution time.


Requirements
------------

- Logitech RGB mouse or keyboard
- Logitech driver / SDK / gamings software installed
- logipy Python module

Installation
------------

You can install "pytest-mousecolor" via `pip`_ from `PyPI`_::

    $ pip install pytest-mousecolor


Usage
-----

Use it as any other Pytest plugin.

For example:
``pytest --mousecolor_wait``

Contributing
------------

Contributions are very welcome.


License
-------

Distributed under the terms of the `MIT`_ license, "pytest-mousecolor" is free and open source software


Author
------

:Author:
    BigBirdCode

:Version:
    0.1 of 2020 Apr 29

:Homepage:
    https://github.com/bigbirdcode/pytest-mousecolor

Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/bigbird/pytest-mousecolor/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
