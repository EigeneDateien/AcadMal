
init:
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    transform slideright:
        xalign 0.5
        linear 1.0 xalign 0.75
    transform slideleft:
        xalign 0.5
        linear 1.0 xalign 0.25
    transform slidewideright:
        xalign 0.75
        linear 1.0 xalign 0.9
    transform slidewideleft:
        xalign 0.25
        linear 1.0 xalign 0.1
    transform zoomed_in:
        zoom 0.7
    transform zoom_norm:
        zoom 0.6
    transform slightright:
        xalign 0.75
    transform slightleft:
        xalign 0.25
    transform wideright:
        xalign 0.9
    transform wideleft:
        xalign 0.1
    transform sitting:
        yalign -4.0
    style laptop_text:
        size 40

label first_day:
    $ score = calculate_score()
    $ initial_score = score
    $ plag_play += 1

    ##################################################################
    # INTRO
    ##################################################################

    scene black
    "You, [povname], are a new student at the University of Manchester"
    "At first, you were really nervous!"
    "Studying in a new city, a new environment"

    "But luckily, you found some new friends during Welcome Week"

    scene black
    with flashbulb


    show alex happy at zoom_norm, top

    "This is Alex, your best friend at university. He feels pretty confident with everything programming related"

    hide alex happy
    with fade
    show keri happy at zoom_norm, top
    with Dissolve(1.1, alpha=True)

    "And this is Pari, your other best friend. She is excellent at writing!"
    show keri happy at zoom_norm, slideleft
    show alex happy at zoom_norm:
        xalign 0.75
    with Dissolve(1.1, alpha=True)
    "The three of you arranged to meet outside the university on the first day"


    scene bg outside
    with flashbulb

    show keri happy at zoom_norm, slightleft
    show alex mhappy at zoom_norm, slightright
    pause 1.0
    show alex mhappy at zoomed_in, slightright
    a "Hey, [povname]"

    show keri mhappy at zoomed_in, slightleft
    show alex happy at zoom_norm, slightright
    p "Heeyyy, [povname], how are you?"

    show keri happy at zoom_norm, slightleft

    menu:
        "Hey Pari, hey Alex! I'm a bit nervous to be honest":
            show keri mhappy at zoomed_in, slightleft
            p "Yeah, me as well!"
            show keri mhappy at zoom_norm, slightleft

        "Hey Pari, hey Alex! I'm super excited!":
            show alex mhappy at zoomed_in, slightright
            a "Yessss, I'm really looking forward to our first lecture"

    a "Let's go inside! Shall we?"
    show keri talk at zoomed_in, slightleft
    show alex happy at zoom_norm, slightright
    p "Yesss!"
    show keri happy at zoom_norm, slightleft

    "You enter the lecture hall with your friends"

    scene bg kilburn lecture1
    pause 1.0
    show alex vhappy at zoomed_in, top
    a "I am so excited!!!"
    show alex happy at zoom_norm, slightright
    show keri talk at zoomed_in, slightleft
    with Dissolve(0.5, alpha=True)
    p "C'mon! Let's take a seat"

    scene bg kilburn lecture
    show alex happy at zoom_norm, slightright, sitting
    show keri happy at zoom_norm, slightleft, sitting
    pov "Let's see what this lecture is all about..."

    scene bg kilburn lecture
    with flashbulb
    show alex happy at zoom_norm, wideright, sitting
    show keri happy at zoom_norm, wideleft, sitting

    show instructor talk at top
    s "Good morning, class!"
    s "Before we start with our lecture, let's give you some facts about this lecture!"
    s "In the morning we will have a lecture. And after the lunch break we will go to the labs to have some practical work"
    s "You will have some coursework that you can start during the lab session"
    s "And you can ask questions to the TAs and me, your instructor"

    # Cool effect to show time transition

    s "So that was our lecture part! I will see you after the lunch break in the labs!"

    scene black
    "You spend the lunch break with Pari and Alex"

    scene bg home
    show keri angry at zoomed_in, slightleft
    p "Alex! [povname]! Hurry up, we will be late!"
    show keri angry at zoom_norm, slightleft
    show alex happy at zoom_norm, slightright
    pov "Coming!"
    show keri happy at zoom_norm, slightleft
    pov "Let's get ourself some seats"

    scene bg home2
    show alex happy at zoom_norm, wideleft, sitting
    show keri happy at zoom_norm, wideright, sitting
    show instructor mhappy at top
    s "Welcome back! In this lab session you can start with you coursework!"
    s "Please remember that all coursework in this week will be individual coursework"
    s "We recommend that you have a look at the essay first, since most of you might struggle with this the most"
    show alex surprised at zoom_norm, wideleft, sitting
    a "There will be essays in Computer Science?!"

    menu:
        a "Maaaan, I'm super bad at essays"
        "Don't worry, we will help you":
            $ change_score('plagiarism', -1)
        "Shhh, I want to hear what she has to say":
            pass
        "I'm sure they will teach us how to write these essays":
            pass

    show alex happy at zoom_norm, wideleft, sitting
    s "If you have any questions, feel free to ask me or the teaching assistant"
    s "Speaking of TAs, Sara, would you like to introduce yourself?"
    show instructor happy:
        xalign 0.5
        linear 1.0 xalign 0.35
    pause 0.5
    show sara talk at zoom_norm:
        xalign 0.65
    with Dissolve(0.5, alpha=True)
    ta1 "Thanks! Well, my name is Sara and I am the teaching assistant"
    ta1 "If you have any questions just ask me"
    ta1 "I will be in the lab two days a week and you can ask a question on Blackboard"
    show sara happy at zoom_norm:
        xalign 0.65
    show instructor talk:
        xalign 0.35
    s "So, that would be all. Feel free to start your coursework now"
    s "But as I said, I would recommend starting with the essay"
    s "We will go around now and you can ask us some questions"


    scene black
    with dissolve
    show text "Five minutes later..."
    ""


    scene bg lab
    show alex happy at zoom_norm, slightright
    show keri happy at zoom_norm, slightleft
    "You enter the lab room and choose your seat between Pari and Alex"
    show alex talk at zoomed_in, slightright
    a "Hey, [povname]. Can you help?"
    show alex happy at zoom_norm, slightright
    pov "Sure, what's up?"
    show alex talk at zoomed_in, slightright
    a "I'm struggling with the essay..."
    a "Have you looked at it yet?"
    show alex happy at zoom_norm, slightright
    pov "No, I will have a look"

    show alex happy at zoom_norm, slidewideright
    show keri happy at zoom_norm, slidewideleft
    show turing question at truecenter
    pause
    show turing question:
        yalign 0.5
        linear 1.0 yalign 0.05
    show keri mhappy at zoomed_in
    p "This looks tricky!"
    show keri happy at zoom_norm
    menu:
        "It does look tricky. We should divide up the work.":
            hide turing question
            jump failing
        "It seems straighforward. I'm going to do it on my own.":
            show alex angry at zoomed_in
            a "That's not very nice! Be a jerk about it!"
            show alex angry at zoom_norm
            show keri mhappy at zoomed_in
            p "Hey, Alex, caml down! I think [povname] is actually right"
            p "We are supposed to work on it alone! But we could ask the TA"
            show keri happy at zoom_norm
            hide turing question
            jump ask_sara
        "Look! It says it should be our own work. We can't collaborate.":
            show alex talk at zoomed_in
            a "I don't think it means we can't work together."
            a "It just means we can't submit the same essay."
            show alex happy at zoom_norm
            menu:
                "You're right. Let's get started.":
                    hide turing question
                    jump failing
                "You're wrong. I'm going to work alone.":
                    show alex angry at zoomed_in
                    a "Don't be so rude! I'm sure we can work together!"
                    show alex angry at zoom_norm
                    menu:
                        "Let's ask the TA then":
                            jump ask_sara
                        "No, please leave me alone":
                            $ change_score('no_collab', +3)
                            show alex angry at zoomed_in
                            a "Fine! But stop being so rude"
                            show alex angry at zoom_norm
                            pov "I'm sorry, Alex! But we are not allowed to work together!"
                            show keri talk at zoomed_in
                            p "Alex, [povname] is right. It literally says that it should be done individually"
                            jump coursework_writing
                "I'm unsure and think we should ask a TA.":
                    hide turing question
                    jump ask_sara

