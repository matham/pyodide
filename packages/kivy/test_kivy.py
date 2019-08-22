from textwrap import dedent

import pytest


def test_bool(selenium_standalone, request):
    selenium = selenium_standalone
    selenium.load_package("kivy")
    selenium_standalone.load_package("micropip")
    selenium_standalone.run("import micropip")
    selenium_standalone.run("micropip.install('docutils')")
    selenium_standalone.run("micropip.install('pygments')")
    cmd = dedent(r"""
        import kivy.properties
        """)

    selenium.run(cmd)
