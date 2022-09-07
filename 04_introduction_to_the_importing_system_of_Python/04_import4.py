print(__name__)
from simplemathexample.const import FIRST as first, SECOND as second
print('04_import4')

result=first+second
answer_str = input(f"How much is {first} + {second} ? ")
answer = int(answer_str)
if result==answer:
    print("You're right!")
else:
    print("Sorry, you're wrong.")



