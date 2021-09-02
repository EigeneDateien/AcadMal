label first_day:
    $ plag_play += 1

    ##################################################################
    # INTRO
    ##################################################################

    scene black
    pause 0.5
    show text "Collusion examples"
    with fade
    pause
    show text "You, [povname], are a student at university"
    pause

    if not alex_pari_intro_seen:
        scene black
        with flashbulb

        show alex happy at zoom_norm, top

        "This is Alex, your best friend at university. He feels pretty confident with everything programming related"

        hide alex happy
        with fade
        show keri happy at zoom_norm, top
        with Dissolve(1.1, alpha=True)

        "And this is Pari, your other best friend. She is excellent at writing!"
        $ alex_pari_intro_seen = True

        jump start_first_day

label start_first_day:
    scene black
    show text "In one of your lectures, you have a lab session where you are supposed to work on your coursework"
    pause
    jump lab_session

label lab_session:
    $ score = calculate_score()
    $ initial_score = score
    scene bg home2
    show alex happy at zoom_norm, wideleft, sitting
    show keri happy at zoom_norm, wideright, sitting
    show instructor mhappy at top
    s "Welcome back! In this [practical_part_of_the_course], you can start with your coursework!"
    show instructor talk at top
    s "Please remember that all coursework in this week in this week is supposed to be done on your own"
    show instructor mhappy at top
    s "We recommend that you first have a look at the essay since most of you might struggle with it the most"
    show instructor happy at top
    show alex surprised:
        zoom 0.7
        yalign -1.0
        xalign 0.1
    a "There will be essays in [study_course]?!"
    show alex surprised:
        zoom 0.6
        yalign -4.0

    menu:
        a "I'm suuuuuper bad at essays"
        "Don't worry, we will help you":
            $ change_score('plagiarism', -1)
        "Shhh, I want to hear what she has to say":
            pass
        "I'm sure they will teach us how to write these essays":
            pass

    hide alex surprised
    show alex happy at zoom_norm, wideleft, sitting
    show instructor mhappy at top
    s "If you have any questions, feel free to ask me or the teaching assistant"
    show instructor talk at top
    s "Speaking of teaching assistants: Sara, would you like to introduce yourself?"
    show instructor happy:
        xalign 0.5
        linear 1.0 xalign 0.35
    pause 0.5
    show sara talk at zoomed_in:
        xalign 0.65
    with Dissolve(0.5, alpha=True)
    ta1 "Thanks! Well, my name is Sara and I am the teaching assistant or short TA"
    show sara mhappy
    ta1 "If you have any questions just ask me"
    show sara talk
    ta1 "I will be here two days a week and you can also ask questions on our online forum Blackboard"
    show sara happy at zoom_norm:
        xalign 0.65
    show instructor talk:
        xalign 0.35
    s "So, that would be all. Let's start our [practical_part_of_the_course] now."
    show instructor mhappy
    s "Everyone has their own computer. Feel free to start your coursework now"
    show instructor talk
    s "But, as I said, I would recommend starting with the essay"
    show instructor mhappy
    s "We will go around now and you can ask us some questions"


    scene black
    with dissolve
    show text "Five minutes later..."
    pause
    jump lab_work

