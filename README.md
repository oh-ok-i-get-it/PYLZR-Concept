PyLZR 

v0.1

This is a proof of concept for Python software that uses an audio analyzer to add sound reactivity funcionality to simple DMX laser show machines.

Audio analyzer uses live audio from system mic to determine average sound amplitude over a given interval. Prints average to console for user interpretations.
If sound mode is on and the sound mode has changed, updates DMX laser by sending MIDI signal corresponding to mapped key press to SoundSwitch DMX software 
via virtual MIDI.

TO USE:
Run the PyLZR.py file from the terminal.
Press [SPACE] bar to toggle sound mode on/off
Edit sound mode ranges by editing CUTOFF values in the source code of the soundMode.py file.

Tested on MacOS 12.7.5




