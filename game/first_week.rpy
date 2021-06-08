
label first_day:
    $ plag_play += 1

    ##################################################################
    # INTRO
    ##################################################################

    scene black
    pause 0.5
    show text "Chapter 1"
    with fade
    pause
    show text "You, [povname], are a new [study_course] student at the [university_name]"
    pause
    show text "At first, you were really nervous!"
    pause
    show text "Studying in a new city, a new environment"
    pause

    show text "But luckily, you found some new friends during Welcome Week"
    pause

    scene black
    with flashbulb


    show alex happy at zoom_norm, top

    "This is Alex, your best friend at university. He feels pretty confident with everything hands-on"

    hide alex happy
    with fade
    show keri happy at zoom_norm, top
    with Dissolve(1.1, alpha=True)

    "And this is Pari, your other best friend. She is excellent at writing!"
    show keri happy at zoom_norm, slideleft
    show alex happy at zoom_norm:
        xalign 0.75
    with Dissolve(1.1, alpha=True)


    scene black
    show keri happy at zoom_norm, slideleft
    show alex happy at zoom_norm:
        xalign 0.75
    "The three of you arranged to meet outside the university on the first day"
    jump start_first_day

label start_first_day:
    scene bg outside
    with flashbulb

    show keri happy at zoom_norm, slightleft
    show alex mhappy at zoom_norm, slightright
    pause 0.5
    show screen skip_button
    show alex mhappy at zoomed_in, slightright
    a "Hey, [povname]"
    show keri mhappy at zoomed_in, slightleft
    show alex happy at zoom_norm, slightright
    p "Heeyyy, [povname], how are you?"

    show keri happy at zoom_norm, slightleft

    menu:
        "Hey, Pari, hey, Alex! I'm a bit nervous, to be honest":
            show keri mhappy at zoomed_in, slightleft
            p "Yeah, me as well!"
            show keri mhappy at zoom_norm, slightleft

        "Hey, Pari, hey, Alex! I'm super excited!":
            show alex mhappy at zoomed_in, slightright
            a "Yessss, I'm really looking forward to our first lecture"
            show alex happy at zoom_norm, slightright

    show alex mhappy at zoomed_in, slightright
    a "Let's go inside! Shall we?"
    show keri talk at zoomed_in, slightleft
    show alex happy at zoom_norm, slightright
    p "Yesss!"
    show keri happy at zoom_norm, slightleft

    "You enter the lecture hall with your friends"

    hide screen skip_button

    scene bg lectureroom1
    pause 1.0
    show screen skip_button
    show alex vhappy at zoomed_in, top
    a "I am so excited!!!"
    show alex happy at zoom_norm, slightright
    show keri talk at zoomed_in, slightleft
    with Dissolve(0.5, alpha=True)
    p "Let's take a seat already"

    scene bg lectureroom
    show alex happy at zoom_norm, slightright, sitting
    show keri happy at zoom_norm, slightleft, sitting
    pov "I'm curious what this lecture is all about..."
    hide screen skip_button

    scene bg lectureroom
    with flashbulb
    show alex happy at zoom_norm, wideright, sitting
    show keri happy at zoom_norm, wideleft, sitting

    show instructor talk at top
    show screen skip_button
    s "Good morning, class!"
    show instructor mhappy
    s "Before we start, let's give you some facts about this course!"
    show instructor talk
    s "In the morning we will have a lecture. And after the lunch break, we will go to the [practical_room] to do some practical work"
    show instructor mhappy
    s "You will have some coursework that you can start during the [practical_part_of_the_course]"
    show instructor talk
    s "And you can ask questions to the teaching assistants and me, your instructor"
    show instructor mhappy
    s "So, let's make a start..."
    hide screen skip_button
    scene black
    with dissolve
    show text "After the lecture..."
    pause
    scene bg lectureroom
    with flashbulb
    show screen skip_button
    show alex happy at zoom_norm, wideright, sitting
    show keri happy at zoom_norm, wideleft, sitting
    show instructor talk at top

    s "So that was our lecture part! I will see you after the lunch break in the [practical_room]!"
    hide screen skip_button

    scene black
    with dissolve
    show text "You spend the lunch break with Pari and Alex"
    pause

    scene bg home
    show keri angry at zoomed_in, slightleft
    p "Alex! [povname]! Hurry up, we will be late!"
    show keri angry at zoom_norm, slightleft
    show alex happy at zoom_norm, slightright
    menu:
        "Coming!":
            pass
        "Let's get ourselves some seats":
            pass
    scene black
    show text "The [practical_part_of_the_course] begins..."
    pause
    jump lab_session

