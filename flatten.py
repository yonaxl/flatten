def flatten(arr):
    to_return = []
    for x in arr:
        if isinstance(x, list):
            for y in flatten(x):
                to_return.append(y)
        else:
            to_return.append(x)
    return to_return