import gitAutomate as automate
import click

# Default variables
_remote = "origin"


@click.command()
@click.option('--choice', prompt='Type Command Shorthand', help='Commit & Push active branch.')
@click.option('--remote', default=_remote, prompt='Remote Name', help='Remote name of your project Repo')
def GitHub(choice, remote):
    """GitHub automation tool for numerous workflow."""
    if choice == 'sync':
        automate.sync(remote)
    elif choice == 'np':
        automate.normalPush(remote)
    elif choice == 'npr':
        automate.normalPushPR(remote)


if __name__ == '__main__':
    print("Available Commands: \n")
    print("\033[1;32;40m [sync]   :       \033[0m Synchronize local with remote. ")
    print("\033[1;32;40m [np]     :       \033[0m Normal Push Current Branch. ")
    print(
        "\033[1;32;40m [npr]    :       \033[0m Normal Push with pull-request (except Master). ")

    GitHub()

# automate.newBranchPush("origin")
# automate.normalPushPR("origin")
# automate.normalPush("origin")
# output = git.getAllLocalBranchName()

# output = cmd.check_output(
#     ['git', 'remote', 'prune', 'origin']).decode("utf-8")
# output = output.split()

# git.pruneLocal("origin", True)
