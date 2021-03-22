label introduction_tut:
    scene bg office
    show sara talk:
        zoom 0.7
        xalign 0.5

    if tutorial_already:
        ta1 "Hello again, [povname]"
        show sara vhappy
        ta1 "So, you decided on another tutorial!"
        show sara mhappy
        ta1 "Great!"

    else:
        $ tutorial_already = True

        ta1 "Hello, [povname]"
        show sara vhappy
        ta1 "So you decided on virtual tutoring. Excellent choice"
        show sara mhappy
        ta1 "We will now go through some examples that might help you understand the topic"

    if plag:
        $ plag = False
        jump plag_tut

    elif collab:
        $ collab = False
        jump coll_tut

    elif fabrication:
        $ fabrication = False
        jump fabr_tut

    else:
        jump tut_decision

label tut_decision:
    show sara happy at zoom_norm
    menu:
        ta1 "Which topic would you like to talk about?"

        "Plagiarism":
            jump plag_tut

        "Collusion":
            jump coll_tut

        "Fabrication and Falsification":
            jump fabr_tut


label plag_tut:
    scene bg office
    show sara mhappy:
        zoom 0.7
        xalign 0.5
    ta1 "So, let's talk about plagiarism!"
    show sara happy at zoom_norm
    show sara happy at slidewideleft
    menu:
        ta1 "What do you think is plagiarism?"

        "Taking someone else's work and passing it off as your own":
            show sara talk:
                xalign 0.5
                zoom 0.7
            ta1 "That's certainly one example of plagiarism"
            show sara mhappy
            ta1 "It's actually all of the previously mentioned examples"
            show sara talk
            ta1 "Copying someone else's work without paraphrasing or correct quotation is plagiarism, too"
            show sara happy at zoom_norm
            pov "And copying a paragraph from a friend's essay without them knowing?"
            show sara talk at zoomed_in
            menu:
                ta1 "What do you think: is it plagiarism?"

                "Yes":
                    show sara vhappy
                    "Correct!"

                "No":
                    show sara sad
                    "Well, actually, it is"


        "Copying a paragraph from a friend's essay without their knowing":
            show sara talk:
                xalign 0.5
                zoom 0.7
            ta1 "That's certainly one example of plagiarism"
            show sara mhappy
            ta1 "It's actually all of the previously mentioned examples"
            show sara talk
            ta1 "Taking someone else's work and passing it off as your own is plagiarism, too"
            show sara happy at zoom_norm
            pov "And copying someone else's work without paraphrasing or correct quotation?"
            show sara talk at zoomed_in
            menu:
                ta1 "What do you think? Is it plagiarism?"

                "Yes":
                    show sara vhappy
                    "Correct!"

                "No":
                    show sara sad
                    "Well, actually, it is"


        "Copying someone else's work without paraphrasing or using quotation marks around the copied sentence":
            show sara talk:
                xalign 0.5
                zoom 0.7
            ta1 "That's certainly one example of plagiarism"
            show sara mhappy
            ta1 "It's actually all of the previously mentioned examples"
            show sara talk
            ta1 "Taking someone else's work and passing it off as your own is plagiarism, too"
            show sara happy at zoom_norm
            pov "And copying a paragraph from a friend's essay without their knowing?"
            show sara talk at zoomed_in
            menu:
                ta1 "What do you think, is it plagiarism?"

                "Yes":
                    show sara vhappy
                    "Correct!"

                "No":
                    show sara sad
                    "Well, actually, it is"



        "All of the above":
            show sara talk:
                xalign 0.5
                zoom 0.7
            ta1 "That's right!"


    ta1 "So, let's see some examples then"
    show sara mhappy

    scene bg home white
    show manchester original:
        xalign 0.5
        yalign 0.5
        zoom 0.8
    ta1 "Let this be the source text that we want to use for our essay"
    scene bg home white
    show manchester original:
        xalign 0.15
        yalign 0.11
        zoom 0.7

    show manchester_original:
        xalign 0.9
        yalign 0.11
        zoom 0.7

    show manchester_copied_reference:
        xalign 0.15
        yalign 0.62
        zoom 0.7

    show manchester_copied_quotation:
        xalign 0.9
        yalign 0.62
        zoom 0.7

    ta1 "Let's now compare it with these three attempts"
    show manchester_copied_reference:
        xalign 0.15
        yalign 0.8
        zoom 0.7

    show manchester_copied_quotation:
        xalign 0.9
        yalign 0.8
        zoom 0.7
    pause
    show manchester_copied_reference:
        xalign 0.15
        yalign 0.62
        zoom 0.7

    show manchester_copied_quotation:
        xalign 0.9
        yalign 0.62
        zoom 0.7

    ta1 "Can you identify the correct paragraph?"
    ta1 "Which paragraph was NOT plagiarised?"
    show manchester_copied_reference:
        xalign 0.15
        yalign 0.9
        zoom 0.7

    show manchester_copied_quotation:
        xalign 0.9
        yalign 0.9
        zoom 0.7
    menu:

        "Upper right":
            $ chosen_tut_paragraph = "upperright"
            jump upper_right_paragraph

        "Lower left":
            $ chosen_tut_paragraph = "lowerleft"
            jump lower_left_paragraph

        "Lower right":
            $ chosen_tut_paragraph = "lowerright"
            jump lower_right_paragraph



    # ta1 "Let's say, you have found an interesting paragraph, you want to include in your essay"
    # show sara talk
    # ta1 "The paragraph is about something you have previously discussed in class"
    # ta1 "So the content is considered to be common knowledge among you students"
    # show sara happy at zoom_norm
    #
    # menu:
    #
    #     ta1 "What is NOT considered as plagiarism?"
    #
    #     "Copying the paragraph as is without referencing":
    #         show sara sad at zoomed_in
    #         ta1 "Well, that is plagiarism"
    #         ta1 "If you copy something, you have to reference it and put quotation marks around the copied paragraph"
    #         show sara talk
    #
    #     "Copying the paragraph as is with a reference":
    #         show sara sad at zoomed_in
    #         ta1 "Well, that is plagiarism"
    #         ta1 "If you copy something, you have to reference it and put quotation marks around the copied paragraph"
    #         show sara talk
    #
    #     "Copying the paragraph as is with a reference and quotation marks around the paragraph":
    #         show sara vhappy at zoomed_in
    #         ta1 "Correct!"
    #         ta1 "That is not considered plagiarism."
    #         show sara talk


