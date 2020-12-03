import git
import webbrowser

# webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
#     "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))


def sync(remote):
    git.fetch()
    git.pull(remote)


def newBranchPushPR(remote):
    branch = input("\nType the branch name you want to create: ")
    userName, repoName = git.gitRemoteInfo()
    url = f'https://github.com/{userName}/{repoName}/pull/new/{branch}'
    git.add()
    git.commit()
    git.branch(branch)
    git.push(remote, branch)
    # webbrowser.get('chrome').open(url)
    webbrowser.open(url)


def normalPushPR(remote):
    branch = git.getActiveBranchName()
    userName, repoName = git.gitRemoteInfo()
    url = f'https://github.com/{userName}/{repoName}/pull/new/{branch}'
    git.add()
    git.commit()
    git.push(remote, branch)
    if branch != "master":
        # webbrowser.get('chrome').open(url)
        webbrowser.open(url)


def justPulrequest(remote):
    branch = git.getActiveBranchName()
    userName, repoName = git.gitRemoteInfo()
    url = f'https://github.com/{userName}/{repoName}/pull/new/{branch}'
    git.push(remote, branch)
    if branch != "master":
        # webbrowser.get('chrome').open(url)
        webbrowser.open(url)


def normalPush(remote, branch=None):
    git.add()
    git.commit()
    if branch is None:
        git.push(remote)
    else:
        git.push(remote, branch)
