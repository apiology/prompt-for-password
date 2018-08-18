from typing import Optional, Union


def cap_enter() -> bool:
    ...


def disallow_swap() -> bool:
    ...


def disallow_core_dumps() -> bool:
    ...


def zero(s: str) -> bool:
    ...


def drop_privileges(username: Optional[str]=None, groupname: Optional[str]=None) -> bool:
    ...


def goodrandom(size: int=64) -> Union[bool, bytes]:
    ...