label failing:
    # intervention by the ta
    $ change_score('failing_coll', -4)
    show sara mhappy at zoomed_in:
        xalign 0.5
    with dissolve
    ta1 "Hey, you two are seem to get along well."
    show sara mhappy at zoom_norm
    show alex vhappy at zoomed_in
    a "Yeah, [povname] is a great working partner"
    show alex vhappy at zoom_norm
    show sara mhappy at zoomed_in

    menu:
        ta1 "Excuse me, you two are not working on the essay together, do you?"

        "We are just discussing what to write":
            ta1 "If you don't understand a question or what you should do, you can always ask a TA or the instructor"
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
            p "Why? I thought we could work together on the essay?"
            show alex happy at zoom_norm

        "We are splitting up the work, because it is too much":
            show sara happy at zoomed_in
            ta1 "Well, I know that these questions seem hard in the beginning, but please stop working together immediately!"
            show sara happy at zoom_norm
            show alex talk at zoomed_in
            p "Why? I thought we could work together on the essay?"
            show alex happy at zoom_norm

    jump sara_feedback

label ask_sara:
    $ change_score('ask_sara', +2)
    show alex mhappy at zoomed_in
    a "Oh, alright. Let's ask Sara the TA."
    show alex mhappy at zoomed_in
    show sara happy at zoom_norm:
        xalign 0.5

    a "Hey Sara. It's ok if we work together on SE1, right?"
    a "I mean, as long as the final essays are different?"
    show alex happy at zoom_norm
    jump sara_feedback

