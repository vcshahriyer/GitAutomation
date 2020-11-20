import subprocess as cmd
import re
import os
import git
import gitAutomate as automate

basePath = "./movies"
# automate.newBranchPush("origin")
# output = git.getAllLocalBranchName()

# output = cmd.check_output(
#     ['git', 'remote', 'prune', 'origin']).decode("utf-8")
# output = output.split()

automate.normalPush("origin")
