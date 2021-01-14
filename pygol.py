from github import Github
import os

f = open('key.key','r')
key = f.read()

g = Github(key)

repo = g.get_repo("24engiball/pygol")

data = repo.get_commits()

print(data[0].sha)
text = repo.get_git_commit(data[0].sha)
print(text)
