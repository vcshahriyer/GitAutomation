import subprocess
from pyfiglet import figlet_format
from termcolor import cprint


logo = 'Git-Commands'


class color:
    NOTICE = '\033[91m'
    END = '\033[0m'


info = color.NOTICE + '''
Automate the process of using commands such as clone, commit, branch, pull, merge, blame and stash.\n''' + color.END


def run(*args):
    return subprocess.check_call(['git'] + list(args))


def runWithOutput(*args):
    proc = subprocess.Popen(['git'] + list(args), stdout=subprocess.PIPE)
    stdout, _ = proc.communicate()
    return sorted(v.strip(' *') for v in stdout.decode('utf-8').split('\n') if v)


def clone():
    print("\nYou will be asked for the user first and then the repository name.\n")

    user = input("User: ")
    __user__ = f'{user}'
    repo = input("Repository: ")
    __repo__ = f'{repo}'

    print("\nChoose the local path for your clone.")
    local = input("Local path: ")
    local_path = f'{local}'

    subprocess.Popen(['git', 'clone', "https://github.com/" +
                      __user__ + "/" + __repo__ + ".git", local_path])


def commit():
    message = input("\nType in your commit message: ")
    commit_message = f'{message}'

    run("add", "-A")
    run("commit", "-am", commit_message)
    # run("push", "-u", "origin", "master")


def branch(name=None):
    if name is not None:
        br = f'{name}'
    else:
        branch = input("\nType in the name of the branch you want to make: ")
        br = f'{branch}'

    run("checkout", "-b", br)

    # choice = input(
    #     "\nDo you want to push the branch right now to GitHub? (y/n): ")
    # choice = choice.lower()

    # if choice == "y":
    #     run("push", "-u", "origin", br)

    # elif choice == "n":
    #     print("\nOkay, goodbye!\n")

    # else:
    #     print("\nInvalid command! Use y or n.\n")


def push(remote, br):
    # run("push", "-u", remote, br)
    runWithOutput("push", "-u", remote, br)


def pull():
    print("\nPulls changes from the current folder if *.git is initialized.")

    choice = input("\nDo you want to pull the changes from GitHub? (y/n): ")
    choice = choice.lower()

    if choice == "y":
        run("pull", "origin")

    elif choice == "n":
        print("\nOkay, goodbye!\n")

    else:
        print("\nInvalid command! Use y or n.\n")


def fetch():
    print("\nFetches changes from the current folder.")
    run("fetch")


def merge():
    branch = input("\nType in the name of your branch: ")
    br = f'{branch}'

    run("merge", br)


def reset():
    filename = input("\nType in the name of your file: ")
    fl = f'{filename}'

    run("reset", fl)


def blame():
    file = input("\nType in the name of the file: ")
    fi = f'{file}'

    run("blame", fi)


def stash():
    print("\nDo you want to save, list, pop, show, branch, clear or drop? ")

    cmd = 'save, li, pop, show, branch, clear and drop'

    print("\nCommands to use: " + cmd)

    choice = input("\nType in the command you want to use: ")
    choice = choice.lower()

    if choice == "save":
        message = input("\nType in your stash message: ")
        stash_message = f'{message}'

        run("stash", "save", stash_message)

    elif choice == "li":
        run("stash", "li")

    elif choice == "pop":
        run("stash", "pop")

    elif choice == "show":
        run("stash", "show", "-p")

    elif choice == "branch":
        branch = input("\nType in the name of the branch you want to stash: ")
        br = f'{branch}'

        run("stash", "branch", br)

    elif choice == "clear":
        run("stash", "clear")

    elif choice == "drop":
        run("stash", "drop")

    else:
        print("\nNot a valid command!")
        print("\nUse " + cmd)


def main():
    cprint(figlet_format(logo, font='slant'), 'green')
    print(info + "\n")

    choices = 'clone, commit, branch, push, pull, fetch, merge, reset, blame and stash'
    print("Commands to use: " + choices)

    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == "clone":
        clone()

    elif choose_command == "commit":
        commit()

    elif choose_command == "branch":
        branch()

    elif choose_command == "pull":
        pull()

    elif choose_command == "push":
        push("origin")

    elif choose_command == "fetch":
        fetch()

    elif choose_command == "merge":
        merge()

    elif choose_command == "reset":
        reset()

    elif choose_command == "blame":
        blame()

    elif choose_command == "stash":
        stash()

    else:
        print("\nNot a valid command!")
        print("\nUse " + choices)


if __name__ == '__main__':
    main()
