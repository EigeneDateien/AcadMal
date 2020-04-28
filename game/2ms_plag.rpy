
label start_plag:
    scene bg home2

    #show txtexamp at top
    # show pari happy at right

    show keri happy:
        pos(950, 40)
        zoom 0.6

    p "Hi! You are [povname], right? My name is Pari."

    # show pari talk at right
    show keri talk:
        pos(950, 40)
        zoom 0.6
    p "I'm a new student as well. Everything is so confusing."

    p "For example, everyone is talking about Plagiarism. I didn't know what it was..."

    p "I had to ask the teaching assistant and she explained it to me."

    menu:
        p "Do you know what Plagiarism is?"

        "Taking someone else's work and passing it off as your own":
            $ change_score('plagiarism', +1)
            p "Oh, there is Sara, the TA."
            jump plagiarism_detail
        "Copying a paragraph from a friend's essay without their knowing":
            $ change_score('plagiarism', +1)
            p "Oh, there is Sara, the TA."
            jump plagiarism_detail
        "Copying someone else's work without paraphrasing or using quotation marks around the copied sentence":
            $ change_score('plagiarism', +1)
            p "Oh, there is Sara, the TA."
            jump plagiarism_detail
        "All of the above":
            $ change_score('plagiarism', +3)
            p "Wow, [povname]. That's right! I did not know that all these examples were plagiarism."
            p "Luckily, the TA explained it to me!"
            jump cont_plag



label cont_plag:
    # show pari mhappy at right
    show keri mhappy:
        pos(950, 40)
        zoom 0.6
    pov "Plagarism is such a big deal here."
    "But what if we are really struggling or stuck for time on our essay?"



    #show pari happy at right
    show keri happy:
        pos(950, 40)
        zoom 0.6

    menu:
        p "Do you think it's alright if we really need to do it?"

        "Plagiarism is fine if you need to do it!":
            # show pari sad at right
            show keri sad:
                pos(950, 40)
                zoom 0.6
            $ change_score('j1', -3)
            p "NOOO! Plagiarism could not only lead to a bad mark."
            p "If it is a severe case, you could risk your whole degree!"
            p "Be careful!"
            # HERE SOME MORE DIALOG THAT PLAGIARISM ALWAYS LEADS TO BAD MARKS
        "Plagiarism is always wrong, even if you need to do it!":
            # show pari vhappy at right
            show keri vhappy:
                pos(950, 40)
                zoom 0.6
            "That's right!"
            $ change_score('j2', +1)

    # show pari happy at right
    show keri happy:
        pos(950, 40)
        zoom 0.6

    p "Anyways, it was nice talking to you, [povname]"

    p "See you later!"

    pov "Bye"

    # hide pari happy
    hide keri happy


    pov "Let's see, if we can find some other students to talk to"

    jump patchwriting



label patchwriting:
    scene bg lab

    show alex happy at left

    a "Hello, I'm Alex"

    a "I am an MSc student studying Computer Science here at the University of Manchester."

    show alex talk at left

    a """I have my dissertation due tomorrow and I've still got a paragraph left to write.
    The last assignment I handed in wasn't a very good one either..."""

    a "I need to write something and I need to do it as fast as I can."

    show alex happy at left
    # show paragraph1 at right

    # show logicrep at right

    show logicrep at right

    a "But look at this article... This part of the paragraph is all I need to finish my dissertation."

    show alex talk at right

    a "I just want my dissertation to be finished at last"

    a "I'll just use that and the main idea from this article."

    # show bad_paragraph at right

    a "Finally I'm finished"

    menu:

        a "What do you think? Great, isn't it?"

        "No, not really":

            menu:
                pov "You really need to change something"

                "You need to reference your source text":
                    pass

                "You should put everything in quotation marks":
                    a "But it's my sentence structure and I left some words from the original"
                    a "Maybe I should just reference it"
                    pov "Do at least that"

                "We should ask a TA!":
                    jump patchwriting_minigame


        "Yeah, I think it's fine":
            jump patchwriting_minigame

    # show cited_paragraph at right
    menu:
        a "Now I referenced it. Do you think I should change something?"

        "No, it's perfect now!":
            jump ta_intervention

        "Yes, I think your text is too close to the original":
            a "You are right! I have to use my own words!"
            jump patchwriting_part2

        "Yes, you should just copy the original text. It sounds better!":
            a "Hey, [povname]! Do you want me to get a bad mark? I can't cite a whole paragraph and get a good mark!"
            jump ta_intervention


