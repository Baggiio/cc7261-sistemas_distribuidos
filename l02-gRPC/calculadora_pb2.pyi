from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MsgCliente(_message.Message):
    __slots__ = ("operacao", "numero1", "numero2")
    OPERACAO_FIELD_NUMBER: _ClassVar[int]
    NUMERO1_FIELD_NUMBER: _ClassVar[int]
    NUMERO2_FIELD_NUMBER: _ClassVar[int]
    operacao: int
    numero1: float
    numero2: float
    def __init__(self, operacao: _Optional[int] = ..., numero1: _Optional[float] = ..., numero2: _Optional[float] = ...) -> None: ...

class MsgServidor(_message.Message):
    __slots__ = ("resultado",)
    RESULTADO_FIELD_NUMBER: _ClassVar[int]
    resultado: float
    def __init__(self, resultado: _Optional[float] = ...) -> None: ...