label sara_feedback:
    show sara angry at zoomed_in
    ta1 "No! Didn't you see the part of the question where it says it must be your own work?"
    show keri talk at zoomed_in
    show sara happy at zoom_norm
    p "We did, but we were unsure."
    p "Can we discuss the question and give each other feedback?"
    p "Or does it mean that we have to work individually?"
    show keri happy at zoom_norm
    show sara talk at zoomed_in
    ta1 "That's exactly what it means. You shouldn't work together at all on SE1."
    show sara happy at zoom_norm
    show alex surprised at zoomed_in
    a "Whaaaaat? But if we have a question?"
    show alex surprised at zoom_norm
    show sara talk at zoomed_in
    ta1 "If you have a question or problem, you should ask a TA, email an instructor, or post a question on Blackboard."
    ta1 "If you had worked together on SE1 that would have been collusion!"
    ta1 "In the best case, you would have gotten zero points on SE1 and a mark on your record."
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
    a "Yeah. But I don't know. It's strange. The instructor talked about the importance of collaboration."
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
        $ s = ta1
    else:
        show instructor happy:
            xalign 0.5
    show alex happy at zoom_norm
    "We find [speaker] in the lab."
    if speaker == "Sara":
        pov "Hello, we have another question about SE1."
        show sara talk:
            zoom 0.7
            xalign 0.5
        $ s = ta1
    else:
        pov "Hello, we have a question about SE1."
        show instructor talk:
            xalign 0.5

    s "Sure, what's up?"

    if speaker == "Sara":
        show sara happy at zoom_norm
    else:
        show instructor happy


    show alex talk at zoomed_in

    a "We know we aren't supposed to work together on SE1, even if we produce different essays."

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

    s """I understand your concerns.

    We think a lot about how our assignments affect your learning, esp. for writing.

    You'll have to do a lot of writing in the program here."""

    s "For example, you have other coursework..."

    s "...exams..."

    s "...and your dissertation to write."

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
            s "You aren't doomed."
    if speaker == "Sara":
        show sara talk at zoomed_in
    else:
        show instructor talk
    s """You can get various sorts of help, but not always before you have to finish some writing.

    For example, consider exams."""
    #TODO: show exam situation
    s """Many exams have short essays on them. You need to formulate an answer, by yourself, with a lot of time pressure.

    You can get help revising for your exam, but no help during the exam.

    And the best way to get better at writing is to practice it."""

    if speaker == "Sara":
        show sara happy at zoom_norm
        $ s = ta1
    else:
        show instructor happy

    menu:
        "But we don't even know how to get started on SE1!":
            if speaker == "Sara":
                show sara talk
            else:
                show instructor talk
            s "If you want, we can talk individually and I will answer your questions as far as possible"
        "We'll lose points if we don't get help now!":
            if speaker == "Sara":
                show sara talk
            else:
                show instructor talk
            s "Part of the assignement is to figure out how to start and what an essay should entail"
            s "This way, you will learn the most"
            s "And you will get helpful feedback after the submission so that you know what to do next time"
        "What sort of help are we going to get?":
            if speaker == "Sara":
                show sara talk
            else:
                show instructor talk
            s "First, you can always ask a TA or an instructor for help."
            s "We know how much aid to give without breaking the value of the assignment."
            if comp61511:
                s "Next, in a lab after submitting SE1, we'll have an exercise where we will do some peer review."
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
    s "So, class! Our lab session is over now"
    s "However, you can still ask some questions via Blackboard"
    s "Sara, the TA will be here for two days over the week"
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
    ""
    show text "Tomorrow, you will try to write the essay"
    ""

    # Auswertung how well do
    jump essay_writing_mg

