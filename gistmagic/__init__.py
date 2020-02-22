__version__ = '0.0.1'

from .gistmagic import GistMagic


def load_ipython_extension(ipython):
    token = input("\nGitHub token: ")
    gistmagic = GistMagic(ipython, token)
    ipython.register_magics(gistmagic)
