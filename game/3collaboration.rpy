label start_col:
    $ collab = True
    scene bg home
    show keri happy:
        pos(950, 40)
        zoom 0.6

    if meet_already:
        p "Hello, [povname]. Nice to see you again!"
        p "How are you dealing with the assignments?"
    else:
        p "Hello, you must be [povname]! My name is Pari. I am a new student as well."
        p "This is my first time in the UK. I'm a bit nervous about the MSc program."
    $ meet_already = True
    p "I thought I would be programming all the time, but they want us to write essays."
    p "I haven't had to write a lot of essays before. And some of them are quite strange!"
    p "Have you done coursework like this before?"
    menu:
        "Yes, I have.":
            jump essay_experienced
        "No, it's new to me.":
            jump essay_novice
        "I can't even tell!":
            jump essay_confused


label essay_experienced:
    p "Great! Then you can help me!"
    p "I really don't know what to do for the first essay, SE1."
    p "Maybe we can work together on it?"
    menu:
        "Yes! We'll both do better if we collaborate.":
            jump failing
        "No! I want to do it all by myself.":
            p "Wow, why are you so rude?"
            p "Please, can we just share ideas on what to write?"
            menu:
                "I really think you should work on it alone.":
                    "Please ask the TA if you have any questions"
                "Ok, fine! I will help you":
                    jump failing
                "Please let's ask the TA if it is fine":
                    jump ask_sara
        "I'd like to, but is it ok for us to work together on SE1?":
            jump se1_confused


label essay_novice:
    p "I'm glad to meet another beginner! Maybe we can help each other figure it out."
    p "Would you like to work together on the first essay, SE1?"
    menu:
        "Yes! We'll both do better if we collaborate.":
            jump failing
        "No! I want to do it all by myself.":
            p "Wow, why are you so rude?"
            p "Please, can we just share ideas on what to write?"
            menu:
                "I really think you should work on it alone.":
                    pov "Please ask the TA if you have any questions"
                "Ok, fine! I will help you":
                    jump failing
                "Please let's ask the TA if it is fine":
                    jump ask_sara
        "I'd like to, but is it ok for us to work together on SE1?":
            jump se1_confused

label se1_confused:
    $ change_score("se1_confused", +2)
    p "I think it's fine. We're supposed to be learning from each other."
    p "Let's look at the question!"
    show se1q at truecenter
    p "This looks tricky!"
    menu:
        "It does look tricky. We should divide up the work.":
            hide se1q
            jump failing
        "It seems straighforward. I'm going to do it on my own.":
            p "That's not very nice! Be a jerk about it!"
            hide se1q
            jump one_day_before
        "Look! It says it should be our own work. We can't collaborate.":
            hide se1q
            p "I don't think it means we can't work together."
            p "It just means we can't submit the same essay."
            menu:
                "You're right. Let's get started.":
                    jump failing
                "You're wrong. I'm going to work alone.":
                    p "Don't be so rude! I'm sure we can work together!"
                    menu:
                        "Let's ask the TA then":
                            jump ask_sara
                        "No, please leave me alone":
                            p "Fine! But stop being so rude"
                            pov "I'm sorry, Pari! But we are not allowed to work together!"
                            return
                "I'm unsure and think we should ask a TA.":
                    jump ask_sara


label ask_sara:
    $ change_score('ask_sara', +2)
    p "Oh, alright. Let's ask Sara the TA."
    show sara mhappy:
        pos(100, 40)
        zoom 0.6

    p "Hey Sara. It's ok if we work togehter on SE1, right?"
    p "I mean, as long as the final essays are different?"
    jump sara_feedback

label sara_feedback:
    ta1 "No! Didn't you see the part of the question where it says it must be your own work?"
    p "I did, but that doesn't mean we can't discuss the question and give each other feedback?"
    ta1 "That's exactly what it means. You shouldn't work together at all on SE1."
    ta1 "If you have a question or problem, you should ask a TA, email an instructor, or post a question on Blackboard."
    ta1 "If you had worked together on SE1 that would have been collusion!"
    ta1 "In the best case, you would have gotten zero points on SE1 and a mark on your record."
    p "Yeek! Thanks for this! I didn't realise."
    "We walk away from Sara."
    hide sara
    p """I guess it's a good thing we talked with Sara about this.

    But, it's strange. The instructor talked about the importance of
    collaboration.

    What's wrong with working together as long as we each write our own essays?
    """
    menu:
        "Tell [p_name] that we should just do what we are told":
            jump one_day_before
        "Walk away from [p_name] as fast as you can. She's trouble.":
            jump one_day_before
        "Suggest asking Sara again.":
            call se1_collaboration pass (speaker = "Sara") from _call_se1_collaboration
        "Suggest that you ask the instructor":
            call se1_collaboration pass (speaker = "Instructor") from _call_se1_collaboration_1
    return

