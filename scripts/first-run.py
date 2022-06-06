#!/usr/bin/env python3

# This script is run the first time any action is performed after the repository
# is cloned. If you are reading this because the automatic initialization failed,
# skip down to the section headed "INITIALIZATION STEPS".

from sh import git
import datetime
import re
import sys
from urllib.parse import quote
import subprocess

BASE_OWNER = "googlefonts"
BASE_REPONAME = "googlefonts-project-template"
DUMMY_URL = "https://yourname.github.io/your-font-repository-name"


def repo_url(owner, name):
    return f"https://github.com/{owner}/{name}"


def web_url(owner, name):
    return f"https://{owner}.github.io/{name}"


def raw_url(owner, name):
    return f"https://raw.githubusercontent.com/{owner}/{name}"


def touch():
    open(".init.stamp", "w").close()


def lose(msg, e=None):
    print(msg)
    print("You will need to do the initialization steps manually.")
    print("Read scripts/first-run.py for more instructions how to do this.")
    if e:
        print(
            "\nHere's an additional error message which may help diagnose the problem."
        )
        raise e
    sys.exit(1)

# Pin the dependencies
print("Pinning dependencies")
dependencies = subprocess.check_output(["pip", "freeze"])
with open("requirements.txt", "wb") as dependency_file:
    dependency_file.write(dependencies)

# Finally, we add a "touch file" called ".init.stamp" to the repository which
# prevents this first-run process from being run again.
touch()