label skipped_intro:
    hide screen skip_button
    scene black
    show text "After a lecture in the morning, you have a [practical_part_of_the_course] in the afternoon"
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
                s1 "Next, in a [practical_part_of_the_course] after submitting SE1, we'll have an exercise where we will do some peer review."

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
    show text "You go home and fall asleep almost immediately"
    pause
    show text "Tomorrow, you will try to write the essay"
    pause

    # Assessment of how well student performed
    jump essay_writing_mg

label essay_writing_mg:


    scene bg home desk
    with dissolve
    pov "Ok, let's see the essay question again"
    pov "I hope I can answer it correctly"
    scene bg home laptop
    if custom_texts:
        show screen text_screen(essay_question)
    else:
        show essay question:
            yalign 0.11
            xalign 0.5
    pause

    pov "Hmm, I should [essay_question_short]"

    menu:
        "What should I do first?"

        "Look it up on Wikipedia":
            jump wikipedia_storyline

        "Look it up on the slides":
            jump slides_storyline



label wikipedia_storyline:
    $ slides = False
    pov "I could copy the answer from Wikipedia!"
    if custom_texts:
        hide screen text_screen
        show screen wikipedia_screen
    else:
        hide essay question
        show essay source wikipedia

    with dissolve
    pov "Indeed, it seems like the first paragraph does the job!"
    jump cut_and_paste

label slides_storyline:
    $ slides = True
    pov "I will have a look at the slides"
    if custom_texts:
        hide screen text_screen
        window hide
        show screen slide_screen
        with dissolve
    else:
        hide essay question
        window hide
        show essay source slide
        with dissolve
    pause 1.0
    pov "Perfect, I found the right slide!"
    pov "Indeed, this is the exact paragraph I need!"
    pov "Oh, and it's taken from Wikipedia"
    jump cut_and_paste


label cut_and_paste:
    pov "I could cut and paste it and have an answer!"

    if custom_texts:
        hide screen wikipedia_screen
        hide screen slide_screen
        show screen text_screen(wikipedia_short_paragraph)
    else:
        hide essay source slide
        show 1essaytext_copied_source_text

    pov "Hmm, I should clean it up a bit! Just getting rid of the footnote markers."

    if custom_texts:
        hide text_screen
        show screen text_screen(short_paragraph_cleaned)
    else:
        show 2essaytext_no_footnotes

    pov "Perfect! Now, it looks like a pretty decent answer!"

    pov "Should I do anything else? I think it is common knowledge since it can be also found in the slides"

    pov "But the text is not mine, so should I reference it?"

    scene bg home white
    if custom_texts:
        hide text_screen
        show screen text_screen(short_paragraph_cleaned, "below")
    else:
        show 2_5essaytext_no_footnotes_below

    menu:

        "No, it's common knowledge, so I guess it's fine!":
            $ change_score('plagiarism', -1)
            $ change_score('passivity', -1)
            if custom_texts:
                hide screen text_screen
            jump failed_essay
        "Hmm, maybe I should cite my source":
            $ change_score('plagiarism', +1)
            if custom_texts:
                hide screen text_screen
                show screen text_screen(short_paragraph_cleaned, "middle")
            else:
                show 2essaytext_no_footnotes
            pov "Let's fix that citation issue!"
            call .plag(True) from _call_theory_plag

        "Well, that's a good start but I should do way more":
            $ change_score('plagiarism', +2)
            if custom_texts:
                hide screen text_screen
                show screen text_screen(short_paragraph_cleaned, "middle")
            else:
                show 2essaytext_no_footnotes
            pov "Let's start with the citation problem first"
            jump .plag

label .plag(only_one=False):
    pov "These are not my original words!"
    pov "So I guess I should reference it properly"
    if custom_texts:
        hide screen text_screen
        show screen text_screen(short_paragraph_referenced, "middle")
    else:
        show 3essaytext_reference_wikipedia
    pov "Perfect! Now I have referenced it properly"
    pov "I wonder if this is sufficient"
    pov "I found the right paragraph which actually answers the question, so this is fine"

    pov "But should I try to write it in my own words?"
    pov "I am a bit anxious about my English"


    menu:
        "I think I should leave it like that.":
            $ change_score('passivity', -2)
            if custom_texts:
                hide screen text_screen
            jump bad_essay
        "I should write it in my own words for a better grade.":
            $ change_score('plagiarism', +1)
    jump .passive