label se1_collaboration(speaker="Instructor"):
    if speaker == "Sara":
        show sara mhappy:
            pos(100, 40)
            zoom 0.6
        $ s = ta1
    else:
        show instructor happy at left
    p "That's a good idea! [speaker] should explain what's going on."
    "We find [speaker] in the lab."
    "Hello, we have a question about SE1."
    show instructor talk at left
    s "Sure, what's up?"
    p """We know we aren't supposed to work together on SE1, even if we produce different essays.

    But we don't understand why. What's wrong with collaboration?"""
    menu:
        "You add in:"
        "We'll get a worse grade if we can't get some help.":
            pass
        "We'll learn less if we don't work together.":
            pass
        "We've never done something like this before" if True: #hook back to "novice" path.
            pass
    s """I understand your concerns.

    We think a lot about how our assignments affect your learning, esp. for writing.

    You'll have to do a lot of writing in the program here."""

    s "For example, you have other coursework..."

    s "...exams..."

    s "...and your dissertation to write."

    menu:
        "But we can get help for those, right?":
            pass
        "We're doomed!!!":
            s "You aren't doomed."
    s """You can get various sorts of help, but not always before you have to finish some writing.

    For example, consider exams."""
    #TODO: show exam situation
    s """Many exams have short essays on them. You need to formulate an answer, by yourself, with a lot of time pressure.

    You can get help revising for your exam, but no help during the exam.

    And the best way to get better at writing is to practice it."""

    menu:
        "But we don't even know how to get started on SE1!":
            s "If you want, we can talk individually and I will answer your questions as far as possible"
        "We'll lose points if we don't get help now!":
            s "Part of the assignement is to figure out how to start and what an essay should entail"
            s "This way, you will learn the most"
            s "And you will get helpful feedback after the submission so that you know what to do next time"
        "What sort of help are we going to get?":
            s "First, you can always ask a TA or an instructor for help."
            s "We know how much aid to give without breaking the value of the assignment."
            if comp61511:
                s "Next, in a lab after submitting SE1, we'll have an exercise where we will do some peer review."
    jump one_day_before

label one_day_before:
    scene black
    "One day before the deadline"
    scene bg home2
    show keri sad:
        pos(950, 40)
        zoom 0.6

    p "Hey, [povname]! I'm still struggling with the essay. And I can't reach the TAs! I really need your help!"

    menu:
        p "Could you show me your essay and give me some tipps on what to write?"

        "Yes, of course":
            p "Great, let me compare our essays"
            jump near_miss

        "I'm sorry, Pari, but I am not allowed to help you":
            p "Please, I need you! Don't be like that! Without your help I will fail the essay!"
            menu:
                p "Just let me have a look what you have written"

                "Okay, but don't copy anything":
                    jump near_miss

                "No, I'm sorry, Pari!":
                    """Well done! You did not commmit collusion. However, be sure to be polite and explain to your fellow students
                    why you are not allowed to help them with their individual coursework. And of course, you can and should help your fellow students
                    for everything that is not related to individual work."""
                    jump intro

label near_miss:
    # pari will use the same ideas
    p "Thank you, [povname]! You are a life saver"
    p "This is such a great help! Your essay is way better than mine!"
    pov "But don't copy my text"
    p "No worries, I will rewrite it and use my own words"
    jump collusion

label failing:
    # intervention by the ta
    show sara happy:
        pos(100, 40)
        zoom 0.6
    ta1 "Hey, you two are seem to get along well."
    p "Yeah, [povname] is a great working partner"
    menu:
        ta1 "Excuse me, you two are not working on the essay together, do you?"

        "We are just discussing what to write":
            ta1 "If you don't understand a question or what you should do, you can always ask a TA or the instructor"
            ta1 "But please don't discuss your answers with each other"
            p "But we can work together, right?"

        "We are working on it together, but we will both write an individual text":
            ta1 "Please stop that immediately!"
            p "Why? I thought we could work together on the essay?"

        "We are splitting up the work, because it is too much":
            ta1 "Well, I know that these questions seem hard in the beginning, but please stop working together immediately!"
            p "Why? I thought we could work together on the essay?"

    jump sara_feedback

label collusion:
    # scene black
    "One week later"
    # scene lab
    show keri angry:
        pos(950, 40)
        zoom 0.6
    p "[povname]! Have you seen the marks? I got zero points! What have you got?"
    pov "Let me check..."
    p "Oh no! I also got zero points. But why?"
    show sara mhappy:
        pos(100, 40)
        zoom 0.6
    ta1 "Pari, [povname]? Can I talk to you?"
    p "Sara, why do we have zero points?"
    ta1 "We found that your essays were very alike! You even made the same mistakes"
    ta1 "Did you two worked together on the essay or compared your essays"
    pov "Yes, we compared it, but we wrote different essays"
    ta1 "Thank you for your honesty, [povname]. As I told you before, it was an individual coursework"
    ta1 "We wanted to see how well you understand the topic. But each of you and not just one of you"
    ta1 "You are glad that it was in a coursework"
    ta1 "Now you will only get zero marks on this coursework"
    menu:
        ta1 "But beware! If you do any kind of academic malpractice during exams or your dissertation, it will have severe effects"

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
                    return


label school_comitee:
    # having to speak in front of the school commitee
    ta1 "If you commit academic malpractice in a more severe context, there will be a chain of escalation"
    p "What is a more severe context?"
    ta1 "Assessments such as final essays, exams or your dissertation"
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
    ta1 "You can read about here: {a=http://documents.manchester.ac.uk/display.aspx?DocID=639}Academic Malpractice Procedure{/a}!"
    hide sara
    menu:
        "Do you want to try again?"

        "Yes":
            jump one_day_before

        "No":
            return


label essay_confused:
    jump essay_novice
