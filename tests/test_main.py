import re

import wx.cli


def test_main(capsys):
    """Tests the output of wx"""
    wx.cli.hello_world()
    out, _ = capsys.readouterr()
    assert bool(re.match("Hello world!", out))
