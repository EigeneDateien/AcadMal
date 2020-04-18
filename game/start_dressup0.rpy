#image keri = DynamicDisplayable(keri_sprite) #uncomment to use python version


label start_dressup0:
    scene bg outside

    menu:
        "Which character would you like to change?"

        "Pari":
            $ name = "keri"
            jump start_dressup_female
        "Alex":
            $ name = "alex"
            jump start_dressup_male


label start_dressup_male:
    call screen dress_alex()
    scene school
    $ quick_menu = True
    define alex = "alex"
    image alex composite = alex
    image alex happy = Composite(
        (311, 631),
        (0, 0), "Create_Character/male/Base/base[skin_color_alex].png",
        (0, 0), "Create_character/male/Eyebrows/eyebrows_normal.png",
        (0, 0), "Create_character/male/Eyes/eyes[eyes_alex]_[eye_color_alex].png",
        (0, 0), "Create_character/male/Mouth/mouth_happy.png",
        (0, 0), "Create_character/male/Hair/hair[hairstyle_alex]_[hair_color_alex].png",
    )

    image alex angry = Composite(
        (311, 631),
        (0, 0), "Create_Character/male/Base/base[skin_color_alex].png",
        (0, 0), "Create_character/male/Eyebrows/eyebrows_angry.png",
        (0, 0), "Create_character/male/Eyes/eyes[eyes_alex]_[eye_color_alex].png",
        (0, 0), "Create_character/male/Mouth/mouth_angry.png",
        (0, 0), "Create_character/male/Hair/hair[hairstyle_alex]_[hair_color_alex].png",
    )

    image alex talk = Composite(
        (311, 631),
        (0, 0), "Create_Character/male/Base/base[skin_color_alex].png",
        (0, 0), "Create_character/male/Eyebrows/eyebrows_normal.png",
        (0, 0), "Create_character/male/Eyes/eyes[eyes_alex]_[eye_color_alex].png",
        (0, 0), "Create_character/male/Mouth/mouth_talk.png",
        (0, 0), "Create_character/male/Hair/hair[hairstyle_alex]_[hair_color_alex].png",
    )

    image alex surprised = Composite(
        (311, 631),
        (0, 0), "Create_Character/male/Base/base[skin_color_alex].png",
        (0, 0), "Create_character/male/Eyebrows/eyebrows_sad.png",
        (0, 0), "Create_character/male/Eyes/eyes[eyes_alex]_[eye_color_alex].png",
        (0, 0), "Create_character/male/Mouth/mouth_surprised.png",
        (0, 0), "Create_character/male/Hair/hair[hairstyle_alex]_[hair_color_alex].png",
    )


    image alex mhappy = Composite(
        (311, 631),
        (0, 0), "Create_Character/male/Base/base[skin_color_alex].png",
        (0, 0), "Create_character/male/Eyebrows/eyebrows_normal.png",
        (0, 0), "Create_character/male/Eyes/eyes[eyes_alex]_[eye_color_alex].png",
        (0, 0), "Create_character/male/Mouth/mouth_mhappy.png",
        (0, 0), "Create_character/male/Hair/hair[hairstyle_alex]_[hair_color_alex].png",
    )

    image alex vhappy = Composite(
        (311, 631),
        (0, 0), "Create_Character/male/Base/base[skin_color_alex].png",
        (0, 0), "Create_character/male/Eyebrows/eyebrows_normal.png",
        (0, 0), "Create_character/male/Eyes/eyes[eyes_alex]_[eye_color_alex].png",
        (0, 0), "Create_character/male/Mouth/mouth_vhappy.png",
        (0, 0), "Create_character/male/Hair/hair[hairstyle_alex]_[hair_color_alex].png",
    )

    image alex sad = Composite(
        (311, 631),
        (0, 0), "Create_Character/male/Base/base[skin_color_alex].png",
        (0, 0), "Create_character/male/Eyebrows/eyebrows_sad.png",
        (0, 0), "Create_character/male/Eyes/eyes[eyes_alex]_[eye_color_alex].png",
        (0, 0), "Create_character/male/Mouth/mouth_sad.png",
        (0, 0), "Create_character/male/Hair/hair[hairstyle_alex]_[hair_color_alex].png",
    )

    "You've created your look!"
    return

label start_dressup_female:
    call screen dress_keri()
    scene school
    $ quick_menu = True
    define keri = "Keri"
    image keri composite = keri
    image keri happy = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color_keri].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows[skin_color_keri]_1.png",
        (0, 0), "Create_character/Eyes/eyes[eyes_keri]_[eye_color_keri].png",
        (0, 0), "Create_character/Mouth/mouth[skin_color_keri]_1.png",
        (0, 0), "Create_character/Hair/hair[hairstyle_keri]_[hair_color_keri].png",
    )

    image keri angry = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color_keri].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows_angry.png",
        (0, 0), "Create_character/Eyes/eyes[eyes_keri]_[eye_color_keri].png",
        (0, 0), "Create_character/Mouth/mouth_angry.png",
        (0, 0), "Create_character/Hair/hair[hairstyle_keri]_[hair_color_keri].png",
    )

    image keri talk = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color_keri].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows_normal.png",
        (0, 0), "Create_character/Eyes/eyes[eyes_keri]_[eye_color_keri].png",
        (0, 0), "Create_character/Mouth/mouth_talk.png",
        (0, 0), "Create_character/Hair/hair[hairstyle_keri]_[hair_color_keri].png",
    )

    image keri mhappy = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color_keri].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows_normal.png",
        (0, 0), "Create_character/Eyes/eyes[eyes_keri]_[eye_color_keri].png",
        (0, 0), "Create_character/Mouth/mouth_mhappy.png",
        (0, 0), "Create_character/Hair/hair[hairstyle_keri]_[hair_color_keri].png",
    )

    image keri vhappy = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color_keri].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows_normal.png",
        (0, 0), "Create_character/Eyes/eyes[eyes_keri]_[eye_color_keri].png",
        (0, 0), "Create_character/Mouth/mouth_vhappy.png",
        (0, 0), "Create_character/Hair/hair[hairstyle_keri]_[hair_color_keri].png",
    )

    image keri sad = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color_keri].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows_sad.png",
        (0, 0), "Create_character/Eyes/eyes[eyes_keri]_[eye_color_keri].png",
        (0, 0), "Create_character/Mouth/mouth_sad.png",
        (0, 0), "Create_character/Hair/hair[hairstyle_keri]_[hair_color_keri].png",
    )

    "You've created your look!"
    return