label essay_writing_mg:
    # start minigame of writing an short essay on turing machines taken from best practices


    scene bg home desk
    with dissolve
    pov "Ok, let's see the essay question again"
    pov "I hope I can answer it correctly"
    scene bg home laptop
    show turing question:
         yalign 0.11
         xalign 0.5
    pause
    # for one_day, alex asks via smartphone to come to the lab, it's urgent

    pov "Hmm, I should define the term Turing machine"

    menu:
        "What should I do first?"

        "Look it up on Wikipedia":
            jump wikipedia_storyline

        "Look it up on the slides":
            jump slides_storyline



label wikipedia_storyline:
    pov "I could answer it from Wikipedia!"
    hide turing question
    show bg home turing wiki
    with dissolve
    pov "Indeed, it seems like the first paragraph does the job!"
    jump cut_and_paste

label slides_storyline:
    pov "I will have a look at the slides"
    hide turing question
    window hide
    show bg home turing slide
    with dissolve
    pause 1.0
    pov "Perfect, I found the right slide!"
    pov "Indeed, this is the exact paragraph I need!"
    jump cut_and_paste


label cut_and_paste:
    pov "I could cut and paste it and have an answer!"

    show bg home turing tm1

    pov "Hmm, I should clean it up a bit! Just getting rid of the footnote markers."

    show bg home turing tm2

    pov "Perfect! Now, it looks like a pretty decent answer!"

    pov "Should I do some more? I think it is common knowledge since it can be also found in the slides"

    pov "But the text is not mine, so should I reference it?"
    show bg home turing tm2_5

    menu:

        "No, it's common knowledge, so I guess it's fine!":
            $ change_score('plagiarism', -1)
            $ change_score('passivity', -1)
            jump failed_essay
        "Hmm, maybe I should cite my source":
            $ change_score('plagiarism', +1)
            show bg home turing tm2
            pov "Let's fix that citation issue!"
            call .plag(True) from _call_theory_plag

        "Well, that's a good start but I should do way more":
            $ change_score('plagiarism', +2)
            show bg home turing tm2
            pov "Let's start with the citation problem first"
            jump .plag

label .plag(only_one=False):
    pov "These are not my original words!"
    pov "So I guess I should reference it properly"
    show bg home turing tm3
    pov "Perfect! Now I have referenced it properly"
    pov "I wonder if this is sufficient"
    pov "I found the right paragraph which actually answers the question, so this is fine"

    pov "But should I try to write it in my own words?"
    pov "I am a bit anxious about my English"


    menu:
        "I think I should leave it like that.":
            $ change_score('passivity', -2)
            jump bad_essay
        "I should write it in my own words for a better grade.":
            $ change_score('plagiarism', +1)
    jump .passive

label .passive:
    pov "Honestly, I didn't do much until now!"
    pov "I just searched and retrieved a paragraph. But I didn't learn anything about Turing Machines."
    pov "Let me use some synonyms"
    "In the following minigame, you have to select the words you want to change"
    jump selection_mg

label selection_mg:
    call screen essay_text
    pov "Let's change up these words with synonyms"
    show bg home turing tm4
    pov "Ahh, great! Now my text is different from the original text"
    pov "Now let's get rid of the quotation marks and reference the original text."
    pov "Let's have another look"
    show bg home turing tm4_1
    pov "Well, that is indeed a pretty good paragraph"
    show bg home turing tm4_2
    menu:
        pov "Should I do something else?"

        "No, I'm finally done with everything!":
            jump bad_essay

        "I should write a text completely in my own words":
            jump avoid_patchwriting






