import webbrowser
import subprocess as cmd
import re
import click


# Default variables
_remote = "origin"

# webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
#     "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))


def gitRemoteInfo():
    output = cmd.check_output(['git', 'remote', '-v']).decode("utf-8")
    output = output.split()
    for str in output:
        m = re.search('com[:\/](.+)git$', str)
        if m:
            found = m.group(1)
            userName, repoName = found.split('/')
            return [userName, repoName[:-1]]
    return None


def getActiveBranchName():
    output = cmd.check_output(
        ["git", "branch"]).decode("utf-8")
    output = output.split()
    return output[output.index("*") + 1]


def getAllLocalBranchName():
    output = cmd.check_output(
        ['git', 'branch']).decode("utf-8")
    output = output.split()
    output.remove("*")
    return(output)


def getAllRemoteBranchName(remote):
    output = cmd.check_output(
        ['git', 'branch', '-r']).decode("utf-8")
    output = output.split()
    remoteBranches = []
    for branch in output:
        if f'{remote}/' in branch:
            if branch.split("/")[1] != "HEAD":
                remoteBranches.append(branch.split("/")[1])
    return(remoteBranches)


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
    if name is None:
        name = input("\nType in the name of the branch you want to make: ")
    run("checkout", "-b", name)


def fetch(remote):
    run("fetch", remote)


def pull(remote=None, b_name=None):
    if remote is None:
        remote = input("\nType in the name (origin) of the remote:  ")
    if b_name is None:
        b_name = getActiveBranchName()
    run("pull", remote, b_name)


def push(remote=None, br=None):
    if remote is None:
        remote = input("\nType in the name (origin) of the remote: ")
    if br is None:
        br = getActiveBranchName()
    run("push", "-u", remote, br)
    # runWithOutput("push", "-u", remote, br)


def deleteBranch(b_name, force):
    if force:
        run("branch", "-D", b_name)
    else:
        run("branch", "-d", b_name)


def pruneRemote(force=False, remote=None):
    fetch(remote)
    if remote is None:
        remote = input("\nType in the name (origin) of the remote: ")
    localBranches = getAllLocalBranchName()

    output = cmd.check_output(
        ['git', 'remote', 'prune', remote]).decode("utf-8")
    output = output.split()
    for pruned in output:
        if f'{remote}/' in pruned:
            origin, branch = pruned.split('/')
            if branch in localBranches:
                print(f'Deleted Branch : {branch}')
                deleteBranch(branch, force)


def pruneLocal(force=False, remote=None):
    if remote is None:
        remote = input("\nType in the name (origin) of the remote: ")
    fetch(remote)
    run('remote', 'prune', remote)
    localBranches = getAllLocalBranchName()
    remoteBranches = getAllRemoteBranchName(remote)
    for br in localBranches:
        if br not in remoteBranches:
            print(f'Deleted Branch : {br}')
            deleteBranch(br, force)


def sync(remote):
    fetch(remote)
    pull(remote)


def justNewBranchPushPR(remote):
    b_name = input("\nType the branch name you want to create: ")
    userName, repoName = gitRemoteInfo()
    url = f'https://github.com/{userName}/{repoName}/pull/new/{b_name}'
    branch(b_name)
    push(remote, b_name)
    webbrowser.open(url)


def newBranchPushPR(remote):
    b_name = input("\nType the branch name you want to create: ")
    userName, repoName = gitRemoteInfo()
    url = f'https://github.com/{userName}/{repoName}/pull/new/{b_name}'
    add()
    commit()
    branch(b_name)
    push(remote, b_name)
    # webbrowser.get('chrome').open(url)
    webbrowser.open(url)


def normalPushPR(remote):
    b_name = getActiveBranchName()
    userName, repoName = gitRemoteInfo()
    url = f'https://github.com/{userName}/{repoName}/pull/new/{b_name}'
    add()
    commit()
    push(remote, b_name)
    if b_name != "master":
        # webbrowser.get('chrome').open(url)
        webbrowser.open(url)


def justPulrequest(remote):
    b_name = getActiveBranchName()
    userName, repoName = gitRemoteInfo()
    url = f'https://github.com/{userName}/{repoName}/pull/new/{b_name}'
    push(remote, b_name)
    if b_name != "master":
        # webbrowser.get('chrome').open(url)
        webbrowser.open(url)


def normalPush(remote, b_name=None):
    add()
    commit()
    if b_name is None:
        push(remote)
    else:
        push(remote, b_name)


@click.command()
@click.option('--choice', prompt='Type Command Shorthand', help='Commit & Push active branch.')
# @click.option('--remote', default=_remote, prompt='Remote Name', help='Remote name of your project Repo')
@click.argument('remote', required=False)
def GitHub(choice, remote):
    if not remote:
        remote = _remote
    """GitHub automation tool for numerous workflow."""
    if choice == 'sync':
        sync(remote)
    elif choice == 'np':
        normalPush(remote)
    elif choice == 'npr':
        normalPushPR(remote)
    elif choice == 'nbpr':
        newBranchPushPR(remote)
    elif choice == 'prnr':
        force = input("\nForce Prune? (True/False) : ")
        pruneRemote(force, remote)
    elif choice == 'prnl':
        force = input("\nForce Prune? (True/False) : ")
        pruneLocal(force, remote)
    elif choice == 'jpr':
        justPulrequest(remote)
    elif choice == 'jnbpr':
        justNewBranchPushPR(remote)
    else:
        print("\033[1;31;40m Wrong Command Shorthand!")


if __name__ == '__main__':
    print("Available Commands: \n")
    print("\033[1;32;40m [sync]   :       \033[0m Synchronize local with remote. ")
    print("\033[1;32;40m [np]     :       \033[0m Normal Push Current Branch. ")
    print(
        "\033[1;32;40m [npr]    :       \033[0m Normal Push with pull-request (except Master). ")
    print(
        "\033[1;32;40m [nbpr]   :       \033[0m New Branch Push with pull-request. ")
    print(
        "\033[1;32;40m [prnr]   :       \033[0m Prune Remote Branches. ")
    print(
        "\033[1;32;40m [prnl]   :       \033[0m Prune Local Branches. ")
    print(
        "\033[1;32;40m [jpr]   :       \033[0m Just create pull-request. (No git -add,-commit) ")
    print(
        "\033[1;32;40m [jnbpr]   :       \033[0m Just create new Branch and pull-request. (No git -add,-commit) ")

    GitHub()
