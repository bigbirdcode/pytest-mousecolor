# -*- coding: utf-8 -*-


def test_bar_fixture(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module
    testdir.makepyfile(
        """
        def test_sth():
            assert True
    """
    )

    # run pytest with the following cmd args
    result = testdir.runpytest("--mousecolor_nowait", "-v")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        ["*::test_sth PASSED*",]
    )

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0


def test_help_message(testdir):
    result = testdir.runpytest("--help",)
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        [
            "mousecolor:",
            "*--mousecolor_wait*",
            "*--mousecolor_nowait*",
        ]
    )
