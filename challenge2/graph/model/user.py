from typing import List, Any
# from .comment import Comment


class User:

    def __init__(
        self,
        name: str,
        comments_ids: List[int],
        # comments: List[Comment]
        comments: List[Any]
    ):
        self.name = name
        self.comments_ids = comments_ids
        self.comments = comments