label .passive:
    pov "Honestly, I didn't do much until now!"
    pov "I just searched and retrieved a paragraph. But I didn't learn anything about the [essay_topic]."
    pov "Let me use some synonyms"
    "In the following minigame, you have to select the words you want to change"
    jump selection_mg

label selection_mg:
    if custom_texts:
        hide screen text_screen
        call screen mg_identify_replace_words
        show screen text_screen(short_paragraph_replaced, "middle")
    else:
        call screen essay_text
        pov "Let's change up these words with synonyms"
        show 4essaytext_synonyms_before
    pov "Ahh, great! Now my text is different from the original text"
    pov "Now let's get rid of the quotation marks and reference the original text."
    pov "Let's have another look"
    if custom_texts:
        hide screen text_screen
        show screen text_screen(paragraph_wiki_referenced, "middle")
    else:
        show 4essaytext_synonyms
    pov "Well, that is indeed a pretty good paragraph"
    if custom_texts:
        hide screen text_screen
        show screen text_screen(paragraph_wiki_referenced, "up")
    else:
        show 4essaytext_synonyms_top
    menu:
        pov "Should I do anything else?"

        "No, I'm finally done with everything!":
            if custom_texts:
                hide screen text_screen
            jump bad_essay_selected

        "I should write a text completely in my own words":
            jump avoid_patchwriting



label avoid_patchwriting:
    pov "Okay, let me try to paraphrase the paragraph in my own words"
    pov "I will try different approaches"
    "Please select the paragraph that you think fits best"
    if custom_texts:
        hide screen text_screen
        call screen custom_essay_choice
    else:
        call screen essay_choice
    $ essay_chosen = _return
    if only_plagiarism:
        jump essay_feedback
    else:
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
    call message_start("Alex", "Wow, [povname]! You never have time for me :(") from _call_message_start_3
    call message("Alex", "") from _call_message_1
    call phone_after_menu from _call_phone_after_menu_1
    jump essay_feedback


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
                    # """Well done! You did not commit collusion. However, be sure to be polite and explain to your fellow students
                    # why you are not allowed to help them with their individual coursework. And of course, you can and should help your fellow students
                    # for everything that is not related to individual work."""
                    jump essay_feedback

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
            menu:
                "Do you want to try again?"

                "Yes":
                    jump one_day_before

                "No":
                    scene black
                    jump failed_coursework


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
    menu:
        "Do you want to try again?"

        "Yes":
            jump one_day_before

        "No":
            jump failed_coursework


