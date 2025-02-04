# maestro
A music player frontend intended for SBCs with small touch screens.

## Dependencies
* Python 3 (tested on 3.13)
    * pexpect (for managing VLC)
    * tkinter (for the GUI)
    * pillow  (for album art)
* VLC (tested on 3.0.21)

## Current hardware
Running on a Raspberry Pi 3B+ with the RPi 3.5inch SPI Display. [(lcdwiki.com)](http://www.lcdwiki.com/3.5inch_RPi_Display)
It has a resolution of 480x320. Low resolution touch displays like these are what maestro is intended for.
