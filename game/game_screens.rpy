init:
    # possibility of designing more (like UoM logo)
    image title = Text("{color=#000000}Item Name: {space=50} SE 1{/color}")


###################################
# Intro
###################################

# Skip button to skip the intro
screen skip_button:
    frame:
        xalign 0.95 yalign 0.73
        button:
            action Jump("skipped_intro")
            text _("Skip Intro") style "button_text"


###################################
# First Week - Plagiarism
###################################

# Screen to show text with no (= transparent) background on screen
# For a screen with white background, see text_screen_white below
# Option to define the position of the text at the screen: up, middle, below
screen text_screen(input_text, position="up"):
    $ input_t = input_text
    if position == "below":
        frame:
            background None
            xmaximum 680
            yalign 0.85
            xalign 0.53
            text "{color=#000000}[input_t]{/color}"
    elif position == "middle":
        frame:
            background None
            xmaximum 800
            yalign 0.5
            xalign 0.53
            text "{size=+5}{color=#000000}[input_t]{/color}{/size}"
    else:
        frame:
            background None
            xmaximum 680
            yalign 0.2
            xalign 0.53
            text "{color=#000000}[input_t]{/color}"


# Screen to show text with WHITE background on screen
# For a screen with no or transparent background, see text_screen above
# Option to define the position of the text at the screen: up, middle, below
image white = Solid("#fff")
screen text_screen_white(position):
    if position == "middle":
        frame:
            background "white"
            xmaximum 600
            ypos 200
            xpos 380
            text "{size=-4}{color=#000000}[essay_question]{/color}{/size}"
    elif position == "below":
        frame:
            background "white"
            xmaximum 600
            ypos 430
            xpos 380
            text "{size=-4}{color=#000000}[essay_question]{/color}{/size}"


# Screen to mimic an opened Wikipedia article on a laptop
screen wikipedia_screen:
    frame:
        background "Scene/bg home wiki_blank.png"

    frame:
        background None
        yalign 0.28
        xalign 0.28
        text "{color=#000000}{size=+10}[wikipedia_title]{/size}{/color}"

    frame:
        background None
        xmaximum 800
        yalign 0.65
        xalign 0.6
        text "{color=#000000}{size=-5}[wikipedia_article]{/size}{/color}"


# Screen to mimic opened slides (e.g. powerpoint) on a laptop
screen slide_screen:
    frame:
        background "Scene/bg home slide_blank.png"

    frame:
        background None
        yalign 0.28
        xalign 0.28
        text "{color=#000000}{size=+10}{b}[wikipedia_title]{/b}{/size}{/color}"

    frame:
        background None
        xmaximum 800
        yalign 0.5
        xalign 0.53
        text "{color=#000000}{size=+5}[wikipedia_short_paragraph]{/size}{/color}"

    frame:
        background None
        xmaximum 800
        yalign 0.7
        xalign 0.53
        text "{color=#000000}{size=-5}{i}[reference]{/i}{/size}{/color}"




###############################
# Minigames
###############################

# Minigame - Change word with synonyms
# Screenshot version - see folder game\images\customisable_paragraphs\change_essay_synonyms
# Words have to be selected to be replaced by synonyms
screen essay_text:
    default mathematical = None
    default machine = None
    default tape = None
    default table = None
    default model_simplictiy = None
    default algorithm = None
    default turing_machine = None
    default selected_words = 7

    imagemap:
        ground "customisable_paragraphs/change_essay_synonyms/mg_change_essay_synonyms.png"
        idle "customisable_paragraphs/change_essay_synonyms/mg_change_essay_synonyms.png"
        hover "customisable_paragraphs/change_essay_synonyms/mg_change_essay_synonyms hover.png"
        selected_idle "customisable_paragraphs/change_essay_synonyms/mg_change_essay_synonyms selected.png"
        selected_hover "customisable_paragraphs/change_essay_synonyms/mg_change_essay_synonyms selected.png"

        hotspot (407, 233, 200, 27) action [SetScreenVariable("selected_words", selected_words-1), SetScreenVariable("mathematical", True)]
        hotspot (218, 268, 122, 24) action [SetScreenVariable("selected_words", selected_words-1), SetScreenVariable("machine", True)]
        hotspot (912, 268, 69, 26) action [SetScreenVariable("selected_words", selected_words-1), SetScreenVariable("tape", True)]
        hotspot (119, 296, 78, 27) action [SetScreenVariable("selected_words", selected_words-1), SetScreenVariable("table", True)]
        hotspot (433, 296, 307, 27) action [SetScreenVariable("selected_words", selected_words-1), SetScreenVariable("model_simplictiy", True)]
        hotspot (98, 328, 135, 25) action [SetScreenVariable("selected_words", selected_words-1), SetScreenVariable("algorithm", True)]
        hotspot (247, 328, 899, 27) action [SetScreenVariable("selected_words", selected_words-1), SetScreenVariable("turing_machine", True)]

        if selected_words >= 1:
            text "{color=#801a34}Please select [selected_words] more phrases{/color}":
                xalign 0.5
                yalign 0.7
                size 30

        if mathematical and machine and tape and table and model_simplictiy and algorithm and turing_machine:
            imagebutton auto "select_%s.png":
                xalign 0.5
                yalign 0.7
                action Return()
        else:
            textbutton "Skip minigame" xalign 0.88 yalign 0.78 action Return()


