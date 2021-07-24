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
import pulsectl
# pylint: disable=line-too-long

USAGE = "[seconds]\n\nThis command only works on Linux with pulseaudio/pipewire-pulse installed.\n\nDefault is 30 seconds."
DEFAULT_SECS = 30

def timed_mute(seconds):
    """
    Mute for specified number of seconds
    """
    with pulsectl.Pulse('volume-increaser') as pulse:
      for sink in pulse.sink_list():
        pulse.volume_set_all_chans(sink, 0.0)
    time.sleep(seconds)
    with pulsectl.Pulse('volume-increaser') as pulse:
      for sink in pulse.sink_list():
        pulse.volume_set_all_chans(sink, 0.5)


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
