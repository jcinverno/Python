# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 13:01:23 2021

@author: jcinv
"""

class QuizBrain:
    
    def __init__(self, q_list):
        
        self.q_number = 0 
        self.q_list = q_list
        self.number_correct = 0
     
    def still_has_questions(self):
        
        return self.q_number < len(self.q_list)
            
        
    def next_question(self):
        
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_ans = input(f"Q.{self.q_number}: {current_question.text} (True/False): ")
        self.check_answer(user_ans, current_question.answer)
    
    
    def check_answer(self, user_ans, correct_answer):
        
        if user_ans.lower() == correct_answer.lower():
            print("You got it right!")
            self.number_correct += 1
        else:
            print("That's wrong.")
            
            
        print (f"The correct answer was: {correct_answer}.")
        print (f"Your current score is {self.number_correct}/{self.q_number}.")
        print ("\n")
        