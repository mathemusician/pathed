import os
from pathed import Path, cwd
from util import temp_folder_with_files


file_name = __file__
directory = file_name.split(os.path.sep)[:-1]
directory = os.path.sep.join(directory)


def test_common_operations():
    assert str(Path("/a/b", "/a/b", custom=True)) == "/a/b/a/b"

    a = Path("a", custom=True)
    b = a / "b"
    assert str(b / b) == "/a/b/a/b"

    assert str(b / ".." / ".." / "a" / "b") == "/a/b"
    assert str(a / ".." / ".." / "..") == "/."
    assert str(b / ".." / ".." / ".." / ".." / ".." / "..") == "/."

    assert str(cwd / "*md") == str(Path(cwd + os.path.sep + "*md"))

    with pytest.raises(RuntimeError):
        cwd / "*.py"

    assert str(Path("/a/b/c")) == "/a/b/c"
