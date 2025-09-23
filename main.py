import importlib
from mylib import myfunc

character = input("Input character: ") 
rounds = int(input("Turns want to run: ")) 

for i in range(1, rounds + 1):
    print(myfunc(character, i))