label continue_plag_tut:
    scene bg office
    with dissolve
    show sara talk:
        xalign 0.5
        zoom 0.7
    ta1 "So, as we could see in the examples:"
    show sara mhappy
    ta1 "If you copy a paragraph, you have to reference it."
    show sara happy at zoom_norm
    pov "And you have to put the copied paragraph in quotation marks"
    show sara vhappy at zoomed_in
    ta1 "Yeah, right!"
    show sara talk
    ta1 "This way, it is clear what content you quoted and where you quote comes from"
    show sara mhappy
    ta1 "However, make sure to not use too many quotes but more of your own words"
    show sara happy at zoom_norm
    pov "Yes, I will try"
    show sara talk at zoomed_in
    ta1 "Great, so, let's have another round of examples"
    scene bg home white
    show manchester original:
        xalign 0.5
        yalign 0.5
        zoom 0.8
    ta1 "As you can see, we have the same source text as before"
    scene bg home white
    show manchester original:
        xalign 0.15
        yalign 0.11
        zoom 0.7

    show manchester_synonyms:
        xalign 0.9
        yalign 0.11
        zoom 0.7

    show manchester_perfect:
        xalign 0.15
        yalign 0.62
        zoom 0.7

    show manchester_synonyms_structure:
        xalign 0.9
        yalign 0.62
        zoom 0.7

    ta1 "Let's now compare it with these three new attempts"

    show manchester_perfect:
        xalign 0.15
        yalign 0.8
        zoom 0.7

    show manchester_synonyms_structure:
        xalign 0.9
        yalign 0.8
        zoom 0.7
    pause
    show manchester_perfect:
        xalign 0.15
        yalign 0.62
        zoom 0.7

    show manchester_synonyms_structure:
        xalign 0.9
        yalign 0.62
        zoom 0.7

    ta1 "This time, which paragraph do you think is the best?"
    show manchester_perfect:
        xalign 0.15
        yalign 0.9
        zoom 0.7

    show manchester_synonyms_structure:
        xalign 0.9
        yalign 0.9
        zoom 0.7

    menu:

        "Upper right":
            $ chosen_tut_paragraph2 = "upperright"
            jump upper_right_paragraph2

        "Lower left":
            $ chosen_tut_paragraph2 = "lowerleft"
            jump lower_left_paragraph2

        "Lower right":
            $ chosen_tut_paragraph2 = "lowerright"
            jump lower_right_paragraph2



    # ta1 "Speaking of own words:"
    # ta1 "What if you are in a hurry, because a deadline is coming up"
    # show sara happy at zoom_norm
    # menu:
    #     "Can you just copy a paragraph and change up the words with synonyms"
    #
    #
    #     "Yes, as long as I use enough synonyms":
    #         show sara sad at zoomed_in
    #         ta1 "No, sorry. You still haven't done much"
    #         show sara talk
    #         ta1 "You just replaced some words"
    #         ta1 "But you should write it in your own words"
    #         show sara mhappy
    #         ta1 "Especially if you do not reference the original paragraph"
    #         ta1 "Try to paraphrase the paragraph, reference the idea and try to use more than just one source"
    #
    #     "No, only if I change up the structure as well":
    #         show sara sad at zoomed_in
    #         ta1 "Sorry, [povname]! I know that most students think that this is enough"
    #         show sara talk
    #         ta1 "But you should write it in your own words"
    #         show sara happy at zoom_norm
    #         pov "But what if I am not too confident about my English?"
    #         show sara mhappy at zoomed_in
    #         ta1 "You would still need a reference. But even if you struggle with your English:"
    #         ta1 "It is always better to write a text in your own words. Even when there are some mistakes"
    #         ta1 "Try to paraphrase the paragraph, reference the idea and try to use more than just one source"
    #
    #
    #     "No, I should write it completely in my own words.":
    #         show sara vhappy at zoomed_in
    #         ta1 "Yes! Perfect!"
    #         show sara talk
    #         ta1 "It is always better to write a text in your own words. Even when there are some mistakes"
    #         ta1 "And remember to try to paraphrase the paragraph. Reference the idea and try to use more than just one source"


