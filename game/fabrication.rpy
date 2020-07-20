label fabrication:
    scene black
    show text "In the third week, you have your first group work"
    pause
    show text "You are very excited, since you will be working together with Pari and Alex"
    pause
    scene bg home2
    with dissolve
    show keri happy at wideleft, zoom_norm
    show alex happy at wideright, zoom_norm
    show instructor talk:
        xalign 0.5
    s "Hello class. In this lab session you will be working in groups of three"
    s "As shown on blackboard, you can choose your own groups"
    s "In your groups, you can discuss freely, but please do not discuss with other groups"
    s "Your goal for this lab is to come up with optimized queries that are faster then the given queries on the PDF"
    s "For this, you will not only have to write down the queries"
    s "But we want you to test the queries on the lab machines as a proof that they are faster"
    s "Please do not forget to submit these statistics as well as they will make up the most of this week's mark"
    s "If you have any questions, please feel free to ask me or Sara"
    s "We will collect your queries and the statistics at the end of this lab session"
    s "So be sure to work correctly but also fast"
    s "We wish you the best of luck!"
    hide instructor talk
    with fade
    show keri happy:
        xalign 0.1
        linear 2.0 xalign 0.3

    show alex happy:
        xalign 0.9
        linear 2.0 xalign 0.7

    pov "Ok, guys. I guess we work together as a group, right?"
    show keri vhappy at zoomed_in
    p "Of course, [povname]!"
    show keri happy at zoom_norm
    pov "So, does any of you have some experience with this?"
    show alex mhappy at zoomed_in
    a "Yeah, I have done something similiar before"
    show alex surprised
    a "But I am not to sure about the testing"
    a "I have never done these kind of statistics before. And you?"
    show alex happy at zoom_norm
    show keri talk at zoomed_in
    p "This is all new to me. But I am confident that we will succeed"
    show keri happy at zoom_norm
    pov "Let's get to work then!"
    jump query_selection_loop

label query_selection_loop:
    call screen query_selection
    $ return_value = _return
    if return_value == "False":
        show alex sad at zoomed_in
        a "I think it's a different one"
        jump query_selection_loop

    show alex happy:
        xalign 0.7
        zoom 0.7
    "Perfect. So let's create our new query!"

    call start_jigsaw

    jump hurry_up_dialogue

screen query_selection:
    imagemap:
        ground "Scene/bg home queryselection.png"
        idle "Scene/bg home queryselection.png"
        hover "Scene/bg home queryselection hover.png"
        selected_idle "Scene/bg home queryselection selected.png"
        selected_hover "Scene/bg home queryselection selected.png"

        hotspot (123, 220, 489, 39) clicked Return("False")
        hotspot (123, 269, 316, 39) clicked Return("False")
        hotspot (140, 317, 682, 39) clicked Return("False")
        hotspot (832, 317, 277, 39) clicked Return("False")
        hotspot (123, 364, 728, 39) clicked Return("False")
        hotspot (123, 413, 484, 42) clicked Return("True")
        hotspot (123, 463, 397, 39) clicked Return("False")

screen query_choice:
    default query_list = []
    default goal_list = ["select", "from", "(", "select2", "from2", "where2", ")", "t1", "where", ";"]
    imagemap:
        ground "Scene/bg home query choice.png"
        idle "Scene/bg home query choice.png"
        hover "Scene/bg home query choice hover.png"
        selected_idle "Scene/bg home query choice selected.png"
        selected_hover "Scene/bg home query choice selected.png"

        hotspot (925, 198, 230, 25) clicked ToggleSetMembership(query_list, "select")
        hotspot (195, 278, 154, 26) clicked ToggleSetMembership(query_list, "from")
        hotspot (391, 496, 11, 26) clicked ToggleSetMembership(query_list, "(")
        hotspot (423, 592, 306, 26) clicked ToggleSetMembership(query_list, "select2")
        hotspot (168, 132, 133, 26) clicked ToggleSetMembership(query_list, "from2")
        hotspot (789, 425, 335, 26) clicked ToggleSetMembership(query_list, "where2")
        hotspot (222, 431, 11, 26) clicked ToggleSetMembership(query_list, ")")
        hotspot (975, 578, 22, 26) clicked ToggleSetMembership(query_list, "t1")
        hotspot (140, 336, 204, 26) clicked ToggleSetMembership(query_list, "where")
        hotspot (127, 596, 11, 26) clicked ToggleSetMembership(query_list, ";")

        if query_list == goal_list:
            imagebutton auto "select_%s.png":
                xalign 0.5
                yalign 0.7
                action Return()