label bad_essay:
    $ change_score('bad_essay', -1)
    $ plag = True
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home2
    show alex angry at zoomed_in:
        xalign 0.5
    a "[povname]! Have you seen the marks? I got low points! What did you get?"
    show alex angry at zoom_norm
    pov "Let me check..."
    pov "Oh no! I also have only a few points. But why?"
    show alex sad at slightright, zoom_norm
    show keri happy at slightleft, zoom_norm
    with dissolve
    pov "Hey, Pari! What did you get on your essay?"
    show keri mhappy at zoomed_in
    p "I got full points... And you?"
    show keri happy at zoom_norm
    pov "Alex and I only got a few points"
    show keri surprised at zoomed_in
    p "Whaaat? What did you guys do?!"
    show keri happy at zoom_norm
    pov "I don't know..."
    pov "I will go to Sara and ask her. I will be back in a minute"
    show keri mhappy at zoomed_in
    p "Good Luck, [povname]"
    scene bg home2
    with dissolve
    show sara happy at top, zoom_norm
    pov "Hey, Sara? Can I talk to you?"
    show sara talk at zoomed_in
    ta1 "Sure, what do you want to talk about?"
    show sara happy at zoom_norm
    pov "About my essay. I don't understand why I only have so few points"
    show sara talk at zoomed_in
    ta1 "I see. Well, to be honest, you were lucky"
    show sara mhappy
    ta1 "You closely copied the source paragraph but at least you referenced it"
    menu:
        ta1 "What do you think? Why did you get only a few points out of it?"

        "I didn't put much effort into it":
            ta1 "Yes, and that is part of the problem"

        "I don't know! I looked up the information and gave the correct answer!":
            show sara surprised at zoom_norm
            pov "What was wrong with it?"
            show sara mhappy at zoomed_in
            ta1 "Well, [povname]. Let me explain it to you"

    show sara talk
    ta1 "We were not assessing your googling skills"
    show sara mhappy
    ta1 "We expected you to look up the information"
    show sara happy at zoom_norm
    menu:
        "Which I correctly did":
            show sara mhappy at zoomed_in
            ta1 "Yes, but we wanted you to understand the information"

        "So, what was wrong?":
            show sara mhappy at zoomed_in
            ta1 "We wanted you to understand the information"
    menu:
        "So, copying and referencing a paragraph was not enough?":
            ta1 "Exactly!"

        "Well, I understood the information!":
            ta1 "I'm not saying that you didn't"
            show sara talk
            ta1 "But with just copying and referencing we can't see that you did"
    show sara mhappy
    ta1 "That way, you spent more time referencing the paragraph than actually thinking about the content"
    show sara talk
    ta1 "Even, when you change some words or the structure of the text, this is not sufficient for a high mark"
    show sara happy at zoom_norm
    pov "So what should I have done?"
    show sara talk at zoomed_in
    ta1 "Well, read the text. Understand it. Try to find some more sources."
    show sara mhappy
    ta1 "Then take the information together and write an essay in your own words without copying large chunks from your sources..."
    show sara happy at zoom_norm
    pov "I see! I think I understand! Thank you, Sara!"
    pov "I will do it better next time!"
    show sara talk at zoomed_in
    ta1 "Good luck! See you"
    hide sara
    jump after_essay_mark


label bad_essay_selected:
    $ plag = True
    $ change_score('bad_essay', -1)
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home2
    show alex angry at zoomed_in:
        xalign 0.5
    a "[povname]! Have you seen the marks? I got low points! What did you get?"
    show alex angry at zoom_norm
    pov "Let me check..."
    pov "Oh no! I also only got a few points. But why?"
    show alex sad at slightright, zoom_norm
    show keri happy at slightleft, zoom_norm
    with dissolve
    pov "Hey, Pari! What did you get on your essay?"
    show keri mhappy at zoomed_in
    p "I got full points... And you?"
    show keri happy at zoom_norm
    pov "Alex and I only got a few points"
    show keri surprised at zoomed_in
    p "Whaaat? What did you guys do?!"
    show keri happy at zoom_norm
    pov "I don't know..."
    pov "I will go to Sara and ask her. I will be back in a minute"
    show keri mhappy at zoomed_in
    p "Good Luck, [povname]"
    scene bg home2
    with dissolve
    show sara happy at top, zoom_norm
    pov "Hey, Sara? Can I talk to you?"
    show sara talk at zoomed_in
    ta1 "Sure, what do you want to talk about?"
    show sara happy at zoom_norm
    pov "About my essay. I don't understand why I only got so few points"
    show sara talk at zoomed_in
    ta1 "I see. Well, to be honest, you were lucky"
    show sara mhappy
    ta1 "You closely copied the source paragraph but at least you referenced it"
    menu:
        ta1 "What do you think why you got only a few points out of it?"

        "I didn't put much effort into it":
            ta1 "Yes, and that is part of the problem"

        "I don't know! I looked up the information and gave the correct answer!":
            show sara surprised at zoom_norm
            pov "What was wrong with it?"
            show sara mhappy at zoomed_in
            ta1 "Well, [povname]. Let me explain it to you"

    menu:
        ta1 "So, tell me exactly how you tackled this problem"

        "I looked the information up on Wikipedia":
            pass

        "I looked the information up on the slides":
            pass

    menu:
        ta1 "And what did you do then?"

        "I took the paragraph and changed some words":
            pass

        "I used synonyms to make the text my own":
            pass

    show sara talk
    ta1 "Well, but was it really your own text?"
    show sara happy at zoom_norm

    pov "Yes, I think so"

    show sara surprised at zoomed_in

    ta1 "But think about the process. You just replaced some of the words"

    show sara talk

    ta1 "You didn't change any of the structure of the text"

    show sara mhappy

    ta1 "We were not assessing your googling skills"
    show sara talk
    ta1 "We expected you to look up the information"
    show sara happy at zoom_norm
    menu:
        "Which I correctly did":
            show sara mhappy at zoomed_in
            ta1 "Yes, but we wanted you to understand the information"

        "So what was wrong?":
            show sara mhappy at zoomed_in
            ta1 "We wanted you to understand the information"

    menu:
        "So inserting synonyms was not enough?":
            show sara talk
            ta1 "Exactly!"

        "Well, I understood the information!":
            ta1 "I'm not saying that you didn't"
            show sara talk
            ta1 "But with just using synonyms we can't see that you did"

    show sara mhappy
    ta1 "That way, you spent more time thinking about synonyms than actually thinking about the content"
    show sara talk
    ta1 "Even when you change some words or the structure of the text, this is not sufficient for a high mark"
    show sara happy at zoom_norm
    pov "So what should I have done?"
    show sara talk at zoomed_in
    ta1 "Well, read the text. Understand it. Try to find some more sources."
    show sara mhappy
    ta1 "Then take the information together and write an essay in your own words without copying large chunks from your sources..."
    show sara happy at zoom_norm
    pov "I see! I think I understand! Thank you, Sara!"
    pov "I will do it better next time!"
    show sara talk at zoomed_in
    ta1 "Good luck! See you"
    hide sara
    jump after_essay_mark

