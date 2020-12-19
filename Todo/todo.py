import sys
from datetime import date
import os


inp = sys.argv

try:
    command = (inp)[1].strip()
except:
    command = "help"

if command == "help":
    print("Usage :-")
    print("$ ./todo add \"todo item\"  # Add a new todo")
    print("$ ./todo ls               # Show remaining todos")
    print("$ ./todo del NUMBER       # Delete a todo")
    print("$ ./todo done NUMBER      # Complete a todo")
    print("$ ./todo help             # Show usage")
    print("$ ./todo report           # Statistics", end="")


elif command == "add":
    with open(os.path.join(sys.path[0], "todo.txt"), "a") as file:
        try:
            message = (inp)[2].strip()
            file.write(message + "\n")
            print("Added todo: " + "\"" + message + "\"")
        except:
            print("Error: Missing todo string. Nothing added!")

elif command == "ls":
    arr = list()
    if os.path.isfile("todo.txt") == False:
        file = open(os.path.join(sys.path[0], "todo.txt"), "w")
        file.close()

    with open(os.path.join(sys.path[0], "todo.txt"), "r") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("There are no pending todos!")
        else:
            for num, line in enumerate(lines, 1):
                arr.insert(0, "[" + str(num) + "] " + line.strip("\n"))
            for line in arr:
                print(line)


elif command == "del":
    if os.path.isfile("todo.txt") == False:
        file = open(os.path.join(sys.path[0], "todo.txt"), "w")
        file.close()

    with open(os.path.join(sys.path[0], "todo.txt"), "r") as file:
        try:
            no = (inp)[2].strip()
            lines = file.readlines()
            flag = 0
            with open(os.path.join(sys.path[0], "todo.txt"), "w") as file:
                for num, line in enumerate(lines, 1):
                    if str(num) != no:
                        file.write(line)
                    else:
                        flag = 1

            if flag == 0:
                print("Error: todo #" + no + " does not exist. Nothing deleted.")
            else:
                print("Deleted todo #" + no)
        except:
            print("Error: Missing NUMBER for deleting todo.")


elif command == "done":
    if os.path.isfile("todo.txt") == False:
        file = open(os.path.join(sys.path[0], "todo.txt"), "w")
        file.close()

    with open(os.path.join(sys.path[0], "todo.txt"), "r") as file:
        try:
            no = (inp)[2].strip()
            lines = file.readlines()
            done = ""
            flag = 0
            with open(os.path.join(sys.path[0], "todo.txt"), "w") as file:
                for num, line in enumerate(lines, 1):
                    if str(num) != no:
                        file.write(line)
                    else:
                        flag = 1
                        done = "x " + str(date.today()) + " " + line
            with open(os.path.join(sys.path[0], "done.txt"), "a") as file:
                file.write(done)

            if flag == 0:
                print("Error: todo #" + no + " does not exist.")
            else:
                print("Marked todo #" + no + " as done.")
                if len(lines) == 1:
                    print("There are no pending todos!")
        except:
            print("Error: Missing NUMBER for marking todo as done.")


elif command == "report":
    pend = 0
    comp = 0

    with open(os.path.join(sys.path[0], "todo.txt"), "r") as file:
        lines = file.readlines()
        pend = len(lines)

    with open(os.path.join(sys.path[0], "done.txt"), "r") as file:
        lines = file.readlines()
        comp = len(lines)

    print(str(date.today()) + " Pending : " +
          str(pend) + " Completed : " + str(comp))
