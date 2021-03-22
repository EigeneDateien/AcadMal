
init python:
    # label_callback code from: https://lemmasoft.renai.us/forums/viewtopic.php?t=10578

    def label_callback(name, abnormal):
        store.last_label = name
        visiting(last_label)
    config.label_callback = label_callback

    def use_slideviewer(name_slide, max_number_slides):
        slide_name = name_slide
        renpy.call_screen("show_slides")


    def change_score(tagname, v):
        mark(tagname, v)
        visiting(tagname)

    def calculate_score():
        score = 0
        for k,v in scoring.items():
            k1 = getattr(persistent, k)
            if k1 and k1 > 0:
                score += v
        return score

    def visiting(tagname):
        # If we haven't seen this tag before, c == None
        c = getattr(persistent, tagname)
        if c != None:
            setattr(persistent, tagname, c+1)
        else:
        # First time!
            setattr(persistent, tagname, 1)

    def mark(tagname, v):
        if tagname not in scoring.keys():
            scoring[tagname] = 0
        scoring[tagname] += v
        return scoring[tagname]

    def tracked_menu(items, call=False, count=False, suffix=' Again'):
        """items is a list of 2-tuples. First arg is a string
        which is the menu item, second is a label.

        Returns a menu where the blocks are
        labels which are called or jumped too after. If
        the label has been entered before, suffix is added to that
        menu item. NOTE: This will happen even if the reader
        hasn't seen *this* menu before, so it can reveal things."""
        # Technique from https://lemmasoft.renai.us/forums/viewtopic.php?t=30323

        m = []
        for k,v in items:
            c = getattr(persistent, v)
            if c == None:
                m.append((k, v))
            else:
                s = suffix + ' (%d)' % c if count else suffix
                m.append((k + s, v))

        choice = menu(m)
        if call:
            renpy.call(choice)
        else:
            renpy.jump(choice)

    scoring = {}
    comp61511 = True
    markdown_slides = {}
    meet_already = False
    goodwritingbool = False
    plag = False
    collab = False
    fabrication = False
    plag_play = 0
    fab_play = 0
    diss_play = 0
    one_chapter_only = False
    only_plagiarism = False
    only_coll_fab = False
    tutorial_already = False
    upper_right_paragraph_b = False
    lower_right_paragraph_b = False
    lower_left_paragraph_b = False
    chosen_tut_paragraph = ""
    chosen_tut_paragraph2 = ""
    upper_right_paragraph_b2 = False
    lower_right_paragraph_b2 = False
    lower_left_paragraph_b2 = False
    ta_visited = False


python:
    def cond_item(condition, truebranch, falsebranch):
        pass

define p_name = "Pari"
define p = Character(p_name)

define a = Character("Alex")

define ta1 = Character("Sara the TA")

define s = Character("Supervisor")

define e = Character("Eileen")

# image pari composite = Composite(
#     (300, 600),
#     (64, 0), "Curly.png",
#     (0, 30+187), "Baggy Pants.png",
#     (12, 104), "Hoodie.png")

image instructor happy = "instructor/instructor happy.png"
image eileen happy = "eileen happy.png"
image pari happy  = "instructor/instructor happy.png"

image txtexamp = Text("\nHello, World! This is fun\nif you like that sort of\nthing", size=40, justify=True)

image se1q = "seq1.png"
image bg home = "Scene/kilburn-inside2.png"
image bg home2 = "Scene/kilburn-inside.png"
image bg lab = "Scene/kilburn-lab.png"
image bg office = "Scene/kilburn-office.png"
image bg outside = "Scene/bg kilburn outside.png"
image bg kilburn lecture = "Scene/kilburn lecture.png"
image bg kilburn lecture1 = "Scene/kilburn lecture1.png"
image bg home desk = "Scene/bg home desk.png"

define pov = Character("[povname]")

transform flip:
    xzoom -1.0

# The game starts here.

label start:

    scene bg home

    menu:
        "Which device are you playing on?"

        "Laptop/PC":

            python:
                if not persistent.povname:
                    povname = renpy.input("What is your nickname?")
                    povname = povname.strip()
                    if not povname:
                        povname = "Anony M. Ous"
                    persistent.povname = povname
                else:
                     povname = persistent.povname
                     persistent.povname = False

        "Mobile device/tablet":
            python:
                povname = "Player"
                persistent.povname = povname

    jump intro

label intro:
    scene black
    with dissolve
    # show text "The following game consists of three chapters"
    # pause
    # show text "The first chapter will take you around 20 minutes. The whole game will take around 45 minutes"
    # pause
    # show text "You can decide know whether you only want to play one chapter or whether you want to start the game from the beginning"
    # pause
    # show text "When you start the game from the beginning, you can end the game after each of the three chapters"
    # pause
    # show text "When you decide to play only one chapter, you can choose which topic you are most interested in"
    # pause
    # scene black
    # menu:
    #     "Do you want to play only one chapter?"
    #
    #     "Yes, one chapter is enough":
    #         $ one_chapter_only = True
    #
    #         menu:
    #             "Which topic are you more interested in?"
    #
    #             "Plagiarism":
    #                 $ only_plagiarism = True
    #
    #             "Collusion and Fabrication of results":
    #                 $ only_coll_fab = True
    #
    #     "No, I want to start the game from the beginning":
    #         pass


    scene bg home


    "Hi [povname]! Let's start the adventure!"
    jump first_day


    # "Return to the menu" if plag and collab and fabrication

    scene black

    $ score = plagiarism_score + collaboration_score + fabrication_score


    $ MainMenu(confirm=False)()


    return
