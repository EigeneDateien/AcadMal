init python:

    def piece_dragged(drags, drop):

        if not drop:
            store.piecelist[(int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1]))][0] = drags[0].x
            store.piecelist[(int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1]))][1] = drags[0].y
            return

        store.movedpiece = int(drags[0].drag_name[0]) * 10 + int(drags[0].drag_name[1])
        store.movedplace = [int(drop.drag_name[0]), int(drop.drag_name[1])]

        return True


label fabrication:
    if fabrication_topic == "code":
        jump fabrication_code
    else:
        jump fabrication_survey


label fabrication_code:
    scene black
    pause 0.5
    show text "Chapter 2"
    with dissolve
    pause
    scene black
    pause 0.5
    show text "In the third week, you have your first group work"
    pause
    show text "You are very excited since you will be working together with Pari and Alex"
    pause
    scene bg home2
    with dissolve
    show keri happy at wideleft, zoom_norm
    show alex happy at wideright, zoom_norm
    show instructor talk:
        xalign 0.5
    s "Hello class. In this [practical_part_of_the_course], you will be working in groups of three"
    show instructor mhappy
    s "As shown on Blackboard, you can choose your own groups"
    show instructor talk
    s "You can discuss freely within your groups, but please do not discuss with others"
    show instructor mhappy
    s "Your goal for this [practical_part_of_the_course] is [goal_fabrication_session]"
    $ subtasks = subtask_list
    while len(subtasks) > 0:
        if len(subtasks) % 2:
            show instructor mhappy
        else:
            show instructor talk
        $ subtask = subtasks.pop(0)
        s "[subtask]"

    show instructor talk
    s "If you have any questions, please feel free to ask me or Sara"
    show instructor talk
    s "We wish you the best of luck!"
    hide instructor talk
    with fade
    show keri happy:
        xalign 0.1
        linear 2.0 xalign 0.3

    show alex happy:
        xalign 0.9
        linear 2.0 xalign 0.7

    pov "Ok, guys. I guess we are working together as a group, right?"
    show keri vhappy at zoomed_in
    p "Of course, [povname]!"
    show keri happy at zoom_norm
    pov "So, does any of you have some experience with this?"
    show alex mhappy at zoomed_in
    a "Yeah, I did something similar before"
    show alex surprised
    a "But I am not too sure about the testing"
    show alex talk
    a "I have never done this kind of statistics before. And you?"
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

    call start_jigsaw from _call_start_jigsaw

    jump hurry_up_dialogue

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
    show keri talk
    p "Does anyone of you know how to do this?"
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
    show sara happy at top, zoom_norm:
        xalign 0.5
    pov "Hey, Sara! Can you give us a hint on how to obtain the statistics"
    show sara mhappy at zoomed_in
    ta1 "Well, you should have a closer look on Blackboard!"
    show sara talk
    ta1 "There is a guide on how to obtain the statistical data"
    show sara happy at zoom_norm
    pov "Oops! Thank you, Sara"
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
    show keri talk
    p "Look at the statistics of the given queries"
    show keri mhappy
    p "We know that our query is faster and we know how the data should look like!"
    show keri talk
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
    show alex talk
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
                    p "It is group work: we are supposed to work together!"

                "It is fabrication of results":
                    $ change_score('fabrication_recognised', +4)
                    show keri vhappy
                    p "Oh yes, you are right"
                    jump falsification_intro

                "It is a falsification of results":
                    show keri talk
                    p "Well, we did not have any results before"

        "No, we aren't plagiarising or colluding":
            pass
    show keri mhappy
    p "I guess we can continue then"
    call fabrication_fail pass (path="fabrication") from _call_fabrication_fail


