label dissertation_transition:
    $ score = calculate_score()
    $ initial_score = score
    $ diss_play += 1
    scene black
    with dissolve
    show text "During the rest of the year, you learn a lot of useful stuff"
    pause
    show text "And you spend most of your time with Alex and Pari"
    pause
    show text "But at the end of the year, there is one big milestone left..."
    pause
    show text "Your dissertation"
    pause
    scene black
    with flashbulb
    show text "End of August"
    pause
    scene bg home desk
    pov "Alright, I am nearly finished with my dissertation"
    pov "Finally!"
    pov "Only one paragraph left, and then I will finally be able to submit the dissertation"
    pov "I need to write something about robots and how they are enabled to interact with their environment"
    pov "I don't have much time left and I just want to finish my dissertation"
    pov "Let's see if we can find something"
    scene bg home laptop
    show logicrep:
        xalign 0.5
        yalign 0.3

    pov "Ahh, this looks perfect!"
    pov "This part of the paragraph is all I need to finish my dissertation."

    pov "I'll just use that and the main idea from this article."

    scene bg home white
    with flashbulb
    show logicrep:
        xalign 0.5
        yalign 0.12
        zoom 0.8


    show bad_paragraph:
        xalign 0.5
        yalign 0.3

    pov "Finally I'm finished"
    pov "Looks great! Should I do something?"

    menu:

        "Yeah, there are some more things to be done":
            pov "Ohhh, I nearly forgot to reference the source text!"

        "No, it's fine! I can finally submit my thesis":
            $ paragraph_chosen = "bad_paragraph"
            pov "I will show it to my supervisor first. Just to make sure"
            jump ta_intervention

    jump writing_continue

label writing_continue:
    scene bg home white
    show logicrep:
        xalign 0.5
        yalign 0.12
        zoom 0.75
    show cited_paragraph:
        xalign 0.5
        yalign 0.3


    pov "Now I referenced it!"

    menu:
        pov "Do I want to change some more?"

        "No, it's perfect now!":
            $ paragraph_chosen = "cited_paragraph"
            pov "I will show it to my supervisor first. Just to make sure"
            jump ta_intervention

        "Yes, I think my text is too close to the original":
            $ change_score('patchwriting', +3)
            pov "I have to use my own words!"
            jump patchwriting_part2

        "No, I can show it to my supervisor!":
            $ paragraph_chosen = "cited_paragraph"
            jump ta_intervention


    # Some Minigame simulating your project
    # Another Minigame simulating your dissertation
    # But then, one paragraph is still missing
    # Patchwriting process
    # Check in with supervisor all the time
    # Afterwards, final end with alex and pari at graduation
    # or failed dissertation and you get lower degree and don't want to attend graduation



label patchwriting_part2:
    pov "Well, let's try to write the paragraph"
    scene black
    with flashbulb
    show text "A few minutes later..."
    pause
    scene bg home white
    show logicrep:
        xalign 0.5
        yalign 0.12
        zoom 0.75
    show paragraph1a:
        xalign 0.5
        yalign 0.6
        zoom 0.8

    pov "Okay that's good. It's entirely in my own words."
    pov "But I'm still unsure..."
    pov "I think I will write three versions of my paragraph, and then I can choose the one I like best"
    scene black
    with dissolve
    show text "Several minutes later..."
    pause

    call screen paragraph_choice
    $ paragraph_chosen = _return
    scene bg home desk
    pov "Now I can check with my supervisor"
    jump ta_intervention

screen paragraph_choice:
    imagemap:
        ground "Scene/bg home paragraphchoice.png"
        idle "Scene/bg home paragraphchoice.png"
        hover "Scene/bg home paragraphchoice hover.png"
        selected_idle "Scene/bg home paragraphchoice selected.png"
        selected_hover "Scene/bg home paragraphchoice selected.png"

        hotspot (644, 64, 553, 167) clicked Return("paragraph_good")
        hotspot (644, 232, 553, 213) clicked Return("paragraph_patchwritten")
        hotspot (644, 437, 553, 166) clicked Return("paragraph1c")



