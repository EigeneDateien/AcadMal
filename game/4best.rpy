
define b = Character("Sara", kind=nvl)
label start_best:
    #show bee helpful
    b "Hi there!"
    b "I'm an expert writer with a lot of experience."
    b "You probably have gotten a lot of {b}Don't{/b}s i.e.,..."
    b "{b}Don't collude!{/b}"
    b "{b}Don't plagiarise!{/b}"
    nvl clear
    b "And some {b}Do{/b}s that feel a bit like {b}Don't{/b}s e.g.,..."
    b "Cite your sources (so you {b}don't{/b} plagiarise)!"
    b """That's a lot about what {i}not{/i} to do.

    I'm here to give you some {i}positive{/i} tips. Instead of focusing
    on what {i}not{/i} to do, I'm going to focus on what {i}to do{/i}.

    These are generally known as \"best practices\".

    {clear}

    One thing to remember about best practices:

    They don't guaruntee success! Even at avoiding malpractice!

    You still need the {b}don't{/b}s and to check your work.

    Best practices still can be done poorly. You need to practice them!
    """
    show sara talk:
        pos(100, 40)
        zoom 0.6
    define b_adv = Character("Sara")
    $ b = b_adv
    b "Let's get started!"
    if persistent.start_goals == None:
        b "I recommend starting with the goals of writing."

    python:

        cs = [("The Goals of Writing", 'start_goals'),
              ("Explore Coursework Essay Questions", 'coursework'),
              ("Explore Exam Essay Questions", 'exam'),
              ("Explore Dissertation Writing", 'dissertation')]
        tracked_menu(cs, call=True)

label start_goals:
    b """People use writing for different purposes.

    Three key reasons for writing something are 1) to improve your understanding,
    2) to communicate with others, and...

    3) to get a certain mark.

    They are interrelated, but we can consider each in turn."""

    show sara happy:
        pos(100, 40)
        zoom 0.6

    menu:
        "Goal 1: Improve Understanding":
            show sara talk:
                pos(100, 40)
                zoom 0.6
            b """This is probably the most important goal and a key reason for writing.

            This is what most of your coursework is trying to do.

            Even if you get marks for it, the assignments are intended to be {i}formative{/i}.

            That is, they aim to help you improve your mastery of the material.

            We can contrast that with exam situations, which are {i}summative{/i}.

            That is, the aim to measure your mastery of the material.

            Getting things wrong on coursework can be a good thing...{i}if{/i} you can
            use your mistakes to improve.

            This is one reason that plagiarism, in addition to being wrong, is also counterproductive. You
            don't learn how to write an essay or much about a topic by merely copying someone else."""
            menu:
                "Explore some of the theory behind this":
                    jump theory
                "Move on to Goal 2":
                    jump .communicate

        "Goal 2: Communicate With Others":
            label .communicate:
                show sara talk:
                    pos(100, 40)
                    zoom 0.6
                "WE ARE COMMUNICATING!!"
                b """You might have to work with others during your coursework.

                When working in groups as well as for individual tasks, you should always try to be as clear as possible

                For written assignments, we will assess how well you communicate and explain difficult scenarios or terms.

                For group assignments, you won't be able to get high marks without a good communication.

                """

                b "Let's move to goal 3"

                jump mark
        "Goal 3: Get a Mark":
            label mark:
                show sara talk:
                    pos(100, 40)
                    zoom 0.6
                b "This might be the most interesting goal for your study. But beware that the other options are just as important"
                show sara happy:
                    pos(100, 40)
                    zoom 0.6
                menu:
                    b "If you like, I can give you some tips and best practices on how to deal with coursework, exams and your dissertation"

                    "That would be great":
                        jump best_practices

                    "No, thanks":
                        scene black
                        "Returning to explorations"
                        jump intro

