microbit-dummy-python-api
=====

A dummy Python implementation of the [microbit module](https://microbit-micropython.readthedocs.io/en/latest/microbit_micropython_api.html) for MicroPython.

Motivation
-------

[Mu](http://codewith.mu/) is a neat editor for micro:bit, with [built-in knowledge](https://github.com/mu-editor/mu/blob/master/mu/resources/api.py) of the microbit module. Other Python editors don't know about the microbit module, so can't show autocomplete or documentation for it. Installing this dummy Python implementation solves that problem.

Important note
----

You can't use this library to control a [BBC micro:bit](http://microbit.org/). If you try to run code written for the micro:bit on your computer it will not work. You will need to flash your script to your micro:bit somehow with [Mu](http://codewith.mu/) or [uFlash](https://uflash.readthedocs.io/en/latest/).

Compatible editors
----

Autocomplete has been tested with the following editors:

* [Python Tools for Visual Studio](https://microsoft.github.io/PTVS/)
* [Sublime Text](https://www.sublimetext.com/) with [SublimeJEDI](https://github.com/srusskih/SublimeJEDI) package
* [IDLE](https://docs.python.org/3/library/idle.html)

Installation
----

From [PyPI](https://pypi.python.org/pypi/microbit):

    pip install microbit

Usage
----

1. Write code in your favourite Python editor
2. Enjoy autocomplete and documentation for microbit module
3. Flash your script to your micro:bit with [uFlash](https://uflash.readthedocs.io/en/latest/)

Note that where [MicroPython differs from Python](https://github.com/micropython/micropython/wiki/Differences), your editor will show documentation for Python. It will also show documentation for modules on your computer absent from MicroPython.
