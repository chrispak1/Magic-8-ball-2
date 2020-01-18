# magic 8-ball
import random

def print_output():
  choice = random.randint(1,10)
  if choice==1:
    print("\nYes")
  elif choice==2:
    print ("\nIt's a maybe")
  elif choice==3:
    print("That's a question I can't answer")
  elif choice==4:
    print("\nIt appears you may")
  elif choice==5: 
    print ("\nThere is a 12% chance you will")
  elif choice==6:
    print("\nDepends")
  elif choice==7:
    print("\nMost likely not.")
  elif choice==8:
    print("\nI want you too but there is someone that doesn't")
  else:
    print("\nNo")


answer = input("What's your question for the Magic 8-ball to answer? ")
print_output()

  