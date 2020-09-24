from datetime import datetime
from typing import List, Any

from .user import User


class Comment:

    def __init__(
        self,
        by_id: int,
        by: User,
        id: int,
        parent_id: int,
        parent: Any,
        kids_ids: List[int],
        kids: List[Any],
        text: str,
        time: datetime,
        type: str
    ):
        self.by_id = by_id
        self.by = by
        self.id = id
        self.parent_id = parent_id
        self.parent = parent
        self.kids_ids = kids_ids
        self.kids = kids
        self.text = text
        self.time = time
        self.type = type
