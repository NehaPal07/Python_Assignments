def toString(arr):
    s = ''
    for i in range(len(arr)):
        if i > 0:
            if i == len(arr) - 1:
                s = s + ' and '
            else:
                s = s + ', '
        s = s + arr[i];
    return s