# Minigame - Change word with synonyms
# Input string version - see customisable_input_texts -> short_paragraph_referenced/short_paragraph_identified
# Words have to be selected to be replaced by synonyms
style mg_textbutton is button:
    background "#82dbff"              # LightBlue
    hover_background "#1fbcff"

style mg_textbutton_text is text:
    hover_color "#000000"             # DarkerGrey
    outlines [ (0, "#0000FF", 1, 1) ] # Blue
    color "#3B454A" # DarkGrey

screen mg_identify_replace_words:
    default state = "initial"

    frame:
        background "Scene/bg home white.png"

    frame:
        background None
        xmaximum 850
        ymaximum 600
        yalign 0.6
        xalign 0.5
        if state == "initial":
            text "{size=+5}{color=#000000}[short_paragraph_referenced]{/color}{/size}"

        elif state == "identified":
            text "{size=+5}{color=#000000}[short_paragraph_identified]{/color}{/size}"

        frame:
            yalign 0.78
            xalign 0.88
            if state == "initial":
                textbutton "Identify words to replace" action SetScreenVariable("state", "identified") style "mg_textbutton"
            elif state == "identified":
                textbutton "Replace words" action Return() style "mg_textbutton"

# -----------------------------------------------------------------------

# Minigame - Choose the best written essay
# Screenshot version - see folder customisable_paragraphs/essay_choice
screen essay_choice:
    imagemap:
        ground "customisable_paragraphs/essay_choice/bg home essaychoice.png"
        idle "customisable_paragraphs/essay_choice/bg home essaychoice.png"
        hover "customisable_paragraphs/essay_choice/bg home essaychoice hover.png"
        selected_idle "customisable_paragraphs/essay_choice/bg home essaychoice selected.png"
        selected_hover "customisable_paragraphs/essay_choice/bg home essaychoice selected.png"

        hotspot (51, 51, 573, 313) clicked Return("bad")
        hotspot (51, 366, 573, 309) clicked Return("good")
        hotspot (626, 51, 864, 313) clicked Return("mediocre")
        hotspot (626, 366, 603, 309) clicked Return("overtop")

# Minigame - Choose the best written essay
# Input string version - see folder customisable_paragraphs/essay_choice
screen custom_essay_choice:
    imagemap:
        ground "Scene/bg home essaychoice_blank.png"
        idle "Scene/bg home essaychoice_blank.png"
        hover "Scene/bg home essaychoice hover_blank.png"

        hotspot (51, 51, 573, 313) clicked Return("bad")
        hotspot (51, 366, 573, 309) clicked Return("good")
        hotspot (626, 51, 864, 313) clicked Return("mediocre")
        hotspot (626, 366, 603, 309) clicked Return("overtop")

        frame:
            background None
            xmaximum 515
            ymaximum 250
            ypos 55
            xpos 55
            text "{size=-6}{color=#000000}[paragraph_wiki_referenced]{/color}{/size}"

        frame:
            background None
            xmaximum 515
            ymaximum 250
            ypos 370
            xpos 55
            text "{color=#000000}{size=-6}[good_example]{/size}\n\n{size=-11}[references_essays]{/size}{/color}"

        frame:
            background None
            xmaximum 515
            ymaximum 250
            ypos 55
            xpos 630
            text "{color=#000000}{size=-6}[too_many_quotes]{/size}\n\n{size=-11}[references_essays]{/size}{/color}"

        frame:
            background None
            xmaximum 515
            ymaximum 250
            ypos 370
            xpos 630
            text "{color=#000000}{size=-6}[false_synonyms]{/size}\n\n{size=-11}[references_essays]{/size}{/color}"


###################################
# Fabrication
###################################

#################
# Minigames
#################

