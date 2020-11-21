import subprocess as cmd
import re
import os
import git
import gitAutomate as automate
import click

remote = "origin"


@click.command()
@click.option('--np', default='np', help='Commit & Push active branch.')
@click.argument('remote', required=False)
def GitHub(np, remote):
    """GitHub automation tool for numerous workflow."""
    if np == 'np':
        automate.normalPush(remote)


if __name__ == '__main__':
    GitHub()

# automate.newBranchPush("origin")
# automate.normalPushPR("origin")
# automate.normalPush("origin")
# output = git.getAllLocalBranchName()

# output = cmd.check_output(
#     ['git', 'remote', 'prune', 'origin']).decode("utf-8")
# output = output.split()

# git.pruneLocal("origin", True)
