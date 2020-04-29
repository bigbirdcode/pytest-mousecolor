#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


LONG_DESCRIPTION = """
Show the test status on the color of your RGB mouse

WARNING: Logitech RGB mouse (or RGB keyboard) is needed!!!

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
"""


setup(
    name="pytest-mousecolor",
    version="0.1.0",
    author="BigBirdCode",
    author_email="na",
    license="MIT",
    url="https://github.com/bigbirdcode/pytest-mousecolor",
    description="Show the test status on the color of your RGB mouse",
    long_description=LONG_DESCRIPTION,
    py_modules=["pytest_mousecolor"],
    python_requires=">=3.5",
    install_requires=["pytest>=3.5.0", "logipy"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"pytest11": ["mousecolor = pytest_mousecolor"]},
)
