#image keri = DynamicDisplayable(keri_sprite) #uncomment to use python version

init python:
    character = {}
    def create_character(gender, name):
        if gender == "male":
            character_values = {}
            character[name] = character_values
            renpy.jump(start_dressup_male(name))
        else:
            character_values = {}
            character[name] = character_values
            renpy.jump(start_dressup_female(name))

# sara definition
define sara = "Sara"

layeredimage sara:

    always:
        "Create_Character/Base/base3.png"

    always:
        "Create_Character/Bottoms/bottom1_6.png"

    always:
        "Create_Character/Tops/top5_5.png"

    always:
        "Create_Character/Eyes/eyes2_9.png"

    always:
        "Create_Character/Hair/hair4_7.png"

    group eyebrows:

        attribute happy default:
            "Create_character/Eyebrows/eyebrows_normal.png"

        attribute angry:
            "Create_character/Eyebrows/eyebrows_angry.png"

        attribute talk:
            "Create_character/Eyebrows/eyebrows_normal.png"

        attribute mhappy:
            "Create_character/Eyebrows/eyebrows_normal.png"

        attribute vhappy:
            "Create_character/Eyebrows/eyebrows_normal.png"

        attribute sad:
            "Create_character/Eyebrows/eyebrows_sad.png"

    group mouth:

        attribute happy default:
            "Create_character/Mouth/mouth_happy.png"

        attribute angry:
            "Create_character/Mouth/mouth_angry.png"

        attribute talk:
            "Create_character/Mouth/mouth_talk.png"

        attribute mhappy:
            "Create_character/Mouth/mouth_mhappy.png"

        attribute vhappy:
            "Create_character/Mouth/mouth_vhappy.png"

        attribute sad:
            "Create_character/Mouth/mouth_sad.png"

layeredimage alex:

    always:
        "Create_Character/male/Base/base[skin_color_male].png"
    always:
        "Create_character/male/Eyes/eyes[eyes_male]_[eye_color_male].png"
    always:
        "Create_character/male/Hair/hair[hairstyle_male]_[hair_color_male].png"

    group eyebrows:

        attribute happy default:
            "Create_character/male/Eyebrows/eyebrows_normal.png"

        attribute angry:
            "Create_character/male/Eyebrows/eyebrows_angry.png"

        attribute talk:
            "Create_character/male/Eyebrows/eyebrows_normal.png"

        attribute mhappy:
            "Create_character/male/Eyebrows/eyebrows_normal.png"

        attribute vhappy:
            "Create_character/male/Eyebrows/eyebrows_normal.png"

        attribute surprised:
            "Create_character/male/Eyebrows/eyebrows_sad.png"

        attribute sad:
            "Create_character/Eyebrows/eyebrows_sad.png"

    group mouth:

        attribute happy default:
            "Create_character/male/Mouth/mouth_happy.png"

        attribute angry:
            "Create_character/male/Mouth/mouth_angry.png"

        attribute talk:
            "Create_character/male/Mouth/mouth_talk.png"

        attribute mhappy:
            "Create_character/male/Mouth/mouth_mhappy.png"

        attribute vhappy:
            "Create_character/male/Mouth/mouth_vhappy.png"

        attribute surprised:
            "Create_character/male/Mouth/mouth_surprised.png"

        attribute sad:
            "Create_character/male/Mouth/mouth_sad.png"


define keri = "Keri"

layeredimage keri:

    always:
        "Create_Character/Base/base[skin_color_female].png"
    always:
        "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png"
    always:
        "Create_character/Tops/top[top_choice]_[top_style].png"
    always:
        "Create_character/Hair/hair[hairstyle_female]_[hair_color_female].png"
    always:
        "Create_character/Eyes/eyes[eyes_female]_[eye_color_female].png"

    group eyebrows:

        attribute happy default:
            "Create_character/Eyebrows/eyebrows_normal.png"

        attribute angry:
            "Create_character/Eyebrows/eyebrows_angry.png"

        attribute talk:
            "Create_character/Eyebrows/eyebrows_normal.png"

        attribute mhappy:
            "Create_character/Eyebrows/eyebrows_normal.png"

        attribute vhappy:
            "Create_character/Eyebrows/eyebrows_normal.png"

        attribute surprised:
            "Create_character/Eyebrows/eyebrows_sad.png"

        attribute sad:
            "Create_character/Eyebrows/eyebrows_sad.png"

    group mouth:

        attribute happy default:
            "Create_character/Mouth/mouth_happy.png"

        attribute angry:
            "Create_character/Mouth/mouth_angry.png"

        attribute talk:
            "Create_character/Mouth/mouth_talk.png"

        attribute mhappy:
            "Create_character/Mouth/mouth_mhappy.png"

        attribute vhappy:
            "Create_character/Mouth/mouth_vhappy.png"

        attribute surprised:
            "Create_character/Mouth/mouth_surprised.png"

        attribute sad:
            "Create_character/Mouth/mouth_sad.png"


label start_dressup:
    scene bg outside

    menu:
        "Which character would you like to change?"

        "Pari":
            $ name = "keri"
            jump start_dressup_female
        "Alex":
            $ name = "alex"
            jump start_dressup_male


label start_dressup_male(name="alex"):
    call screen dress_male()
    scene school
    $ quick_menu = True
    define alex = "alex"


    "You've created your look!"
    return

label start_dressup_female:
    call screen dress_female()
    scene school
    $ quick_menu = True
    # get name from the ()
    # define variables for that name
    # skin_color_[name] =
    python:
        skin_color = skin_color_female





    "You've created your look!"
    return
