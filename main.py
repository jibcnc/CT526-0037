import importlib
from mylib import myfunc

x = input("Input character: ")
y = int(input("Turn want to run: "))

for i in range(1, y + 1):
    print(myfunc(x, i))
