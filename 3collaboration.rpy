label start_col:
    scene bg plants
    show pari happy at left

    p "Hello! My name is Pari."
    p "This is my first time in the UK. I'm a bit nervous about the MSc program."
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
    "I know enough not to share with her."
    return


label essay_novice:
    p "I'm glad to meet another beginner! Maybe we can help each other figure it out."
    p "Would you like to work together on the first essay, SE1?"
    menu:
        "Yes! We'll both do better if we collaborate.":
            pass
        "No! I want to do it all by myself.":
            pass
        "I'd like to, but is it ok for us to work together on SE1?":
            jump se1_confused

label se1_confused:
    p "I think it's fine. We're supposed to be learning from each other."
    p "Let's look at the question!"
    show se1q at truecenter
    p "This looks tricky!"
    menu:
        "It does look tricky. We should divide up the work.":
            pass
        "It seems straighforward. I'm going to do it on my own.":
            p "That's not very nice! Be a jerk about it!"
        "Look! It says it should be our own work. We can't collaborate.":
            p "I don't think it means we can't work together."
            p "It just means we can't submit the same essay."
            menu:
                "You're right. Let's get started.":
                    pass
                "You're wrong. I'm going to work alone.":
                    pass
                "I'm unsure and think we should ask a TA.":
                    jump ask_sara

label ask_sara:
    p "Oh, alright. Let's ask Sara the TA."
    show sara at right
    p "Hey Sara. It's ok if we work togehter on SE1, right?"
    p "I mean, as long as the final essays are different?"
    ta1 "No! Didn't you see the part of the question where it says it must be your own work?"
    p "I did, but that doesn't mean we can't discuss the question and give each other feedback?"
    ta1 "That's exactly what it means. You shouldn't work together at all on SE1."
    ta1 "If you have a question or problem, you should ask a TA, email an instructor, or post a question on Blackboard."
    ta1 "If you had worked together on SE1 that would have been collusion!"
    ta1 "In the best case, you would have gotten a 0 on SE1 and a mark on your record."
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
            pass
        "Walk away from [p_name] as fast as you can. She's trouble.":
            pass
        "Suggest asking Sara again.":
            call se1_collaboration pass (speaker = "Sara") from _call_se1_collaboration
        "Suggest that you ask the instructor":
            call se1_collaboration pass (speaker = "Instructor") from _call_se1_collaboration_1
    return

label se1_collaboration(speaker="Instructor"):
    $ s = ta1
    p "That's a good idea! [speaker] should explain what's going on."
    "We find [speaker] in the lab."
    "Hello, we have a question about SE1."
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
    ta1 """I understand your concerns.

    We think a lot about how our assignments affect your learning, esp. for writing.

    You'll have to do a lot of writing in the program here."""

    ta1 "For example, you have other coursework..."

    ta1 "...exams..."

    ta1 "...and your dissertation to write."

    menu:
        "But we can get help for those, right?":
            pass
        "We're doomed!!!":
            ta1 "You aren't doomed."
    ta1 """You can get various sorts of help, but not always before you have to finish some writing.

    For example, consider exams."""
    #TODO: show exam situation
    ta1 """Many exams have short essays on them. You need to formulate an answer, by yourself, with a lot of time pressure.

    You can get help revising for your exam, but no help during the exam.

    And the best way to get better at writing is to practice it."""

    menu:
        "But we don't even know how to get started on SE1!":
            pass
        "We'll lose points if we don't get help now!":
            pass
        "What sort of help are we going to get?":
            ta1 "First, you can always ask a TA or an instructor for help."
            ta1 "We know how much aid to give without breaking the value of the assignment."
            if comp61511:
                ta1 "Next, in a lab after submitting SE1, we'll have an exercise where we will do some peer review."


label essay_confused:
    pass
