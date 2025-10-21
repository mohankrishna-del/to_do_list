# Load tasks from file
try:
    f = open("tasks.txt", "r")
    tasks = [line.strip() for line in f.readlines()]
    f.close()
except:
    tasks = []

while True:
    print("\nOptions: view | add | remove | exit")
    cmd = input("Enter command: ").strip().lower()

    if cmd == "view":
        if not tasks:
            print("No tasks.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif cmd == "add":
        t = input("Enter task: ").strip()
        if t:
            tasks.append(t)
            print("Added.")
        else:
            print("Empty task not added.")

    elif cmd == "remove":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            try:
                i = int(input("Task number to remove: "))
                if 1 <= i <= len(tasks):
                    print("Removed:", tasks.pop(i-1))
                else:
                    print("Invalid number.")
            except:
                print("Enter a valid number.")

    elif cmd == "exit":
        f = open("tasks.txt", "w")
        for t in tasks:
            f.write(t + "\n")
        f.close()
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Unknown command.")