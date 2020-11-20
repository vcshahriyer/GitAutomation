import subprocess as cmd
import re
import os
import git
import gitAutomate as automate

basePath = "./movies"
# wd = os.getcwd()
# os.chdir(basePath)
# cmd.run('dir', shell=True, cwd=basePath)
# cmd.run("dir", check=True, shell=True)
# cmd.run("git status", check=True, shell=True)
# output = cmd.check_output(
#     ['git', 'config', '--list'])

automate.normalPush("origin")


# print(git.getActiveBranchName())
