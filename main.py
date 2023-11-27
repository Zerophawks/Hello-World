# generated by fastapi-codegen:
#   filename:  score.yaml
#   timestamp: 2023-11-27T07:22:34+00:00

from __future__ import annotations

from typing import List

from fastapi import FastAPI, Path

from .models import Score

app = FastAPI(
    title='Game Scores API',
    description='API for tracking game scores.',
    version='1.0.0',
    servers=[{'url': 'http://35.163.187.47'}],
)


@app.get('/scores', response_model=List[Score])
def get_scores() -> List[Score]:
    """
    Get a list of scores
    """
    pass


@app.post('/scores', response_model=None)
def post_scores(body: Score) -> None:
    """
    Create a new score
    """
    pass


@app.get('/scores/{userId}', response_model=Score)
def get_scores_user_id(user_id: str = Path(..., alias='userId')) -> Score:
    """
    Get a score by user ID
    """
    pass


@app.put('/scores/{userId}', response_model=None)
def put_scores_user_id(
    user_id: str = Path(..., alias='userId'), body: Score = ...
) -> None:
    """
    Update a score for a specific user
    """
    pass


@app.delete('/scores/{userId}', response_model=None)
def delete_scores_user_id(user_id: str = Path(..., alias='userId')) -> None:
    """
    Delete a score for a specific user
    """
    pass