label dialogue_fabrication_good:
    $ change_score('fabrication_dialogue_good', +2)
    show keri talk
    p "Oh, come on! We have to get the statistical data!"
    show keri happy at zoom_norm
    pov "I know, but we cannot fabricate the data"
    show keri talk at zoomed_in
    p "But why not?"
    show keri happy at zoom_norm
    show alex talk at zoomed_in
    a "Pari, [povname] is actually right"
    show alex mhappy
    a "Have a look at the slides about academic malpractice"
    show academic_malpractice_tablet at top
    pause
    hide academic_malpractice_tablet
    show alex happy at zoom_norm
    show keri surprised at zoomed_in
    p "Oh, I see. I'm sorry, guys! I didn't know that"
    show keri happy at zoom_norm
    pov "No worries!"
    jump falsification_intro

label falsification_intro:
    scene black
    with dissolve
    show text "You try some more time and you are finally able to obtain the statistical data..."
    pause
    scene bg home2
    show alex happy at zoom_norm, slightright
    show keri vhappy at zoomed_in, slightleft
    p "Yessss! It is working now! Let's look at the statistics"
    show keri sad
    p "Oh no! Our queries are way too slow!"
    p "And we only have a few minutes left"
    p "We will never be able to get a good mark!"
    show keri talk
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
    show alex talk
    a "In the slides I showed you, there was something about the falsification of results"
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
    $ fabrication = True
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
    p "We got zero points!"
    show keri sad at zoom_norm
    show alex sad at zoom_norm
    show alex sad at slidewideright
    show keri angry at slidewideleft
    p "I want to know why we got zero points!"
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
    show sara angry at zoomed_in
    ta1 "I'm sorry, but this is no excuse!"
    ta1 "You should never fabricate or falsify data. It is bad scientific practice and can even put people in danger"
    show sara talk
    ta1 "Wrong statistics could lead to severe damage! So never fake your data"
    show sara sad
    ta1 "You are risking your degree! You will have to face disciplinary actions for this"
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


label fabrication_survey:
    scene black
    pause 0.5
    show text "Chapter 2"
    with dissolve
    pause
    scene black
    pause 0.5
    show text "During your first semester, you worked on a group project together with your friends Pari and Alex"
    pause
    scene black
    show text "In the project, you conducted a survey. Today is the final seminar. At the end of the this session, you are supposed to hand in your survey report"
    pause
    scene bg home2
    with dissolve
    show keri happy at wideleft, zoom_norm
    show alex happy at wideright, zoom_norm
    show instructor talk:
        xalign 0.5
    s "Hello class. Welcome to the final seminar. Today, you can go through your results again."
    show instructor mhappy
    s "Please remember that you have to hand in after this session"
    show instructor talk
    s "Since most of you might not be too familiar with writing survey reports, we provided you with a template"
    show instructor mhappy
    s "But be aware, that your structure and your results might look different"
    show instructor talk
    s "This is just for you as a guidance"
    show instructor mhappy
    s "If you have any questions, please feel free to ask me or Sara"
    show instructor talk
    s "We will collect your report at the end of this session"
    show instructor mhappy
    s "We wish you the best of luck!"
    hide instructor mhappy
    with fade
    show keri happy:
        xalign 0.1
        linear 2.0 xalign 0.3

    show alex happy:
        xalign 0.9
        linear 2.0 xalign 0.7

    pov "Ok, guys. Did you look at the template before today's session?"
    show keri vhappy at zoomed_in
    p "Of course, [povname]!"
    show keri happy at zoom_norm
    menu:
        "So, do we have to change anything?":
            pass

        "So, our report is finished, I guess?":
            pass
    show alex surprised at zoomed_in
    a "Well, I think we have to look at our reports again. There is a huge difference between our results and the results in the template"
    show alex surprised
    show alex happy at zoom_norm
    show keri talk at zoomed_in
    p "Yes, I think we are missing some data..."
    show keri happy at zoom_norm
    jump to_few_survey_responses


