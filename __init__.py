__version__ = '0.0.1'

from .gister import Gister


def load_ipython_extension(ipython):
    token = input("\nGitHub token: ")
    gister = Gister(ipython, token)
    ipython.register_magics(gister)
