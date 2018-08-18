from typing import Optional, Callable


class Pinentry:
    def __init__(self,
                 pinentry_path: str="pinentry",
                 fallback_to_getpass: bool=True) -> None:
        ...

    def ask(self,
            prompt: str="Enter the password: ",
            description: Optional[str]=None,
            error: str="Wrong password!",
            validator: Callable[[Optional[object]], bool]=
            lambda x: x is not None) -> str:
        ...

    def close(self) -> None:
        ...
