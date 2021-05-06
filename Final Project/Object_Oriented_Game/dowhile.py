# 6. Create a do while loop
# this is an emmulation of a do while loop in py
while True: 
    print ("please type c to continue, anything else to quit. ") 
    x = input() 
    if not x == "c": 
        break 


import threading
    
def hello():
    print("hello")
    print("world")

t = threading.Timer(7,hello)
t.start()