screen essay_text:
    default mathematical = None
    default machine = None
    default tape = None
    default table = None
    default model_simplictiy = None
    default algorithm = None
    default turing_machine = None
    imagemap:
        ground "Scene/bg home turing tm3.png"
        idle "Scene/bg home turing tm3.png"
        hover "Scene/bg home turing tm3 hover.png"
        selected_idle "Scene/bg home turing tm3 selected.png"
        selected_hover "Scene/bg home turing tm3 selected.png"

        hotspot (407, 233, 200, 27) clicked SetScreenVariable("mathematical", True)
        hotspot (218, 268, 122, 24) clicked SetScreenVariable("machine", True)
        hotspot (912, 268, 69, 26) clicked SetScreenVariable("tape", True)
        hotspot (119, 296, 78, 27) clicked SetScreenVariable("table", True)
        hotspot (433, 296, 307, 27) clicked SetScreenVariable("model_simplictiy", True)
        hotspot (98, 328, 135, 25) clicked SetScreenVariable("algorithm", True)
        hotspot (247, 328, 899, 27) clicked SetScreenVariable("turing_machine", True)

        if mathematical and machine and tape and table and model_simplictiy and algorithm and turing_machine:
            imagebutton auto "select_%s.png":
                xalign 0.5
                yalign 0.7
                action Return()



label avoid_patchwriting:
    pov "Okay, let me try to paraphrase the paragraph in my own words"
    pov "I will try different approaches"
    "Please select the paragraph that you think fits best"
    call screen essay_choice
    $ essay_chosen = _return
    jump alex_emergency

label alex_emergency:
    # https://lemmasoft.renai.us/forums/viewtopic.php?t=40245
    call phone_start
    call message_start("Alex", "Hey [povname], I need your help!!!")
    pause
    call message_start("Alex", "Can you come to the Lab please?!")
    call screen phone_reply("Of course, Alex!","choice1","I'm sorry, Alex! I have no time","choice2")

label choice1:
    call message_start("Alex", "Thank youuuuuu, [povname]!!!!")
    call message("Alex", "")
    call phone_after_menu
    jump one_day_before

label choice2:
    call message_start("Alex", "Wow, [povname]! You never have time for me :(")
    call message("Alex", "")
    call phone_after_menu
    jump essay_feedback

screen essay_choice:
    imagemap:
        ground "Scene/bg home turing essaychoice.png"
        idle "Scene/bg home turing essaychoice.png"
        hover "Scene/bg home turing essaychoice hover.png"
        selected_idle "Scene/bg home turing essaychoice selected.png"
        selected_hover "Scene/bg home turing essaychoice selected.png"

        hotspot (51, 51, 573, 313) clicked Return("bad")
        hotspot (51, 366, 573, 309) clicked Return("good")
        hotspot (626, 51, 864, 313) clicked Return("mediocre")
        hotspot (626, 366, 603, 309) clicked Return("overtop")


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
            a "Please, I need you! Don't be like that! Without your help I will fail the essay!"
            menu:
                a "Just let me have a look what you have written"

                "Okay, but don't copy anything":
                    jump near_miss

                "No, I'm sorry, Alex!":
                    $ change_score('no_collab_final', +2)
                    # """Well done! You did not commmit collusion. However, be sure to be polite and explain to your fellow students
                    # why you are not allowed to help them with their individual coursework. And of course, you can and should help your fellow students
                    # for everything that is not related to individual work."""
                    jump essay_feedback

label near_miss:
    # pari will use the same ideas
    show alex vhappy
    a "Thank you, [povname]! You are a life saver"
    show alex talk
    a "This is such a great help! Your essay is way better than mine!"
    show alex vhappy at zoom_norm
    pov "But don't copy my text"
    show alex talk at zoomed_in
    a "No worries, I will rewrite it and use my own words"
    jump collusion


