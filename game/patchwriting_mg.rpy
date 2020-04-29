# label patchwriting:
#     scene bg lab
#
#     show alex happy at left
#
#     a "Hello, I'm Alex"
#
#     a "I am an MSc student studying Computer Science here at the University of Manchester."
#
#     show alex talk at left
#
#     a """I have my dissertation due tomorrow and I've still got a paragraph left to write.
#     The last assignment I handed in wasn't a very good one either..."""
#
#     a "I need to write something and I need to do it as fast as I can."
#
#     show alex happy at left
#     # show paragraph1 at right
#
#     # show logicrep at right
#
#     show logicrep at right
#
#     a "But look at this article... This part of the paragraph is all I need to finish my dissertation."
#
#     show alex talk at right
#
#     a "I just want my dissertation to be finished at last"
#
#     a "I'll just use that and the main idea from this article."
#
#     # show bad_paragraph at right
#
#     a "Finally I'm finished"
#
#     menu:
#
#         a "What do you think? Great, isn't it?"
#
#         "No, not really":
#
#             menu:
#                 pov "You really need to change something"
#
#                 "You need to reference your source text":
#                     pass
#
#                 "You should put everything in quotation marks":
#                     a "But it's my sentence structure and I left some words from the original"
#                     a "Maybe I should just reference it"
#                     pov "Do at least that"
#
#                 "We should ask a TA!"
#                     jump patchwriting_minigame
#
#
#         "Yeah, I think it's fine":
#             jump patchwriting_minigame
#
#     # show cited_paragraph at right
#     menu:
#         a "Now I referenced it. Do you think I should change something?"
#
#         "No, it's perfect now!":
#             jump ta_intervention
#
#         "Yes, I think your text is too close to the original":
#             a "You are right! I have to use my own words!"
#             jump patchwriting_part2
#
#         "Yes, you should just copy the original text. It sounds better!":
#             a "Hey, [povname]! Do you want me to get a bad mark? I can't cite a whole paragraph and get a good mark!"
#             jump ta_intervention
#
#
# label patchwriting_part2
#     show paragragh1a at right
#
#     a "Okay that's good. It's entirely in my own words."
#
#     menu:
#
#         a "You don't think I've plagiarised, do you?"
#
#         "No":
#             jump noplag1
#
#         "Yeah":
#             jump yesplag1
#
#
#
# label ta_intervention:
#     ta1 "Hey, I heard you two were discussing about correct citation."
#     ta1 "By now, you should know about plagiarism"
#     ta1 "But do you know what patchwriting is?"
#     a "Not at all, can you explain it to us?"
#     ta1 "Sure! We don't expect you to know everything here!"
#     ta1 "You are encouraged to search for information in order to answer questions or to use in your dissertation"
#     ta1 "However, you should always make sure that you don't plagiarise!"
#     ta1 "And, if you want good marks, you should avoid patchwriting!"
#     pov "So, what is patchwriting then?"
#     ta1 "If you find an interesting text or paragraph in a paper, make sure to paraphrase it in your own words"
#     ta1 "We want you to understand the information and not just consume it"
#     menu:
#         ta1 "[povname], what do you think is an example for patchwriting?"
#
#         "If I use the same structure and similiar words as in the original source":
#             ta1 "That's correct! Great, [povname]!"
#         "If I just copy and paste a text without referencing":
#             ta1 "Nooo! That is plagiarism!"
#             ta1 "Alex, can you think of an example?"
#             a "Well, maybe if I use the same structure and similiar words as in the original source?"
#             ta1 "Great, Alex! That's correct!"
#     ta1 "So, let's look at an example!"
#     jump patchwriting_minigame
#
#
# label patchwriting_minigame:
#     screen white
#     show logicrep at left
#     ta1 "Let's look at the original source"
#     ta1 "And here are some paragraphs that reference this source"
#     #show paragraphs at right
#     menu:
#         ta1 "Which of these paragraphs is an example for patchwriting?"
#
#         "Paragraph 1":
#             ta1 "That is not correct! Paragraph 2 is an example for patchwriting"
#         "Paragraph 2":
#             ta1 "That's correct!"
#         "Paragraph 3":
#             ta1 "That is not correct! Paragraph 2 is an example for patchwriting"
#         ta1 "Even though he referenced the original paragraph, he merely just copied and pasted the text"
#         ta1 "Using synonyms and changing the original structure just a tiny bit is bad academic practice"
#         ta1 "In this way, we don't know whether the student actually understood what he was writing or was just copying the original source"
#     jump patchwriting_part2