label lab_work:
    scene bg lab
    show alex happy at zoom_norm, slightright
    show keri happy at zoom_norm, slightleft
    "You enter the [practical_room] and choose your seat between Pari and Alex"
    show alex talk at zoomed_in, slightright
    a "Hey, [povname]. Can you help me?"
    show alex happy at zoom_norm, slightright
    pov "Sure, what's up?"
    show alex talk at zoomed_in, slightright
    a "I'm struggling with the essay..."
    show alex mhappy
    a "Have you looked at it yet?"
    show alex happy at zoom_norm, slightright
    pov "No, I will have a look"

    show alex happy at zoom_norm, slidewideright
    show keri happy at zoom_norm, slidewideleft
    if custom_texts:
        show screen text_screen_white("middle")
    else:
        show essay question at truecenter
    "Let me read that"
    show keri mhappy at zoomed_in:
        xalign 0.1
    p "This looks tricky!"
    if custom_texts:
        hide screen text_screen_white
        show screen text_screen_white("below")
    else:
        show essay question:
            yalign 0.5
            linear 1.0 yalign 0.85
    show keri happy at zoom_norm
    menu:
        "It does look tricky. We should divide up the work.":
            if custom_texts:
                hide screen text_screen_white
            else:
                hide essay question
            jump failing
        "It seems straightforward. I'm going to do it on my own.":
            if custom_texts:
                hide screen text_screen_white
            else:
                hide essay question
            show alex angry at zoomed_in
            a "That's not very nice! Be a jerk about it!"
            show alex angry at zoom_norm
            show keri mhappy at zoomed_in
            p "Hey, Alex, calm down! I think [povname] is actually right"
            show keri talk
            p "We are supposed to work on it on our own! But we could ask the TA"
            show keri happy at zoom_norm
            if not custom_texts:
                hide essay question
            jump ask_sara
        "Look! It says it should be our own work. We can't collaborate.":
            if custom_texts:
                hide screen text_screen_white
            else:
                hide essay question
            $ change_score('own_work', +2)
            show alex talk at zoomed_in
            a "I don't think it means we can't work together."
            show alex mhappy
            a "It just means we can't submit the same essay."
            show alex happy at zoom_norm
            menu:
                "You're right. Let's get started.":
                    $ change_score('own_work', -2)
                    if custom_texts:
                        hide screen text_screen_white
                    else:
                        hide essay question
                    jump failing
                "You're wrong. I'm going to work alone.":
                    show alex angry at zoomed_in
                    a "Don't be so rude! I'm sure we can work together!"
                    show alex angry at zoom_norm
                    menu:
                        "Let's ask the TA then":
                            if custom_texts:
                                hide screen text_screen_white
                            jump ask_sara
                        "No, please leave me alone":
                            $ change_score('no_collab', +3)
                            show alex angry at zoomed_in
                            a "Fine! But stop being so rude"
                            show alex angry at zoom_norm
                            pov "I'm sorry, Alex! But we are not allowed to work together!"
                            show keri talk at zoomed_in
                            p "Alex, [povname] is right. It literally says that it should be done individually"
                            if custom_texts:
                                hide screen text_screen_white
                            jump coursework_writing
                "I'm unsure and think we should ask a TA.":
                    if custom_texts:
                        hide screen text_screen_white
                    else:
                        hide essay question
                    jump ask_sara

label failing:
    # intervention by the ta
    if custom_texts:
        hide screen text_screen_white
    else:
        hide essay question
    $ collab = True
    $ change_score('failing_coll', -4)
    show sara mhappy at zoomed_in:
        xalign 0.5
    with dissolve
    ta1 "Hey, you three seem to get along well."
    show sara mhappy at zoom_norm
    show alex vhappy at zoomed_in
    a "Yeah, [povname] is a great working partner"
    show alex vhappy at zoom_norm
    show sara mhappy at zoomed_in

    menu:
        ta1 "Excuse me, you are not working on the essay together, are you?"

        "We are just discussing what to write":
            ta1 "If you don't understand a question or the instructions, you can always ask a TA or the instructor"
            show sara talk
            ta1 "But please don't discuss your answers with each other"
            show sara happy at zoom_norm
            show alex surprised at zoomed_in
            p "But we can work together, right?"
            show alex surprised at zoom_norm

        "We are working on it together, but we will both write an individual text":
            show sara angry at zoomed_in
            ta1 "Please stop that immediately!"
            show sara happy at zoom_norm
            show alex talk at zoomed_in
            p "Why? I thought we could work together on the essay!"
            show alex happy at zoom_norm

        "We are splitting up the work because it is too much":
            show sara angry at zoomed_in
            ta1 "Well, I know that these questions seem hard in the beginning, but please stop working together immediately!"
            show sara happy at zoom_norm
            show alex talk at zoomed_in
            p "Why? I thought we could work together on the essay!"
            show alex happy at zoom_norm

    jump sara_feedback

label ask_sara:
    if custom_texts:
        hide screen text_screen_white
    else:
        hide essay question
    $ change_score('ask_sara', +2)
    show alex mhappy at zoomed_in
    a "Oh, alright. Let's ask Sara the TA."
    show alex talk at zoomed_in
    show sara happy at zoom_norm:
        xalign 0.5

    a "Hey Sara. It's ok if we work together on the short essay SE1, right?"
    show alex mhappy
    a "I mean, as long as the final essays are different?"
    show alex happy at zoom_norm
    jump sara_feedback

