import subprocess as cmd
import re
import os


def gitRemoteInfo():
    output = cmd.check_output(['git', 'remote', '-v']).decode("utf-8")
    output = output.split()
    for str in output:
        m = re.search('com[:\/](.+)git$', str)
        if "github.com" in str:
            if m:
                found = m.group(1)
                break
    userName, repoName = found.split('/')
    return [userName, repoName[:-1]]


def getActiveBranchName():
    output = cmd.check_output(
        ["git", "branch"]).decode("utf-8")
    output = output.split()
    return output[output.index("*") + 1]


def run(*args):
    return cmd.check_call(['git'] + list(args))


def add():
    run("add", "-A")


def commit(message=None):
    if message is None:
        message = input("\nType in your commit message: ")
    commit_message = f'{message}'
    run("commit", "-am", commit_message)
    # run("push", "-u", "origin", "master")


def branch(name=None):
    if name is not None:
        br = f'{name}'
    else:
        branch = input("\nType in the name of the branch you want to make: ")
        br = f'{branch}'
    run("checkout", "-b", br)


def push(remote=None, br=None):
    if remote is None:
        remote = input("\nType in the name of the remote: ex: origin")
    if br is None:
        br = getActiveBranchName()
    run("push", "-u", remote, br)
    # runWithOutput("push", "-u", remote, br)


def prune(remote=None):
    if remote is None:
        remote = input("\nType in the name of the remote: ex: origin")
    run("remote", "prune", remote)