label final_plag_tut:
    scene bg office
    with dissolve
    show sara talk:
        xalign 0.5
        zoom 0.7
    ta1 "It is always better to write a text in your own words. Even when there are some mistakes"
    show sara mhappy
    ta1 "And remember to try to paraphrase the paragraph. Reference the idea and try to use more than just one source"
    show sara talk
    ta1 "I hope this little tutorial helped you a bit"
    show sara mhappy
    ta1 "And remember: if you have any questions, you can always ask your instructors or the TAs"
    if collab:
        ta1 "I see that there is some confusion about collusion as well"
        jump coll_tut

    menu:
        ta1 "Do you want to discuss something else?"

        "Yes":
            jump tut_decision

        "No":
            ta1 "Ok. See you, [povname]"

    return

label upper_right_paragraph:
    $ upper_right_paragraph_b = True
    scene bg home white
    show manchester original:
        xalign 0.15
        yalign 0.11
        zoom 0.7

    show manchester_original:
        xalign 0.9
        yalign 0.11
        zoom 0.7
    show manchester_copied_reference:
        xalign 0.15
        yalign 0.62
        zoom 0.7

    show manchester_copied_quotation:
        xalign 0.9
        yalign 0.62
        zoom 0.7
    ta1 "Let's see the paragraph on the upper right side"
    scene bg home white
    show manchester original:
        xalign 0.5
        yalign 0.11
        zoom 0.7

    show manchester_original:
        xalign 0.5
        yalign 0.6
        zoom 0.7

    ta1 "On top we see the original paragraph"
    if chosen_tut_paragraph == "upperright":
        ta1 "Below is your chosen paragraph that you think was not plagiarised"
    else:
        ta1 "Again, below is the paragraph we want to compare"
    menu:
        ta1 "Can you spot any difference between these two paragraphs?"

        "There is no difference":
            pass

        "They are the same":
            pass

    ta1 "Exactly! So, the paragraph was copied"
    menu:
        ta1 "Do you think a direct copy without reference is considered plagiarism?"

        "No, I think it is the correct way":
            ta1 "Well, it is plagiarism in its purest form"
            ta1 "You just copied a paragraph from somewhere without referencing it at all or marking it as copied"
            pov "Oh, I see."

        "Oh yes, it is":
            ta1 "You are right. This paragraph was plagiarised"
            ta1 "Just directly copying a paragraph is clearly not enough"

    if not lower_left_paragraph_b or not lower_right_paragraph_b:
        ta1 "So, let's see the next possible paragraph"
        if not lower_left_paragraph_b:
            jump lower_left_paragraph
        elif not lower_right_paragraph_b:
            jump lower_right_paragraph
        else:
            jump continue_plag_tut
    else:
        jump continue_plag_tut