label sara_feedback:
    show sara angry at zoomed_in
    ta1 "No! Didn't you see the part of the question where it says:'it must be your own work?'"
    show keri talk at zoomed_in
    show sara happy at zoom_norm
    p "We did, but we were unsure."
    show keri mhappy
    p "Can we discuss the question and give each other feedback?"
    show keri talk
    p "Or does it mean that we have to work individually?"
    show keri happy at zoom_norm
    show sara talk at zoomed_in
    ta1 "That's exactly what it means. You should NOT work together at all on the short essay SE1."
    show sara happy at zoom_norm
    show alex surprised at zoomed_in
    a "Whaaaaat? But if we have a question?"
    show alex surprised at zoom_norm
    show sara talk at zoomed_in
    ta1 "If you have a question or problem, you should ask a TA, email an instructor, or post a question on Blackboard, our online forum."
    show sara mhappy
    ta1 "If you had worked together on SE1 that would have been collusion!"
    show sara talk
    ta1 "You would have gotten zero points on SE1 and a mark on your record."
    show sara mhappy
    ta1 "And it would have had severe consequences"
    show sara happy at zoom_norm
    show keri surprised
    show alex surprised at zoomed_in
    a "Yeek! Thanks for this! I didn't realise."
    show alex surprised at zoom_norm
    "We walk away from Sara."
    hide sara
    show keri talk at zoomed_in
    p "I guess it's a good thing we talked with Sara about this."
    show keri happy at zoom_norm
    show alex talk at zoomed_in
    a "Yeah. But I don't know. It's strange. Today in the lecture, the instructor talked about the importance of collaboration."
    show alex mhappy
    a "What's wrong with working together as long as we each write our own essays?"
    show alex happy at zoom_norm
    menu:
        "Tell Alex that we should just do what we are told":
            jump coursework_writing
        "Ignore Alex for the rest of the day":
            jump coursework_writing
        "Suggest asking Sara again.":
            call se1_collaboration pass (speaker = "Sara") from _call_se1_collaboration
        "Suggest that you ask the instructor":
            call se1_collaboration pass (speaker = "Instructor") from _call_se1_collaboration_1
    return


label se1_collaboration(speaker="Instructor"):
    show alex talk at zoomed_in
    a "That's a good idea! [speaker] should explain what's going on."
    if speaker == "Sara":
        show sara happy:
            zoom 0.6
            xalign 0.5
        $ s1 = ta1
    else:
        show instructor happy:
            xalign 0.5
        $ s1 = s
    show alex happy at zoom_norm
    "We find [speaker] in the lab."
    if speaker == "Sara":
        pov "Hello, we have another question about SE1."
        show sara talk:
            zoom 0.7
            xalign 0.5
    else:
        pov "Hello, we have a question about SE1."
        show instructor talk:
            xalign 0.5

    s1 "Sure, what's up?"

    if speaker == "Sara":
        show sara happy at zoom_norm
    else:
        show instructor happy


    show alex talk at zoomed_in

    a "We know we aren't supposed to work together on SE1, even if we produce different essays."

    show alex mhappy

    a "But we don't understand why. What's wrong with collaboration?"

    show alex happy at zoom_norm

    menu:
        "You add in:"
        "We'll get a worse grade if we can't get some help.":
            pass
        "We'll learn less if we don't work together.":
            pass
        "We've never done something like this before":
            pass

    if speaker == "Sara":
        show sara talk at zoomed_in
    else:
        show instructor talk

    s1 """I understand your concerns.

    We think a lot about how our assignments affect your learning, especially for writing.

    You'll have to do a lot of writing in the program here."""

    s1 "For example, you have other coursework..."

    s1 "...exams..."

    s1 "...and your dissertation to write."

    if speaker == "Sara":
        show sara happy at zoom_norm
    else:
        show instructor happy

    menu:
        "But we can get help for those, right?":
            pass
        "We're doomed!!!":
            if speaker == "Sara":
                show sara talk at zoomed_in
            else:
                show instructor talk
            s1 "You aren't doomed."
    if speaker == "Sara":
        show sara talk at zoomed_in
    else:
        show instructor talk
    s1 """You can get various sorts of help, but not always before you submitted your coursework.

    For example, consider exams."""
    #TODO: show exam situation
    s1 """Many exams have short essays on them. You need to formulate an answer, by yourself, with a lot of time pressure.

    You can get help revising for your exam, but no help during the exam.

    And the best way to get better at writing is to practice it."""

    if speaker == "Sara":
        show sara happy at zoom_norm
    else:
        show instructor happy

    menu:
        "But we don't even know how to get started on SE1!":
            if speaker == "Sara":
                show sara talk
            else:
                show instructor talk
            s1 "If you want, we can talk individually and I will answer your questions as far as possible"
        "We'll lose points if we don't get help now!":
            if speaker == "Sara":
                show sara talk
            else:
                show instructor talk
            s1 "Part of the assignment is to figure out how to start and what an essay should entail"
            s1 "This way, you will learn the most"
            s1 "And you will get helpful feedback after the submission so that you know what to improve next time"
        "What sort of help are we going to get?":
            if speaker == "Sara":
                show sara talk
            else:
                show instructor talk
            s1 "First, you can always ask a TA or an instructor for help."
            s1 "We know how much aid to give without breaking the value of the assignment."
            if comp61511:
                s1 "Next, in a lab after submitting SE1, we'll have an exercise where we will do some peer review."

    jump coursework_writing