label theory:
    show sara talk:
        pos(100, 40)
        zoom 0.6
    b """There are a lot of theories about how people learn.

    None of them are conclusive...learning is a very complex phenomenon.

    One common theme, however, is that learning is something {i}active{/i}. That is,
    learning is something students need to {i}do{/i}, not something that {i}happens{/i} to them.

    Let's consider a simple example of asnwering a short essay question."""

    show text "What is a Turing Machine?"

    b """The essence of this question can be phrased in many ways.

    But as it's written, it looks like a simple recall or research question.

    We could answer it from Wikipedia!"""
    hide text "What is a Turing Machine?"
    show wikipedia_turing_machine at top
    b "Indeed, it seems like the first paragraph does the job!"

    b "We could cut and paste it and have an answer!"

    hide wikipedia_turing_machine
    image tm 1 = Text("A Turing machine is a mathematical model of computation that defines an abstract machine,[[1]\n which manipulates symbols on a strip of tape according to a table of rules.[[2] \nDespite the model's simplicity, given any computer algorithm, a Turing machine capable of simulating that algorithm's logic can be constructed.", size=30, justify=True)
    show tm 1 at truecenter

    b "Ok, we might want to clean it up a bit! You know, get rid of the footnote markers."
    image tm 2 = Text("A Turing machine is a mathematical model of computation that defines an abstract machine, which manipulates symbols on a strip of tape according to a table of rules. Despite the model's simplicity, given any computer algorithm, a Turing machine capable of simulating that algorithm's logic can be constructed.", size=30, justify=True)


    show tm 2 at truecenter
    b "So! What sort of answer is it?"
    show sara happy:
        pos(100, 40)
        zoom 0.6
    menu:

        "This is a perfectly fine answer.":
            $ mark('plagiarism', -1)
            $ mark('passivity', -1)
            show sara sad:
                pos(100, 40)
                zoom 0.6
            b "At the very least, you should have noted the potentially very serious academic malpractice issue!"
        "This will be a perfectly fine answer once you fix the citation issue.":
            show sara talk:
                pos(100, 40)
                zoom 0.6
            $ mark('passivity', -1)
            b "At the very least, we must fix that citation issue!"
            call .plag(True) from _call_theory_plag

        "This is not a good answer.":
            show sara vhappy:
                pos(100, 40)
                zoom 0.6
            p "Yes, it has multiple problems."
            show sara talk:
                pos(100, 40)
                zoom 0.6
            p "Let's deal with the citation problem first"
            jump .plag

label .plag(only_one=False):
    show sara talk:
        pos(100, 40)
        zoom 0.6
    b "Note that the problem here isn't claiming credit for the {i}idea{/i}, since that's common knowledge, but for the text."
    b "We in no way wrote those words!"
    b "But a simple fix gets us out of that problem:"

    image tm 3 = Text("\"A Turing machine is a mathematical model of computation that defines an abstract machine, which manipulates symbols on a strip of tape according to a table of rules. Despite the model's simplicity, given any computer algorithm, a Turing machine capable of simulating that algorithm's logic can be constructed.\"\n--From https://en.wikipedia.org/wiki/Turing_machine", size=25, justify=True)
    show tm 3
    b "Quote and reference!"
    show sara happy:
        pos(100, 40)
        zoom 0.6
    menu:
        "With the citation, we've fixed all the problems.":
            show sara talk:
                pos(100, 40)
                zoom 0.6
            p "With the citation we've avoided sanctionable academic malpractice."
            p "Which is a good thing."
            p "But this answer has a lot of problems, both from grade you'll get and from a learning perspective."
        "Even with this tweak, it's not a good answer.":
            show sara talk:
                pos(100, 40)
                zoom 0.6
            p "Exactly. We've managed to avoid sanctionable academic malpractice, but we're unlikely to get a good grade and we problably haven't learned much."
    jump .passive

label .passive:
    show sara talk:
        pos(100, 40)
        zoom 0.6
    b """A major issue with this answer, both from the perspective of your learning and of assessing your learning is that you didn't do much!

    If this was a formative question, the goal wasn't for you to search and retrieve a paragraph. We're not testing your googling skills!

    Typically, we want you to {i}learn something{/i} about Turing Machines.

    Think what happens when you cut and paste an answer.

    You may read the paragraph, but you don't need to fully understand it to {i}recognise{/i} that it's a plausible
    answer.

    Indeed, the content of the paragraph doesn't spend much time \"in your head\".

    You spend more time getting the citation right than you do on Turing Machines!

    """
    hide tm 2
    show wf tm 1 at top

    b "When you cut and paste, you can spend almost no time at all thinking about the content."

    b "Even mere retyping has a better chance of getting some of the content into your head."

    b "Of course, you can always try modifying the result of a cut and paste or retyping."
    hide wf
    show tm 3 at truecenter
    b "We can try to modify our quote into a paraphrase."
    b "We remove the quotes and identify some words to change."
    image tm 4 = Text("A Turing machine is a {u}mathematical{/u} model of computation that defines an abstract {u}machine{/u}, which manipulates symbols on a strip of {u}tape{/u} according to a {u}table{/u} of rules. Despite {u}the model's simplicity{/u}, given any computer {u}algorithm{/u}, {u}a Turing machine capable of simulating that algorithm's logic can be constructed{/u}.\n--From https://en.wikipedia.org/wiki/Turing_machine", size=25, justify=True)
    show tm 4
    b "Now we can replace or rewrite the identified bits."
    image tm 5 = Text("A Turing machine is a {u}conceptual{/u} model of computation that defines an abstract {u}system{/u}, which manipulates symbols on a strip of {u}paper{/u} according to a {u}set{/u} of rules. Despite {u}this minimalism{/u}, given any computer {u}program{/u}, {u}we can design a Turing machine which can execute that program.{/u}.\n--From https://en.wikipedia.org/wiki/Turing_machine", size=25, justify=True)
    show tm 5
    b "This does give us an answer different from the original text!"


