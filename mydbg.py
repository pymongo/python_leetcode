"""
https://github.com/tylerwince/pydbg
Rust dbg! macro alternative in Python3
"""
import inspect
import sys
import typing
import os

_ExpType = typing.TypeVar('_ExpType')


def dbg(exp: _ExpType) -> _ExpType:
    """
    改写pydbg的dbg方法，原方法文件名打印的是绝对路径，太长了影响阅读
    """
    for frame in inspect.stack():
        line = frame.code_context[0]
        if "dbg" in line:
            start = line.find('(') + 1
            end = line.rfind(')')
            if end == -1:
                end = len(line)
            # os.path.basename(frame.filename)
            print(
                f"[line:{frame.lineno}] {line[start:end]} = {exp!r}",
                file=sys.stderr,
            )
            break

    return exp