label lower_left_paragraph:
    $ lower_left_paragraph_b = True
    scene bg home white
    show manchester original:
        xalign 0.15
        yalign 0.11
        zoom 0.7

    show manchester_original:
        xalign 0.9
        yalign 0.11
        zoom 0.7
    show manchester_copied_reference:
        xalign 0.15
        yalign 0.62
        zoom 0.7

    show manchester_copied_quotation:
        xalign 0.9
        yalign 0.62
        zoom 0.7
    ta1 "Let's see the paragraph on the lower left side"
    scene bg home white
    show manchester original:
        xalign 0.5
        yalign 0.11
        zoom 0.7

    show manchester_copied_reference:
        xalign 0.5
        yalign 0.6
        zoom 0.7


    ta1 "On top we see the original paragraph"
    if chosen_tut_paragraph == "lowerleft":
        ta1 "Below is your chosen paragraph that you think was not plagiarised"
    else:
        ta1 "Again, below is the paragraph we want to compare"
    menu:
        ta1 "So, what is the difference between these two paragraphs?"

        "Well, the lower paragraph has a reference":
            pass

        "The text is the same":
            pass

    ta1 "Exactly! So, the paragraph was copied"
    ta1 "But at least, it was referenced where it was copied from"
    menu:
        ta1 "Do you think a direct copy with a reference is considered plagiarism?"

        "No, because of the reference this is not plagiarism":
            ta1 "Well, even with a reference it is plagiarism"
            ta1 "The text is copied without any quotation marks."
            ta1 "So, a reference just tells the reader where the information is drawn from"
            ta1 "But without quotation marks it seems like you wrote the text..."
            pov "... which is not the case because I just copied it"
            ta1 "Exactly!"
            pov "Okay, I think I understand"

        "Oh yes, a reference is not enough":
            ta1 "You are right"
            ta1 "The reference just tells the reader where the information is drawn from"
            ta1 "But without quotation marks it seems like you wrote the text..."
            pov "... which is not the case because I just copied it"
            ta1 "Exactly! So, this paragraph was plagiarised"
            pov "Yes, yes! That makes sense"
    ta1 "Great to hear!"

    if not upper_right_paragraph_b or not lower_right_paragraph_b:
        ta1 "So, let's see the next possible paragraph"
        if not upper_right_paragraph_b:
            jump upper_right_paragraph
        elif not lower_right_paragraph_b:
            jump lower_right_paragraph
        else:
            jump continue_plag_tut
    else:
        jump continue_plag_tut




label lower_right_paragraph:
    $ lower_right_paragraph_b = True
    scene bg home white
    show manchester original:
        xalign 0.15
        yalign 0.11
        zoom 0.7

    show manchester_original:
        xalign 0.9
        yalign 0.11
        zoom 0.7
    show manchester_copied_reference:
        xalign 0.15
        yalign 0.62
        zoom 0.7

    show manchester_copied_quotation:
        xalign 0.9
        yalign 0.62
        zoom 0.7
    if chosen_tut_paragraph == "lowerright":
        ta1 "Great, let's see the paragraph on the lower right side"
    else:
        ta1 "Now, to the last paragraph on the lower right side"
    scene bg home white
    show manchester original:
        xalign 0.5
        yalign 0.11
        zoom 0.7

    show manchester_copied_quotation:
        xalign 0.5
        yalign 0.6
        zoom 0.7

    ta1 "If we compare both paragraphs, what do you think?"
    menu:
        ta1 "Is this paragraph plagiarised?"

        "No, the copied paragraph is in quotation marks and the source is referenced":
            ta1 "Yeah! Right!"
            ta1 "The paragraph is not plagiarised!"
            ta1 "If you need to directly quote something, always use quotation marks and a reference"
            ta1 "But of course, the prefered way is often to paraphrase the text in your own words"
            pov "Yeah, sure!"


        "Yes, a reference and quotation marks are not enough":
            ta1 "Noooo, the paragraph is not plagiarised"
            ta1 "This is the right way to quote"
            ta1 "If you need to directly quote something, always use quotation marks and a reference"
            ta1 "But of course, the prefered way is often to paraphrase the text in your own words"
            pov "Oh, I see! I think I understand now"
            ta1 "Great! And if you still have questions or are unsure, just ask a TA or your instructor"
            pov "Thank you, Sara!"

    if not upper_right_paragraph_b or not lower_left_paragraph_b:
        ta1 "So, let's see the next possible paragraph"
        if not upper_right_paragraph_b:
            jump upper_right_paragraph
        elif not lower_left_paragraph_b:
            jump lower_left_paragraph
        else:
            jump continue_plag_tut
    else:
        jump continue_plag_tut