label to_few_survey_responses:
    $ fabrication = True
    $ score = calculate_score()
    $ initial_score = score
    $ fab_play += 1
    scene bg home2
    with dissolve
    show keri happy:
        xalign 0.3

    show alex happy:
        xalign 0.7
    show keri happy at zoom_norm
    show alex sad at zoomed_in
    a "We have too many male participants and not enough female participants!"
    a "In the template it is written, that it is important to have more or less an equal number of male and female participants"
    show alex happy at zoom_norm
    pov "But this is our final lab session!!!"
    show alex sad
    show keri sad at zoomed_in
    p "Yes, you are right. We are running out of time"
    show keri talk
    p "Does anyone know what to do about this?"
    show keri sad at zoom_norm
    show alex sad at zoomed_in
    a "I have no idea! And you, [povname]?"
    show alex sad at zoom_norm
    pov "No, I'm sorry"
    show keri surprised at zoomed_in
    p "But, we need to have more female participants!"
    menu:
        p "How do we do it then?"

        "Hmm, we should do something fast":
            p "Yes, we are running out of time!"
            show keri happy at zoom_norm
            jump survey_fabricate_data

        "I don't know! Do you have an idea?":
            show keri happy at zoom_norm
            jump survey_fabricate_data

        "Maybe we should ask Sara, the TA?":
            show keri happy at zoom_norm
            jump survey_fabricate_sara



label survey_fabricate_sara:
    $ change_score('asked_sara', +1)
    show alex mhappy at slidewideright
    show keri happy at slidewideleft
    a "Oh, alright. Let's ask Sara the TA."
    show sara happy at top, zoom_norm:
        xalign 0.5
    pov "Hey, Sara! We have a problem with out survey. Can you help us out?"
    show sara mhappy at zoomed_in
    ta1 "Sure, what is your problem?!"
    show sara happy at zoom_norm
    show keri talk at zoomed_in
    p "We don't have enough female participants"
    show keri sad at zoom_norm
    show alex sad
    pov "Do you think we will get a bad mark because of this?"
    show sara talk at zoomed_in
    ta1 "Well, to be completely honest with you, this is not ideal"
    show sara mhappy
    ta1 "However, you will not fail. Just make sure to explain what happened"
    hide sara talk
    with fade
    show keri sad:
        xalign 0.1
        linear 2.0 xalign 0.3

    show alex sad:
        xalign 0.9
        linear 2.0 xalign 0.7
    pov "Oh no, that didn't sound too good!"
    show keri surprised at zoomed_in
    p "Yes, what do we do now?"
    jump survey_fabricate_data




label survey_fabricate_data:
    show keri mhappy at zoomed_in
    p "I have an idea!"
    show keri talk
    p "Look at the answers of the template"
    show keri mhappy
    p "We know that our current survey responses are pretty similar. We just don't have enough female participants!"
    show keri talk
    p "But we know how the data is supposed to look like"
    show keri mhappy
    p "And I can't see any TA or instructor around..."
    show keri vhappy
    menu:
        p "Maybe we should just invent some responses and submit it"

        "I don't think that this is a good idea":
            jump survey_dialogue_fabrication_good

        "Maybe you are right":
            jump survey_dialogue_fabrication_bad

label survey_dialogue_fabrication_bad:
    $ change_score('fabrication_dialogue_bad', -2)
    show keri happy at zoom_norm
    show alex surprised at zoomed_in
    a "Guys! I don't think this is a good idea!"
    show alex talk
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
                    p "It is group work: we are supposed to work together!"

                "It is fabrication of results":
                    $ change_score('fabrication_recognised', +4)
                    show keri vhappy
                    p "Oh yes, you are right"
                    jump survey_falsification_intro

                "It is a falsification of results":
                    show keri talk
                    p "Well, we do not change any data. We just add some additonal data"

        "No, we aren't plagiarising or colluding":
            pass
    show keri mhappy
    p "I guess we can continue then"
    call survey_fabrication_fail pass (path="fabrication") from _call_survey_fabrication_fail


label survey_dialogue_fabrication_good:
    $ change_score('fabrication_dialogue_good', +2)
    show keri talk
    p "Oh, come on! We have to get the responses!"
    show keri happy at zoom_norm
    pov "I know, but we cannot fabricate the data"
    show keri talk at zoomed_in
    p "But why not?"
    show keri happy at zoom_norm
    show alex talk at zoomed_in
    # a "Pari, [povname] is actually right"
    a "Pari, Charlie is actually right"
    show alex mhappy
    a "Have a look at the slides about academic malpractice"
    show academic_malpractice_tablet at top
    pause
    hide academic_malpractice_tablet
    show alex happy at zoom_norm
    show keri surprised at zoomed_in
    p "Oh, I see. I'm sorry, guys! I didn't know that"
    show keri happy at zoom_norm
    pov "No worries!"
    jump survey_falsification_intro