label collusion:
    $ change_score('collusion', -4)
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home2
    show alex angry at zoomed_in:
        xalign 0.5
    a "[povname]! Have you seen the marks? I got zero points! What have you got?"
    show alex angry at zoom_norm
    pov "Let me check..."
    pov "Oh no! I also got zero points. But why?"
    show alex sad at slightright, zoom_norm
    show keri happy at slightleft, zoom_norm
    with dissolve
    pov "Hey, Pari! What have you got on your essay?"
    show keri mhappy at zoomed_in
    p "I have full points... And you?"
    show keri happy at zoom_norm
    pov "Alex and me got zero points"
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
    ta1 "Did you two worked together on the essay or compared your essays"
    show sara happy at zoom_norm
    pov "Yes, we compared it, but we wrote different essays"
    show sara talk at zoomed_in
    ta1 "Thank you for your honesty, [povname]. As I told you before, it was an individual coursework"
    ta1 "We wanted to see how well you understand the topic. But each of you and not just one of you"
    ta1 "You are glad that it was in a coursework"
    ta1 "Now you will only get zero marks on this coursework"
    ta1 "But this will most likely affect your overall mark in this course."
    menu:
        ta1 "And beware! If you do any kind of academic malpractice during exams or your dissertation, it will have severe effects"

        "Can you tell us more about it?":
            ta1 "Yes, of course"
            jump school_comitee
        "We are sorry! We won't do it again!":
            hide sara
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
    ta1 "If you commit academic malpractice in a more severe context, there will be a chain of escalation"
    show sara happy at zoom_norm
    show alex talk at zoomed_in
    p "What is a more severe context?"
    show alex happy at zoom_norm
    show sara talk at zoomed_in
    ta1 "Assessments such as final essays, exams or your dissertation"
    show sara happy at zoom_norm
    pov "And what will happen then?"
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

    show sara talk at zoomed_in
    ta1 "You can read about here: {a=http://documents.manchester.ac.uk/display.aspx?DocID=639}Academic Malpractice Procedure{/a}!"
    hide sara
    menu:
        "Do you want to try again?"

        "Yes":
            jump one_day_before

        "No":
            jump failed_coursework


label bad_essay:
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home2
    show alex angry at zoomed_in:
        xalign 0.5
    a "[povname]! Have you seen the marks? I got low points! What have you got?"
    show alex angry at zoom_norm
    pov "Let me check..."
    pov "Oh no! I have also only a few points. But why?"
    show alex sad at slightright, zoom_norm
    show keri happy at slightleft, zoom_norm
    with dissolve
    pov "Hey, Pari! What have you got on your essay?"
    show keri mhappy at zoomed_in
    p "I have full points... And you?"
    show keri happy at zoom_norm
    pov "Alex and me only have a few points"
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
    pov "Hey, Sara? Can I talk to you"
    show sara talk at zoomed_in
    ta1 "Sure, what do you want to talk about?"
    show sara happy at zoom_norm
    pov "About my essay. I don't understand why I have only so few points"
    show sara talk at zoomed_in
    ta1 "I see. Well, to be honest you were in luck"
    ta1 "You closely copied the source paragraph but at least you referenced it"
    ta1 "But, be honest, you haven't put much effort in it"
    show sara surprised at zoom_norm
    pov "I looked up the information and gave a correct answer!"
    pov "What was wrong about it?"
    show sara mhappy at zoomed_in
    ta1 "Well, [povname]. Let me explain it to you"
    ta1 "We were not assessing your googling skills"
    ta1 "We expected you to look up the information"
    show sara happy at zoom_norm
    pov "That is what I did!"
    show sara mhappy at zoomed_in
    ta1 "Yes, but we wanted you to understand the information"
    ta1 "Just copying and referencing a paragraph is not enough"
    ta1 "That way, you have spend more time referencing the paragraph than actually thinking about the content"
    ta1 "Even, when you change some words or the structure of the text, this is not sufficient for a high mark"
    show sara happy at zoom_norm
    pov "So what should I have done?"
    show sara talk at zoom_norm
    ta1 "Well, read the text. Understand it. Try to find some more sources."
    ta1 "Then take the information together and write an essay in your own words without copying large chunks from your sources..."
    show sara happy at zoom_norm
    pov "I see! I think I understand! Thank you, Sara!"
    pov "I will do it better next time!"
    show sara talk at zoom_norm
    ta1 "Good luck! See you"
    hide sara
    jump after_essay_mark


