####################################################################
# INTRO
####################################################################


init:
    # possibility of designing more (like UoM logo)
    image title = Text("{color=#000000}Item Name: {space=50} SE 1{/color}")



# Example 1
label plagiarism_scenario:
    scene black
    with dissolve
    show text "Click on the screen to advance"
    pause
    show text "Plagiarism examples - Example 1"
    pause
    # show text "You are a student at the university"
    show text "You are Charlie, a [study_course] student at the [university_name]"
    pause
    show text "In this scenario, you are supposed to write an essay for your coursework"
    pause
    jump essay_scenario_1

label essay_scenario_1:
    $ score = calculate_score()
    $ initial_score = score
    scene bg home desk
    with dissolve
    pov "Ok, let's see the essay question"
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
    jump essay_feedback


label essay_feedback:
    if essay_chosen == "bad":
        jump bad_essay
    elif essay_chosen == "mediocre":
        jump mediocre_essay
    elif essay_chosen == "good":
        jump good_essay
    elif essay_chosen == "overtop":
        jump overtop_essay


label bad_essay:
    $ change_score('bad_essay', -1)
    $ plag = True
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home laptop
    with fade
    show blackboard_points:
        xalign 0.5 yalign 0.2
    image grade_bad = Text("{color=#000000}Points {space=120}2/10{/color}")
    show title:
        xalign 0.318 yalign 0.45
    show grade_bad:
        xalign 0.318 yalign 0.5
    pov "Oh no! I only got a few points. But why?"
    pov "I will go to Sara, the TA, and ask her."
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
    scene bg home laptop
    with fade
    show blackboard_points:
        xalign 0.5 yalign 0.2
    image grade_bad = Text("{color=#000000}Points {space=120}2/10{/color}")
    show title:
        xalign 0.318 yalign 0.45
    show grade_bad:
        xalign 0.318 yalign 0.5
    pov "Oh no! I only got a few points. But why?"
    pov "I will go to Sara, the TA, and ask her."
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
    scene bg home laptop
    with fade
    show blackboard_points:
        xalign 0.5 yalign 0.2
    image grade_mediocre = Text("{color=#000000}Points {space=120}7.5/10{/color}")
    show title:
        xalign 0.318 yalign 0.45
    show grade_mediocre:
        xalign 0.318 yalign 0.5
    pov "Oh no! I didn't get full points. But why?"
    pov "I will go to Sara, the TA, and ask her."
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
    scene bg home laptop
    with fade
    show blackboard_points:
        xalign 0.5 yalign 0.2
    image grade_good = Text("{color=#000000}Points {space=120}10/10{/color}")
    show title:
        xalign 0.318 yalign 0.45
    show grade_good:
        xalign 0.318 yalign 0.5
    pov "Yes, I got full points!"
    pov "Awesome"
    pov "I will keep up the great work"
    jump after_essay_mark



label overtop_essay:
    $ change_score('overtop_essay', +1)
    scene black
    with dissolve
    show text "The next day..."
    pause
    scene bg home laptop
    with fade
    show blackboard_points:
        xalign 0.5 yalign 0.2
    image grade_overtop = Text("{color=#000000}Points {space=120}7.5/10{/color}")
    show title:
        xalign 0.318 yalign 0.45
    show grade_overtop:
        xalign 0.318 yalign 0.5
    pov "Hmm! I didn't get full points. But why?"
    pov "I will go to the teaching assistant tomorrow and ask her"
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
    ta1 "For example, there is no such thing as [false_synonyms_examples[0][0]]. This is called a [false_synonyms_examples[0][1]]"
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

    ta1 "What exactly did you do? Did you write your own paragraph"
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
    show text "Please try again"
    pause
    jump essay_scenario_1




label after_essay_mark:
    jump plagiarism_example1_end


label plagiarism_example1_end:

    scene black
    if not one_chapter_only:
        $ score = calculate_score()
        $ example1_score = score - initial_score
        if formative:


            if example1_score >= 6:
                show text "Excellent! You did very well"
                pause
                show text "You may graduate with distinction"
                pause
                show text "Keep up the good work"
                pause
            elif example1_score >= 3:
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
                        jump essay_scenario_1

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
                        jump essay_scenario_1

                    "Nah, I'm fine":
                        pass

    jump dissertation_transition


label dissertation_transition: # example 2
    if not one_chapter_only:
        $ initial_score = score
        $ diss_play += 1
        $ score = calculate_score()
    scene black
    with dissolve
    show text "Plagiarism examples - Example 2"
    pause
    show text "At the end of the year, there is one final milestone..."
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

        "Yes, but not from the start":
            jump dissertation_transition
        "Yes, I want to restart from the beginning!":
            jump essay_scenario_1
        "No":
            show text "The End"
            pause
            return


label happy_end:
    scene black
    if not one_chapter_only:
        $ score = calculate_score()
        $ dissertation_score = score - initial_score
        if formative:

            # menu:
            #
            #     "Do you want to know, how well you did?"
            #
            #     "Yes":

            if dissertation_score >= 3:
                show text "Well done!"
                pause
                show text "You wrote an excellent dissertation"
                pause
            else:
                show text "You did good, but you could have done better!"
                pause
                show text "You should consider replaying this part of the game"
                pause
                scene black
                menu:
                    "Would you like to try again?"

                    "Yes, but not from the start":
                        jump dissertation_transition
                    "Yes, I want to restart from the beginning!":
                        jump essay_scenario_1

                    "Nah, I'm fine":
                        pass
                # "No":
                #     pass
    scene black
    show text "The End"
    pause
    show text "Feel free to click Continue below to advance"
    pause
    show text "Otherwise, the game will restart automatically"
    pause
    # $ MainMenu(confirm=False)()
    # return
    # return
