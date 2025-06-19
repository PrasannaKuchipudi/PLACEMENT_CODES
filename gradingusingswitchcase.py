grade=input("Enter a grade:")
match grade:
  case 'A':
    print("Excellent")
  case 'B':
    print("Very Good")
  case 'C':
    print("Good")
  case 'D':
    print("Fair")
  case 'F':
    print("Fail")
  case _:
    print("Invalid grade")
