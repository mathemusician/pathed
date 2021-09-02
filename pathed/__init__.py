"""
Made by Jv Kyle Eclarin

Borrows heavily from pathlib, os, shutil, and glob
"""

import os as _os
import sys as _sys
import importlib.util
import shutil as _shutil
import inspect as _inspect
from glob import glob as _glob
from pathlib import Path as _Path
from copy import deepcopy as _deepcopy
from typing import Optional, Any, List, Union


# find path of the file doing the importing
filedir = None

for frame in _inspect.stack()[1:]:
    if frame.filename[0] != "<":
        filedir = frame.filename
        break
if filedir == None:
    # Returns cwd for interactive terminals
    filedir = str(_Path.cwd())


class Path(str):
    """
    class Path:
        returns str-like object

    Parameters:
        *args: objects that can be turned into a string

    Path/str/int/list will concatenate the string versions and return a str-like Path object
    """

    def __new__(cls, *args, custom: bool = False, start_at_root: bool = True) -> str:

        if custom:
            paths = []
        else:
            paths = [_os.path.dirname(filedir)]

        for arguments in args:
            if arguments == "..":
                paths[0] = _os.path.split(paths[0])[0]
            else:
                paths.append(arguments)

        path = str(_Path(*paths))

        if start_at_root == True:
            if path[0] != _os.path.sep:
                path = _os.path.sep + path

        return str.__new__(cls, path)

    def __init(self) -> None:
        super().__init__(self)

    def add(self, *args) -> str:
        return self.__truediv__(*args)

    def __truediv__(self, *args) -> str:
        """
        Parameters:
            *args: Any class that can be turned into a string
        """
        current_path = _deepcopy(self.__str__())

        paths = [current_path]

        for arguments in args:
            # convert arguments to string
            if type(arguments) != type(str()):
                try:
                    arguments = str(arguments)
                except:
                    print("path could not be converting to a string")
                    raise TypeError

            if arguments == "..":
                paths[0] = _os.path.split(paths[0])[0]
            else:
                paths.append(arguments)

        return Path(*paths, custom=True)

    def ls(self, full=False) -> List[str]:
        """
        returns [str, str, ...] of files and directories in Path

        if full=True, returns [Path, Path, ...] of absolute Paths

        throws error if Path doesn't exist
        """
        path = self.string()

        files_and_stuff = _os.listdir(path)

        if full == True:
            return [Path(path, custom=True) for path in files_and_stuff]
        else:
            return files_and_stuff

    def find(self, path: str, *args, **kwargs) -> List[str]:
        """
        find('*.py') returns [Path, Path, ...] in current Path that have the .py extension

        find('**.py') returns [Path, Path, ...] in current Path and subdirectories that have the .py extension
        """
        files_and_stuff = _glob(_os.path.join(self.__str__(), path), *args, **kwargs)
        return [Path(path, custom=True) for path in files_and_stuff]

    def isfile(self) -> bool:
        """
        returns True if Path is a file
        """
        return _os.path.isfile(self.string())

    def isdir(self) -> bool:
        """
        returns True if Path is a directory
        """
        return _os.path.isdir(self.string())

    def exists(self) -> bool:
        """
        returns True if the Path exists
        """
        return _os.path.exists(self.string())

    def copyfile(self, destination, **kwargs) -> str:
        """
        copies Path to destination if Path is a file, returns destination as Path
        """
        assert _os.path.isfile(self.string()) == True
        _shutil.copyfile(self.string(), destination, **kwargs)
        return Path(destination, custom=True)

    def copydir(self, destination, **kwargs) -> str:
        """
        copies Path to destination if Path is a directory, returns destination as Path
        """
        assert _os.path.isdir(self.string()) == True
        _shutil.copy(self.string(), destination, **kwargs)
        return Path(destination, custom=True)

    def move(self, destination: str, **kwargs) -> str:
        """
        moves Path to destination, returns destination as Path
        """
        assert _os.path.exists(self.string()) == True
        _shutil.move(self.string(), destination, **kwargs)
        return Path(destination, custom=True)

    def mkdir(self, **kwargs) -> None:
        """
        makes a directory called Path, throws error if Path is already a directory
        """
        _os.makedirs(self.string(), **kwargs)

    def rmdir(self, **kwargs) -> None:
        """
        removes Path if Path is a directory
        """
        assert _os.path.isdir(self.string()) == True
        _os.rmdir(self.string(), **kwargs)

    def mkfile(self, data: str = "", *args, **kwargs) -> None:
        """
        mkfile(data) writes data to Path, throws error if Path does not exist

        mkfile(data, 'w') write data, makes file if Path does not exist
        mkfile(data, 'wb') writes bytes data to Path
        mkfile(data, 'a') appends data to Path
        """
        with open(self.string(), *args, **kwargs) as file_handler:
            file_handler.write(data)

    def rmfile(self, **kwargs) -> None:
        """
        removes Path if Path is a file
        """
        assert _os.path.isfile(self.string()) == True
        _os.remove(self.string(), **kwargs)

    def write(self, *args, **kwargs) -> None:
        """
        write(data) writes data to Path, throws error if Path does not exist

        write(data, 'w') write data, makes file if Path does not exist
        write(data, 'wb') writes bytes data to Path
        write(data, 'a') appends data to Path
        """
        self.mkfile(*args, **kwargs)

    def read(self, *args, **kwargs) -> str:
        """
        read() returns text of Path if Path is a file

        read('rb') returns text of byte file if Path is a file
        """
        assert _os.path.isfile(self.string()) == True
        with open(self.string(), *args, **kwargs) as file_handler:
            file_handler.read(data)

    def readfast(self, *args, **kwargs) -> Any:
        """
        good for reading the first few of lines of a VERY LARGE file
        
        returns generator for reading large files one line at a time

        file_text = Path.readfast()
        next(file_text) to get string of next file, throws StopIteration Error at end of file
        """
        assert _os.path.isfile(self.string()) == True

        with open(self.string(), *args, **kwargs) as file_handler:
            for line in file_handler:
                yield line

    def up(self, num: int, *args) -> str:
        """
        goes up the directory 'num' times

        returns Path
        """
        path = self.__str__()

        times_up = [".." for i in range(num + 1)]
        return Path(path, *times_up, custom=True)

    def splitpath(self, full: bool = False) -> List[str]:
        """
        /absolute/path/to/leaf -> returns [branch, leaf]

        print(branch) # /absolute/path/to
        print(leaf)   # leaf

        if full=True, returns [absolute, path, to, leaf]
        """
        path = _os.path.split(self.string())
        if full == True:
            return self.__str__().split(os.path.sep)
        else:
            return [Path(path[0], custom=True), path[1]]

    def branch(self) -> str:
        """
        /absolute/path/to/leaf -> returns branch
        
        print(Path.branch()) # /absolute/path/to
        """
        return self.splitpath()[0]

    def leaf(self) -> str:
        """
        /absolute/path/to/leaf -> returns leaf
        
        print(Path.leaf()) # leaf
        """
        return self.splitpath()[1]

    def string(self) -> str:
        """
        useful for printing raw Windows paths

        \\this\\is\\a\\windows\\path
        """
        return str(_Path(self.__str__()))


