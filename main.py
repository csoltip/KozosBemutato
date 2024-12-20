def on_button_pressed_a():
    if mehet == 1:
        basic.show_icon(IconNames.CHESSBOARD)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if mehet == 1:
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

mehet = 0
mehet = 0
basic.show_arrow(ArrowNames.NORTH)
basic.pause(200)
basic.show_arrow(ArrowNames.NORTH_EAST)
basic.pause(200)
basic.show_arrow(ArrowNames.EAST)
basic.pause(200)
basic.show_arrow(ArrowNames.SOUTH_EAST)
basic.pause(200)
basic.show_arrow(ArrowNames.SOUTH)
basic.pause(200)
basic.show_arrow(ArrowNames.SOUTH_WEST)
basic.pause(200)
basic.show_arrow(ArrowNames.WEST)
basic.pause(200)
basic.show_arrow(ArrowNames.NORTH_WEST)
basic.show_string("GO!")
mehet += 1