label mediocre_essay:
    $ change_score('mediocre_essay', +1)
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
    pov "Oh no! I have some points but not full points. What should I have done differently?"
    show alex sad at slightright, zoom_norm
    show keri happy at slightleft, zoom_norm
    with dissolve
    pov "Hey, Pari! What did you get on your essay?"
    show keri mhappy at zoomed_in
    p "I got full points... And you?"
    show keri happy at zoom_norm
    pov "Alex got zero points and I got some but not all"
    show keri surprised at zoomed_in
    p "I see! Do you know why?"
    show keri happy at zoom_norm
    pov "I don't know..."
    pov "I will go to Sara and ask her. I will be back in a minute"
    show keri mhappy at zoomed_in
    p "Good Luck, [povname]"
    scene bg home2
    with dissolve
    show sara happy at top, zoom_norm
    pov "Hey, Sara? Can I talk to you?"
    show sara talk at zoomed_in
    ta1 "Sure, what do you want to talk about?"
    show sara happy at zoom_norm
    pov "About my essay. I don't understand why I don't have full points"
    show sara talk at zoomed_in
    ta1 "I see. Well, let me explain it to you"
    show sara mhappy
    ta1 "Your essay wasn't bad at all. You referenced all your sources"
    show sara talk
    menu:
        ta1 "So why do you think you did not get full points?"

        "Did I reference the sources incorrectly?":
            show sara mhappy
            ta1 "No, the references themselves were all fine"
            menu:
                ta1 "It was more the number of direct quotations"

                "But I thought we should use several sources?":
                    show sara talk
                    ta1 "Yes, the sources were fine, but your essay consisted of almost nothing else than quotations"

                "So, I used too many quotations?":
                    show sara mhappy
                    ta1 "Exactly, [povname]!"
        "Hmm, maybe I used too many quotations?":
            show sara mhappy
            ta1 "Exactly, [povname]!"

    ta1 "There were not enough of your own words"
    show sara talk
    ta1 "So, we weren't sure whether you understood the source texts"
    show sara happy at zoom_norm
    pov "What do you mean?"
    show sara mhappy at zoomed_in
    ta1 "We wanted you to understand the information in the source texts"
    show sara talk
    ta1 "But you just wrote a text around your quotations"
    show sara mhappy
    ta1 "That way, we can see that you were not thinking enough about the content"
    show sara talk
    ta1 "If you had understood the information you would have been able to phrase everything in your own words"
    show sara happy at zoom_norm
    pov "Ok, so next time, you want a paragraph with no quotations?"
    show sara talk at zoomed_in
    ta1 "As I said, you can use quotations. But not that many"
    show sara mhappy
    ta1 "Try to really understand the text and then you will see that you will be able to phrase it in your own words"
    show sara happy at zoom_norm
    pov "Okay, I will try my best! Thank you, Sara!"
    pov "I will do it better next time!"
    show sara talk at zoomed_in
    ta1 "Good luck! See you"
    hide sara
    jump after_essay_mark


