label fabrication:
    $ fabrication = True
    $ score = calculate_score()
    $ initial_score = score
    $ fab_play += 1
    scene bg home2

    show alex happy:
        pos(900, 40)
        zoom 0.6

    if meet_already_alex:
        a "Hello, [povname]. Nice to see you again!"
        show alex talk:
            pos(900, 40)
            zoom 0.6
        a "I'm struggling with my dissertation."

    else:
        a "Hello, I'm Alex"
        show alex talk:
            pos(900, 40)
            zoom 0.6
        a "I am an MSc student studying Computer Science here at the University of Manchester."

    $ meet_already_alex = True

    a "My dissertation is due tomorrow! However, I am missing an essential part of my dissertation"
    show alex sad:
        pos(900, 40)
        zoom 0.6
    a "I have to prove that my image recognition algorithm performs faster than any other state of the art algorithm."
    show alex vhappy:
        pos(900, 40)
        zoom 0.6
    a "I know that it performs better, since I have tested it on my own computer."
    show alex sad:
        pos(900, 40)
        zoom 0.6
    a "But my supervisor wants me to obtain the data on the lab computer and it does not work on the lab computer!"


    show alex happy:
        pos(900, 40)
        zoom 0.6
    menu:
        "Do you have an idea how I could get the statistics?"

        "You should try more":
            show alex surprised:
                pos(900, 40)
                zoom 0.6
            p "But I am running out of time!"
            jump fabricate_data

        "I don't know! Do you have an idea?":
            jump fabricate_data

label fabricate_data:
    scene bg home2
    show alex mhappy:
        pos(900, 40)
        zoom 0.6
    a "Well, I know that it performs better than the other algortihms."
    a "For these algorithms, I have the statistics on the lab machine"
    a "So, I know how the statistics of my algorithm would look like"
    show alex vhappy:
        pos(900, 40)
        zoom 0.6
    menu:
        a "Maybe I should just make up the missing data and submit it"

        "I don't think that this is a good idea":
            jump dialogue_fabrication_good

        "Maybe you are right":
            jump dialogue_fabrication_bad

label dialogue_fabrication_bad:
    $ change_score('fabrication_dialogue_bad', -2)
    show alex surprised:
        pos(900, 40)
        zoom 0.6
    a "Oh, I have just found some slides about academic malpractice"
    if preferences.fullscreen == True:
        define b = Character("Helper", kind=nvl)
        b "Hey there, sorry to interupt!"

        b "You are currently playing the game in fullscreen mode which is awesome"

        b "However, we have some linked resources that can help you understand academic malpratice"

        b "If you play in fullscreen mode, you will not see the documents until the end of the game"

        b "You could however play the game in window mode and have a look at the resources"
        menu:
            b "Do you want to turn fullscreen off to have a look on the linked resource"

            "Yes":
                $ preferences.fullscreen = False

            "No":
                b "Alright, then! Please feel free to continue"
    show alex mhappy:
        pos(900, 40)
        zoom 0.6
    a "You can find them {a=https://documents.manchester.ac.uk/display.aspx?DocID=2870}here{/a}!"
    show alex happy:
        pos(900, 40)
        zoom 0.6
    menu:
        a "Hmm, do you think they apply here?"

        "Oh yes":
            show alex surprised:
                pos(900, 40)
                zoom 0.6
            menu:
                a "Where do they apply then?"

                "It is plagiarism":
                    show alex talk:
                        pos(900, 40)
                        zoom 0.6
                    a "I did not copy from anyone!"

                "It is collusion":
                    show alex talk:
                        pos(900, 40)
                        zoom 0.6
                    a "But I am working on my own!"

                "It is fabrication of results":
                    $ change_score('fabrication_recognised', +4)
                    show alex vhappy:
                        pos(900, 40)
                        zoom 0.6
                    a "Oh yes, you are right"
                    jump falsification_intro

                "It is falsification of results":
                    show alex talk:
                        pos(900, 40)
                        zoom 0.6
                    a "Well, I cannot adjust any results without having them first."
                    a "And I do not have the results for my algorithm yet"

        "No, you didn't plagiarise or collude":
            pass
    show alex mhappy:
        pos(900, 40)
        zoom 0.6
    a "I guess we can continue then"
    call fabrication_fail pass (path="fabrication") from _call_fabrication_fail