label upper_right_paragraph2:
    $ upper_right_paragraph_b2 = True

    scene bg home white
    show manchester original:
        xalign 0.15
        yalign 0.11
        zoom 0.7

    show manchester_synonyms:
        xalign 0.9
        yalign 0.11
        zoom 0.7
    show manchester_perfect:
        xalign 0.15
        yalign 0.62
        zoom 0.7

    show manchester_synonyms_structure:
        xalign 0.9
        yalign 0.62
        zoom 0.7
    ta1 "So, the paragraph on the upper right side"
    scene bg home white
    show manchester original:
        xalign 0.5
        yalign 0.11
        zoom 0.7

    show manchester_synonyms:
        xalign 0.5
        yalign 0.6
        zoom 0.7

    ta1 "As before, on top, we see the original paragraph"
    if chosen_tut_paragraph == "upperright":
        ta1 "Below is your chosen paragraph that you think fits best"
    else:
        ta1 "Again, below is the paragraph we want to compare"
    menu:
        ta1 "Do you think this paragraph is a good paraphrase?"

        "Yes, it is":
            ta1 "Well, look closely at the wording"

            menu:
                ta1 "Do you think that the paragraph below uses completely different words?"

                "Mostly, yes":
                    ta1 "Then, look at the first sentence"
                    ta1 "Only the words in the quotations marks are different"
                    ta1 "Apart from that, the first sentence in the two paragraphs is identical"

                "Well, not really":
                    ta1 "See"

            ta1 "There are just some words that are replaced with synonyms"
            ta1 "But the structure of the paragraphs is identical"
            pov "So, it is plagiarised?"
            ta1 "Yes that paragraph is plagiarised"
            ta1 "And also, there is no reference to the original text"


        "No, it's too close":
            ta1 "You are right!"
            ta1 "There are just some words that are replaced with synonyms"
            ta1 "But the structure of the paragraphs is identical"
            pov "So, it is plagiarised?"
            ta1 "Yes that paragraph is plagiarised"
            ta1 "And also, there is no reference to the original text"

    if not lower_left_paragraph_b2 or not lower_right_paragraph_b2:
        ta1 "Ok, let's compare another of the paragraphs"
        if not lower_left_paragraph_b2:
            jump lower_left_paragraph2
        elif not lower_right_paragraph_b2:
            jump lower_right_paragraph2
        else:
            jump final_plag_tut
    else:
        jump final_plag_tut

label lower_left_paragraph2:
    $ lower_left_paragraph_b2 = True
    scene bg home white
    show manchester original:
        xalign 0.15
        yalign 0.11
        zoom 0.7

    show manchester_synonyms:
        xalign 0.9
        yalign 0.11
        zoom 0.7
    show manchester_perfect:
        xalign 0.15
        yalign 0.62
        zoom 0.7

    show manchester_synonyms_structure:
        xalign 0.9
        yalign 0.62
        zoom 0.7
    ta1 "So, the paragraph on the lower left side"
    scene bg home white
    show manchester original:
        xalign 0.5
        yalign 0.11
        zoom 0.7

    show manchester_perfect:
        xalign 0.5
        yalign 0.6
        zoom 0.7

    ta1 "As before, the original paragraph is on top"
    if chosen_tut_paragraph == "lowerleft":
        ta1 "Your paragraph that you think fits best is below"
    else:
        ta1 "Again, the paragraph to compare is below"

    menu:
        ta1 "Is the paragraph below a good paraphrase?"

        "Yes, I think so":
            ta1 "I see"

            menu:
                ta1 "Why do you think? Is this a good paraphrase?"

                "It is written in the student's own words and still has a reference to the original":
                    ta1 "Yes, you are right! It is a good paraphrase"

                "It gets rid of all the unnecessary information":
                    ta1 "Yes, and it still references the original text but is paraphrased well"


        "No, it is too far from the original":
            ta1 "Well, actually, that is the point"
            ta1 "It is written in the student's own words"
            ta1 "But it still includes all the important information"
            pov "So, it is a good paraphrase?"
            ta1 "Yes, that is the aim of referring to source texts"
            ta1 "To reference the source text but to paraphrase it in your own words"



    if not upper_right_paragraph_b2 or not lower_right_paragraph_b2:
        ta1 "So, let's see if another paragraph fits as well"
        if not upper_right_paragraph_b2:
            jump upper_right_paragraph2
        elif not lower_right_paragraph_b2:
            jump lower_right_paragraph2
        else:
            jump final_plag_tut
    else:
        jump final_plag_tut

