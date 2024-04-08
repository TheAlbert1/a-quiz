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

  {
    "question": "This is question number...",
    "options": ["A: 4", "B: 6", "C: 5", "D: 7"],
    "answer": "C"
  },

  {
    "question": "Before December there's...",
    "options": ["A: September", "B: November", "C: August", "D: October"],
    "answer": "B"
  },

  {
    "question": "Imagine you're watching Bob the Builder. Which version do you watch?",
    "options": ["A: The classic stop-motion version", "B: The horrible new CGI version"],
    "answer": "A"
  },

  {
    "question": "What does the line-height property in CSS do?",
    "options": ["A: Nothing unless font-size is also specified", "B: It sets the font's x-height", "C: It sets the vertical height of the text", "D: It sets the space between lines of text"],
    "answer": "D"
  },

  {
    "question": "When setting the color of the text in a HTML document, it's important to think about...",
    "options": ["A: A good contrast against the background", "B: A poor contrast against the background"],
    "answer": "A"
  },

  {
    "question": "Did you like my quiz?",
    "options": ["A: Yes", "B: No"],
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
  print(f"\n You got {score} out of {len(questions)} questions correct!")

run_quiz(questions)