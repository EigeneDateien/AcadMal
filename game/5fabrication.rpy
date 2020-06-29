label fabrication:
    $ fabrication = True
    $ score = calculate_score()
    $ initial_score = score
    scene bg home2

    "On the third week, Pari and you have a group work together"
    "You are supposed to program an efficient way to query for data"
    "To prove efficiency, you will have to submit statistics about the time needed for querying the data"
    show keri talk:
        pos(950, 40)
        zoom 0.6
    p "Hey. [povname]! We need to hurry up! Tommorow is deadline!"
    p "It is still not working! And I have to go home soon."
    p "We need to get the statistics now!"
    show keri happy:
        pos(950, 40)
        zoom 0.6
    menu:
        "Do you have an idea how we could get the statistics?"

        "We should try more":
            show keri surprised:
                pos(950, 40)
                zoom 0.6
            p "But we are running out of time!"
            jump fabricate_data

        "I don't know! Do you have an idea?":
            jump fabricate_data

label fabricate_data:
    show keri mhappy:
        pos(950, 40)
        zoom 0.6
    p "I can't see any TA or instructor around"
    p "And we both know how the data should look like!"
    show keri vhappy:
        pos(950, 40)
        zoom 0.6
    menu:
        p "Maybe we should just invent some data and submit it"

        "I don't think that this is a good idea":
            jump dialogue_fabrication_good

        "Maybe you are right":
            jump dialogue_fabrication_bad

label dialogue_fabrication_bad:
    $ change_score('fabrication_dialogue_bad', -2)
    show keri surprised:
        pos(950, 40)
        zoom 0.6
    p "Oh, I have just found some slides about academic malpractice"
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
    show keri mhappy:
        pos(950, 40)
        zoom 0.6
    p "You can find them {a=https://documents.manchester.ac.uk/display.aspx?DocID=2870}here{/a}!"
    show keri happy:
        pos(950, 40)
        zoom 0.6
    menu:
        p "Hmm, do you think they apply here?"

        "Oh yes":
            show keri surprised:
                pos(950, 40)
                zoom 0.6
            menu:
                p "Where do they apply then?"

                "It is plagiarism":
                    show keri talk:
                        pos(950, 40)
                        zoom 0.6
                    p "We did not copy from anyone!"

                "It is collusion":
                    show keri talk:
                        pos(950, 40)
                        zoom 0.6
                    p "It is a group work: we are supposed to work together!"

                "It is fabrication of results":
                    $ change_score('fabrication_recognised', +4)
                    show keri vhappy:
                        pos(950, 40)
                        zoom 0.6
                    p "Oh yes, you are right"
                    jump falsification_intro

                "It is falsification of results":
                    show keri talk:
                        pos(950, 40)
                        zoom 0.6
                    p "Well, we did not have any results before."

        "No, we don't plagiarise or collude":
            pass
    show keri mhappy:
        pos(950, 40)
        zoom 0.6
    p "I guess we can continue then"
    call fabrication_fail pass (path="fabrication") from _call_fabrication_fail


label dialogue_fabrication_good:
    $ change_score('fabrication_dialogue_good', +2)
    show keri talk:
        pos(950, 40)
        zoom 0.6
    p "Oh cmon! We have to get the statistical data!"
    show keri happy:
        pos(950, 40)
        zoom 0.6
    pov "I know, but we cannot fabricate the data"
    show keri talk:
        pos(950, 40)
        zoom 0.6
    p "But why not?"
    show keri happy:
        pos(950, 40)
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
    show keri surprised:
        pos(950, 40)
        zoom 0.6
    p "Oh, I see. I'm sorry! I didn't knew that"
    show keri happy:
        pos(950, 40)
        zoom 0.6
    pov "No worries!"
    jump falsification_intro

label falsification_intro:
    scene black
    "Several minutes later"
    scene bg home2
    show keri vhappy:
        pos(950, 40)
        zoom 0.6
    p "Yessss! It is working now! Let's look at the statistics"
    show keri sad:
        pos(950, 40)
        zoom 0.6
    p "Oh no! Our queries are way too slow!"
    menu:
        "What do we do now?"

        "We should submit it like this":
            jump good_ending

        "We could adjust the numbers":
            jump dialogue_falsification

label dialogue_falsification:
    $ change_score('falsification_proposed', -2)
    show keri sad:
        pos(950, 40)
        zoom 0.6
    p "Hmm, [povname], I don't think we should do it!"
    p "In the {a=https://documents.manchester.ac.uk/display.aspx?DocID=2870}document{/a} you showed me, there was something about falsification of results"
    menu:
        p "I don't think we should fake our results"

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
    "One week later"
    scene bg home2
    show keri sad:
        pos(950, 40)
        zoom 0.6
    p "Oh no, we did get zero points!"
    p "Sara! Why did we get no points?"
    show sara talk:
        pos(100, 40)
        zoom 0.6
    ta1 "Oh hey, I wanted to talk to you either way"
    ta1 "We tested your code and the statistics could in no way be correct! We tried on different machines! We never came even close to your results"
    show sara happy:
        pos(100, 40)
        zoom 0.6
    menu:
        ta1 "Did you guys fake the statistics?"

        "Yes, we did":
            p "But we were really desperate"

        "No, we didn't":
            ta1 "Well, then please show me how you obtained the data"
            p "Okay, yes! We faked the data! But we were really desperate"
    show sara mhappy:
        pos(100, 40)
        zoom 0.6
    show sara talk:
        pos(100, 40)
        zoom 0.6
    ta1 "I'm sorry, but this is no excuse!"
    ta1 "You should never fabricate or falsify data. It is bad scientific practice and can even put people in danger"
    ta1 "Wrong statistics could lead to severe damage! So never fake your data"
    ta1 "You are lucky, that we only punished you in this coursework. You could risk your degree!"
    show keri talk:
        pos(950, 40)
        zoom 0.6
    p "We are sorry! We will never do it again!"
    hide keri
    hide sara
    menu:
        "Do you want to try again?"

        "Yes":
            if path == "fabrication":
                jump fabricate_data
            if path == "falsification":
                jump falsification_intro

        "No":
            hide keri
            jump fabrication_feedback



label good_ending:
    show keri talk:
        pos(950, 40)
        zoom 0.6
    p "Hmm, but then we should explain our results"
    show keri happy:
        pos(950, 40)
        zoom 0.6
    pov "What do you mean?"
    menu:
        p "Well, we should explain why we think we obtained these results and where the error might be"

        "That is a great idea":
            p "Thank you, [povname]"

        "Whatever...":
            pass

    scene black

    hide keri

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
                    jump start_plag

                "Nah, I'm fine":
                    pass
    scene black
    "Returning to explorations again"
    jump intro
