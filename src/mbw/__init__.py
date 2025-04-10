def mbw():

    from os import environ

    v = "PYCHARM_HOSTED"
    b = "TkAgg"

    if v in environ.keys() and environ[v] == "1":
        import matplotlib

        if matplotlib.get_backend() != b:
            matplotlib.use(b)
