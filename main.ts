input.onButtonPressed(Button.A, function () {
    if (mehet == 1) {
        basic.showIcon(IconNames.Chessboard)
    }
})
input.onButtonPressed(Button.B, function () {
    if (mehet == 1) {
        basic.clearScreen()
    }
})
let mehet = 0
mehet = 0
basic.showArrow(ArrowNames.North)
basic.pause(200)
basic.showArrow(ArrowNames.NorthEast)
basic.pause(200)
basic.showArrow(ArrowNames.East)
basic.pause(200)
basic.showArrow(ArrowNames.SouthEast)
basic.pause(200)
basic.showArrow(ArrowNames.South)
basic.pause(200)
basic.showArrow(ArrowNames.SouthWest)
basic.pause(200)
basic.showArrow(ArrowNames.West)
basic.pause(200)
basic.showArrow(ArrowNames.NorthWest)
basic.showString("GO!")
mehet += 1