label coursework_writing:
    scene black
    with dissolve
    show text "Some time later..."
    pause

    scene bg lab
    show alex happy at zoom_norm, wideleft
    show keri happy at zoom_norm, wideright
    show instructor talk at top
    s "So, class! Our [practical_part_of_the_course] is over now"
    show instructor mhappy
    s "However, you can still ask some questions via Blackboard"
    show instructor talk
    s "Sara, the TA, will be here for two days over the week"
    show instructor mhappy
    s "Otherwise, I will see you next week!"
    hide instructor
    show alex happy at zoom_norm:
        xalign 0.1
        linear 1.0 xalign 0.35
    show keri happy at zoom_norm:
        xalign 0.9
        linear 1.0 xalign 0.65
    "I'm really hungry and want to go home"
    pov "Hey, Pari, Alex! I think I will go home now!"
    pov "We will be in touch!"
    show keri talk at zoomed_in
    p "See you, [povname]!"
    show keri happy at zoom_norm
    show alex talk at zoomed_in
    a "Bye, [povname]!"

    scene black
    with dissolve
    show text "You go home and write the essay"
    pause
    show text "One day before the deadline, you get a message from Alex"
    pause
    scene bg home desk
    with dissolve
    jump alex_emergency

label alex_emergency:
    # https://lemmasoft.renai.us/forums/viewtopic.php?t=40245
    call phone_start from _call_phone_start
    call message_start("Alex", "Hey [povname], I need your help!!!") from _call_message_start
    pause
    call message_start("Alex", "Can you come to the Lab please?!") from _call_message_start_1
    call screen phone_reply("Of course, Alex!","choice1","I'm sorry, Alex! I have no time","choice2")

label choice1:
    call message_start("Alex", "Thank youuuuuu, [povname]!!!!") from _call_message_start_2
    call message("Alex", "") from _call_message
    call phone_after_menu from _call_phone_after_menu
    jump one_day_before

label choice2:
    call message_start("Alex", "[povname]! Please! You have to help me!") from _call_message_start_3
    call reply_message("Fine, I'll come") from _call_reply_message_1
    pause
    hide reply_message
    call message_start("Alex", "Thank youuuuuu, [povname]!!!!") from _call_message_start_4
    call message("Alex", "") from _call_message_5
    call phone_after_menu from _call_phone_after_menu_1
    jump one_day_before


label one_day_before:
    scene black
    with dissolve
    show text "You meet Alex one day before the deadline"
    pause
    scene bg home2
    show alex sad at zoomed_in, top

    a "Hey, [povname]! I'm still struggling with the essay. And I can't reach the TAs! I really need your help!"

    menu:
        a "Could you show me your essay and give me some tips on what to write?"

        "Yes, of course":
            show alex vhappy
            a "Great, let me compare our essays"
            jump near_miss

        "I'm sorry, Alex, but I am not allowed to help you":
            a "Please, I need you! Don't be like that! I will fail the essay without your help!"
            menu:
                a "Just let me have a look what you have written"

                "Okay, but don't copy anything":
                    jump near_miss

                "No, I'm sorry, Alex!":
                    $ change_score('no_collab_final', +2)
                    "You did not help Alex"
                    "Alex failed his essay, but you got a high mark for your essay"
                    jump good_end

label near_miss:
    # alex will use the same ideas
    show alex vhappy
    a "Thank you, [povname]! You are a lifesaver"
    show alex talk
    a "This is such a great help! Your essay is way better than mine!"
    show alex vhappy at zoom_norm
    pov "But don't copy my text"
    show alex talk at zoomed_in
    a "No worries, I will rewrite it and use my own words"
    jump collusion