label mediocre_essay:
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home2
    show alex angry at zoomed_in:
        xalign 0.5
    a "[povname]! Have you seen the marks? I got zero points! What have you got?"
    show alex angry at zoom_norm
    pov "Let me check..."
    pov "Oh no! I have some points but not full points. What should I have done different?"
    show alex sad at slightright, zoom_norm
    show keri happy at slightleft, zoom_norm
    with dissolve
    pov "Hey, Pari! What have you got on your essay?"
    show keri mhappy at zoomed_in
    p "I have full points... And you?"
    show keri happy at zoom_norm
    pov "Alex has a few points and I have some but not all points"
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
    pov "Hey, Sara? Can I talk to you"
    show sara talk at zoomed_in
    ta1 "Sure, what do you want to talk about?"
    show sara happy at zoom_norm
    pov "About my essay. I don't understand why I don't have full points"
    show sara talk at zoomed_in
    ta1 "I see. Well, let me explain it to you"
    ta1 "Your essay wasn't bad at all. You referenced all your sources"
    ta1 "However, you cited way too much"
    show sara surprised at zoom_norm
    pov "But I thought we are supposed to cite our sources"
    show sara mhappy at zoomed_in
    ta1 "Well, it is always a good idea to cite something that could not be expressed better"
    ta1 "And referencing your sources is vital"
    ta1 "However, your essay consisted of almost nothing else than quotations"
    ta1 "So, we weren't sure whether you have understood the source textes"
    show sara happy at zoom_norm
    pov "What do you mean?"
    show sara mhappy at zoomed_in
    ta1 "We wanted you to understand the information in the source textes"
    ta1 "But you just wrote a text around your quotations"
    ta1 "That way, we can see that you were not thinking enough about the content"
    ta1 "If you have understood the information you would have been able to phrase everything in your own words"
    show sara happy at zoom_norm
    pov "Ok, so next time, you want a paragraph with no quotations"
    show sara talk at zoom_norm
    ta1 "As I said, you can use quotations. But not that many"
    ta1 "Try to really understand the text and then you will see that you will be able to phrase it in your own words"
    show sara happy at zoom_norm
    pov "Okay, I will try my best! Thank you, Sara!"
    pov "I will do it better next time!"
    show sara talk at zoom_norm
    ta1 "Good luck! See you"
    hide sara
    jump after_essay_mark


label good_essay:
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home2
    show alex sad at zoomed_in:
        xalign 0.5
    a "[povname]! Have you seen the marks? I only got a few points! What have you got?"
    show alex sad at zoom_norm
    pov "Let me check..."
    pov "Oh wow! I got full points!?"
    show alex angry at zoomed_in
    a "Well, you could have helped me then..."
    show alex sad at slightright, zoom_norm
    show keri happy at slightleft, zoom_norm
    with dissolve
    pov "Hey, Pari! What have you got on your essay?"
    show keri mhappy at zoomed_in
    p "I have full points... And you?"
    show keri happy at zoom_norm
    pov "Alex has some points and I have full points as well"
    show alex angry at zoomed_in
    a "You both could have helped me"
    show alex sad at slightright, zoom_norm
    show keri mhappy at zoomed_in
    p "Alex, we are not allowed to help you writing your essays"
    p "But if you want, we can practice with some fictional essays that are not part of our coursework"
    p "That way, we can all practice writing essays even more"
    show keri happy at zoom_norm
    pov "What a great idea!"
    show alex talk at zoomed_in
    a "Well, ok, that sounds fair. Thank you, guys!"
    jump transition_to_fabrication



label overtop_essay:
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home2
    show alex angry at zoomed_in:
        xalign 0.5
    a "[povname]! Have you seen the marks? I got only a few points! What have you got?"
    show alex angry at zoom_norm
    pov "Let me check..."
    pov "Hmm! I didn't get full points. But why?"
    show alex sad at slightright, zoom_norm
    show keri happy at slightleft, zoom_norm
    with dissolve
    pov "Hey, Pari! What have you got on your essay?"
    show keri mhappy at zoomed_in
    p "I have full points... And you?"
    show keri happy at zoom_norm
    pov "Alex has a few points and I have some but not all points"
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
    ta1 "Your essay wasn't bad at all. But you did something that is common for a non-native speaker"
    ta1 "You tried to come up with synonyms but some of them didn't make sense"
    show sara happy at zoom_norm
    pov "Oh, what do you mean?"
    show sara mhappy at zoomed_in
    ta1 "Well, it is always good to come up with your own text in your own words"
    ta1 "But some terms are definite scientific terms and you should keep them"
    show sara happy at zoom_norm
    pov "What do you mean?"
    show sara mhappy at zoomed_in
    ta1 "For example, there is no such thing as an Alan Turing system. This system is called Turing machine"
    ta1 "And a computer is a computer and not a digital workspace"
    ta1 "Try to be precise and write a text in your own words"
    ta1 "But keep the scientific terms"
    show sara happy at zoom_norm
    pov "Hmm, and how do I recognise which terms I shouldn't change?"
    show sara talk at zoom_norm
    ta1 "Well, there is no definite answer"
    ta1 "But as a rule-of-thumb: if the term has its own article (e.g. on Wikipedia) then you should consider to not change that term"
    show sara happy at zoom_norm
    pov "Okay, I will try my best! Thank you, Sara!"
    pov "I will do it better next time!"
    show sara talk at zoom_norm
    ta1 "Good luck! See you"
    hide sara
    jump after_essay_mark

