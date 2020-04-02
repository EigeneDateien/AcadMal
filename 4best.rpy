
define b = Character("Bee", kind=nvl)
label start_best:
    show bee helpful
    b "Hi there!"
    b "I'm an expert writer will a lot of experience."
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
    define b_adv = Character("Bee")
    $ b = b_adv
    b "Let's get started!"
    if persistent.start_goals == None:
        b "I recommend starting with the goals of writing."

    python:

        cs = [("The Goals of Writing", 'start_goals'),
              ("Explore Coursework Essay Questions", 'start_cw'),
              ("Explore Exam Essay Questions", 'start_examq'),
              ("Explore Dissertation Writing", 'start_diss')]
        tracked_menu(cs, call=True)

label start_goals:
    b """People use writing for different purposes.

    Three key reasons for writing something are 1) to improve your understanding,
    2) to communicate with others, and...

    3) to get a certain mark.

    They are interrelated, but we can consider each in turn."""

    menu:
        "Goal 1: Improve Understanding":
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
                "WE ARE COMMUNICATING!!"
        "Goal 3: Get a Mark":
            pass
label theory:
    b """There are a lot of theories about how people learn.

    None of them are conclusive...learning is a very complex phenomenon.

    One common theme, however, is that learning is something {i}active{/i}. That is,
    learning is something students need to {i}do{/i}, not something that {i}happens{/i} to them.

    Let's consider a simple example of asnwering a short essay question."""

    show text "What is a Turing Machine?"

    b """The essence of this  question can be phrased in many ways.

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
    menu:

        "This is a perfectly fine answer.":
            $ mark('plagiarism', -1)
            $ mark('passivity', -1)
            b "At the very least, you should have noted the potentially very serious academic malpractice issue!"
        "This will be a perfectly fine answer once you fix the citation issue.":
            $ mark('passivity', -1)
            b "At the very least, we must fix that citation issue!"
            call .plag(True)

        "This is not a good answer.":
            p "Yes, it has multiple problems."
            p "Let's deal with the citation problem first"
            jump .plag

label .plag(only_one=False):
    b "Note that the problem here isn't claiming credit for the {i}idea{/i}, since that's common knowledge, but for the text."
    b "We in no way wrote those words!"
    b "But a simple fix gets us out of that problem:"

    image tm 3 = Text("\"A Turing machine is a mathematical model of computation that defines an abstract machine, which manipulates symbols on a strip of tape according to a table of rules. Despite the model's simplicity, given any computer algorithm, a Turing machine capable of simulating that algorithm's logic can be constructed.\"\n--From https://en.wikipedia.org/wiki/Turing_machine", size=25, justify=True)
    show tm 3
    b "Quote and reference!"
    if only_one:
        menu:
            "With the citation, we've fixed all the problems.":
                p "With the citation we've avoided sanctionable academic malpractice."
                p "Which is a good thing."
                p "But this answer has a lot of problems, both from grade you'll get and from a learning perspective."
            "Even with this tweak, it's not a good answer.":
                p "Exactly. We've managed to avoid sanctionable academic malpractice, but we're unlikely to get a good grade and we problably haven't learned much."
    jump .passive

label .passive:
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
