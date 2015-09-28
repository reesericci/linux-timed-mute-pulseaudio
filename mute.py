#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Mute system sound
    ~~~~~~~~~~~~~~~~~
"""

from __future__ import print_function
import os
import sys
import time

# pylint: disable=line-too-long

USAGE = "[seconds]\n\nThis command only works on Linux with amixer installed.\n\nDefault is 30 seconds."
DEFAULT_SECS = 30


def timed_mute(seconds):
    """
    Mute for specified number of seconds
    """

    os.system("amixer set Master mute")
    time.sleep(seconds)
    os.system("amixer set Master unmute")

if __name__ == '__main__':

    secs = DEFAULT_SECS

    if len(sys.argv) > 1:
        try:
            secs = int(sys.argv[1])
        except ValueError:
            print(sys.argv[0], USAGE, file=sys.stderr)
            sys.exit(-1)

    print('muting for', secs, 'seconds')
    timed_mute(secs)
