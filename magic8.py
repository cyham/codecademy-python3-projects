import random

name = "Sam"
question = "Is today a Monday?"
answer = ""

if question:
  random_number = random.randint(1, 12)
  if random_number == 1:
    answer = "Yes - definitely."
  elif random_number == 2:
    answer = "It is decidely so."
  elif random_number == 3:
    answer = "Without a doubt."
  elif random_number == 4:
    answer = "It is certain."
  elif random_number == 5:
    answer = "Reply hazy, try again."
  elif random_number == 6:
    answer = "Ask again later."
  elif random_number == 7:
    answer = "Better not tell you now."
  elif random_number == 8:
    answer = "Cannot predict now."
  elif random_number == 9:
    answer = "My sources say no."
  elif random_number == 10:
    answer = "Outlook not so good."
  elif random_number == 11:
    answer = "Very doubtful."
  elif random_number == 12:
    answer = "Don't count on it."
  else:
    answer = "Error"

  introduction = ""
  if name:
    introduction = name + " asks: " + question
  else:
    introduction = "Question: " + question

  print(introduction)
  print("Magic 8-Ball's answer: " + answer)
else:
  print("Error: You need to give Magic 8-Ball a question to get a fortune.")