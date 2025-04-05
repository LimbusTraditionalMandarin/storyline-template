# This file is part of ptsd project which is released under GNU GPL v3.0.
# Copyright (c) 2025- Limbus Traditional Mandarin

from dataclasses import dataclass, field
from enum import Enum

from anyio import Path as AnyioPath


class OperationType(Enum):
    ADD = "A"
    DELETE = "D"
    MODIFY = "M"


@dataclass
class FileOperation:
    op_type: OperationType
    full_path: str
    folder: str = field(init=False)
    filename: str = field(init=False)

    def __post_init__(self) -> None:
        path_obj = AnyioPath(self.full_path)
        self.folder = str(path_obj.parent) if path_obj.parent.name else ""
        self.filename = path_obj.name


@dataclass
class ProjectFile:
    id: int
    name: str
