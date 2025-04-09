import os

if "PYCHARM_HOSTED" in os.environ.keys() and os.environ["PYCHARM_HOSTED"] == "1":
    import matplotlib
    if matplotlib.get_backend() != matplotlib.get_backend():
        matplotlib.use("TkAgg")
