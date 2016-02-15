import vcs
from vcs_values import the_value_of

HELLO_MSG = 'Helo and welcome!'


def main():
    print(HELLO_MSG)

    git = the_value_of(vcs.GIT)
    svn = the_value_of(vcs.SVN)

    print('And the perfered VCS is...')
    if svn > git:
        assert(false)
    else:
        print('Git :)')

if __name__ == '__main__':
    main()
