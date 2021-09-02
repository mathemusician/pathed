# Why Use op?
Ever wanted to import a file that was hard to get? Or a whole directory of files? Ever get tired of changing the pathing when transferring a program from one computer to another? This modules helps with all that! Inspired by pathlib, os.path, shutil, and glob.

---

# Quick Start

Importing files, folders, and adding to paths should be easy
```
from op import cwd, importfile, importdir

# import file or directory to variable
hard_to_import_file = importfile(cwd/'..'/'..'/'file.py')
hard_to_import_dir = importdir(cwd/'..'/'..')

path = cwd/2/3+'.txt' # accepts objects that can be converted into string

cwd.find(*.txt) # lists all text files in cwd
```

You can also import an entire directory into the namespace. Convenient, but not really recommended. Let's keep this between you and me...
```
importfile(cwd/'..'/'..', sys.modules[__name__])
importdir(cwd/'..'/'..', sys.modules[__name__])
```

For pathing, I recommend using "filedir", the path to the current file directory, since cwd changes frequently within large projects
```
from op import filedir

filedir/'..'/'path'/'to'/'file.txt'
```
---
# Methods

### filedir

### cwd

### importfile

### importdir


### Path.isdir()
returns True if Path is a directory
```
from op import cwd

cwd.isdir() # returns True
```

### Path.mkdir()
makes a directory called Path, throws error if Path is already a directory
```
from op import cwd

cwd.add('new_directory').mkdir()
```

### Path.rmdir()
removes Path if Path is a directory
```
from op import cwd

new_dir = cwd/'new_directory'
new_dir.mkdir()
new_dir.rmdir()
```

### Path.copydir(destination)
copies Path to destination if Path is a directory, returns destination as Path
```
from op import cwd

a = cwd/'a'
b = cwd/'b'
a.copydir(b/'a')
# copies directory a and places into directory b
```

### Path.isfile(path)
returns True if Path is a file
```
from op import cwd

cwd.isfile() # returns false
```


### Path.mkfile()
mkfile(data) writes data to Path, throws error if Path does not exist

mkfile(data, 'w') write data, makes file if Path does not exist
mkfile(data, 'wb') writes bytes data to Path
mkfile(data, 'a') appends data to Path
```
from op import cwd

cwd.add('new.txt').mkfile('hello world')
```

### Path.rmfile()
removes Path if Path is a file
```
from op import cwd

textfile = cwd.add('new.txt')
textfile.mkfile('goodbye world')
textfile.rmfile()
```

### Path.copyfile(destination)
copies Path to destination if Path is a file, returns destination as Path
```
from op import cwd

textfile = cwd.add('a.txt')
textfile.mkfile('hello world')
textfile.copyfile(textfile/'..'/'b.txt')
# copies a.txt and pastes it in the same directory as b.txt
```

### Path.branch()
/absolute/path/to/leaf -> returns branch
```
from op import cwd

text_file = cwd.add('blank.txt').mkfile()
text_file.branch() # returns cwd
```

### Path.leaf()
/absolute/path/to/leaf -> returns leaf
```
from op import cwd

text_file = cwd.add('blank.txt').mkfile()
text_file.branch() # returns 'blank.txt'
```

### Path.add(*args)
does the same thing as cwd/'path'/'to'/'wonderland'
```
from os import cwd

# These should give the same output
cwd.add('path').add('to').add('wonderland')
cwd/'path'/'to'/'wonderland'
```

### Path.ls()
returns [str, str, ...] of files and directories in Path

if full=True, returns [Path, Path, ...] of absolute Paths

throws error if Path doesn't exist
```
from op import cwd

cwd.ls() # lists files and directories in cwd
```

### Path.up(num)
goes up the directory 'num' times

returns Path
```
from op import cwd

b = cwd/'a'/b'

b.up(1) # cwd/a
b.up(2) # cwd
```

### Path.find()
find('*.py') returns [Path, Path, ...] in current Path that have the .py extension

find('**.py') returns [Path, Path, ...] in current Path and subdirectories that have the .py extension
```
from op import cwd

cwd.find(*.py) # returns list of *.py files
```

### Path.string()
useful for printing raw Windows paths

\\this\\is\\a\\windows\\path

### Path.exists()
returns True if the Path exists
```
from op import cwd

cwd.exists() # should return True
```

### Path.splitpath()
/absolute/path/to/leaf -> returns [branch, leaf]

print(branch) # /absolute/path/to
print(leaf)   # leaf

if full=True, returns [absolute, path, to, leaf]
```
from op import cwd

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
```
from op import cwd

cwd.add('new.txt').write('hello world')
```

### Path.read()
read() returns text of Path if Path is a file

read('rb') returns text of byte file if Path is a file
```
from op import cwd

textfile = cwd.add('new.txt')
textfile.mkfile('hello world')
textfile.read() # hello world
```

### Path.readfast()
good for reading the first few of lines of a VERY LARGE file

returns generator for reading large files one line at a time

file_text = Path.readfast()
next(file_text) to get string of next file, throws StopIteration Error at end of file
```
from op import cwd

textfile = cwd.add('new.txt')
textfile.mkfile('hello world')
file_gen = textfile.readfast()
next(file_gen) # hello world
```

### Path.move()
moves Path to destination, returns destination as Path

---
# Summary of path operations
```
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

# TODO:
 - Better documentation
 - Unit tests