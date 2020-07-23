import threading, time

print('Start of program')

def takeANap():
    time.sleep(5)
    print('Wake up!')

# This means the function we want to call in the new thread is takeANap()
# Notice that the keyword argument is target=takeANap, not target=takeANap().
# This is because you want to pass the takeANap() function itself as the argument,
# not call takeANap() and pass its return value.
threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program')