import git
import subprocess
import webbrowser

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))


def sync(remote):
    git.fetch()
    git.pull(remote)


def newBranchPush(remote):
    branch = input("\nType the branch name you want to create: ")
    userName, repoName = git.gitRemoteInfo()
    url = f'https://github.com/{userName}/{repoName}/pull/new/{branch}'
    git.add()
    git.commit()
    git.branch(branch)
    git.push(remote, branch)
    webbrowser.get('chrome').open(url)


def normalPush(remote, branch=None):
    git.add()
    git.commit()
    if branch is None:
        git.push(remote)
    else:
        git.push(remote, branch)
