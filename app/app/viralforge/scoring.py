from typing import List

from .schemas import Idea


def calculate_score(idea: Idea) -> float:
    """
    Calculate the ViralForge priority score.

    This score is used to prioritize ideas for production.
    It is not a prediction or guarantee of virality.
    """

    score = (
        idea.hook_score * 0.30
        + idea.audience_score * 0.20
        + idea.curiosity_score * 0.15
        + idea.emotion_score * 0.15
        + idea.trend_score * 0.10
        + idea.cta_score * 0.10
    )

    return round(score, 2)


def score_idea(idea: Idea) -> Idea:
    """Calculate and update an idea's overall score."""

    idea.score = calculate_score(idea)
    return idea


def rank_ideas(ideas: List[Idea], limit: int = 5) -> List[Idea]:
    """
    Score and rank ideas from highest to lowest.

    Only the best ideas should continue to the expensive
    script/video generation stages.
    """

    scored_ideas = [score_idea(idea) for idea in ideas]

    return sorted(
        scored_ideas,
        key=lambda idea: idea.score,
        reverse=True,
    )[:limit]
