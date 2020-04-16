#image keri = DynamicDisplayable(keri_sprite) #uncomment to use python version
image school = "Modern_School.png"
label start_dressup:
    call screen dress_keri
    scene school
    $ quick_menu = True
    define keri = "Keri"
    image keri composite = keri
    image keri happy = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows[skin_color]_1.png",
        (0, 0), "Create_character/Eyes/eyes[eyes]_[eye_color].png",
        (0, 0), "Create_character/Mouth/mouth[skin_color]_1.png",
        (0, 0), "Create_character/Hair/hair[hairstyle]_[hair_color].png",
    )

    image keri angry = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows_angry.png",
        (0, 0), "Create_character/Eyes/eyes[eyes]_[eye_color].png",
        (0, 0), "Create_character/Mouth/mouth_angry.png",
        (0, 0), "Create_character/Hair/hair[hairstyle]_[hair_color].png",
    )

    image keri talk = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows_normal.png",
        (0, 0), "Create_character/Eyes/eyes[eyes]_[eye_color].png",
        (0, 0), "Create_character/Mouth/mouth_talk.png",
        (0, 0), "Create_character/Hair/hair[hairstyle]_[hair_color].png",
    )

    image keri talk = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows_normal.png",
        (0, 0), "Create_character/Eyes/eyes[eyes]_[eye_color].png",
        (0, 0), "Create_character/Mouth/mouth_talk.png",
        (0, 0), "Create_character/Hair/hair[hairstyle]_[hair_color].png",
    )

    image keri mhappy = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows_normal.png",
        (0, 0), "Create_character/Eyes/eyes[eyes]_[eye_color].png",
        (0, 0), "Create_character/Mouth/mouth_mhappy.png",
        (0, 0), "Create_character/Hair/hair[hairstyle]_[hair_color].png",
    )

    image keri vhappy = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows_normal.png",
        (0, 0), "Create_character/Eyes/eyes[eyes]_[eye_color].png",
        (0, 0), "Create_character/Mouth/mouth_vhappy.png",
        (0, 0), "Create_character/Hair/hair[hairstyle]_[hair_color].png",
    )

    image keri sad = Composite(
        (311, 631),
        (0, 0), "Create_Character/Base/base[skin_color].png",
        (0, 0), "Create_character/Bottoms/bottom[bottom_choice]_[bottom_style].png",
        (0, 0), "Create_character/Tops/top[top_choice]_[top_style].png",
        (0, 0), "Create_character/Eyebrows/eyebrows_sad.png",
        (0, 0), "Create_character/Eyes/eyes[eyes]_[eye_color].png",
        (0, 0), "Create_character/Mouth/mouth_sad.png",
        (0, 0), "Create_character/Hair/hair[hairstyle]_[hair_color].png",
    )

    "You've created your look!"
    return
