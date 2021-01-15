def expand(D = dict(), path = str(), res = dict()):
    if type(D) == dict:
        for elem in list(D):
            path += elem + '/'
            expand(D[elem], path)
            path = path[: -len(elem) - 1]
    else:
        res[path[: -1]] = D
    return res