label survey_falsification_intro:
    scene black
    with dissolve
    show text "You decide to not invent some data. However, there is still another problem"
    pause
    scene bg home2
    show alex sad at zoom_norm, slightright
    show keri sad at zoomed_in, slightleft
    p "I think we have another problem..."
    p "For one questions, the choices are in the wrong order"
    p "Now, all the answers are mixed up"
    p "But from the template, we can see, how the answers should have been"
    show keri talk
    menu:
        p "What do we do now?"

        "We should submit it like this":
            jump survey_good_ending

        "We could adjust the numbers":
            jump survey_dialogue_falsification

label survey_dialogue_falsification:
    $ change_score('falsification_proposed', -2)
    show keri sad at zoom_norm
    show alex sad at zoomed_in
    a "Hmm, [povname], I don't think we should do it!"
    show alex talk
    a "In the slides I showed you, there was something about the falsification of results"
    show academic_malpractice_tablet at top:
        zoom 0.7
    a "See?"
    hide academic_malpractice_tablet

    menu:
        a "I don't think we should fake our results"

        "It is okay, they won't notice":
            call survey_fabrication_fail pass (path="falsification") from _call_survey_fabrication_fail_1

        "Yes, you are right!":
            jump survey_good_ending

label survey_fabrication_fail(path="falsification"):
    $ fabrication = True
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
    p "We got zero points!"
    show keri sad at zoom_norm
    show alex sad at zoom_norm
    show alex sad at slidewideright
    show keri angry at slidewideleft
    p "I want to know why we got zero points!"
    show sara happy at top:
        xalign 0.5 zoom 0.6
    p "Sara! Why did we get no points?"
    show sara talk at zoomed_in
    ta1 "Oh hey, I wanted to talk to you either way"
    ta1 "We looked at your raw data from before the final lab session and the results in the report"
    show sara mhappy
    menu:
        ta1 "Did you guys fake some of the responses?"

        "Yes, we did":
            show sara sad at zoom_norm
            show keri sad at zoomed_in
            p "But we were really desperate"

        "No, we didn't":
            show sara angry
            ta1 "Well, then please explain to me why the data changed"
            show sara angry at zoom_norm
            show keri sad at zoomed_in
            p "Okay, yes! We faked the data! But we were really desperate"


    show keri sad at zoom_norm
    show sara angry at zoomed_in
    ta1 "I'm sorry, but this is no excuse!"
    ta1 "You should never fabricate or falsify data. It is bad scientific practice and can even put people in danger"
    show sara talk
    ta1 "Wrong statistics could lead to severe damage! So never fake your data"
    show sara sad
    ta1 "You are risking your degree! You will have to face disciplinary actions for this"
    show sara sad at zoom_norm
    show keri talk at zoomed_in
    p "We are sorry! We will never do it again!"
    hide sara
    menu:
        "Do you want to try again?"

        "Yes":
            $ score = calculate_score()
            $ initial_score = score
            if path == "fabrication":
                jump survey_fabricate_data
            if path == "falsification":
                jump survey_falsification_intro

        "No":
            hide keri
            hide alex
            jump fabrication_feedback



