import vcs
from vcs_values import the_value_of

HELLO_MSG = 'Helo and welcome!'
GOOD_BYE_MSG = 'Good by!'


def main():

    print(HELLO_MSG)

    git = the_value_of(vcs.GIT)
    svn = the_value_of(vcs.SVN)

    print('And the perfered VCS is...')

    if svn > git:
        assert False
    else:
        print('Git :)')

    print(GOOD_BYE_MSG)


if __name__ == '__main__':
    main()
