
init python:
    # label_callback code from: https://lemmasoft.renai.us/forums/viewtopic.php?t=10578

    def label_callback(name, abnormal):
        store.last_label = name
        visiting(last_label)
    config.label_callback = label_callback


    def change_score(tagname, v):
        mark(tagname, v)
        visiting(tagname)

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


    scoring = {
               'ohright': 1,
               'failedassignment': -1}
    comp61511 = True

python:
    def cond_item(condition, truebranch, falsebranch):
        pass

define p_name = "Pari"
define p = Character(p_name)

define a = Character("Alex")

define ta1 = Character("Sara the TA")

define s = Character("Supervisor")

# image pari composite = Composite(
#     (300, 600),
#     (64, 0), "Curly.png",
#     (0, 30+187), "Baggy Pants.png",
#     (12, 104), "Hoodie.png")

image pari happy  = "Pari/pari happy.png"

image alex happy = "Alex/alex happy.png"

image sara  = "Humaaans/sitting-5.png"

image txtexamp = Text("\nHello, World! This is fun\nif you like that sort of\nthing", size=40, justify=True)

image se1q = Text("\nGive an example of using reverse engineering \nto extract a requirment from an existing program.\nYou should discuss all the steps \nwith specific details.\n\nThis is to be your own work.", size=30, justify=True)

image bg home = "Scene/kilburn-inside2.png"
image bg home2 = "Scene/kilburn-inside.png"
image bg lab = "Scene/kilburn-lab.png"
image bg office = "Scene/kilburn-office.png"
image bg outside = "Scene/bg kilburn outside.png"
image bg plants = "Scene/Plants.png"
define pov = Character("[povname]")

transform flip:
    xzoom -1.0

# The game starts here.

label start:
    scene bg home
    python:
        if not persistent.povname:
            povname = renpy.input("What is your name?")
            povname = povname.strip()
            if not povname:
                povname = "Anony M. Ous"
            persistent.povname = povname
        else:
             povname = persistent.povname
             persistent.povname = False

        score = 0

    "Hi [povname]! Enjoy your explorations!"
    python:
        cs = [("Explore Plagiarism", 'start_plag'),
              ("Explore Collusion", 'start_col'),
              ("Explore Best Pratices", 'start_best')]
        tracked_menu(cs, call=True)

    scene

    # Old version: calculating scoring incorrectly (using all entries in scoring items)
    python:
        tags = ""
        for k,v in scoring.items():
            k1 = getattr(persistent, k)
            if k1 and k1 > 0:
                tags += k + ","
                score += v
    "The tags are [tags]"
    $ val1 = scoring["plagiarism"]
    "The value for plagiarism is [val1]"
    $ val2 = scoring["yesplag1"]
    "The value for yesplag1 is [val2]"

    if score >= 4 and "ask_sara" in scoring.keys():
        "Well done! Always make sure to not validate academic malpractice"
    elif "ask_sara" in scoring.keys() and score < 4:
        "Please make sure to not collaborate on assignments where it is not explicitly stated"
    elif score >= 7:
        "Well done! You are a plagiarism expert!"
        "But please make sure to understand what plagiarism is."
        "When in doubt, ask your TA!"
    #other possibilities

    show text "Your score is [score]!"

    python:
        for k, v in scoring.items():
            scoring[k] = 0
            setattr(persistent, k, None)

    "There is so much to learn."


    return
