init python:

    ##########################################################################################
    # General options
    ##########################################################################################

    # Please decide whether you want to use custom strings as texts or replace the screenshots
    custom_texts = False

    # Please decide what topic is to be studied
    study_course = "Computer Science"
    university_name = "University of Manchester"

    # lab session or seminar?
    # practical_part_of_the_course = "seminar"
    # practical_room = "seminar room"
    practical_part_of_the_course = "lab session"
    practical_room = "labs"

    # Please decide whether the fabrication example is about a survey or a computer programm
    fabrication_topic = "code"
    # fabrication_topic = "survey"





    ##########################################################################################
    # Game content
    ##########################################################################################


    #####################################
    # Plagiarism - Essay question
    #####################################

    # Please provide a short essay question, around 130 characters
    essay_question = "As discussed in the lecture:\nDefine the term “Turing machine” and explain what it is capable of.\nThis is to be your own work."
    essay_question_short = "define the term 'Turing machine'"
    essay_topic = "Turing machine"

    # Please provide the title of the wikipedia article
    wikipedia_title = "Turing machine"
    # Please provide the wikipedia articles text
    wikipedia_article = """A Turing machine is a mathematical model of computation that defines an abstract machine[1] that manipulates symbols on a strip of tape according to a table of rules.[2] Despite the model's simplicity, given any computer algorithm, a Turing machine capable of simulating that algorithm's logic can be constructed.[3]\n\nThe machine operates on an infinite[4] memory tape divided into discrete "cells".[5] The machine positions its "head" over a cell and "reads" or "scans"[6] the symbol there. Then, based on the symbol and the machine's own present state in a "finite table"[7] of user-specified instructions, the machine (i) writes a symbol (e.g., a digit or a letter from a finite alphabet) in the cell (some models allow symbol erasure or no writing),[8] then (ii) either moves the tape one cell left or right (some models allow no motion, some models move the head),[9] then (iii) based on the observed symbol and the machine's own state in the table either proceeds to another instruction or halts the computation.[10]
    """
    # Please provice the paragraph from the wikipedia article that is important
    wikipedia_short_paragraph = "A {b}Turing machine{/b} is a mathematical model of computation that defines an abstract machine[1] that manipulates symbols on a strip of tape according to a table of rules.[2] Despite the model's simplicity, given any computer algorithm, a Turing machine capable of simulating that algorithm's logic can be constructed.[3]"
    # Please provide the reference to the wikipedia article, where the short paragraph on zhe slide is taken from
    reference = "Taken from: https://en.wikipedia.org/wiki/Turing_machine"

    # Please provide the wikipedia short paragraphs without footnotes (e.g. [1])
    short_paragraph_cleaned = "A {b}Turing machine{/b} is a mathematical model of computation that defines an abstract machine that manipulates symbols on a strip of tape according to a table of rules. Despite the model's simplicity, given any computer algorithm, a Turing machine capable of simulating that algorithm's logic can be constructed."

    # Please provide the cleaned paragraph with a reference
    short_paragraph_referenced = '''"A {b}Turing machine{/b} is a mathematical model of computation that defines an abstract machine that manipulates symbols on a strip of tape according to a table of rules. Despite the model's simplicity, given any computer algorithm, a Turing machine capable of simulating that algorithm's logic can be constructed."\n\n''' + reference

    # Please mark all words to be sorrounded by color like this {color=#FF0000}word{/color}
    short_paragraph_identified = '''"A {b}Turing machine{/b} is a {color=#FF0000}mathematical{/color} model of computation that defines an abstract {color=#FF0000}machine{/color} that manipulates symbols on a strip of {color=#FF0000}tape{/color} according to a {color=#FF0000}table{/color} of rules. Despite {color=#FF0000}the model's simplicity{/color}, given any computer {color=#FF0000}algorithm{/color}, {color=#FF0000}a Turing machine capable of simulating that algorithm's logic can be constructed{/color}."\n\n''' + reference

    # Please replace the marked words and colour with {color=#9E0808}word{/color}
    short_paragraph_replaced = '''"A {b}Turing machine{/b} is a {color=#9E0808}conceptual{/color} model of computation that defines an abstract {color=#9E0808}system{/color} that manipulates symbols on a strip of {color=#9E0808}paper{/color} according to a {color=#9E0808}set{/color} of rules. Despite {color=#9E0808}the minimalism{/color}, given any computer {color=#9E0808}program{/color}, {color=#9E0808}we can design a Turing machine which can execute that program{/color}."\n\n''' + reference

    # Please now get rid of the color tags and reference the text
    reference = "[1] https://en.wikipedia.org/wiki/Turing_machine"
    paragraph_wiki_referenced = '''"A {b}Turing machine{/b} is a conceptual model of computation that defines an abstract system that manipulates symbols on a strip of paper according to a set of rules. Despite the minimalism, given any computer program, we can design a Turing machine which can execute that program.[1]"\n\n''' + reference

    # Please provide a good example for an essay
    good_example = "A Turing machine is an abstract mathematical model [1]. The finite-state system can store and retrieve any symbol [2]. The Turing machine consists of an infinite tape on which these symbols can be scanned. Given a finite set of rules, the Turing machine can write a new symbol and then either continues or stops the computation [2]. The Turing machine can simulate a real computer: every computer program can be simulated on a Turing machine [3]."

    # Please provide an example consisting mainly of quotes
    too_many_quotes = '''Stone states that the Turing machine is “an abstract mathematical model” [1]. As Minsky states, the Turing machine is a “finite-state machine” that is “associated with […] its tape” [2]. In this tape, it can save and reload “sequences of symbols” [2]. According to Sipser, the machine is able to simulate “everything that a real computer can do” [3]. The machine consists of “an infinite memory tape” that is divided into discrete “cells”. With its head, it “reads […] the symbol” in the particular cell. Then, it “write a symbol”, “move the tape one cell left or right” and then “either proceeds or stops. [3].'''

    # Please provide an example replacing fixed scientific terms with synonyms (e.g. Alan Turing system instead of the correct scientific term Turing machine)
    false_synonyms = "The Alan Turing system is an abstract conceptual model [1]. The fixed-condition machine can save and recover every symbol [2]. The Alan Turing system consist of an unlimited ribbon on which these symbols can be read. Given a limited plan of directives, the Alan Turing system can write a new symbol and then either continues or stops the program [2]. The system can simulate a real digital workstation: every computer application can be simulated on this system [3]."

    # For the essay that uses wrong synonyms for scientific terms, please provide
    # False synonyms in form of (false synonym, fixed scientific term)
    false_synonyms_examples = [("Alan Turing system", "Turing machine"), ("digital workspace", "computer")]

    # References for all three new essays
    references_essays = "[1] Stone, H.S. [1972). Introduction to Computer Organization and Data Structures. p. 8. New York: McGraw-Hill Book Company.\n[2] Minsky, M. L. (1967). Computation. p.107. Englewood Cliffs: Prentice-Hall.\n[3] Sipser, M. (2006). Introduction to the Theory of Computation. p. 137. Boston: PWS Publishing Company"


    #####################################
    # Fabrication - Task
    #####################################

    # The goal of the seminar/lab session where fabrication and falsification might occur
    # The input may fit the following sentence structure
    # "The goal of this seminar/lab session is [goal_fabrication_session]
    goal_fabrication_session = "to come up with optimized SQL queries that are faster than the given ones on the PDF"

    # Subtasks that need to be accomplished to complete the previously given goal
    subtask1 = "For this, you will not only have to write down the queries"
    subtask2 = "But we want you to test them on the lab machines as proof that they are faster"
    subtask3 = "Please do not forget to submit these statistics. They will make up most of this week's mark"
    subtask4 = "We will collect your queries and the statistics at the end of this lab session. So be sure to work correctly but also fast"
    subtask_list = [subtask1, subtask2, subtask3, subtask4]


    #####################################
    # Dissertation - Content of paragraph
    #####################################

    # Dissertation topic so that the sentence "I have to write something about 'dissertation_topic'" works
    dissertation_topic = "robots and how they are enabled to interact with their environment"

    # Provide a short paragraph from a scientific paper
    source_paragraph = "{b}{size=+10}2 Related Work{/size}{/b}\n\nKnowledge representation, reasoning and learning are well-researched areas in robotics and AI. Logic-based representations and probabilistic graphical models have been used to control sensing, navigation and interaction for robots and agents [Bai {i}et al.{/i}, 2014; Galindo {i}et al.{/i}, 2008]. Formulations based on probabilistic representations (by themselves) make it difficult to perform commonsense reasoning, whereas classical planning algorithms and logic programming tend to require considerable prior knowledge of the domain and the agent’s capabilities."
    # Provide a reference for the short paragraph
    source_reference = "[1] Sridhan, M. [2017). Integrating knowledge representation, reasoning and learning for human-robot interaction. In 2017 AAAI Fall Symposium Series."

    # Provide a bad paraphrase of the short paragraph from the paper
    bad_paragraph = "For navigation and interaction of robots, logic-based representations and probabilistic graphical models are used. The representation of knowledge, explanation generation and planning are areas of robotics and artificial intelligence that are well-researched. Commonsense reasoning is difficult because of formulations based on probabilistic representations. Furthermore, planning algorithms and logic programming require prior domain knowledge and capabilities by the agent."

    cited_paragraph = "{size=-5}" + bad_paragraph + "[1]\n\n" + source_reference + "{/size}"

    paragraph_patchwritten = bad_paragraph + " [1]"

    patchwritten_words = ["Logic-based representations", "Commonsense reasoning"]

    # Provide an good and an excellent paragraph
    paragraph_good = "For robots or agents to be able to interact with their environment, logical reasoning is vital. However, common algorithms used in robotics that allow the agent to interact, are based on statistics and can lead to difficulties in reasoning. Furthermore, it may be hard to integrate new data e.g. by sensors because of their potential unreliability that could affect the data integrity of prior knowledge required by planning and reasoning algorithms. [1]"
    paragraph_excellent = "Whether the approach is based on a probabilistic representation or logic programming, the Knowledge Representation needed for controlling robot interaction has many complications. Basing formulations on probabilistic representations make it harder to apply common sense reasoning. Problems also arise when using a logic programming approach, as there is no straightforward way to use this approach without good background information about the domain relevant to the interactions talking place. [1]"


    ###########################################
    # Functions to highlight patchwritten words
    ###########################################


    def highlight_words(sentence, words):
        """
        Highlights words in red if they occur in the sentence
        """
        for word in words:
            c_ind = sentence.lower().find(word.lower())
            if c_ind >= 0:
                sentence = sentence[:c_ind] + "{color=#ff0000}" + word + "{/color}" + sentence[c_ind+len(word):]
        return sentence

    def highlight_word(sentence, word):
        """
        Highlights a word in red if it occurs in the sentence
        """
        c_ind = sentence.lower().find(word.lower())
        if c_ind >= 0:
            sentence = sentence[:c_ind] + "{color=#ff0000}" + word + "{/color}" + sentence[c_ind+len(word):]
        return sentence
