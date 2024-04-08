print("\n Welcome to who wants to become a millionare!")

questions = [
  {
    "question": "In what year was the first iPhone launched?",
    "options": ["A: 2005", "B: 2002", "C: 1999", "D: 2007"],
    "answer": "D"
  },

  {
    "question": "What is Windows 7's design language called?",
    "options": ["A: Material You", "B: Windows Aero", "C: Metro"],
    "answer": "B"
  },

  {
    "question": "Who is the CEO of Google?",
    "options": ["A: Jawed Karim", "B: Sergey Brin", "C: Roy Trenneman", "D: Sundar Pichai"],
    "answer": "D"
  },

  {
    "question": "How is nginx pronounced?",
    "options": ["A: engine x", "B: enjincs", "C: n.g.i.n.x."],
    "answer": "A"
  },
]

def run_quiz(questions):
  score = 0 #Score variable

  for question in questions:
    print("\n" + question["question"]) #Print the question
    for option in question["options"]:
      print(option) #Print answer options
    
    user_answer = input("Answer (letter of the option): ").strip().upper() #Get user answer

    #Check if answer is correct
    if user_answer == question["answer"]:
      print("Correct!")
      score += 1 #Increment score if correct
    else:
      print("Wrong!")
  
  #Show final score
  print(f"\n You got {score} out of {len(questions)} questions correct! ")

run_quiz(questions)