label collusion:
    $ change_score('collusion', -4)
    $ collab = True
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home2
    show alex angry at zoomed_in:
        xalign 0.5
    a "[povname]! Have you seen the marks? I got zero points! What did you get?"
    show alex angry at zoom_norm
    pov "Let me check..."
    pov "Oh no! I also got zero points. But why?"
    show alex sad at slightright, zoom_norm
    show keri happy at slightleft, zoom_norm
    with dissolve
    pov "Hey, Pari! What did you get on your essay?"
    show keri mhappy at zoomed_in
    p "I got full points... And you?"
    show keri happy at zoom_norm
    pov "Alex and I got zero points"
    show keri surprised at zoomed_in
    p "Whaaat? What did you guys do?!"
    show keri happy at slidewideleft, zoom_norm
    show alex at slidewideright

    show sara mhappy at top, zoomed_in
    with Dissolve(1.1, alpha=True)
    ta1 "Alex, [povname]? Can I talk to you?"
    ta1 "Pari? Can you give us a minute?"
    show sara happy at zoom_norm
    show keri talk at zoomed_in
    p "Of course!"
    show keri happy:
        zoom 0.6
        xalign 0.25
        linear 3.0 xalign -1.0
    pause 0.5
    show sara happy at slideleft
    show alex sad at zoomed_in
    a "Sara, why do we have zero points?"
    show alex sad at zoom_norm
    show sara talk at zoomed_in
    ta1 "We found that your essays were very alike! You even made the same mistakes"
    show sara mhappy
    ta1 "Did you two work together on the essay or compare your essays?"
    show sara happy at zoom_norm
    pov "Yes, we compared them, but we wrote different essays"
    show sara talk at zoomed_in
    ta1 "Thank you for your honesty, [povname]. As I told you before, it was supposed to be individual coursework"
    show sara mhappy
    ta1 "We wanted to see how well you understand the topic. But each of you and not just one of you"
    show sara talk
    ta1 "You will now face consequences in addition to zero marks on this coursework"
    menu:
        ta1 "And beware! If you commit any academic malpractice again, it will have even more severe effects"

        "Can you tell us more about it?":
            ta1 "Yes, of course"
            jump school_comitee
        "We are sorry! We won't do it again!":
            hide sara
            show alex sad:
                xalign 0.5 zoom 0.7
            a "I'm sorry, [povname]"
            scene black
            jump tutoring_end


label school_comitee:
    # having to speak in front of the school commitee
    show sara talk at zoomed_in
    ta1 "If you commit academic malpractice, there will be a chain of escalation"
    show sara happy at zoom_norm
    pov "And what will happen?"
    show sara talk at zoomed_in
    ta1 "Your case will be taken to a disciplinary panel and you will most likely be disciplined"
    if preferences.fullscreen == True:
        define b = Character("Helper", kind=nvl)
        b "Hey there, sorry to interrupt!"

        b "You are currently playing the game in fullscreen mode which is awesome"

        b "However, we have some linked resources that can help you understand academic malpractice"

        b "If you play in fullscreen mode, you will not see the documents until the end of the game"

        b "You could, however, play the game in window mode and have a look at the resources"
        menu:
            b "Do you want to turn fullscreen off to have a look at the linked resource?"

            "Yes":
                $ preferences.fullscreen = False

            "No":
                b "Alright, then! Please feel free to continue"

    show sara talk at zoomed_in
    ta1 "You can read about it here: {a=http://documents.manchester.ac.uk/display.aspx?DocID=639}Academic Malpractice Procedure{/a}!"
    hide sara
    scene black
    show text "You commited academic malpractice"
    pause
    hide text
    jump tutoring_end

label tutoring_end:
    scene black
    show text "It is strongly recommended that you attend a virtual tutoring about collusion"
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
        "Do you want to try again?"

        "Yes":
            jump one_day_before

        "No":
            pass

    scene black
    show text "End of collusion examples"
    pause
    show text "Feel free to click Continue below to advance"
    pause
    show text "Otherwise, the game will restart automatically"
    pause
    return

label good_end:
    scene black
    show text "Excellent! You did not commit collusion"
    pause
    show text "Feel free to click Continue below to advance"
    pause
    show text "Otherwise, the game will restart automatically"
    pause
    return
