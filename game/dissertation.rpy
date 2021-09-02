label dissertation_transition:
    if not one_chapter_only:
        $ initial_score = score
        $ diss_play += 1
        $ score = calculate_score()
    scene black
    show text "Final chapter"
    with fade
    pause
    scene black
    with fade
    pause 0.5
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
    pov "I need to write something about [dissertation_topic]"
    pov "I don't have much time left and I just want to finish my dissertation"
    pov "Let's see if we can find something"
    scene bg home laptop
    if custom_texts:
        show screen text_screen(source_paragraph, "up")
    else:
        show original_source_paragraph:
            xalign 0.5
            yalign 0.3

    pov "Ahh, this looks perfect!"
    pov "This part of the paragraph is all I need to finish my dissertation."

    pov "I'll just use that and the main idea from this article."

    scene bg home white
    with flashbulb
    if custom_texts:
        hide screen text_screen
        show screen dissertation_text(bad_paragraph)
    else:
        show original_source_paragraph:
            xalign 0.5
            yalign 0.12
            zoom 0.8
        show bad_paragraph:
            xalign 0.5
            yalign 0.3

    pov "Finally, I'm finished"
    pov "Looks great! Should I do something?"
    if custom_texts:
        hide screen dissertation_text
        show screen dissertation_text(bad_paragraph, True)

    menu:
        "Yeah, there are some more things to be done":
            if custom_texts:
                hide screen dissertation_text
                show screen dissertation_text(bad_paragraph)
            pov "Ohhh, I nearly forgot to reference the source text!"

        "No, it's fine! I can finally submit my thesis":
            $ paragraph_chosen = "bad_paragraph"
            if custom_texts:
                hide screen dissertation_text
                show screen dissertation_text(bad_paragraph)
            pov "I will show it to my supervisor first. Just to make sure"
            jump ta_intervention

    jump writing_continue

label writing_continue:
    scene bg home white
    if custom_texts:
        hide screen dissertation_text
        show screen dissertation_text(cited_paragraph)
    else:
        show original_source_paragraph:
            xalign 0.5
            yalign 0.12
            zoom 0.75
        show cited_paragraph:
            xalign 0.5
            yalign 0.3

    pov "Now I referenced it!"

    menu:
        pov "Do I want to change anything else?"

        "No, it's perfect now!":
            $ paragraph_chosen = "cited_paragraph"
            pov "I will show it to my supervisor first. Just to make sure"
            jump ta_intervention

        "Yes, I think my text is too close to the original":
            $ change_score('patchwriting', +3)
            pov "I have to use my own words!"
            if custom_texts:
                hide screen dissertation_text
            jump patchwriting_part2

        "No, I can show it to my supervisor!":
            $ paragraph_chosen = "cited_paragraph"
            jump ta_intervention


label patchwriting_part2:
    pov "Well, let's try to write the paragraph"
    scene black
    with flashbulb
    show text "A few minutes later..."
    pause
    scene black
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

