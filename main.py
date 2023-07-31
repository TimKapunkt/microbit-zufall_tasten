def on_button_pressed_a():
    global ZUFALL
    ZUFALL = randint(1, 10)
    if ZUFALL == 1:
        basic.show_icon(IconNames.HAPPY)
    if ZUFALL == 2:
        basic.show_icon(IconNames.SAD)
    if ZUFALL == 3:
        basic.show_icon(IconNames.ASLEEP)
    if ZUFALL == 4:
        basic.show_icon(IconNames.FABULOUS)
    if ZUFALL == 5:
        basic.show_icon(IconNames.ANGRY)
    if ZUFALL == 6:
        basic.show_icon(IconNames.SILLY)
    if ZUFALL == 7:
        basic.show_icon(IconNames.MEH)
    if ZUFALL == 8:
        basic.show_icon(IconNames.SURPRISED)
    if ZUFALL == 9:
        basic.show_icon(IconNames.SKULL)
    if ZUFALL == 10:
        basic.show_icon(IconNames.STICK_FIGURE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Zufall_2
    Zufall_2 = randint(1, 10)
    if Zufall_2 == 1:
        music.play(music.string_playable("C5 B A G F E D C ", 120),
            music.PlaybackMode.UNTIL_DONE)
    if Zufall_2 == 2:
        music.play(music.string_playable("A B A G F B A G ", 120),
            music.PlaybackMode.UNTIL_DONE)
    if Zufall_2 == 3:
        music.play(music.string_playable("A F E F D G E F ", 120),
            music.PlaybackMode.UNTIL_DONE)
    if Zufall_2 == 4:
        music.play(music.string_playable("G B A G C5 B A B ", 120),
            music.PlaybackMode.UNTIL_DONE)
    if Zufall_2 == 5:
        music.play(music.string_playable("C5 G B A F A C5 B ", 120),
            music.PlaybackMode.UNTIL_DONE)
    if Zufall_2 == 6:
        music.play(music.string_playable("C D E F G A B C5 ", 120),
            music.PlaybackMode.UNTIL_DONE)
    if Zufall_2 == 7:
        music.play(music.string_playable("G F G A - F E D ", 120),
            music.PlaybackMode.UNTIL_DONE)
    if Zufall_2 == 8:
        music.play(music.string_playable("E D G F B A C5 B ", 120),
            music.PlaybackMode.UNTIL_DONE)
    if Zufall_2 == 9:
        music.play(music.string_playable("F C5 E C F G D E ", 120),
            music.PlaybackMode.UNTIL_DONE)
    if Zufall_2 == 10:
        music.play(music.string_playable("B A F E F E A B ", 120),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

Zufall_2 = 0
ZUFALL = 0
ZUFALL = 0
Zufall_2 = 0

def on_forever():
    pass
basic.forever(on_forever)