label good_essay:
    $ change_score('good_essay', +4)
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home2
    show alex sad at zoomed_in:
        xalign 0.5
    a "[povname]! Have you seen the marks? I only got a few points! What did you get?"
    show alex sad at zoom_norm
    pov "Let me check..."
    pov "Oh wow! I got full points!?"
    show alex angry at zoomed_in
    a "Well, you could have helped me then..."
    show alex sad at slightright, zoom_norm
    show keri happy at slightleft, zoom_norm
    with dissolve
    pov "Hey, Pari! What did you get on your essay?"
    show keri mhappy at zoomed_in
    p "I got full points... And you?"
    show keri happy at zoom_norm
    pov "Alex got some points and I got full points as well"
    show alex angry at zoomed_in
    a "You both could have helped me"
    show alex sad at slightright, zoom_norm
    show keri mhappy at zoomed_in
    p "Alex, we are not allowed to help you write your essays"
    show keri talk
    p "But if you want, we can practice with some fictional essays that are not part of our coursework"
    show keri mhappy
    p "That way, we can all practice writing essays even more"
    show keri happy at zoom_norm
    pov "What a great idea!"
    show alex talk at zoomed_in
    a "Well, ok, that sounds fair. Thank you, guys!"
    jump transition_to_fabrication



label overtop_essay:
    $ change_score('overtop_essay', +1)
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home2
    show alex angry at zoomed_in:
        xalign 0.5
    a "[povname]! Have you seen the marks? I got only a few points! What did you get?"
    show alex angry at zoom_norm
    pov "Let me check..."
    pov "Hmm! I didn't get full points. But why?"
    show alex sad at slightright, zoom_norm
    show keri happy at slightleft, zoom_norm
    with dissolve
    pov "Hey, Pari! What did you get on your essay?"
    show keri mhappy at zoomed_in
    p "I got full points... And you?"
    show keri happy at zoom_norm
    pov "Alex got a few points and I got some but not all"
    show keri surprised at zoomed_in
    p "I see! Do you know why?"
    show keri happy at zoom_norm
    pov "I don't know..."
    pov "I will go to Sara and ask her. I will be back in a minute"
    show keri mhappy at zoomed_in
    p "Good Luck, [povname]"
    scene bg home2
    with dissolve
    show sara happy at top, zoom_norm
    pov "Hey, Sara? Can I talk to you?"
    show sara talk at zoomed_in
    ta1 "Sure, what do you want to talk about?"
    show sara happy at zoom_norm
    pov "About my essay. I don't understand why I don't have full points"
    show sara talk at zoomed_in
    ta1 "I see. Well, let me explain it to you"
    show sara mhappy
    ta1 "Your essay wasn't bad at all. But you did something common for non-native speakers"
    menu:
        ta1 "Do you have an idea of what you might have done too extensively?"

        "Maybe I used too many sources":
            show sara surprised
            ta1 "No, the sources were fine. The problem was more about some of the words"
            show sara happy at zoom_norm
            pov "What do you mean?"
            show sara talk at zoomed_in
            ta1 "Well, your choice of words was sometimes a bit off"

        "Hmm, something with the wording? I struggled to find my own words":
            show sara mhappy
            ta1 "Yeah, we could see that"


    ta1 "You tried to come up with synonyms but some of them didn't make sense"
    show sara happy at zoom_norm
    pov "Which words? What do you mean?"
    show sara mhappy at zoomed_in
    ta1 "Well, it is always good to come up with your own text in your own words"
    show sara talk
    ta1 "But some terms are definite scientific terms and you should keep them"
    show sara happy at zoom_norm
    pov "Scientific terms?"
    show sara mhappy at zoomed_in
    ta1 "For example, there is no such thing as [false_synonyms_examples[0][0]]. This is called [false_synonyms_examples[0][1]]"
    show sara talk
    ta1 "And a [false_synonyms_examples[1][1]] is a [false_synonyms_examples[1][1]] and not a [false_synonyms_examples[1][0]]"
    show sara mhappy
    ta1 "Try to be precise and write a text in your own words"
    show sara talk
    ta1 "But keep the scientific terms"
    show sara happy at zoom_norm
    pov "Hmm, and how do I recognise which terms I shouldn't change?"
    show sara talk at zoomed_in
    ta1 "Well, there is no definite answer"
    show sara mhappy
    ta1 "But as a rule-of-thumb: if the term has its own article, for example on Wikipedia, then you should consider not to change that term"
    show sara happy at zoom_norm
    pov "Okay, I will try my best! Thank you, Sara!"
    pov "I will do it better next time!"
    show sara talk at zoomed_in
    ta1 "Good luck! See you"
    hide sara
    jump after_essay_mark

