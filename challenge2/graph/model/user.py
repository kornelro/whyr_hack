from dataclasses import dataclass
from typing import List, Any
# from .comment import Comment


@dataclass
class User:
    name: str
    comments_ids: List[int]
    # comments: List[Comment]
    comments: List[Any]
