# -*- coding: utf-8 -*-
"""python_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gh54syNUS47Ct9mswKcVVO5X9xCGg-jz
"""

import re
import random

class RuleBot:
  ### Potential Negative Responses
  negative_responses = ("no", "nope", "nah", "not a choice", "sorry")
  ### Exit conversation keywords
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  ### Random starter questions
  random_questions = (
      "Is learning python is interesting?\n",
      "Who taught you python?\n",
      "How many days it takes to learn the basics of python?\n"
      "Do you want to learn the advance level of python?\n",
      "What reason make you to learn the python?\n",
      "Which one is your favorite programming language?\n",
      "Name the project you have made during python learning?\n",
      "Do you enjoy the coding?\n",
      "What problem you face while coding and how you handle it?\n"
  )


  def __init__(self):
    self.alienbabble = {'describe_python_intent': r'.*\s*your python.*',
                        'answer_why_intent': r'why\sare.*',
                        'about_project': r'.*\s*project',
                        'about_coding': r'.*\s*coding'
                        }
 

  def greet(self): 
        self.name = input("What is your name?\n")
        will_help = input(
            f"Hi {self.name}, I am Rule-Bot. Will you help me to know more about python?\n")
        if will_help in self.negative_responses:
          print("Ok, have a nice day friend!")
          return
        self.chat()


  def make_exit(self, reply):
    for command in self.exit_commands:
      if reply == command:
        print("Okay, have a nice day friend!") 
        return True 


  def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))


  def match_reply(self, reply):
    for key, value in self.alienbabble.items():
      intent = key
      regex_pattern = value
      found_match = re.match(regex_pattern, reply)
      if found_match and intent == 'describe_python_intent':
        return self.describe_python_intent()
      elif found_match and intent == "answer_why_intent":
        return self.answer_why_intent()
      elif found_match and intent == 'about_project':
        return self.about_project()
      elif found_match and intent == 'about_coding':
        return self.about_coding()
    if not found_match:
      return self.no_match_intent()




  def describe_python_intent(self):
        responses = ("Python was created in the late 1980s by Guido van Rossum and is named after the British comedy group Monty Python.\n",
                     "Python is known for its simplicity, readability, and ease of use, making it a popular language for beginners and experts alike.\n", 
                     "Python code is typically written in plain text files with a .py extension\n", 
                     "Python main strengths is its extensive standard library, which includes modules for tasks.\n",
                     "It help in learning the machine language and artificial intelligence\n")
        return random.choice(responses)
        



  def answer_why_intent(self):
    responses = ("I am here to learn about python programming language.\n",
                 "I came to know that python is an interesting and easy to learn programming language.",
                 "Python is my favorite programming language.\n"
                 )
    



  def about_project(self):
       responses = ("This is the python project\n." ,
                    "I have make a ChatBot\n.", 
                    "A chatbot is a computer program designed to simulate conversation with human users.\n",
                    "Chatbots can be used for a variety of applications, including customer service, sales, marketing, and entertainment.\n",
                    "Chatbots can be designed to have different personalities and styles of communication to fit the needs of the user or brand.\n",
                    "Chatbots can help businesses save time and money by automating simple tasks.\n"
                    )
       return random.choice(responses)        




  def about_coding(self):
        responses = ("Coding is the process of writing instructions for computers to follow.\n",
                 "Syntax errors can occur when code is written incorrectly.\n",
                 "Learning to code can be a valuable skill for a variety of careers.\n",
                 "Comments in code can help explain the purpose and functionality of the code.\n",
                 "Debugging is the process of finding and fixing errors in code.\n",
                 )
        return random.choice(responses)

  def no_match_intent(self):
       responses = ( 
           "Please tell me more.\n", "Why do you say that?\n", "I see. Can you elaborate?\n",
          "Nice!, Do you want to continue it?", "Why?\n", "Good!, Do you want to something more on this?"
          )
       return random.choice(responses)


AlienBot = RuleBot()
AlienBot.greet()