import git
import subprocess
import webbrowser


def newBranchPush():
    branch = "pythonScript"
    git.commit()
    git.branch(branch)
    git.push("origin", branch)


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
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
        "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

    print(output)
    for mystring in arr:
        if '/pull' in mystring:
            webbrowser.get('chrome').open(mystring)
            print("Raghib: "+mystring)


# https://github.com/vcshahriyer/movies/pull/new/pythonScript
