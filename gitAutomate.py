import git
import subprocess
import webbrowser

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
    "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))


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


if __name__ == "__main__":
    # newBranchPush()
    branch = "pythonScript"
    output = subprocess.check_output(
        ['git', 'push', 'origin', 'pythonScript', '--verbose'])

    arr = output.split()
    url = 'https://pythonexamples.org'

    print(output)
    for mystring in arr:
        if '/pull' in mystring:
            webbrowser.get('chrome').open(mystring)
            print("Raghib: "+mystring)


# https://github.com/vcshahriyer/movies/pull/new/pythonScript
