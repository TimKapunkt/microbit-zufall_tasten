input.onButtonPressed(Button.A, function () {
    ZUFALL = randint(1, 10)
    if (ZUFALL == 1) {
        basic.showIcon(IconNames.Happy)
    }
    if (ZUFALL == 2) {
        basic.showIcon(IconNames.Sad)
    }
    if (ZUFALL == 3) {
        basic.showIcon(IconNames.Asleep)
    }
    if (ZUFALL == 4) {
        basic.showIcon(IconNames.Fabulous)
    }
    if (ZUFALL == 5) {
        basic.showIcon(IconNames.Angry)
    }
    if (ZUFALL == 6) {
        basic.showIcon(IconNames.Silly)
    }
    if (ZUFALL == 7) {
        basic.showIcon(IconNames.Meh)
    }
    if (ZUFALL == 8) {
        basic.showIcon(IconNames.Surprised)
    }
    if (ZUFALL == 9) {
        basic.showIcon(IconNames.Skull)
    }
    if (ZUFALL == 10) {
        basic.showIcon(IconNames.StickFigure)
    }
})
input.onButtonPressed(Button.B, function () {
    Zufall_2 = randint(1, 10)
    if (Zufall_2 == 1) {
        music.play(music.stringPlayable("C5 B A G F E D C ", 120), music.PlaybackMode.UntilDone)
    }
    if (Zufall_2 == 2) {
        music.play(music.stringPlayable("A B A G F B A G ", 120), music.PlaybackMode.UntilDone)
    }
    if (Zufall_2 == 3) {
        music.play(music.stringPlayable("A F E F D G E F ", 120), music.PlaybackMode.UntilDone)
    }
    if (Zufall_2 == 4) {
        music.play(music.stringPlayable("G B A G C5 B A B ", 120), music.PlaybackMode.UntilDone)
    }
    if (Zufall_2 == 5) {
        music.play(music.stringPlayable("C5 G B A F A C5 B ", 120), music.PlaybackMode.UntilDone)
    }
    if (Zufall_2 == 6) {
        music.play(music.stringPlayable("C D E F G A B C5 ", 120), music.PlaybackMode.UntilDone)
    }
    if (Zufall_2 == 7) {
        music.play(music.stringPlayable("G F G A - F E D ", 120), music.PlaybackMode.UntilDone)
    }
    if (Zufall_2 == 8) {
        music.play(music.stringPlayable("E D G F B A C5 B ", 120), music.PlaybackMode.UntilDone)
    }
    if (Zufall_2 == 9) {
        music.play(music.stringPlayable("F C5 E C F G D E ", 120), music.PlaybackMode.UntilDone)
    }
    if (Zufall_2 == 10) {
        music.play(music.stringPlayable("B A F E F E A B ", 120), music.PlaybackMode.UntilDone)
    }
})
let Zufall_2 = 0
let ZUFALL = 0
ZUFALL = 0
Zufall_2 = 0
basic.forever(function () {
	
})
