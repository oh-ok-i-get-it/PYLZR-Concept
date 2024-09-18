import midiKeyboard as midi
import textClass as txt

# constants
MODE_QUIET_CUTOFF = 1000
MODE1_CUTOFF = 90000 
MODE2_CUTOFF = 100000 


#set soundmode variable to matching soundmode 
def setMode(amp_avg):
    if amp_avg < MODE_QUIET_CUTOFF:
        soundmode_mode = 0
        print(txt.YELLOW, end="")
    elif amp_avg < MODE1_CUTOFF:
        soundmode_mode = 1
        print(txt.BLUE, end="")
    elif amp_avg < MODE2_CUTOFF:
        soundmode_mode = 2
        print(txt.CYAN, end="")
    else:
        soundmode_mode = 3
        print(txt.PURPLE, end="")
    return soundmode_mode


#sent midi update of matching soundmode
def updateMode(soundmode_mode, midiout):
    if soundmode_mode == 0:
        midi.press_MIDI_note(midi.SPACE, midiout)
        print(txt.YELLOW + txt.I + "\n>>>> SM: 0 SENT <<<<\n" + txt.IOFF)
    elif soundmode_mode == 1:
        midi.press_MIDI_note(midi.ONE, midiout)
        print(txt.BLUE + txt.I + "\n>>>> SM: 1 SENT <<<<\n" + txt.IOFF)
    elif soundmode_mode == 2:
        midi.press_MIDI_note(midi.TWO, midiout)
        print(txt.CYAN + txt.I + "\n>>>> SM: 2 SENT <<<<\n" + txt.IOFF)
    else: 
        midi.press_MIDI_note(midi.THREE, midiout)
        print(txt.PURPLE + txt.I + "\n>>>> SM: 3 SENT <<<<\n" + txt.IOFF)


#overloaded draw text function
def draw_text(text, font, text_col):
    img = font.render(text, True, text_col)
    return img
def draw_text(text, font, text_col, x, y, screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
