
label start_plag:
    scene bg home2
    #show txtexamp at top
    show pari happy at right

    p "Hi! You are [povname], right? My name is Pari."

    show pari talk at right

    p "I'm a new student as well. Everything is so confusing."

    p "For example, everyone is talking about Plagiarism. I didn't know what it was..."

    p "I had to ask the teaching assistant and she explained it to me."

    menu:
        p "Do you know what Plagiarism is?"

        "Taking someone else's work and passing it off as your own":
            pass
        "Copying a paragraph from a friend's essay without their knowing":
                "I think that this is certainly one example of plagiarism"
                jump start_plag
        "Copying someone else's work without paraphrasing or using quotation marks around the copied sentence":
            pass
        "All of the above":
                p "That's right! The TA told me the same!"
                show pari mhappy at right
                pov "Plagarism is such a big deal here."
                "But what if we are really struggling or stuck for time on our essay?"



    show pari happy at right

    menu:
        "Do you think it's alright if we really need to do it?"

        "Plagiarism is fine if you need to do it!":
            show pari sad at right
            call j1 from _call_j1
            # HERE SOME MORE DIALOG THAT PLAGIARISM ALWAYS LEADS TO BAD MARKS
        "Plagiarism is always wrong, even if you need to do it!":
            show pari vhappy at right
            call j2 from _call_j2

    show pari happy at right

    p "Anyways, it was nice talking to you, [povname]"

    p "See you later!"

    pov "Bye"

    hide pari happy

    "Let's see, if we can find some other students to talk to"

    scene bg lab

    show alex happy at left

    a "Hello, I'm Alex"

    a "I am an MSc student studying Computer Science here at the University of Manchester."

    # show alex worried at left

    a """I have my dissertation due tomorrow and I've still got a paragraph left to write.
    The last assignment I handed in wasn't a very good one either..."""

    a "I need to write something and I need to do it as fast as I can."

    # show alex normal at left
    # show paragraph1 at right

    # show logicrep at right

    show logicrep at right

    a "But look at this article... This part of the paragraph is all I need to finish my dissertation."

    # show alex normal

    a "I'll just use that and the main idea from this article."

    # show paragraph1a

    show paragragh1a at right

    a "Okay that's good. It's entirely in my own words."

    menu:

        a "You don't think I've plagiarised, do you?"

        "No":
            jump noplag1

        "Yeah":
            jump yesplag1




label noplag1:

    # show alex normal

    pov "Nope, you haven't copied the text"

    show alex vhappy

    a "Oh good! Phew, my assignment's finally done."

    jump part2

label part2:

    # show alex normal

    a """I could give it to my supervisor to have a read through, but she is very busy and it's very last minute.
    She probably not here right now anyway because it's pretty late."""

menu:

        a "What do you think I should do?"

        "Hand it in.":
            jump failedassignment

        "Check with your Supervisor.":
            jump warning


label failedassignment:

    scene white
    show alex sad

    a "Oh no.. "

    a "I've failed my assignment! But why?"

    a "Wait - My Supervisor said that one of my paragraphs was plagarised."

    show alex angry

    a "You told me that paragraph wasn't plagarised! >:("

    pov "Um.."

    a """Now that I've failed the assignment, I might get a 2:2 at best!
    All my hard work is ruined because of 1 plagarised paragraph..."""

    pov "Sorry Alex.."

    "Alex ignored me. He was devastated."
    "He spent 4 difficult years and thousands of Pounds and he didn't even get a degree at the end of it."


    scene black
    "You Lost. And you're a bad friend. Poor Alex :("


    return

label warning:

    # show supervisor
    scene bg office

    s "Alex - this paragraph is plagarised."

    s "If you hand this in you will fail your assignment..."

    s """I suggest that you reference this paragraph, and if you haven't missed out any other
    references you've used then you should be fine."""

    s "Be careful with your referencing, Alex - you could have failed your assignment!"

    jump goodending


label yesplag1:

    scene white

    show alex surprised
    pov "Yeah, it's still plagiarism if you form a conclusion based on the article and not reference it."

    show alex happy

    a "Oh yeah, I forgot to cite it."

    # show paragraph1b at right

    a "There, how's that?"
    jump submission

label submission:

    scene white
    # show paragraph1b

    menu:

        a "I can hand it in now right?"

        "Yeah, it's okay now":
            jump noplag2

        "No, don't hand it in yet":
            jump yesplag2


label noplag2:
    jump failedassignment


label yesplag2:

    scene white
    pov "You haven't referenced it properly."
    show alex surprised
    a "Why, what's wrong with it?"

    menu:

        pov "You still need to.."

        "Put it in quotation marks":
            jump noidont

        "Reference it again for the second sentence":
            jump ohright

label noidont:

    scene white
    # show alex normal
    a "I don't need to put it in quotation marks - it's in my own words, remember?"

    jump submission

    return

label ohright:
    scene white
    a "Oh right - I forgot about that sentence."

    menu:

        a "Thanks."

        "No  problem.":
            jump goodending

        "Not very good at this, are you?":
            jump goodending

label goodending:

    scene white
    show alex vhappy
    a "I got back my grade for my dissertation!"

    a "Look, I got a First!"

    pov "Congrats!"

    scene black
    "You Won! Well Done :)"

    return


    # This ends the game.

    return

label j1:
    "No!"
    return

label j2:
    "That's right!"
    return