label best_practices:
    show sara happy:
        pos(100, 40)
        zoom 0.6

    menu:
        b "What would you like to discuss first?"

        "Coursework":
            jump coursework

        "Exams":
            jump exam

        "Dissertation":
            jump dissertation

        "I'm fine, thanks!":
            show sara talk:
                pos(100, 40)
                zoom 0.6
            b "You're welcome"
            "Now we return back to your explorations"
            hide sara
            jump intro

label coursework:
    show sara talk:
        pos(100, 40)
        zoom 0.6
    b "In your coursework, you may have not only pure programming tasks"
    b "Many lectures include some kind of essay"
    b "For these essays, there are some best practices to follow"
    b "If you need to answer a question or explain a term or phenomenon you should try to find information"
    show sara happy:
        pos(100, 40)
        zoom 0.6
    menu:
        b "Where would you look for information first?"

        "The slides":
            show sara talk:
                pos(100, 40)
                zoom 0.6
            b "Great, it is always a good idea to consult the slides first"
            b "Most likely, the relevant information will be at least mentioned"

        "The provided literature":
            show sara talk:
                pos(100, 40)
                zoom 0.6
            b "That is a great idea! However, you may consult the slides first"
            b "Often, the information you need is at least mentioned there"
            b "But the provided literature is a excellent second step!"

        "Look it up online":
            show sara talk:
                pos(100, 40)
                zoom 0.6
            b "Well, that is the most straightforward idea, isn't it?"
            b "However, for most of the essay questions the answer is not so obvious."
            b "You may need to consult different sources some of which might be not as qualified as others"
            b "That is why you should try to find some information in the slides and the provided literature"
            b "Afterwards, you may have found out for which information you are looking"
            b "And remember, some online sources may have wrong information"

    show sara talk:
        pos(100, 40)
        zoom 0.6
    b "For these essays, it is not enough to just look for the information"
    b "You will always have to write the gathered information in your own words"
    show sara happy:
        pos(100, 40)
        zoom 0.6
    menu:
        b "What do you think will get you the most marks"

        "Copy and paste should be sufficient":
            show sara talk:
                pos(100, 40)
                zoom 0.6
            b "Well, this will get you exactly zero points. If you forget to reference it properly, you may face some serious problems"

        "Reading and understand the content of several sources before writing my essay":
            show sara talk:
                pos(100, 40)
                zoom 0.6
            b "Right! It is important that you do understand the sources"
            b "If you don't understand a text, we will most likely find out because of the way you are writing about it"

        "Rearranging the text and inserting synonyms for words in the source":
            show sara talk:
                pos(100, 40)
                zoom 0.6
            b "While this might be the way to go in some areas, it won't get you high marks here"
            b "We want to know whether you have understood a topic"
            b "If you don't understand a source text, we will most likely find out because of the way you are writing about it"

    if not goodwritingbool:
        jump goodwriting

label goodwriting(context = "essay"):
    $ goodwritingbool = True
    show sara talk:
        pos(100, 40)
        zoom 0.6
    b "When you have found the right information, it may be useful to follow these steps to get a higher mark:"
    b "First, try to understand the topic of your task"
    b "Then read the information you have several times and try to understand the given information"
    if context == "essay":
        b "When you dont understand something, look for an answer in the slides, the literature or online"
        b "If you can't find anything or you are still struggling to understand you can always ask a TA"
        b "You can always post a question on blackboard as well"
        b "Here, students and staff will see your question and will try to answer it"
    else:
        b "When you dont understand something, look for an answer in the literature"
        b "You can always ask your supervisor"
        b "He will guide you to the relevant resources"
    b "After having read and understood the text, give yourself a short break"
    b "Let the information sink in"
    b "Write down in your own words what you have understood"
    b "Check with the source text to see if they resemble each other"
    b "For resembling paragraphs try to formulate the paragraphs in your own words"
    b "Often, your structure will differ from the structure in the source text because of the question you were given to answer"
    b "And remember, never forget to reference your sources!"
    b "After you wrote your text leave it for some time"
    b "Come back after a while and reread your essay"
    b "You may rewrite some parts that seem unclear or misleading"
    jump best_practices

label exam:
    show sara talk:
        pos(100, 40)
        zoom 0.6
    b "Your exam may include some short essay-style questions"
    b "Most of the lectures with these kind of questions will include some essay assessment during the coursework"
    b "It will help you practicing writing essays"
    b "It is important that you understand the feedback given to you after submission"
    b "The feedback will guide you to understand what we expect from you in the exams"
    b "Also, the library has some useful courses and resources to help you writing."
    b "These courses will help with most of the problems you might encounter"
    jump best_practices

label dissertation:
    show sara talk:
        pos(100, 40)
        zoom 0.6
    b "The library has some useful courses and resources to help you writing."
    b "These courses will help with most of the problems you might encounter"
    b "Also make sure to attend lectures provided by your school about scientific writing"
    b "It is important that you never copy and paste a paper or a book chapter"
    b "Also make sure to reference your sources"
    b "Furthermore, follow the guidlines of good writing"
    if not goodwritingbool:
        call goodwriting pass (context = "dissertation") from _call_goodwriting
    jump best_practices
