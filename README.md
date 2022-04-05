# Why pathed?
Want to import a file that can't be accessed by "import"? Or a whole directory of files? This helps with that! Also, common path operations like find('*.txt'), rmfile, mkfile, read, and more are in the Path module. Tired of writing str(Path())? Try the Path module. Inspired by pathlib, os.path, shutil, and glob.

---

# One Liner for Relative Importing

Completely changes the way the "from _ import _" statement to use relative importing
```python
import builtins, pathed; builtins.__import__ = pathed.new_import
```

Restore "from" statement
```
builtins.__import__ = pathed.old_import
```


# Quick Start On Normal Modules

Relative Importing
```python
import builtins, pathed
builtins.__import__ = pathed.new_import

from ....Destkop.new import *
# imports classes, functions, and variables from new.py
# new.py is up 3 directories, down 1 directory
# MUST use the word "from" in order to do relative importing

import directory.lambda
# this uses the normal import statement because 
# there's no "from" keyword in the beginning

builtins.__import__ = pathed.old_import
# use the "from" keyword normally after this
```


Importing files, folders, and adding to paths should be easy
```python
from pathed import cwd, importfile, importdir

# import file or directory to variable
name = importfile(cwd/'..'/'..'/'name.py')

dirname = importdir(cwd/'..'/'..')

path = cwd/2/3+'.txt' # accepts objects that can be converted into string

cwd.find(*.txt) # lists all text files in cwd
```

You can also import an entire directory into the namespace. Convenient, but not really recommended.
```python
importfile(cwd/'..'/'..', sys.modules[__name__])
importdir(cwd/'..'/'..', sys.modules[__name__])
```

For pathing, I recommend using "filedir", the path to the current file directory, since cwd changes frequently within large projects
```python
from pathed import filedir

filedir/'..'/'path'/'to'/'file.txt'
```
---
# Methods

### filedir
Returns your current file directory as a str-like object
```python
from pathed import filedir

print(filedir) # prints current file directory
```

### cwd
Returns your current working directory as a str-like object
```python
from pathed import cwd

print(cwd) # prints current working directory
```

### new_import()
Replaces the builtins.\__import__ statment, this allows for normal import syntax but with relative imports

Caveats:
- runs \__init__.py if folder is imported
- runs \__init__.py if file is in the same folder as \__init__.py
- only the "from _ import _" statement is overidden
- only *.py files are imported
- directories are not recursively added
- if directories are added in the \__init__.py file, directories are added to namespace

Dot notation:
- go up n-1 folders, with n representing the number of dots

```python
from ......spicy import *
# goes up 5 folders then down one folder called spicy

from ......spicy.file import * 
# import file.py from spicy folder

from .here import *
# imports file here.py from the same directory as file
# same as:
from here import *

# name of directory or file is needed
# this is NOT possible at the moment
from .... import jalapeño
# this just imports everthing from cwd
from . import bell
# this is the right way to do it
from .pepper_file import ghost_module
```


### importfile(path, module)
Parameters:
 - path: str or str-like object with path to directory
 - module: module that will have attributes appended to it

Returns file functions, classes, and global variables from a python file
```python
from pathed import importfile

hard_to_import_file = importfile(cwd/'..'/'..'/'file.py')
```

### importdir(path, module)
Parameters:
 - path: str or str-like object with path to directory
 - module: module that will have attributes appended to it

Imports *.py files from directory

Returns class with attributes named after *.py files
```python
from pathed import importdir

hard_to_import_dir = importdir(cwd/'..'/'..')
```

### Path(*args, custom)
Parameters:
 - *args: objects that can be turned into a string
 - custom: boolean
           if True, will append args to root
           if False, will append args to current file directory
```python
from pathed import Path

Path('a')              # /path/to/filedir/a
Path('a', custom=True) # /a
```

---
# Summary of path operations
```python
# dir ops
Path.isdir()
Path.mkdir()
Path.rmdir()
Path.copydir()

# file ops
Path.isfile()
Path.mkfile()
Path.rmfile()
Path.copyfile()

# path ops
Path.branch()
Path.leaf()
Path.add()
Path.ls()
Path.up()
Path.find()
Path.string()
Path.exists()
Path.splitpath()

# additional ops
Path.write()
Path.read()
Path.readfast()
Path.move()
```
---

### Path.isdir()
returns True if Path is a directory
```python
from pathed import cwd

cwd.isdir() # returns True
```