label ta_intervention:
    if custom_texts:
        hide screen dissertation_text
    else:
        image paragraph_chosen = "[paragraph_chosen]"
    scene black
    with dissolve
    show text "You go to your supervisor's office to check your paragraph"
    pause
    scene bg office
    show instructor talk
    s "Hello, [povname]! How can I help you?"
    show instructor happy
    if not ta_visited:
        pov "Well, I have a question about a paragraph for my dissertation"
        pov "Can I show it to you?"
    else:
        pov "I have rewritten the paragraph, can I show it to you?"
    show instructor talk
    s "Of course!"
    show instructor happy at left
    $ ta_visited = True
    if not custom_texts:
        show paragraph_chosen at truecenter
    if paragraph_chosen == 'bad_paragraph':
        $ change_score('plagiarism_diss', -4)
        if custom_texts:
            show screen show_chosen_paragraph(bad_paragraph)
        show instructor mhappy
        s "Oh wow, [povname]"
        show instructor talk
        s "Please rewrite this paragraph, it's plagiarised"
        show instructor mhappy
        s "You didn't even reference your source"
        show instructor talk
        s "And it's way too close to the original text"
        show instructor mhappy
        s "Please rewrite your paragraph and then come back to me"
        menu:

            "Do as she says":
                if custom_texts:
                    hide screen show_chosen_paragraph
                jump writing_continue

            "Ignore her":
                if custom_texts:
                    hide screen show_chosen_paragraph
                jump failedassignment

    elif paragraph_chosen == 'cited_paragraph' or paragraph_chosen == 'paragraph_patchwritten':
        if custom_texts:
            if paragraph_chosen == 'cited_paragraph':
                show screen show_chosen_paragraph(cited_paragraph)
            else:
                show screen show_chosen_paragraph(paragraph_patchwritten)
        $ change_score('plagiarism2_diss', -2)
        show instructor mhappy
        s "You should really consider rewriting this paragraph"
        show instructor talk
        s "It is way too close to the original paragraph"
        show instructor mhappy
        s "Let's look at it again"
        if custom_texts:
            hide screen show_chosen_paragraph
            if paragraph_chosen == 'cited_paragraph':
                show screen compare_chosen_paragraph(cited_paragraph)
            else:
                show screen compare_chosen_paragraph(paragraph_patchwritten)
        else:
            show original_source_paragraph:
                xalign 0.5
                yalign 0.02
                zoom 0.75
            show paragraph_chosen:
                xalign 0.5
                yalign 0.52

        show instructor talk
        $ similar_words = patchwritten_words
        while len(similar_words) > 0:
            $ word = similar_words.pop(0)
            if custom_texts:
                if paragraph_chosen == 'cited_paragraph':
                    $ marked_paragraph = highlight_word(cited_paragraph, word)
                else:
                    $ marked_paragraph = highlight_word(paragraph_patchwritten, word)
                $ marked_source = highlight_word(source_paragraph, word)
                show screen compare_chosen_paragraph(marked_paragraph, marked_source)
                s "[word]..."
                hide screen compare_chosen_paragraph
            else:
                s "[word]..."
        if custom_texts:
            if paragraph_chosen == 'cited_paragraph':
                show screen compare_chosen_paragraph(cited_paragraph)
            else:
                show screen compare_chosen_paragraph(paragraph_patchwritten)
        show instructor mhappy
        menu:
            s "You just used some synonyms and restructured the text a bit"

            "And?":
                pass

            "So?":
                pass
        show instructor talk
        s "This is known as patchwriting"
        show instructor mhappy
        menu:
            s "I personally wouldn't consider it academic malpractice..."

            "So, I am allowed to do it?":
                s "Well, you shouldn't"

            "And why shouldn't I do it?":
                pass
        show instructor talk
        s "It is still a bad scientific style"
        show instructor mhappy
        s "So if you want a high mark, please rewrite the paragraph and then come back to me"
        if custom_texts:
            hide screen compare_chosen_paragraph
        call screen paragraph_choice
        $ paragraph_chosen = _return
        jump ta_intervention
    elif paragraph_chosen == 'paragraph_good' or paragraph_chosen == 'mediocre_paragraph_with_reference':
        $ change_score('good_paragraph', +2)
        if custom_texts:
            if paragraph_chosen == 'paragraph_good':
                show screen show_chosen_paragraph(paragraph_good)
            else:
                show screen show_chosen_paragraph(paragraph_excellent)
        show instructor mhappy
        s "Well done, [povname]!"
        show instructor talk
        s "You don't need to worry at all. The paragraph is perfectly fine"
        show instructor mhappy
        s "You can submit your dissertation now and I will be more than happy to read it!"
        if custom_texts:
            hide screen show_chosen_paragraph
        jump happy_end




label failedassignment:

    scene white
    $ change_score('failedassignment', -3)

    pov "Oh no... "

    pov "I failed my dissertation! But why?"

    pov "Wait... My supervisor said that one of my paragraphs was plagiarised."

    pov "Maybe I should have taken her advice seriously"

    pov "Now I went through a very difficult year and spent thousands of Pounds..."

    pov "And in the end, I didn't even get my master degree."


    scene black
    show text "You lost..."
    pause
    scene black


    menu:
        "Do you want to try again?"

        "Yes, I can do better!":
            jump dissertation_transition
        "Yes, but not from the start":
            jump ta_intervention
        "No":
            show text "The End"
            pause
            return


label happy_end:

    scene black
    with dissolve
    show text "Several months later..."
    pause
    scene bg outside
    with flashbulb

    show keri happy at zoom_norm, slightleft
    show alex happy at zoom_norm, slightright

    pov "Hey, Pari! Hey, Alex! Are you nervous about the graduation ceremony?"

    show alex mhappy at zoomed_in, slightright

    a "Yeah, I am a bit nervous, to be honest"

    show alex happy at zoom_norm, slightright
    show keri mhappy at zoomed_in, slightleft
    p "Yeah, me as well!"
    show keri happy at zoom_norm, slightleft
    pov "Come on guys, let's go inside!"
    scene black
    with dissolve
    show text "You have a great time at the graduation"
    pause
    show text "Everyone is really proud of you"
    pause
    scene black
    if not one_chapter_only:
        $ score = calculate_score()
        $ dissertation_score = score - initial_score
        if formative:

            if dissertation_score >= 3:
                show text "Well done!"
                pause
                show text "You wrote an excellent dissertation"
                pause
            else:
                show text "You did well, but you could have done better!"
                pause
                show text "You should consider replaying this part of the game"
                pause
                scene black
                menu:
                    "Would you like to try again?"

                    "Yes, I can do better":
                        jump dissertation_transition

                    "Nah, I'm fine":
                        pass

    scene black
    show text "The End"
    pause
    $ MainMenu(confirm=False)()
    return
    return
