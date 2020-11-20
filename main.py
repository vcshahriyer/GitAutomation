import subprocess as cmd
import re
import os
import git
import gitAutomate as automate

# automate.newBranchPush("origin")
automate.normalPushPR("origin")
# automate.normalPush("origin")
# output = git.getAllLocalBranchName()

# output = cmd.check_output(
#     ['git', 'remote', 'prune', 'origin']).decode("utf-8")
# output = output.split()

# git.pruneLocal("origin", True)