label lower_right_paragraph2:
    $ lower_right_paragraph_b2 = True
    scene bg home white
    show manchester original:
        xalign 0.15
        yalign 0.11
        zoom 0.7

    show manchester_synonyms:
        xalign 0.9
        yalign 0.11
        zoom 0.7
    show manchester_perfect:
        xalign 0.15
        yalign 0.62
        zoom 0.7

    show manchester_synonyms_structure:
        xalign 0.9
        yalign 0.62
        zoom 0.7
    ta1 "The paragraph on the lower right side"
    scene bg home white
    show manchester original:
        xalign 0.5
        yalign 0.11
        zoom 0.7

    show manchester_synonyms_structure:
        xalign 0.5
        yalign 0.6
        zoom 0.7

    ta1 "Let's compare these two paragraphs"

    menu:
        ta1 "Looking at it, do you think that paraphrase is well-enough?"

        "Yes, it uses different words and has a different structure":

            ta1 "Well, let's see then. Look at the words used"
            menu:
                ta1 "Do you think that the paragraph below uses completely different words?"

                "Mostly, yes":
                    ta1 "Well, most words are just slightly changed"
                    ta1 "'Radical literary history' becomes 'radical history of literature'"
                    pov "But this is only one phrase..."
                    ta1 "Well, there are other phrases as well"
                    ta1 "'began writing' becomes 'started to write'"

                "Well, not enough, I guess":
                    ta1 "Yes, see, there are some phrases that are just slightly changed"
                    ta1 "'Radical literary history' becomes 'radical history of literature'"
                    ta1 "'began writing' becomes 'started to write'"
                    ta1 "There are several more examples"

            pov "And that is enough to be accounted for as plagiarism?"
            ta1 "Well, it is just not well paraphrased"
            ta1 "But there is one important part missing"
            pov "Which part?"
            ta1 "There is no reference"



        "No, there is one important part missing":
            menu:
                ta1 "What part is missing that is important?"

                "That Engels and Marx wrote The Communist Manifesto in Chetham's Library":
                    ta1 "No, but actually, there is another problem"
                    pov "What do you mean?"
                    ta1 "Apart from not being well paraphrased, the reference is indeed missing"

                "The reference":
                    ta1 "Great, [povname]!"
                    ta1 "Apart from not being well paraphrased, yes, the reference is indeed missing"

    ta1 "Most students think that just changing the structure and replacing some words with synonyms is enough"
    ta1 "But this is not what we consider paraphrasing because they are not using their own words"
    ta1 "And when the original paragraph that the idea is drawn from is not referenced, it becomes plagiarism"
    pov "I see. So, when we use ideas from others, we should always reference them"
    ta1 "It is never a bad idea to reference them, yes"

    if not upper_right_paragraph_b2 or not lower_left_paragraph_b2:
        ta1 "Ok, so what about the other paragraphs?"
        if not upper_right_paragraph_b2:
            jump upper_right_paragraph2
        elif not lower_left_paragraph_b2:
            jump lower_left_paragraph2
        else:
            jump final_plag_tut
    else:
        jump final_plag_tut


