# Linux Timed Mute

## Introduction

Mute Linux system volume for the specified number of seconds.

This is handy for when you are listening to Rdio, or some other music service that has commercials.

When I hit the mute button on my keyboard to mute a commercial, I often forget to unmute.  This application fixes this problem by automatically unmuting after the specified number of seconds.

On my system, I created a panel button to call this application and mute for 27 seconds. Commercials on Rdio are 30 seconds, and it usually takes me a few seconds after a commercial begins before I can hit the panel button.

## Requirements

This command only works on Linux with *amixer* installed.

Amixer is the Linux command-line mixer for the ALSA soundcard driver.

## Future

Automatically detect when a commercial is being played and call this application.
