from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Archive(_message.Message):
    __slots__ = ["busqueda"]
    BUSQUEDA_FIELD_NUMBER: _ClassVar[int]
    busqueda: str
    def __init__(self, busqueda: _Optional[str] = ...) -> None: ...

class TransactionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