def importfile(path: str, module: Optional[Any] = None) -> Any:
    """
    importfile(path, module=None)

    Parameters:
        path: str or str-like object with path to directory
        module: module that will have attributes appended to it

    returns file functions, classes, and global variables from a python file
    """
    path = Path(path, custom=True)
    assert _os.path.isfile(path) == True

    name = path.leaf().split(".")[0]

    spec = importlib.util.spec_from_file_location(name, str(_Path(path)))
    file_handler = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(file_handler)

    if module == None:
        return file_handler
    else:
        try:
            setattr(module, name, file_handler)
        except:
            print("was not able to to load modules from", path)


class importdir:
    """
    importdir(path, module=Optional)

    Parameters:
        path: str or str-like object with path to directory
        module: module that will have attributes appended to it

    imports *.py files from directory

    returns class with attributes named after *.py files
    """

    def __init__(self, path: str, module: Optional[Any] = None) -> Union[Any, None]:
        assert _os.path.isdir(path) == True
        path = Path(path, custom=True)

        python_files = path.find("*.py")
        if len(python_files) == 0:
            return

        for python_file in python_files:
            name = python_file.leaf()[:-3]

            if module == None:
                try:
                    setattr(self, name, importfile(python_file))
                except:
                    print("was not able to to load modules from", python_file)
            else:
                importfile(python_file, module)


cwd = Path(str(_Path.cwd()), custom=True)
filedir = Path(filedir, custom=True)