label patchwriting_part2:
    show paragragh1a at right

    a "Okay that's good. It's entirely in my own words."

    menu:

        a "You don't think I've plagiarised, do you?"

        "No":
            jump noplag1

        "Yeah":
            jump yesplag1



label ta_intervention:
    ta1 "Hey, I heard you two were discussing about correct citation."
    ta1 "By now, you should know about plagiarism"
    ta1 "But do you know what patchwriting is?"
    a "Not at all, can you explain it to us?"
    ta1 "Sure! We don't expect you to know everything here!"
    ta1 "You are encouraged to search for information in order to answer questions or to use in your dissertation"
    ta1 "However, you should always make sure that you don't plagiarise!"
    ta1 "And, if you want good marks, you should avoid patchwriting!"
    pov "So, what is patchwriting then?"
    ta1 "If you find an interesting text or paragraph in a paper, make sure to paraphrase it in your own words"
    ta1 "We want you to understand the information and not just consume it"
    menu:
        ta1 "[povname], what do you think is an example for patchwriting?"

        "If I use the same structure and similiar words as in the original source":
            ta1 "That's correct! Great, [povname]!"
        "If I just copy and paste a text without referencing":
            ta1 "Nooo! That is plagiarism!"
            ta1 "Alex, can you think of an example?"
            a "Well, maybe if I use the same structure and similiar words as in the original source?"
            ta1 "Great, Alex! That's correct!"
    ta1 "So, let's look at an example!"
    jump patchwriting_minigame


label patchwriting_minigame:
    screen white
    show logicrep at left
    ta1 "Let's look at the original source"
    ta1 "And here are some paragraphs that reference this source"
    #show paragraphs at right
    menu:
        ta1 "Which of these paragraphs is an example for patchwriting?"

        "Paragraph 1":
            ta1 "That is not correct! Paragraph 2 is an example for patchwriting"
        "Paragraph 2":
            ta1 "That's correct!"
        "Paragraph 3":
            ta1 "That is not correct! Paragraph 2 is an example for patchwriting"

    ta1 "Even though he referenced the original paragraph, he merely just copied and pasted the text"
    ta1 "Using synonyms and changing the original structure just a tiny bit is bad academic practice"
    ta1 "In this way, we don't know whether the student actually understood what he was writing or was just copying the original source"
    jump patchwriting_part2

label plagiarism_detail:
    show sara at right
    show keri happy:
        pos(120, 40)
        zoom 0.6
    ta1 "Hey, I heard that you two are discussing about plagiarism."
    p "Yes, can you help us understanding the term?"
    ta1 "Don't worry! Most new students are confused about these terms."
    ta1 "There are examples of plagiarism that are more easy to understand"
    ta1 "Can you give us an example for this, [povname]?"
    menu:
        "Passing work done by someone else as my own":
            $ change_score('plagiarism', +1)
            ta1 "Yes, that is a great example!"
            ta1 "Pari, can you think of another example"
            p "Copying a text without using my own works or quotation marks for the copied sentence"
            ta1 "Great! Another example would be to use a text from another student without their knowing"
        "Using a text from another students without their knowing":
            $ change_score('plagiarism', +1)
            ta1 "Yes, that is a great example!"
            ta1 "Pari, can you think of another example"
            p "Copying a text without using my own works or quotation marks for the copied sentence"
            ta1 "Great! It is in general a bad idea to pass in work done by someone else as your own"
        "Copying a text without using my own works or quotation marks for the copied sentence":
            $ change_score('plagiarism', +1)
            ta1 "Yes, that is a great example!"
            ta1 "Pari, can you think of another example"
            p "Using a text from another students without their knowing"
            ta1 "Great! It is in general a bad idea to pass in work done by someone else as your own"
        "All of the above":
            $ change_score('plagiarism', +2)
            ta1 "Right! Great, [povname]! These were all examples for plagiarism"

    hide sara
    jump cont_plag


label noplag1:

    # show alex normal
    $ change_score('noplag1', -2)

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
    $ change_score('failedassignment', -3)

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


    menu:
        "Do you want to try again?"

        "Yes, I can do better!":
            jump patchwriting
        "Yes, but not from the start":
            jump part2
        "No":
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

    $ change_score('yesplag1', 1)

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

    $ change_score('yesplag2', 1)

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

    $ change_score('noidont', -1)

    scene white
    # show alex normal
    a "I don't need to put it in quotation marks - it's in my own words, remember?"

    jump submission

    return

label ohright:
    $ change_score('ohright', 1)
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
    "You won! Well Done :)"

    return


    # This ends the game.

    return
