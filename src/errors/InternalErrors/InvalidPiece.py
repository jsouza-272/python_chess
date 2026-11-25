from .InternalError import InternalError


class InvalidPiece(InternalError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