# Minigame to select the inefficient part of a query
# Screenshot version - see folder customisable_paragraphs/lab_task
screen query_selection:
    imagemap:
        ground "customisable_paragraphs/lab_task/bg home labtask.png"
        idle "customisable_paragraphs/lab_task/bg home labtask.png"
        hover "customisable_paragraphs/lab_task/bg home labtask hover.png"
        selected_idle "customisable_paragraphs/lab_task/bg home labtask selected.png"
        selected_hover "customisable_paragraphs/lab_task/bg home labtask selected.png"

        hotspot (123, 220, 489, 39) clicked Return("False")
        hotspot (123, 269, 316, 39) clicked Return("False")
        hotspot (140, 317, 682, 39) clicked Return("False")
        hotspot (832, 317, 277, 39) clicked Return("False")
        hotspot (123, 364, 728, 39) clicked Return("False")
        hotspot (123, 413, 484, 42) clicked Return("True")
        hotspot (123, 463, 397, 39) clicked Return("False")


# Minigame jigsaw for code assembling
# Based on KimiYoriBaka, https://lemmasoft.renai.us/forums/viewtopic.php?t=12504
screen jigsaw:
    draggroup:
        drag:
            drag_name "00"
            child "empty space.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[0]
        drag:
            drag_name "01"
            child "empty space.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[1]
        drag:
            drag_name "02"
            child "empty space.png"
            draggable False
            xpos coorlistx[0] ypos coorlisty[2]
        drag:
            drag_name "10"
            child "empty space.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[0]
        drag:
            drag_name "11"
            child "empty space.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[1]
        drag:
            drag_name "12"
            child "empty space.png"
            draggable False
            xpos coorlistx[1] ypos coorlisty[2]
        drag:
            drag_name "20"
            child "empty space.png"
            draggable False
            xpos coorlistx[2] ypos coorlisty[0]
        drag:
            drag_name "21"
            child "empty space.png"
            draggable False
            xpos coorlistx[2] ypos coorlisty[1]
        drag:
            drag_name "22"
            child "empty space.png"
            draggable False
            xpos coorlistx[2] ypos coorlisty[2]
        drag:
            drag_name "30"
            child "empty space.png"
            draggable False
            xpos coorlistx[3] ypos coorlisty[0]
        drag:
            drag_name "31"
            child "empty space.png"
            draggable False
            xpos coorlistx[3] ypos coorlisty[1]
        drag:
            drag_name "32"
            child "empty space.png"
            draggable False
            xpos coorlistx[3] ypos coorlisty[2]
        drag:
            drag_name "00 piece"
            child im.Crop("customisable_paragraphs/jigsaw_image.jpg", 0,0, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[0][0] ypos piecelist[0][1]
        drag:
            drag_name "01 piece"
            child im.Crop("customisable_paragraphs/jigsaw_image.jpg", 120,0, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[1][0] ypos piecelist[1][1]
        drag:
            drag_name "02 piece"
            child im.Crop("customisable_paragraphs/jigsaw_image.jpg", 240,0, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[2][0] ypos piecelist[2][1]
        drag:
            drag_name "03 piece"
            child im.Crop("customisable_paragraphs/jigsaw_image.jpg", 360,0, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[3][0] ypos piecelist[3][1]
        drag:
            drag_name "04 piece"
            child im.Crop("customisable_paragraphs/jigsaw_image.jpg", 0,207, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[4][0] ypos piecelist[4][1]
        drag:
            drag_name "05 piece"
            child im.Crop("customisable_paragraphs/jigsaw_image.jpg", 120,207, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[5][0] ypos piecelist[5][1]
        drag:
            drag_name "06 piece"
            child im.Crop("customisable_paragraphs/jigsaw_image.jpg", 240,207, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[6][0] ypos piecelist[6][1]
        drag:
            drag_name "07 piece"
            child im.Crop("customisable_paragraphs/jigsaw_image.jpg", 360,207, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[7][0] ypos piecelist[7][1]
        drag:
            drag_name "08 piece"
            child im.Crop("customisable_paragraphs/jigsaw_image.jpg", 0,414, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[8][0] ypos piecelist[8][1]
        drag:
            drag_name "09 piece"
            child im.Crop("customisable_paragraphs/jigsaw_image.jpg", 120,414, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[9][0] ypos piecelist[9][1]
        drag:
            drag_name "10 piece"
            child im.Crop("customisable_paragraphs/jigsaw_image.jpg", 240,414, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[10][0] ypos piecelist[10][1]
        drag:
            drag_name "11 piece"
            child im.Crop("customisable_paragraphs/jigsaw_image.jpg", 360,414, 120, 207)
            droppable False
            dragged piece_dragged
            xpos piecelist[11][0] ypos piecelist[11][1]
    textbutton "Skip minigame" xalign 0.94 yalign 0.9 action Return("Skipped")


###################################
# Dissertation - Plagiarism
###################################

# Screen to show longer texts with no/transparent background
screen dissertation_text(paragraph, below=False):
    $ input_t = paragraph
    frame:
        background None
        xmaximum 680
        yalign 0.1
        xalign 0.53
        text "{size=-8}{color=#000000}[source_paragraph]{/color}{/size}"
    frame:
        if below:
            background None
            xmaximum 800
            yalign 0.82
            xalign 0.53
            text "{color=#000000}[input_t]{/color}"
        else:
            background None
            xmaximum 800
            yalign 0.5
            xalign 0.53
            text "{color=#000000}[input_t]{/color}"

#####################
# Minigames
#####################

# Minigame - choose the best written paragraph
# Screenshot version - see folder customisable_paragraphs/paragraph_choices
screen paragraph_choice:
    imagemap:
        ground "customisable_paragraphs/paragraph_choices/bg home paragraphchoice.png"
        idle "customisable_paragraphs/paragraph_choices/bg home paragraphchoice.png"
        hover "customisable_paragraphs/paragraph_choices/bg home paragraphchoice hover.png"
        selected_idle "customisable_paragraphs/paragraph_choices/bg home paragraphchoice selected.png"
        selected_hover "customisable_paragraphs/paragraph_choices/bg home paragraphchoice selected.png"

        hotspot (644, 64, 560, 170) clicked Return("paragraph_good")
        hotspot (644, 236, 560, 184) clicked Return("paragraph_patchwritten")
        hotspot (644, 423, 560, 166) clicked Return("mediocre_paragraph_with_reference")

# Minigame - choose the best written paragraph
# Input text version - see customisable_input_texts -> source_paragraph, paragraph_good, paragraph_patchwritten, paragraph_excellent, source_reference
screen custom_paragraph_choice:
    imagemap:
        ground "Scene/bg home paragraphchoice_blank.png"
        idle "Scene/bg home paragraphchoice_blank.png"
        hover "Scene/bg home paragraphchoice hover_blank.png"

        hotspot (644, 64, 560, 170) clicked Return("paragraph_good")
        hotspot (644, 236, 560, 200) clicked Return("paragraph_patchwritten")
        hotspot (644, 433, 560, 170) clicked Return("paragraph_excellent")

        frame:
            background None
            xmaximum 580
            yalign 0.15
            xalign 0.1
            text "{size=-2}{color=#000000}[source_paragraph]{/color}{/size}"

        frame:
            background None
            xsize 510
            ysize 170
            ypos 64
            xpos 1120
            xalign 0.85
            text "{size=-8}{color=#000000}[paragraph_good]{/color}{/size}"

        frame:
            background None
            xsize 510
            ysize 170
            ypos 232
            xpos 1120
            xalign 0.85
            text "{size=-8}{color=#000000}[paragraph_patchwritten]{/color}{/size}"

        frame:
            background None
            xsize 510
            ysize 170
            ypos 436
            xpos 1120
            xalign 0.85
            text "{size=-8}{color=#000000}[paragraph_excellent]{/color}{/size}"

        frame:
            background None
            xsize 510
            xpos 1120
            ypos 602
            xalign 0.85
            text "{size=-12}{color=#000000}[source_reference]{/color}{/size}"

##########
# Helper screens to show paragraphs from customisable_input_texts
##########

# Screen to show chosen paragraph from custom_paragraph_choice minigame
screen show_chosen_paragraph(chosen_paragraph):
    frame:
        background "white"
        xmaximum 600
        ypos 200
        xpos 400
        if chosen_paragraph != cited_paragraph and chosen_paragraph != bad_paragraph:
            text "{size=-4}{color=#000000}[chosen_paragraph]\n\n[source_reference]{/color}{/size}"
        else:
            text "{size=-3}{color=#000000}[chosen_paragraph]{/color}{/size}"


# Screen to show chosen paragraph from custom_paragraph_choice minigame with original source paragraph
screen compare_chosen_paragraph(chosen_paragraph, source=source_paragraph):
    frame:
        background "white"
        xmaximum 510
        xpos 400
        ypos 20
        text "{size=-8}{color=#000000}[source]{/color}{/size}"

    frame:
        background "white"
        xmaximum 510
        ypos 270
        xpos 400
        if chosen_paragraph == cited_paragraph or chosen_paragraph != bad_paragraph:
            text "{size=-6}{color=#000000}[chosen_paragraph]{/color}{/size}"
        else:
            text "{size=-6}{color=#000000}[chosen_paragraph]\n\n[source_reference]{/color}{/size}"
