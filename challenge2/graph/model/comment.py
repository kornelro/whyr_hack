from dataclasses import dataclass
from datetime import datetime
from typing import List, Any

from .user import User


@dataclass
class Comment:
    by_id: int
    by: User
    id: int
    parent_id: int
    parent: Any
    kids_ids: List[int]
    kids: List[Any]
    text: str
    time: datetime
    type: str