label dialogue_fabrication_good:
    $ change_score('fabrication_dialogue_good', +2)
    show alex talk:
        pos(900, 40)
        zoom 0.6
    a "Oh cmon! I really have to get the statistical data!"
    show alex happy:
        pos(900, 40)
        zoom 0.6
    pov "I know, but you cannot fabricate the data"
    show alex talk:
        pos(900, 40)
        zoom 0.6
    a "But why not?"
    show alex happy:
        pos(900, 40)
        zoom 0.6
    pov "Fabrication of data is academic malpractice"
    if preferences.fullscreen == True:
        define b = Character("Helper", kind=nvl)
        b "Hey there, sorry to interupt!"

        b "You are currently playing the game in fullscreen mode which is awesome"

        b "However, we have some linked resources that can help you understand academic malpratice"

        b "If you play in fullscreen mode, you will not see the documents until the end of the game"

        b "You could however play the game in window mode and have a look at the resources"
        menu:
            b "Do you want to turn fullscreen off to have a look on the linked resource"

            "Yes":
                $ preferences.fullscreen = False

            "No":
                b "Alright, then! Please feel free to continue"
    pov "You can read about it {a=https://documents.manchester.ac.uk/display.aspx?DocID=2870}here{/a}!"
    show alex surprised:
        pos(900, 40)
        zoom 0.6
    a "Oh, I see. I'm sorry! I didn't knew that"
    show alex happy:
        pos(900, 40)
        zoom 0.6
    pov "This could have been ended badly!"
    pov "With academic malpractice, your dissertation might fail"
    jump falsification_intro

label falsification_intro:
    scene black
    "Several minutes later"
    scene bg home2
    show alex vhappy:
        pos(900, 40)
        zoom 0.6
    a "Yessss! It is working now! Let's look at the statistics"
    show alex sad:
        pos(900, 40)
        zoom 0.6
    a "Oh no! My algorithm is way too slow!"
    menu:
        "What do I do now?"

        "You should submit it like this":
            jump good_ending

        "You could adjust the numbers":
            jump dialogue_falsification

label dialogue_falsification:
    $ change_score('falsification_proposed', -2)
    show alex sad:
        pos(900, 40)
        zoom 0.6
    a "Hmm, [povname], I don't think I should do it!"
    a "In the {a=https://documents.manchester.ac.uk/display.aspx?DocID=2870}document{/a} you showed me, there was something about falsification of results"
    menu:
        a "I don't think I should fake my results"

        "It is okay, they won't notice":
            call fabrication_fail pass (path="falsification") from _call_fabrication_fail_1

        "Yes, you are right!":
            jump good_ending

label fabrication_fail(path="falsification"):
    if path == "fabrication":
        $ change_score('fabrication_fail', -2)
    if path == "falsification":
        $ change_score('falsification_fail', -2)
    scene black
    "Two months later"
    scene bg office
    show alex sad:
        pos(900, 40)
        zoom 0.6
    p "Professor! Why did I fail my dissertation?"
    show instructor talk at left
    s "I wanted to talk to you either way"
    s "We tested your code and the statistics could in no way be correct! We tried on different machines! We never came even close to your results"
    show instructor sad at left
    s "Did you fake the statistics?"
    a "Yes, but I was really desperate"

    s "I'm sorry, but this is no excuse!"
    s "You should never fabricate or falsify data. It is bad scientific practice and can even put people in danger"
    s "Wrong statistics could lead to severe damage! So never fake your data"
    s "You have risked your degree!"
    show alex talk:
        pos(900, 40)
        zoom 0.6
    a "I am sorry! I will never do it again!"
    hide alex
    hide instructor
    menu:
        "Do you want to try again?"

        "Yes":
            if path == "fabrication":
                jump fabricate_data
            if path == "falsification":
                jump falsification_intro

        "No":
            hide alex
            jump fabrication_feedback



label good_ending:
    show alex talk:
        pos(900, 40)
        zoom 0.6
    a "Hmm, but then I should explain my results"
    show alex happy:
        pos(900, 40)
        zoom 0.6
    pov "What do you mean?"
    menu:
        a "Well, I should explain why I think I obtained these results and where the error might be"

        "That is a great idea":
            a "Thank you, [povname]"

        "Yes, of course. You should have done it either way":
            pass

    scene black

    hide alex

    jump fabrication_feedback

label fabrication_feedback:
    $ score = calculate_score()
    $ fabrication_score = score - initial_score
    if formative:
        "Your score is [fabrication_score]!"

        if fabrication_score >= 2:
            "Congratulations! You did not fabricate or falsify your results!"

            "Even if you did not get the wanted results, never falsify or fabricate data. This will lead to zero marks!"

            "If you can explain where you might have struggled or why you think you got the results you obtained, we will reward you with positive marks"
        else:
            "Unfortunately, you commited academic malpractice"
            "Please make sure to never fabricate or falsify your data"
            "You should really consider to try the fabrication and falsification part again"
            menu:
                "Would you like to try again?"

                "Yes, I can do better":
                    jump fabrication

                "Nah, I'm fine":
                    pass
    scene black
    "Returning to explorations again"
    jump intro