label failed_essay:
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home2
    show alex angry at zoomed_in:
        xalign 0.5
    a "[povname]! Have you seen the marks? I got zero points! What have you got?"
    show alex angry at zoom_norm
    pov "Let me check..."
    pov "Oh no! I also got zero points. But why?"
    show alex sad at slightright, zoom_norm
    show keri happy at slightleft, zoom_norm
    with dissolve
    pov "Hey, Pari! What have you got on your essay?"
    show keri mhappy at zoomed_in
    p "I have full points... And you?"
    show keri happy at zoom_norm
    pov "Alex and me have zero points"
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
    pov "Hey, Sara? Can I talk to you"
    show sara talk at zoomed_in
    ta1 "Sure, what do you want to talk about?"
    show sara happy at zoom_norm
    pov "About my essay. I don't understand why I have no points"
    show sara talk at zoomed_in
    ta1 "I see. Well, to be honest it was academic malpractice"
    ta1 "You just copied the source paragraph and got rid of the footnotes"
    ta1 "But you didn't put any effort in it"
    show sara surprised at zoom_norm
    pov "I looked up the information and gave a correct answer!"
    pov "What was wrong about it?"
    show sara mhappy at zoomed_in
    ta1 "Well, [povname]. Let me explain it to you"
    ta1 "We were not assessing your googling skills"
    ta1 "We expected you to look up the information"
    show sara happy at zoom_norm
    pov "That is what I did!"
    show sara mhappy at zoomed_in
    ta1 "Yes, but we wanted you to understand the information"
    ta1 "Just copy and paste a paragraph is not enough"
    ta1 "That way, you spend no time on understanding the content"
    ta1 "Plus: you plagiarised your paragraph which is academic malpractice"
    show sara happy at zoom_norm
    pov "Hmm, okay"
    show sara mhappy at zoomed_in
    ta1 "You are glad that it was in a coursework"
    ta1 "Now you will only get zero marks on this coursework"
    ta1 "But this will most likely affect your overall mark in this course."
    ta1 "And beware! If you do any kind of academic malpractice during exams or your dissertation, it will have severe effects"
    show sara happy at zoom_norm
    pov "So what should I have done?"
    show sara talk at zoom_norm
    ta1 "Well, read the text. Understand it. Try to find some more sources."
    ta1 "Then take the information together and write an essay in your own words without copying large chunks from your sources..."
    show sara happy at zoom_norm
    pov "I see! I think I understand! Thank you, Sara!"
    pov "I will do it better next time!"
    show sara talk at zoom_norm
    ta1 "Good luck! See you"
    hide sara
    menu:
        "Do you want to try again?"

        "Yes":
            jump cut_and_paste

        "No":
            jump after_essay_mark



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
    show text "You spent the next weeks with your good friends Pari and Alex"
    pause
    # Option for more interlude, e.g. in the lecture you learn a lot of useful things
    show text "In the second week, you are able to gain full marks on your coursework"
    pause
    jump fabrication


label failed_coursework:
    scene black
    with dissolve
    show text "You failed your coursework"
    pause
    show text "Your motivation dropped for the rest of the course"
    pause
    show text "In the exam you weren't that good either"
    pause
    show text "Unfortunately, you had to drop out of the course"
    pause
    show text "It would be best if you would try from the beginning again"
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



    # hide sara
    # hide keri
    # $ score = calculate_score()
    # $ collaboration_score = score - initial_score
    # if formative:
    #     "Your score is [collaboration_score]!"
    #
    #     if collaboration_score >= 4:
    #         "Well done! You did not commit collusion"
    #         "And remember: always make sure to not validate academic malpractice"
    #     else:
    #         "Unfortunately, you commited academic malpractice"
    #         "Please make sure to not collaborate on assignments where it is not explicitly stated"
    #         "You should really consider to try the collaboration part again"
    #         menu:
    #             "Would you like to try again?"
    #
    #             "Yes, I can do better":
    #                 jump start_plag
    #
    #             "Nah, I'm fine":
    #                 pass



    # This ends the game.

    return
