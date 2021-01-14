from github import Github
import os
import ui
import curses
import time

f = open('key.key','r')
key = f.read()

f.close()

f = open('data.txt','r')
std_data = f.read()
f.close()

std_data = std_data.splitlines()
stdlist =[]




g = Github(key)

for std in std_data:
    std = std.split()
    stdlist.append(std)




# coloring:
# ui.info("This is", ui.red, "red",
#         ui.reset, "and this is", ui.bold, "bold")

# # enumerating:
# list_of_things = ["foo", "bar", "baz"]
# for i, thing in enumerate(list_of_things):
#     ui.info_count(i, len(list_of_things), thing)

# # progress indication:
# ui.info_progress("Done",  5, 20)
# ui.info_progress("Done", 10, 20)
# ui.info_progress("Done", 20, 20)

# # reading user input:
# with_sugar = ui.ask_yes_no("With sugar?", default=False)

# fruits = ["apple", "orange", "banana"]
# selected_fruit = ui.ask_choice("Choose a fruit", fruits)

# #  ... and more!


scr = curses.initscr()
for i in range(len(stdlist)):

    scr.addstr(i, 0, stdlist[i][0])
 

for std in stdlist:
        repo = g.get_repo(std[4])
        commit = repo.get_commit(repo.get_commits()[0].sha).raw_data['commit']['message']
        std.append(commit)

while True:
    
    for i in range(len(stdlist)):
        scr.addstr(i, 10, stdlist[i][5])
        scr.refresh()
        time.sleep(1)

    for std in stdlist:
        repo = g.get_repo(std[4])
        commit = repo.get_commit(repo.get_commits()[0].sha).raw_data['commit']['message']
        std[5] = commit