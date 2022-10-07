"""
run the following to update module:

change version number
python3 setup.py sdist bdist_wheel
twine upload dist/* --verbose
"""


import os
import shutil
from os import path
from setuptools import setup, find_packages

VERSION = "1.2.01"
DESCRIPTION = "Common Path and Importing Operations"


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

# get rid of certain folders if they exist
build_path = os.path.join(this_directory, "build")
dist_path = os.path.join(this_directory, "dist")
op_info_path = os.path.join(this_directory, "pathed.egg-info")
pycache_path = os.path.join(this_directory, "pathed", "__pycache__")

for folder_path in (build_path, dist_path, op_info_path, pycache_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)


# Setting up
setup(
    name="pathed",
    version=VERSION,
    author="Jv Kyle Eclarin",
    author_email="<jvykleeclarin@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    url="https://pypi.org/project/pathed/",
    project_urls={
        "Documentation": "https://pypi.org/project/pathed/",
        "Code": "https://github.com/mathemusician/pathed",
        "Issue tracker": "https://github.com/mathemusician/pathed/issues",
    },
    keywords=["python", "pathing", "path", "pathed"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3.5",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
)