label failed_essay:
    $ change_score('failed_essay', -2)
    $ plag = True
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home2
    with dissolve
    show sara talk at zoomed_in:
        xalign 0.5


    ta1 "Hey, [povname]. I need to talk to you about your coursework"
    show sara happy at zoom_norm
    menu:
        "Oh no! Did I do something wrong?":
            pass

        "Sure! Is everything alright?":
            pass

    show sara talk at zoomed_in
    ta1 "Well, we looked at your essay and we have some questions we want to clarify with you"
    show sara mhappy
    menu:
        ta1 "Can you tell me how you approached this task?"
        "I looked up the information and gave the correct answer!":
            pass
        "Was there something wrong with it?":
            pass

    ta1 "What exactly did you do? Did you write your own paragraph?"
    show sara happy at zoom_norm
    if slides:
        pov "Well, no. It was common knowledge. So, I took a paragraph from the slides."
    else:
        pov "Well, no. It was common knowledge. So, I took a paragraph from Wikipedia."
    pov "And I also cleaned it up a bit"
    show sara talk at zoomed_in
    menu:
        ta1 "Did you think about referencing it?"

        "No, it was common knowledge!":
            pass

        "No, I didn't think that it was necessary":
            pass

    show sara mhappy
    ta1 "So, you just copied the source paragraph and got rid of the footnotes"
    show sara talk
    ta1 "But you didn't put any effort into it"
    show sara mhappy
    ta1 "Please have a look at this"
    jump failed_essay_cont

label failed_essay_cont:
    show academic_malpractice_tablet at top
    pause
    hide academic_malpractice_tablet
    show sara mhappy at zoomed_in
    menu:
        ta1 "What do you think applies here"

        "Plagiarism":
            ta1 "Exactly! You committed academic malpractice!"

        "Collusion":
            ta1 "Please have another look"
            jump failed_essay_cont

        "Fabrication of results":
            ta1 "Please have another look"
            jump failed_essay_cont

        "Falsification of results":
            ta1 "Please have another look"
            jump failed_essay_cont

    show sara talk
    ta1 "You were just copying and pasting the paragraph"
    show sara mhappy
    ta1 "You did not produce any own work in addition to this paragraph"
    show sara talk
    ta1 "So, we could not award you any points for this coursework"
    show sara mhappy
    ta1 "You didn't even reference your source text"
    show sara happy at zoom_norm
    menu:
        "But it was common knowledge?":
            pass

        "So, I have to reference it?":
            pass

    show sara talk at zoomed_in
    ta1 "Even if it is common knowledge, you took someone else's words."

    menu:
        "So, if I had referenced it...":
            pass

        "A reference would have been enough?":
            pass

    show sara mhappy at zoomed_in
    ta1 "Well, you did not paraphrase the paragraph."
    show sara talk
    ta1 "And you did not produce any additional text on your own"
    show sara mhappy
    ta1 "So, you would have had to put everything in quotation marks"
    show sara talk
    ta1 "What do you think?"
    menu:
        ta1 "With how many would we have marked a paragraph that consists of one large quote?"

        "At least a few points?":
            show sara mhappy
            ta1 "Well, not that many points"

        "Full points":
            show sara angry
            ta1 "No, it lacks completely of your own work!"

        "Not that many points":
            show sara mhappy
            ta1 "You are right"

    show sara talk
    ta1 "We were not assessing your googling skills"
    show sara mhappy
    ta1 "We wanted you to understand the information"

    menu:
        "Yeah, so, copy and paste were not enough":
            ta1 "Exactly!"

        "Well, I understood the information!":
            ta1 "I'm not saying that you didn't"
            ta1 "But with just a copied paragraph we can't see that you did"

    show sara happy at zoom_norm
    pov "So what should I have done?"
    show sara talk at zoomed_in
    ta1 "Well, read the text. Understand it. Try to find some more sources."
    show sara mhappy
    ta1 "Then take the information together and write an essay in your own words without copying large chunks from your sources..."
    show sara happy at zoom_norm
    menu:
        "Hmm, okay... And now?":
            pass
        "What will happen now?":
            pass
    show sara mhappy at zoomed_in
    ta1 "You will now face consequences in addition to zero marks on this coursework"
    show sara talk
    ta1 "Your case will be taken to a disciplinary panel and you will most likely be disciplined"
    show sara happy at zoom_norm
    pov "I'm sorry, Sara! I won't do it again"
    show sara talk at zoomed_in
    ta1 "Yes, I hope so!"
    show sara happy at zoom_norm
    pov "Anyways, see you, Sara!"
    show sara mhappy at zoomed_in
    ta1 "See you, [povname]!"
    hide sara

    scene black
    with dissolve
    show text "Later that day..."
    pause
    scene bg home2
    with dissolve


    show alex angry at zoomed_in:
        xalign 0.5
    a "[povname]! Have you seen the marks? I got zero points! What did you get?"
    show alex angry at zoom_norm
    pov "Oh no! I also got zero points"
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
    show keri surprised at zoom_norm
    pov "Well, I just copied and pasted a paragraph from Wikipedia"
    show alex talk at slightright, zoomed_in
    a "Yeah, I did the same"
    show alex sad at slightright, zoom_norm
    show keri surprised at zoomed_in
    p "I see. So you both plagiarised..."
    p "Guys, you should have known better!"

    scene black
    with dissolve
    show text "Please try again"
    pause
    jump essay_writing_mg




