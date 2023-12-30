from dataclasses import dataclass


@dataclass
class INewUser:
    id: str
    mention: str
