import os
import pytest
from pathed import Path, cwd
from util import temp_folder_with_files


file_name = __file__
directory = file_name.split(os.path.sep)[:-1]
directory = Path(os.path.sep.join(directory))


def test_common_operations():
    assert str(Path("/a/b", "/a/b", custom=True)) == "/a/b/a/b"

    a = Path("a", custom=True)
    assert str(a / a) == "/a/a"
    b = a / "b"
    assert str(b / b) == "/a/b/a/b"

    assert str(b / ".." / ".." / "a" / "b") == "/a/b"
    assert str(a / ".." / ".." / "..") == "/."
    assert str(b / ".." / ".." / ".." / ".." / ".." / "..") == "/."

    assert str(directory / "*md") == str(Path(directory + os.path.sep + "*md"))

    with pytest.raises(RuntimeError):
        directory / "*.py"

    assert str(Path("/a/b/c")) == "/a/b/c"