label survey_good_ending:
    show alex happy at zoom_norm
    show keri talk at zoomed_in
    p "Hmm, but then we should explain our results"
    show keri happy at zoom_norm
    pov "What do you mean?"
    show keri talk at zoomed_in
    p "Well, we should explain why we think that parts of our data are insufficient and why this could be the case"
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
    scene black
    if not one_chapter_only:
        $ score = calculate_score()
        $ fabrication_score = score - initial_score
        show text "End of Chapter 2"
        with fade
        pause
        scene black
        pause 0.5

        if formative:

            if fabrication_score >= 2:
                show text "Congratulations! You did not fabricate or falsify your results!"
                pause
                show text "Even if you do not manage to get the wanted results, never falsify or fabricate data. This will lead to severe consequences!"
                pause
                show text "If you can explain where you might have struggled or why you think you got the results you obtained, we will reward you with positive marks"
                pause
            elif fabrication_score >= 0:
                show text "You had some problems understanding fabrication and falsification!"
                pause
                show text "Maybe have a look at the definitions again!"
                pause
                show text "You should think about investing more time in understanding the topic"
                pause
                scene black
                menu:
                    "Would you like to have a virtual tutoring?"

                    "Sounds helpful":
                        call introduction_tut
                    "No, thanks":
                        scene black
                        show text "You can still replay the game for a better understanding"
                        pause
                scene black
                menu:
                    "Would you like to try again?"

                    "Yes, I can do better":
                        jump fabrication

                    "Yes, but not from the beginning":
                        if fabrication_topic == "code":
                            jump hurry_up_dialogue
                        else:
                            jump to_few_survey_responses

                    "Nah, I'm fine":
                        pass



            else:
                show text "Unfortunately, you committed academic malpractice"
                pause
                show text "Please make sure to never fabricate or falsify your data"
                pause
                show text "You should really think about investing more time in understanding the topic"
                pause
                scene black
                menu:
                    "Would you like to have a virtual tutoring?"

                    "Sounds helpful":
                        call introduction_tut
                    "No, thanks":
                        scene black
                        show text "You can still replay the game for a better understanding"
                        pause
                scene black
                menu:
                    "Would you like to try again?"

                    "Yes, I can do better":
                        jump fabrication

                    "Yes, but not from the beginning":
                        if fabrication_topic == "code":
                            jump hurry_up_dialogue
                        else:
                            jump to_few_survey_responses

                    "Nah, I'm fine":
                        pass


    if only_coll_fab:
        scene black
        with dissolve
        show text "You have reached the end of the chapter"
        pause
        show text "Thank you very much for playing"
        pause
        return
        return
    scene black
    show text "As before, you can end the game early"
    pause
    show text "In the final short chapter, you will learn about other forms of plagiarism"
    pause
    scene black
    menu:
        "Do you want to continue playing?"

        "Yes, I want to play the last chapter as well":
            jump dissertation_transition

        "No, I want to end the game now":
            return
    return

label puzzle:
    call screen jigsaw
    if ([coorlistx[movedplace[0]], coorlisty[movedplace[1]]] in piecelist):
        python:
            t1 = piecelist[movedpiece]
            t2 = piecelist.index([coorlistx[movedplace[0]], coorlisty[movedplace[1]]])
            piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
            piecelist[t2] = t1
    else:
        $ piecelist[movedpiece] = [coorlistx[movedplace[0]],coorlisty[movedplace[1]]]
    if piecelist == [[coorlistx[0],coorlisty[0]],
                        [coorlistx[1],coorlisty[0]],
                        [coorlistx[2],coorlisty[0]],
                        [coorlistx[3],coorlisty[0]],
                        [coorlistx[0],coorlisty[1]],
                        [coorlistx[1],coorlisty[1]],
                        [coorlistx[2],coorlisty[1]],
                        [coorlistx[3],coorlisty[1]],
                        [coorlistx[0],coorlisty[2]],
                        [coorlistx[1],coorlisty[2]],
                        [coorlistx[2],coorlisty[2]],
                        [coorlistx[3],coorlisty[2]]]:
        return
    elif _return == "Skipped":
        return
    jump puzzle

label start_jigsaw:
    scene bg home jigsaw
    image whole = "jigsaw_image.jpg"
    python:
        coorlistx = [80, 200, 320, 440]
        coorlisty = [55, 263, 469]
        piecelist = [[647,263],[612,465],[884,333],[914,469],[765,241],[572,58],[569,379],[880,338],[818,72],[758,462],[709,57],[985,51]]
        movedpiece = 0
        movedplace = [0, 0]
    jump puzzle
