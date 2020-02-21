__version__ = '0.0.1'

from .gist_magic import Gister


def load_ipython_extension(ipython):
    token = input("\nGitHub token: ")
    gist_magic = Gister(ipython, token)
    ipython.register_magics(gist_magic)
