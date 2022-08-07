
# GistMagic

This package performs upload to GitHub Gist of last X lines of your Ipython session history.


## Quickstart

```ipython
%pip install gistmagic
%load_ext gistmagic
...
%gistmagic -5
```

## Description

- You need to generate a GitHub token. (Please trim its purpose and validity)
- You need to install gistmagic
- GistMagic is extention used only from ipython.
- Your token is kept in memory and prompted every time gistmagic extention is loaded.
- Gistmagic will not include in your Gist any other lines that the last X lines which start with In or Out.
- Gistmagic will re-arrange the sequence of In/Out in Gist as this the only snipped you have created in your current ipython session.


## In REPL help

```
In [3]: %gistmagic?
Docstring:
Upload code to gist

Usage:
    %load_ext gistmagic
    %gistmagic -X  (%gistmagic -5 / %gistmagic -25)

The argument -X is representing the last X In/Out sequences
```

# How to create GitHub token

Quite easy.
Chech it out from here: [GitHub token tutorial](https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

