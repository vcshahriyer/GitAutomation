import gitAutomate as automate
import git
import click

# Default variables
_remote = "origin"


@click.command()
@click.option('--choice', prompt='Type Command Shorthand', help='Commit & Push active branch.')
# @click.option('--remote', default=_remote, prompt='Remote Name', help='Remote name of your project Repo')
@click.argument('remote', required=False)
def GitHub(choice, remote):
    if not remote:
        remote = _remote
    """GitHub automation tool for numerous workflow."""
    if choice == 'sync':
        automate.sync(remote)
    elif choice == 'np':
        automate.normalPush(remote)
    elif choice == 'npr':
        automate.normalPushPR(remote)
    elif choice == 'nbpr':
        automate.newBranchPushPR(remote)
    elif choice == 'prnr':
        force = input("\nForce Prune? (True/False) : ")
        git.pruneRemote(force, remote)
    elif choice == 'prnl':
        force = input("\nForce Prune? (True/False) : ")
        git.pruneLocal(force, remote)


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

    GitHub()
