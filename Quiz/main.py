# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:46:44 2021

@author: jcinv
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
 


question_bank = []

for dic in question_data:
    """creates a list of question-object"""
    q_text = dic["text"]
    q_answer = dic["answer"]
    new_question = Question( q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    
    print(quiz.next_question())
    
print ("You've completed the quiz!")
print(f"Your final score was:{quiz.number_correct}/{quiz.q_number}.")