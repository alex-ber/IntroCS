import random

first=random.randint(1, 9)
second=random.randint(1, 9)
result=first+second
answer_str = input(f"How much is {first} + {second} ? ")
answer = int(answer_str)
if result==answer:
    print("You're right!")
else:
    print("Sorry, you're wrong.")



