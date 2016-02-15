# Get the value of a version controll system

def the_value_of(vcs_name):
    vcs_values = {'git': 42, 'svn': 13}
    try:
        return vcs_values[vcs_name.lower()]
    except:
        return 0
