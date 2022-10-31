def find_max(*args):
    arguments = []
    if len(args) == 0:
        return None
    local_max = args[0]
    for arg in args:
        if local_max < arg:
            local_max = arg
    return local_max
