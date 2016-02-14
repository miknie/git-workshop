import vcs
import hello_messages
import good_byes
from vcs_values import the_value_of


def main():

    print(hello_messages.HELLO_MSG)

    print("Today is a day")

    git = the_value_of(vcs.GIT)
    svn = the_value_of(vcs.SVN)

    print('And the perfered VCS is...')

    if svn > git:
        assert False
    else:
        print('Git :)')

    print(good_byes.GOOD_BYE_MSG)


if __name__ == '__main__':
    main()
