# First of all install: pip3 install py2app
from setuptools import setup

APP = ['1-emailmssg.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True
}

setup(
    app=APP,
    option={'py2app': OPTIONS},
    setup_requires=['py2app']
)

# On terminal python3 tried-to-make-installation-mac.py py2app