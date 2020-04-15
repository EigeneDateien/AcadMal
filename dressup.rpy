init:
    default skin_color = 1
    default hairstyle = 1
    default hair_color = 1
    default eyes = 1
    default eye_color = 1
    default top_choice = 1
    default bottom_choice = 1
    default top_style = 1
    default top_style_max = 6
    default bottom_style = 1
    default bottom_style_max = 6
#####################################renpy langauge version:
image keri = Composite(
    (311, 631),
    (0, 0), "Create_Character/Base/base[skin_color].png",
    (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
    (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
    (0, 0), "Create_character/Eyebrows/eyebrows[skin_color]_1.png",
    (0, 0), "Create_character/Eyes/eyes[eyes]_[eye_color].png",
    (0, 0), "Create_character/Mouth/mouth[skin_color]_1.png",
    (0, 0), "Create_character/Hair/hair[hairstyle]_[hair_color].png",
)
#####################################python version:
init python:
    def keri_sprite(st, at):
        return LiveComposite(
            (311, 631),
            (0, 0), "Create_Character/Base/base{}.png".format(skin_color),
            (0, 0), "Create_character/Bottoms/bottom{}_{}.png".format(bottom_choice, bottom_style),
            (0, 0), "Create_character/Tops/top{}_{}.png".format(top_choice, top_style),
            (0, 0), "Create_character/Eyebrows/eyebrows{}_1.png".format(skin_color),
            (0, 0), "Create_character/Eyes/eyes{}_{}.png".format(eyes, eye_color),
            (0, 0), "Create_character/Mouth/mouth{}_1.png".format(skin_color),
            (0, 0), "Create_character/Hair/hair{}_{}.png".format(hairstyle, hair_color),
        ),.1

screen dress_keri():
    modal True

    imagemap:
        ground "Dressup_Screen/background.png"
        idle "Dressup_Screen/idle.png"
        hover "Dressup_Screen/hover.png"
        selected_idle "Dressup_Screen/selected.png"
        selected_hover "Dressup_Screen/selected.png"

        ##Skin Color##
        hotspot(178, 75, 53, 53) action SetVariable("skin_color", 1)
        hotspot(243, 75, 53, 53) action SetVariable("skin_color", 2)
        hotspot(307, 75, 53, 53) action SetVariable("skin_color", 3)
        hotspot(372, 75, 53, 53) action SetVariable("skin_color", 4)
        hotspot(437, 75, 53, 53) action SetVariable("skin_color", 5)

        ##Hairstyle##
        hotspot(178, 155, 53, 53) action SetVariable("hairstyle", 1)
        hotspot(243, 155, 53, 53) action SetVariable("hairstyle", 2)
        hotspot(307, 155, 53, 53) action SetVariable("hairstyle", 3)
        hotspot(372, 155, 53, 53) action SetVariable("hairstyle", 4)
        hotspot(437, 155, 53, 53) action SetVariable("hairstyle", 5)

        ##Hair Color##
        hotspot(178, 235, 53, 53) action SetVariable("hair_color", 1)
        hotspot(243, 235, 53, 53) action SetVariable("hair_color", 2)
        hotspot(307, 235, 53, 53) action SetVariable("hair_color", 3)
        hotspot(372, 235, 53, 53) action SetVariable("hair_color", 4)
        hotspot(437, 235, 53, 53) action SetVariable("hair_color", 5)
        hotspot(178, 297, 53, 53) action SetVariable("hair_color", 6)
        hotspot(243, 297, 53, 53) action SetVariable("hair_color", 7)
        hotspot(307, 297, 53, 53) action SetVariable("hair_color", 8)
        hotspot(372, 297, 53, 53) action SetVariable("hair_color", 9)
        hotspot(437, 297, 53, 53) action SetVariable("hair_color", 10)
        hotspot(178, 359, 53, 53) action SetVariable("hair_color", 11)
        hotspot(243, 359, 53, 53) action SetVariable("hair_color", 12)
        hotspot(307, 359, 53, 53) action SetVariable("hair_color", 13)
        hotspot(372, 359, 53, 53) action SetVariable("hair_color", 14)
        hotspot(437, 359, 53, 53) action SetVariable("hair_color", 15)

        ##Eyes##
        hotspot(178, 450, 53, 53) action SetVariable("eyes", 1)
        hotspot(243, 450, 53, 53) action SetVariable("eyes", 2)
        hotspot(307, 450, 53, 53) action SetVariable("eyes", 3)

        ##Eye Color##
        hotspot(178, 529, 53, 53) action SetVariable("eye_color", 1)
        hotspot(243, 529, 53, 53) action SetVariable("eye_color", 2)
        hotspot(307, 529, 53, 53) action SetVariable("eye_color", 3)
        hotspot(372, 529, 53, 53) action SetVariable("eye_color", 4)
        hotspot(437, 529, 53, 53) action SetVariable("eye_color", 5)
        hotspot(178, 591, 53, 53) action SetVariable("eye_color", 6)
        hotspot(243, 591, 53, 53) action SetVariable("eye_color", 7)
        hotspot(307, 591, 53, 53) action SetVariable("eye_color", 8)
        hotspot(372, 591, 53, 53) action SetVariable("eye_color", 9)
        hotspot(437, 591, 53, 53) action SetVariable("eye_color", 10)

        ##Top Choice##
        hotspot(635, 75, 53, 53) action SetVariable("top_choice", 1)
        hotspot(700, 75, 53, 53) action SetVariable("top_choice", 2)
        hotspot(764, 75, 53, 53) action SetVariable("top_choice", 3)
        hotspot(829, 75, 53, 53) action SetVariable("top_choice", 4)
        hotspot(893, 75, 53, 53) action SetVariable("top_choice", 5)

        ##Bottom Choice##
        hotspot(635, 155, 53, 53) action SetVariable("bottom_choice", 1)
        hotspot(700, 155, 53, 53) action SetVariable("bottom_choice", 2)
        hotspot(764, 155, 53, 53) action SetVariable("bottom_choice", 3)
        #hotspot(829, 155, 53, 53) action SetVariable("bottom_choice", 4)
        #hotspot(893, 155, 53, 53) action SetVariable("bottom_choice", 5)

        ##Top Style##
        hotspot(821, 348, 59, 51) action If(top_style > 1, SetVariable("top_style", top_style - 1), SetVariable("top_style", 1))
        hotspot(1200, 348, 59, 51) action If(top_style < top_style_max, SetVariable("top_style", top_style + 1), SetVariable("top_style", top_style_max))

        ##Bottom Style##
        hotspot(821, 569, 59, 51) action If(bottom_style > 1, SetVariable("bottom_style", bottom_style - 1), SetVariable("bottom_style", 1))
        hotspot(1200, 569, 59, 51) action If(bottom_style < bottom_style_max, SetVariable("bottom_style", bottom_style + 1), SetVariable("bottom_style", bottom_style_max))

        ##Continue##
        hotspot(1107, 9, 157, 53) action Return()

    add "keri":
        pos(867, 80)
        zoom 0.5
