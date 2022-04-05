from __init__ import Path

print(Path("/a/b", "/a/b", custom=True))

a = Path("a", custom=True)
b = a / "b"
print(str(b / b))


print(b / ".." / ".." / "a" / "b")
print(a / ".." / ".." / "..")
print(b / ".." / ".." / ".." / ".." / ".." / "..")


from __init__ import cwd

print(cwd / "*egg-info")

assert cwd / "*egg-info" == Path(cwd + "/*egg-info")

try:
    cwd / "*md"
except RuntimeError as e:
    print(e)


from __init__ import Path

print(Path("/a/b/c"))
