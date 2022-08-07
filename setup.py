from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='gistmagic',
    version='0.0.2',
    description='History to Gist - line magic for Ipython',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rbagrov/GistMagic',
    author='Rostislav Bagrov',
    author_email='bagrov.rostislav@gmail.com',
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='ipython gist magic',
    install_requires=['ipython>=7', 'PyGithub>=1.46', 'pyperclip>=1.8.2'],
)
