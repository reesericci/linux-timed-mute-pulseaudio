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
import platform

# pylint: disable=line-too-long

USAGE = "[seconds]\n\nThis command only works on Linux with amixer installed.\n\nDefault is 30 seconds."
DEFAULT_SECS = 30

UBUNTU_CMD='amixer -D pulse set Master 1+'
CENTOS_CMD='amixer set Master'

UBUNTU_BASED_DISTS = ['LinuxMint', 'Ubuntu']

def timed_mute(seconds):
    """
    Mute for specified number of seconds
    """

    dist = platform.linux_distribution()[0]


    if dist == '':
        raise RuntimeError('Error: Linux OS was not detected')
    elif dist in UBUNTU_BASED_DISTS:
        cmd = UBUNTU_CMD
    else:
        cmd = CENTOS_CMD

    os.system(cmd + " mute")
    time.sleep(seconds)
    os.system(cmd + " unmute")

if __name__ == '__main__':

    secs = DEFAULT_SECS

    if len(sys.argv) > 1:
        try:
            secs = int(sys.argv[1])
        except ValueError:
            print(sys.argv[0], USAGE, file=sys.stderr)
            sys.exit(-1)

    print('muting for', secs, 'seconds')

    try:
        timed_mute(secs)
    except RuntimeError as e:
        print(e)