label coll_tut:
    scene bg office
    show sara mhappy:
        zoom 0.7
        xalign 0.5
    ta1 "Let's talk about collusion!"
    show sara talk
    ta1 "Let's say you are supposed to work on individual coursework"
    show sara mhappy
    ta1 "For this coursework, you are supposed to work alone"
    show sara happy at zoom_norm
    menu:
        ta1 "Can you lend your essay to someone else?"

        "Yes, as long as they don't copy my text":
            show sara sad at zoomed_in
            ta1 "Nooo, you should work on it on your own"
            show sara talk
            ta1 "This includes not to share your ideas with someone else"

        "No, we should not share our ideas with others":
            show sara mhappy at zoomed_in
            ta1 "Exactly! Great, [povname]"

    show sara happy at zoom_norm
    pov "But, Sara, I have a question"
    show sara mhappy at zoomed_in
    ta1 "Yes, what is your question?"
    show sara happy at zoom_norm
    pov "Can I discuss the essay with other students? And tell them about interesting sources I found"
    show sara mhappy at zoomed_in
    ta1 "I see, what you are referring to. Well, to be honest, it is very risky"
    ta1 "Of course, in general, we encourage you to work together"
    show sara talk
    ta1 "But for individual coursework, we want you to work on your own"
    ta1 "If you discuss your essay and your sources with other students, you risk that you also share your ideas"
    show sara happy at zoom_norm
    pov "So, you would not recommend talking about these essays with other students?"
    show sara talk at zoomed_in
    ta1 "Well, I would not risk it. Try to come up with your own ideas. And if you struggle you can always ask a TA or your instructor"
    show sara happy at zoom_norm
    pov "Ok, but what if I am afraid to say no to another student?"
    show sara mhappy at zoomed_in
    ta1 "What do you mean?"
    show sara happy at zoom_norm
    pov "Well, if I am not confident enough to say no when someone asks for my essay?"
    show sara talk at zoomed_in
    ta1 "I understand! Do not worry. If someone asks you that, just tell him to ask the TA if this is possible. And then we can explain it to him"
    show sara happy at zoom_norm
    pov "Ok, thank you, Sara!"
    show sara talk at zoomed_in
    ta1 "Of course, [povname]!"

    if plag:
        ta1 "I see that there is also some confusion about plagiarism"
        jump plag_tut

    menu:
        ta1 "Do you want to discuss something else?"

        "Yes":
            jump tut_decision

        "No":
            ta1 "Ok. See you, [povname]"

    return


label fabr_tut:
    scene bg office
    show sara mhappy:
        zoom 0.7
        xalign 0.5
    ta1 "Let's talk about fabrication and falsification"
    show sara happy at zoom_norm
    menu:
        ta1 "What is the simplest way to avoid fabrication and falsification?"

        "Always work with other students":
            show sara talk at zoomed_in
            ta1 "Well, there might be some areas, where you are supposed to work alone"
            show sara mhappy
            ta1 "Just be always careful when you record data"
            show sara talk
            ta1 "And never change that data by altering it"
            show sara mhappy
            ta1 "And never invent new data"

        "Never change any recorded data":
            show sara talk at zoomed_in
            ta1 "Well, at least you should not alter it"
            ta1 "And never invent new data"

    ta1 "So, let's consider some examples"
    show sara happy at zoom_norm

    menu:
        ta1 "Are you allowed to convert data from bit to byte?"

        "Yes, that is not fabrication or falsification":
            show sara talk at zoomed_in
            ta1 "Great! Yes, you are allowed to convert data as long as you do not alter it"

        "No, I should never change my data":
            show sara sad at zoomed_in
            ta1 "Well, you are still allowed to convert data as long as you do not alter it"

    show sara talk
    ta1 "Ok, one final question"

    show sara happy at zoom_norm
    menu:
        ta1 "Which is considered to be fabrication or falsification?"

        "Drop some data that does not look right":
            call s_answ_no

        "Change data so that the values reflect more closely what you want to show":
            call s_answ_no

        "Invent some data that is missing due to a blackout during the recording of the data itself":
            call s_answ_no

        "All of the above":
            show sara vhappy at zoomed_in
            ta1 "Yes, [povname]. Exactly"
            ta1 "All of these answers are examples of fabrication or falsification"

    show sara talk
    ta1 "Well, I hope this tutorial was helpful"
    menu:
        ta1 "Do you want to discuss something else?"

        "Yes":
            jump tut_decision

        "No":
            ta1 "Ok. See you, [povname]"

    return

label s_answ_no:
    show sara sad at zoomed_in
    ta1 "Well, [povname]. All of these answers are examples of fabrication or falsification"
    ta1 "You should never alter the data or invent new data"
