"""Pytest plugin MouseColor

Show the test status on the color of your RGB mouse.

WARNING:
Logitech RGB mouse (or RGB keyboard) is needed!!!

When initializing the mouse color change to yellow,
meaning that no test was executed.
When the first test pass mouse color will be green.
When any of the tests fail then mouse will be red,
and it will stay red.
So at the end you will see immediately what was the
overall result of your test.

Options are:
--mousecolor_wait
    At the end of the test it will pause and wait
    for user confirmation with the Enter key.
--mousecolor_nowait
    Quit at the end immediately. Not blocking, but
    unfortunately mouse color will revert to the
    default color. This is a limitation in the SDK.

Note: using this plugin adds 1+1 sec wait to your
test execution time.
"""

import time

import pytest
from logipy import logi_led


USE_MOUSE_COLOR = False
FIRST_RESULT = True


def pytest_addoption(parser):
    """Add the command line options for MouseColor plugin"""
    group = parser.getgroup("mousecolor")
    group.addoption(
        "--mousecolor_wait",
        action="store_true",
        dest="mousecolor_wait",
        default=False,
        help='Enable test status on the color of your RGB mouse with waiting',
    )
    group.addoption(
        "--mousecolor_nowait",
        action="store_true",
        dest="mousecolor_nowait",
        default=False,
        help='Enable test status on the color of your RGB mouse without wait',
    )


def pytest_configure(config):
    """Initialization of MouseColor plugin"""
    global USE_MOUSE_COLOR
    if config.getoption("mousecolor_wait") or config.getoption("mousecolor_nowait"):
        USE_MOUSE_COLOR = True
        logi_led.logi_led_init()
        # Give the SDK a second to initialize
        time.sleep(1)
        # Initialize in yellow, i.e. no test
        logi_led.logi_led_set_lighting(150, 100, 0)


def pytest_unconfigure(config):
    """Shutdown of MouseColor plugin"""
    if USE_MOUSE_COLOR:
        if config.getoption("mousecolor_wait"):
            # https://stackoverflow.com/questions/42760059/how-to-make-pytest-wait-for-manual-user-action
            # https://stackoverflow.com/questions/41194262/how-can-i-make-py-test-tests-accept-interactive-input
            capmanager = config.pluginmanager.getplugin('capturemanager')
            capmanager.suspend_global_capture(in_=True)
            input('Press enter to shutdown test...')
            capmanager.resume_global_capture()
        else:
            time.sleep(1)  # 1 sec to show the final color
        logi_led.logi_led_shutdown()


def pytest_runtest_logreport(report):
    """Show status of test on MouseColor plugin"""
    global FIRST_RESULT
    if USE_MOUSE_COLOR:
        if report.failed:
            logi_led.logi_led_set_lighting(100, 0, 0)
            FIRST_RESULT = False
        elif FIRST_RESULT and report.passed:
            logi_led.logi_led_set_lighting(0, 100, 0)
            FIRST_RESULT = False
