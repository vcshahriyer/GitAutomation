import subprocess as cmd
import re
import os
import git

basePath = "./movies"
# wd = os.getcwd()
# os.chdir(basePath)
# cmd.run('dir', shell=True, cwd=basePath)
# cmd.run("dir", check=True, shell=True)
# cmd.run("git status", check=True, shell=True)
# output = cmd.check_output(
#     ['git', 'config', '--list'])

git.add()
git.commit("Second Commit using py script")
git.push("origin")


# print(git.getActiveBranchName())