label after_essay_mark:
    scene bg home2
    show alex happy at slightright, zoom_norm
    show keri talk at slightleft, zoomed_in
    p "Aaaannd? What did she say?"
    show keri happy at slightleft, zoom_norm
    pov "Well, she gave me some very helpful feedback!"
    pov "I'm sure I will do better next time"
    jump transition_to_fabrication

label transition_to_fabrication:
    scene black
    with dissolve
    show text "You spend the next weeks with your good friends Pari and Alex"
    pause
    # # Option for more interlude, e.g. in the lecture you learn a lot of useful things
    # show text "In the second week, you have to write another essay"
    # pause
    # show text "This time, your topic is for-loops"
    # pause
    # show text "In the following, drag and drop the right paragraphs to the right position"
    # pause
    # call start_parsons_pic from _call_start_parsons_pic
    # scene black
    # show text "Well done! You got full points on your second week's essay!"
    # pause

    hide sara
    hide keri
    scene black
    if not one_chapter_only:
        $ score = calculate_score()
        $ firstweek_score = score - initial_score
        scene black
        pause 0.5
        show text "End of Chapter 1"
        with fade
        pause
        scene black
        with dissolve
        pause 0.5

        if formative:


            if firstweek_score >= 12:
                show text "Excellent! You did very well"
                pause
                show text "You may graduate with distinction"
                pause
                show text "Keep up the good work"
                pause
            elif firstweek_score >= 9:
                show text "Well done!"
                pause
                show text "You understand what academic malpractice is about"
                pause
                show text "Keep up the good work"
                pause
            elif firstweek_score >= 6:
                show text "You did alright"
                pause
                show text "However, you should think about investing more time in understanding the topic"
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
                        jump first_day

                    "Yes, but not from the beginning":
                        jump lab_session

                    "Nah, I'm fine":
                        pass
            else:
                show text "You made many mistakes"
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
                        jump first_day

                    "Yes, but not from the beginning":
                        jump lab_session

                    "Nah, I'm fine":
                        pass

    if only_plagiarism:
        jump dissertation_transition
    if only_coll_fab:
        jump fabrication
    scene black
    show text "You now have the opportunity to end the game early"
    pause
    show text "In the next two (shorter) chapters you will encounter different types of academic malpractices"
    pause
    scene black
    menu:
        "Do you want to learn more about academic malpractice or do you want to end the game?"

        "I want to learn about collusion and fabrication of results as well as some more plagiarism":
            jump fabrication

        "I want to end the game now":
            $ MainMenu(confirm=False)()

    return


label failed_coursework:
    scene black
    with dissolve
    show text "You failed your coursework"
    pause
    show text "Your motivation dropped for the rest of the course"
    pause
    show text "In the exam, you weren't that good either"
    pause
    show text "Unfortunately, you had to drop out of the course"
    pause
    show text "It would be best if you tried again from the beginning"
    pause
    show text "The end"
    pause
    return


label essay_feedback:
    if essay_chosen == "bad":
        jump bad_essay
    elif essay_chosen == "mediocre":
        jump mediocre_essay
    elif essay_chosen == "good":
        jump good_essay
    elif essay_chosen == "overtop":
        jump overtop_essay







    # This ends the game.

    return
