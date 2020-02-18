# **Python Cool Stuff**

![downloads](https://img.shields.io/github/downloads/atom/atom/total.svg)
![build](https://img.shields.io/appveyor/ci/:user/:repo.svg)
![chat](https://img.shields.io/discord/:serverId.svg)

## Table of Contents

- [Multiline Comment](https://github.com/garbagego/python/blob/master/pydoc/README.md#multiline-comments-in-python)
- [Decorator](https://www.datacamp.com/community/tutorials/decorators-python)
- [Docstring](https://www.datacamp.com/community/tutorials/docstrings-python)
- [Reverse string](https://dbader.org/blog/python-reverse-string)

## Multiline comments in Python

I have seen for multiline comment one should use """triple quotes""". This is wrong. Python only has one way of doing comments and that is using #

Triple quotes are treated as regular strings with the exception that they can span multiple lines. By regular strings I mean that if they are not assigned to a variable they will be immediately garbage collected as soon as that code executes. hence are not ignored by the interpreter in the same way that #a comment is.

The only exception to the garbage collection fact is when they are placed immediately after a function or class definition or on top of a module, in which case they are called docstrings and made available via the special variable myobj.__doc__.

Due to the existance of docstrings I've seen a lot of people confused about the use of """ elsewhere.

I suggest that the multiline comment lesson is removed or replaced with the instructions from the official PEP8 - [Block comments section.](http://www.python.org/dev/peps/pep-0008/#block-comments)

### Decorator


