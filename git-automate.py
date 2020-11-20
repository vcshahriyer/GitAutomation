import git
import subprocess
import webbrowser


def newBranchPush():
    branch = "pythonScript"
    git.commit()
    git.branch(branch)
    git.push("origin", branch)


if __name__ == "__main__":
    # newBranchPush()
    branch = "pythonScript"
    # git.commit()
    # git.branch(branch)
    # print(git.push("origin", branch))

    # proc = subprocess.Popen(
    #     ['git', 'push', 'origin', 'pythonScript'], stdout=subprocess.PIPE)
    output = subprocess.check_output(
        ['git', 'push', 'origin', 'pythonScript', '--verbose'])
    # proc = subprocess.Popen(
    #     ['git', 'config', '--list'], stdout=subprocess.PIPE)
    # stdout, _ = proc.communicate()
    # output = stdout.decode('utf-8').strip()
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