label hurry_up_dialogue:
    $ fabrication = True
    $ score = calculate_score()
    $ initial_score = score
    $ fab_play += 1
    scene bg home2
    with dissolve
    show keri happy:
        xalign 0.1
        linear 2.0 xalign 0.3

    show alex happy:
        xalign 0.9
        linear 2.0 xalign 0.7
    show keri vhappy at zoom_norm
    show alex vhappy at zoomed_in
    a "YESSS, we did it!"
    a "This query is way faster than the original one"
    show alex vhappy at zoom_norm
    pov "But now we have to obtain the statistics"
    show alex sad
    show keri sad at zoomed_in
    p "Yes, you are right. And we are running out of time"
    p "Does any one of you know how to do this?"
    show keri sad at zoom_norm
    show alex sad at zoomed_in
    a "I have no idea! And you, [povname]?"
    show alex sad at zoom_norm
    pov "No, I'm sorry"
    show keri surprised at zoomed_in
    p "But, we need to get the statistics now!"
    menu:
        p "How do we do it then?"

        "We should try more":
            p "But we are running out of time!"
            jump fabricate_data

        "I don't know! Do you have an idea?":
            jump fabricate_data

        "Maybe we should ask Sara, the TA?":
            jump fabricate_sara


label fabricate_sara:
    $ change_score('asked_sara', +1)
    show alex mhappy at slidewideright
    show keri happy at slidewideleft
    a "Oh, alright. Let's ask Sara the TA."
    show sara happy at top:
        xalign 0.5
    pov "Hey, Sara! Can you give us a hint on how to obtain the statistics"
    show sara mhappy at zoomed_in
    ta1 "Well, you should have a closer look on Blackboard!"
    ta1 "There is a guide on how to obtain the statistical data"
    show sara happy at zoom_norm
    pov "Opps! Thank you, Sara"
    show sara talk at zoomed_in
    ta1 "You're welcome!"
    hide sara talk
    with fade
    show keri happy:
        xalign 0.1
        linear 2.0 xalign 0.3

    show alex happy:
        xalign 0.9
        linear 2.0 xalign 0.7
    pov "Wow, that guide is super complicated!"
    show keri surprised at zoomed_in
    p "I don't know if we can make it in time!"
    p "What do we do now?"
    jump fabricate_data




label fabricate_data:
    show keri mhappy at zoomed_in
    p "I have an idea!"
    p "Look on the statistics of the given queries"
    p "We know that our query is faster and we know how the data should look like!"
    p "And I can't see any TA or instructor around..."
    show keri vhappy
    menu:
        p "Maybe we should just invent some data and submit it"

        "I don't think that this is a good idea":
            jump dialogue_fabrication_good

        "Maybe you are right":
            jump dialogue_fabrication_bad

label dialogue_fabrication_bad:
    $ change_score('fabrication_dialogue_bad', -2)
    show keri happy at zoom_norm
    show alex surprised at zoomed_in
    a "Guys! I don't think this is a good idea!"
    a "Have a look at the slides about academic malpractice"
    show academic_malpractice_tablet at top
    pause
    hide academic_malpractice_tablet
    show alex happy
    show keri surprised at zoomed_in
    p "Hmm, do you think they apply here?"
    menu:
        "Oh yes":
            menu:
                p "Where do they apply then?"

                "It is plagiarism":
                    show keri talk
                    p "We did not copy from anyone!"

                "It is collusion":
                    show keri talk
                    p "It is a group work: we are supposed to work together!"

                "It is fabrication of results":
                    $ change_score('fabrication_recognised', +4)
                    show keri vhappy
                    p "Oh yes, you are right"
                    jump falsification_intro

                "It is falsification of results":
                    show keri talk
                    p "Well, we did not have any results before."

        "No, we don't plagiarise or collude":
            pass
    show keri mhappy
    p "I guess we can continue then"
    call fabrication_fail pass (path="fabrication") from _call_fabrication_fail


label dialogue_fabrication_good:
    $ change_score('fabrication_dialogue_good', +2)
    show keri talk
    p "Oh cmon! We have to get the statistical data!"
    show keri happy at zoom_norm
    pov "I know, but we cannot fabricate the data"
    show keri talk at zoomed_in
    p "But why not?"
    show keri happy at zoom_norm
    show alex talk at zoomed_in
    a "Pari, [povname] is actually right"
    a "Have a look at the slides about academic malpractice"
    show academic_malpractice_tablet at top
    pause
    hide academic_malpractice_tablet
    show alex happy at zoom_norm
    show keri surprised at zoomed_in
    p "Oh, I see. I'm sorry, guys! I didn't knew that"
    show keri happy at zoom_norm
    pov "No worries!"
    jump falsification_intro

label falsification_intro:
    scene black
    with dissolve
    show text "You try some more time and are finally able to obtain the statistical data..."
    pause
    scene bg home2
    show alex happy at zoom_norm, slightright
    show keri vhappy at zoomed_in, slightleft
    p "Yessss! It is working now! Let's look at the statistics"
    show keri sad
    p "Oh no! Our queries are way too slow!"
    p "And we only have a few minutes left"
    p "We will never be able to good mark out of this!"
    menu:
        p "What do we do now?"

        "We should submit it like this":
            jump good_ending

        "We could adjust the numbers":
            jump dialogue_falsification

