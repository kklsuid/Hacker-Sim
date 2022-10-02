from platform import system
# Run this first.

print("Does your computer support curses?")
sys = system()

if sys == 'Windows':
    print("Your system is Windows.")
    print("Run \"python -m pip install windows-curses\" in CMD to use curses.")
elif sys == 'Linux':
    print("Your system is Linux.")
    print("Fully Supported curses.")
else:
    print(f"Your system is {sys}.")
    print("Check out on Google to Sure.")