### Path.mkdir()
makes a directory called Path, throws error if Path is already a directory
```python
from pathed import cwd

cwd.add('new_directory').mkdir()
```

### Path.rmdir()
removes Path if Path is a directory
```python
from pathed import cwd

new_dir = cwd/'new_directory'
new_dir.mkdir()
new_dir.rmdir()
```

### Path.copydir(destination)
copies Path to destination if Path is a directory, returns destination as Path
```python
from pathed import cwd

a = cwd/'a'
b = cwd/'b'
a.copydir(b/'a')
# copies directory a and places into directory b
```

### Path.isfile(path)
returns True if Path is a file
```python
from pathed import cwd

cwd.isfile() # returns false
```


### Path.mkfile()
mkfile(data) writes data to Path, throws error if Path does not exist

mkfile(data, 'w') write data, makes file if Path does not exist
mkfile(data, 'wb') writes bytes data to Path
mkfile(data, 'a') appends data to Path
```python
from pathed import cwd

cwd.add('new.txt').mkfile('hello world')
```

### Path.rmfile()
removes Path if Path is a file
```python
from pathed import cwd

textfile = cwd.add('new.txt')
textfile.mkfile('goodbye world')
textfile.rmfile()
```

### Path.copyfile(destination)
copies Path to destination if Path is a file, returns destination as Path
```python
from pathed import cwd

textfile = cwd.add('a.txt')
textfile.mkfile('hello world')
textfile.copyfile(textfile/'..'/'b.txt')
# copies a.txt and pastes it in the same directory as b.txt
```

### Path.branch()
/absolute/path/to/leaf -> returns branch
```python
from pathed import cwd

text_file = cwd.add('blank.txt').mkfile()
text_file.branch() # returns cwd
```

### Path.leaf()
/absolute/path/to/leaf -> returns leaf
```python
from pathed import cwd

text_file = cwd.add('blank.txt').mkfile()
text_file.branch() # returns 'blank.txt'
```

### Path.add(*args)
does the same thing as cwd/'path'/'to'/'wonderland'
```python
from os import cwd

# These should give the same output
cwd.add('path').add('to').add('wonderland')
cwd/'path'/'to'/'wonderland'
```

### Path.ls()
returns [str, str, ...] of files and directories in Path

if full=True, returns [Path, Path, ...] of absolute Paths

throws error if Path doesn't exist
```python
from pathed import cwd

cwd.ls() # lists files and directories in cwd
```

### Path.up(num)
goes up the directory 'num' times

returns Path
```python
from pathed import cwd

b = cwd/'a'/b'

b.up(1) # cwd/a
b.up(2) # cwd
```

### Path.find()
find('*.py') returns [Path, Path, ...] in current Path that have the .py extension

find('**.py') returns [Path, Path, ...] in current Path and subdirectories that have the .py extension
```python
from pathed import cwd

cwd.find(*.py) # returns list of *.py files
```

### Path.string()
useful for printing raw Windows paths

\\this\\is\\a\\windows\\path

### Path.exists()
returns True if the Path exists
```python
from pathed import cwd

cwd.exists() # should return True
```

### Path.splitpath()
/absolute/path/to/leaf -> returns [branch, leaf]

print(branch) # /absolute/path/to
print(leaf)   # leaf

if full=True, returns [absolute, path, to, leaf]
```python
from pathed import cwd

a = cwd/'a'
a.splitpath()
# returns ['path/to/cwd', 'a']
a.splitpath(full=True)
# returns ['path','to','cwd','a']
```

### Path.write()
write(data) writes data to Path, throws error if Path does not exist

write(data, 'w') write data, makes file if Path does not exist
write(data, 'wb') writes bytes data to Path
write(data, 'a') appends data to Path
```python
from pathed import cwd

cwd.add('new.txt').write('hello world')
```

### Path.read()
read() returns text of Path if Path is a file

read('rb') returns text of byte file if Path is a file
```python
from pathed import cwd

textfile = cwd.add('new.txt')
textfile.mkfile('hello world')
textfile.read() # hello world
```

### Path.readfast()
good for reading the first few of lines of a VERY LARGE file

returns generator for reading large files one line at a time

file_text = Path.readfast()
next(file_text) to get string of next file, throws StopIteration Error at end of file
```python
from pathed import cwd

textfile = cwd/'new.txt'
textfile.mkfile(data='hello world')
file_gen = textfile.readfast()
next(file_gen) # hello world
```

### Path.move()
moves Path to destination, returns destination as Path

---

# TODO:
 - Better documentation
 - Unit tests