label ta_intervention:
    image paragraph_chosen = "[paragraph_chosen]"
    scene black
    with dissolve
    show text "You go to your supervisor's office to check your paragraph"
    pause
    scene bg office
    show instructor talk
    s "Hello, [povname]! How can I help you?"
    show instructor happy
    pov "Well, I have a question about a paragraph for my dissertation"
    pov "Can I show it to you?"
    show instructor talk
    s "Of course!"
    show instructor happy at left
    show paragraph_chosen at truecenter
    if paragraph_chosen == 'bad_paragraph':
        $ change_score('plagiarism_diss', -4)
        s "Oh wow, [povname]"
        s "Please rewrite this paragraph, it's plagiarised"
        s "You didn't even reference your source"
        s "And it's way too close to the original text"
        s "Please rewrite your paragraph and then come back to me"
        menu:

            "Do as she says":
                jump writing_continue

            "Ignore her":
                jump failedassignment

    elif paragraph_chosen == 'cited_paragraph' or paragraph_chosen == 'paragraph_patchwritten':
        $ change_score('plagiarism2_diss', -2)
        show instructor talk
        s "You should really consider to rewrite this paragraph"
        s "It is way to close to the original paragraph"
        s "Let's look at the original paragraph again"
        show logicrep:
            xalign 0.5
            yalign 0.02
            zoom 0.75
        show paragraph_chosen:
            xalign 0.5
            yalign 0.52

        s "See! You are using the exact some words and a similar structure"
        s "Logic-based representations..."
        s "Commonsense reasoning..."
        s "You just used some synonyms and restructured the text a bit"
        s "This is known as patchwriting"
        s "I personally wouldn't consider it academic malpractice, but its still a bad scientific style"
        s "So if you want a high mark, please rewrite the paragraph and then come back to me"
        call screen paragraph_choice
        $ paragraph_chosen = _return
        jump ta_intervention
    elif paragraph_chosen == 'paragraph_good' or paragraph_chosen == 'paragraph1c':
        $ change_score('good_paragraph', +2)
        s "Well done, [povname]!"
        s "You don't need to worry at all. The paragraph is perfectly fine"
        s "You can submit your dissertation now and I will be more then happy to read it!"
        jump happy_end




label failedassignment:

    scene white
    $ change_score('failedassignment', -3)

    pov "Oh no.. "

    pov "I've failed my dissertation! But why?"

    pov "Wait - My Supervisor said that one of my paragraphs was plagarised."

    pov "Maybe I should have taken her advice seriously"

    pov "Now I spent a very difficult year and thousands of Pounds and I didn't even get a degree at the end of it."


    scene black
    show text "You lost..."
    pause
    scene black


    menu:
        "Do you want to try again?"

        "Yes, I can do better!":
            jump first_day
        "Yes, but not from the start":
            jump dissertation_transition
        "No":
            show text "The End"
            pause
            return


label happy_end:

    scene black
    with dissolve
    show text "Several weeks later..."
    pause
    scene bg outside
    with flashbulb

    show keri happy at zoom_norm, slightleft
    show alex happy at zoom_norm, slightright

    pov "Hey Pari! Hey Alex! Are you nervous about the graduation?"

    show alex mhappy at zoomed_in, slightright

    a "Yeah, I am a bit nervous to be honest"

    show alex happy at zoom_norm, slightright
    show keri mhappy at zoomed_in, slightleft
    p "Yeah, me as well!"
    show keri happy at zoom_norm, slightleft
    pov "C'mon guys, let's go inside!"
    scene black
    with dissolve
    show text "You have a great time at the graduation"
    pause
    show text "Everyone is really proud of you"
    pause
    scene black
    $ score = calculate_score()
    $ dissertation_score = score - initial_score
    if formative:

        menu:

            "Do you want to know, how well you did?"

            "Yes":

                if dissertation_score >= 3:
                    show text "Well done!"
                    pause
                    show text "You wrote an excellent dissertation"
                    pause
                else:
                    show text "You did good, but you could have done better!"
                    pause
                    show text "You should consider to replay this part of the game"
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
    scene black
    show text "The End"
    pause
    $ MainMenu(confirm=False)()
    return
