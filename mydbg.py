import inspect
import sys
import typing

_ExpType = typing.TypeVar('_ExpType')


def dbg(exp: _ExpType) -> _ExpType:
    for frame in inspect.stack():
        line = frame.code_context[0]
        if "dbg" in line:
            start = line.find('(') + 1
            end = line.rfind(')')
            if end == -1:
                end = len(line)
            print(f"class={frame.filename.__class__}, type{frame.filename.__class__}")
            dir(frame.filename)
            print(
                f"[{frame.filename}:{frame.lineno}] {line[start:end]} = {exp!r}",
                file=sys.stderr,
            )
            break

    return exp
