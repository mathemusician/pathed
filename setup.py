"""
run the following to update module:

change version number
python3 setup.py sdist bdist_wheel
twine upload dist/* --verbose
"""


from setuptools import setup, find_packages
import os
import shutil

VERSION = "1.0.00"
DESCRIPTION = "Common Path and Importing Operations"


# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

# get rid of certain folders if they exist
build_path = os.path.join(this_directory, "build")
dist_path = os.path.join(this_directory, "dist")
op_info_path = os.path.join(this_directory, "pathed.egg-info")
pycache_path = os.path.join(this_directory, "pathed", "__pycache__")

if os.path.exists(build_path):
    shutil.rmtree(build_path)
if os.path.exists(dist_path):
    shutil.rmtree(dist_path)
if os.path.exists(op_info_path):
    shutil.rmtree(op_info_path)
if os.path.exists(pycache_path):
    shutil.rmtree(pycache_path)


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
    url="https://pypi.org/project/opt/",
    project_urls={
        "Documentation": "https://pypi.org/project/op/",
        "Code": "https://github.com/mathemusician/op",
        "Issue tracker": "https://github.com/mathemusician/op/issues",
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