label dialogue_falsification:
    $ change_score('falsification_proposed', -2)
    show keri sad at zoom_norm
    show alex sad at zoomed_in
    a "Hmm, [povname], I don't think we should do it!"
    a "In the slides I showed you, there was something about falsification of results"
    show academic_malpractice_tablet at top:
        zoom 0.7
    a "See?"
    hide academic_malpractice_tablet

    menu:
        a "I don't think we should fake our results"

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
    with dissolve
    show text "A few days later you meet again at the lab to discuss your queries with the TA Sara"
    pause
    scene bg home2
    show alex surprised at zoom_norm, slightright
    show keri sad at zoomed_in, slightleft
    p "Alex, [povname]! Have you seen our mark?!"
    p "We did get zero points!"
    show keri sad at zoom_norm
    show alex sad at zoom_norm
    show alex sad at slidewideright
    show keri angry at slidewideleft
    p "I want to know why we did get zero points!"
    show sara happy at top:
        xalign 0.5
    p "Sara! Why did we get no points?"
    show sara talk at zoomed_in
    ta1 "Oh hey, I wanted to talk to you either way"
    ta1 "We tested your code and the statistics could in no way be correct! We tried on different machines! We never came even close to your results"
    show sara mhappy
    menu:
        ta1 "Did you guys fake the statistics?"

        "Yes, we did":
            show sara sad at zoom_norm
            show keri sad at zoomed_in
            p "But we were really desperate"

        "No, we didn't":
            show sara angry
            ta1 "Well, then please show me how you obtained the data"
            show sara angry at zoom_norm
            show keri sad at zoomed_in
            p "Okay, yes! We faked the data! But we were really desperate"


    show keri sad at zoom_norm
    show sara talk at zoomed_in
    ta1 "I'm sorry, but this is no excuse!"
    ta1 "You should never fabricate or falsify data. It is bad scientific practice and can even put people in danger"
    ta1 "Wrong statistics could lead to severe damage! So never fake your data"
    ta1 "You are lucky, that we only punished you in this coursework. You could risk your degree!"
    show sara sad at zoom_norm
    show keri talk at zoomed_in
    p "We are sorry! We will never do it again!"
    hide keri
    hide sara
    menu:
        "Do you want to try again?"

        "Yes":
            $ score = calculate_score()
            $ initial_score = score
            if path == "fabrication":
                jump fabricate_data
            if path == "falsification":
                jump falsification_intro

        "No":
            hide keri
            hide alex
            jump fabrication_feedback



label good_ending:
    show alex happy at zoom_norm
    show keri talk at zoomed_in
    p "Hmm, but then we should explain our results"
    show keri happy at zoom_norm
    pov "What do you mean?"
    show keri talk at zoomed_in
    p "Well, we should explain why we think we obtained these results and where the error might be"
    show keri happy at zoom_norm
    show alex vhappy at zoomed_in
    a "That's a great idea, Pari!"
    menu:
        a "[povname], what do you think?"

        "It is a great idea":
            show alex happy at zoom_norm
            show keri vhappy at zoomed_in
            p "Thank you, [povname]"

        "Whatever...":
            pass


    hide keri
    hide alex

    jump fabrication_feedback

label fabrication_feedback:
    $ score = calculate_score()
    $ fabrication_score = score - initial_score
    scene black

    if formative:

        menu:

            "Do you want to know, how well you did?"

            "Yes":

                if fabrication_score >= 2:
                    show text "Congratulations! You did not fabricate or falsify your results!"
                    pause
                    show text "Even if you did not get the wanted results, never falsify or fabricate data. This will lead to zero marks!"
                    pause
                    show text "If you can explain where you might have struggled or why you think you got the results you obtained, we will reward you with positive marks"
                    pause
                elif fabrication_score >= 0:
                    show text "You had some problems understanding fabrication and falsification!"
                    pause
                    show text "Maybe have a look at the definitions again!"
                    pause
                    show text "You should also consider to replay this chapter"
                    pause
                    scene black
                    menu:
                        "Would you like to try again?"

                        "Yes, I can do better":
                            jump fabrication

                        "Yes, but not from the beginning":
                            jump hurry_up_dialogue

                        "Nah, I'm fine":
                            pass
                else:
                    show text "Unfortunately, you commited academic malpractice"
                    pause
                    show text "Please make sure to never fabricate or falsify your data"
                    pause
                    show text "You should really consider to try the fabrication and falsification part again"
                    pause
                    scene black
                    menu:
                        "Would you like to try again?"

                        "Yes, I can do better":
                            jump fabrication

                        "Yes, but not from the beginning":
                            jump hurry_up_dialogue

                        "Nah, I'm fine":
                            pass
            "No":
                pass

    jump dissertation_transition
