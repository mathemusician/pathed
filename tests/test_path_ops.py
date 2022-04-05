import os
from pathed import Path, cwd
from util import temp_folder_with_files


file_name = __file__
directory = file_name.split(os.path.sep)[:-1]
directory = os.path.sep.join(directory)


def test_common_operations():
    print(Path('/a/b', '/a/b', custom=True))

    a = Path('a', custom=True)
    b = a/'b'
    assert str(b/b) == "/a/b/a/b"

    assert str(b/".."/".."/"a"/"b") == "/a/b"
    assert str(a/".."/".."/"..") == "/."
    assert str(b/".."/".."/".."/".."/".."/"..") == "/."

    #assert str(cwd/"*path_ops") == 
    try:
        cwd/"*md"
    except RuntimeError as e:
        print(e)

    assert str(Path("/a/b/c")) == "/a/b/c"
