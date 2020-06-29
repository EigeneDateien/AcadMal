init:
    default slide_number = 0
    # default slide_number_max = 1

label slide_show_viewer:

    call screen show_slides()

    "Returning to game..."
    return

screen show_slides():
    modal True

    imagemap:
        ground "slides/[slide_name][slide_number].png"
        idle "Dressup_Screen/slideshow_viewer.png"
        hover "Dressup_Screen/slideshow_viewer.png"
        selected_idle "Dressup_Screen/slideshow_viewer.png"
        selected_hover "Dressup_Screen/slideshow_viewer.png"

        ##Scroll slides##
        hotspot(10, 348, 59, 51) action If(slide_number > 1, SetVariable("slide_number", slide_number - 1), SetVariable("slide_number", 1))
        hotspot(1200, 348, 59, 51) action If(slide_number < slide_number_max, SetVariable("slide_number", slide_number + 1), SetVariable("slide_number", slide_number_max))

        ##Continue##
        hotspot(1107, 9, 157, 53) action Return()

    # add "slide":
    #     pos(0, 0)
