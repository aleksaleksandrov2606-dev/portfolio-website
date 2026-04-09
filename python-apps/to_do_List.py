import datetime
import os

date = datetime.datetime.now()



to_do = []
answer = None

to_do_list = open("to_do_list.txt", "w")
to_do_list.write("To-Do List for " + date.strftime("%x") + "\n")

while answer != "No":
    to_do.append(input("Input a task: "))
    answer = input("Do you have more tasks: ")
    
print("Your To-Do List for the " + date.strftime("%x"))

task_num = 1

for task in to_do:
    print(str(task_num) + ". " + task)
    to_do_list.write(str(task_num) + ". " + task + "\n")
    task_num += 1


to_do_list.close()

print("Your To-Do List has been saved to to_do_list.txt")

os.startfile("to_do_list.txt")