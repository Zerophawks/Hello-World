# generated by fastapi-codegen:
#   filename:  score.yaml
#   timestamp: 2023-11-27T07:22:34+00:00

from __future__ import annotations

from pydantic import BaseModel


class Score(BaseModel):
    user: str
    score: int
