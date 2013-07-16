hoodwink-serial
===============

Hoodwink-serial is a drop-in replacement for python-serial which may
be used to simulate the hardware layer of Reprap-style 3D printers.
This is a quick-and-dirty module I'm throwing together to allow 3D
printer hardware to be simulated, to empower programmers to write 3D
Printer control software without the physical hardware, and possibly
produce automated tests for said software.




installation and usage
======================

First, DO NOT INSTALL THIS MODULE.

Well, not quite.  Don't install this on your system, but instead,
install it within a virtualenv.  This module spoofs python-serial, so
you will get unexpected behavior if you install this module in the
normal way.

ONCE YOU HAVE YOUR VIRTUALENV SETUP, Git-clone the repository, and run
"python setup.py develop" from within the repository to install it
into your virtual env.

Then, install all of the python dependencies for the program you wish
to test, and then try running the program you wish to test.  For
example, pronterface or switchprint.




consumer advisory notice
========================

This project doesn't actually do anything yet, but give it time.
