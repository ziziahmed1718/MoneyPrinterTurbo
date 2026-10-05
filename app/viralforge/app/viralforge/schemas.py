from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Platform(str, Enum):
    TIKTOK = "tiktok"
    YOUTUBE_SHORTS = "youtube_shorts"
    INSTAGRAM_REELS = "instagram_reels"


class ContentTone(str, Enum):
    EDUCATIONAL = "educational"
    ENTERTAINING = "entertaining"
    INSPIRATIONAL = "inspirational"
    CONTROVERSIAL = "controversial"
    STORYTELLING = "storytelling"


class CampaignCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    topic: str = Field(..., min_length=1, max_length=500)
    audience: str = Field(..., min_length=1, max_length=500)

    platform: Platform = Platform.TIKTOK
    tone: ContentTone = ContentTone.EDUCATIONAL

    language: str = "en"
    duration_seconds: int = Field(default=30, ge=15, le=180)

    ideas_count: int = Field(default=20, ge=5, le=100)
    videos_count: int = Field(default=3, ge=1, le=5)


class Idea(BaseModel):
    id: str
    hook: str
    angle: str
    topic: str

    emotion: Optional[str] = None
    cta: Optional[str] = None

    score: float = Field(default=0, ge=0, le=100)

    hook_score: float = Field(default=0, ge=0, le=100)
    audience_score: float = Field(default=0, ge=0, le=100)
    curiosity_score: float = Field(default=0, ge=0, le=100)
    emotion_score: float = Field(default=0, ge=0, le=100)
    trend_score: float = Field(default=0, ge=0, le=100)
    cta_score: float = Field(default=0, ge=0, le=100)


class Script(BaseModel):
    id: str
    idea_id: str

    title: str
    hook: str
    body: str
    cta: str

    duration_seconds: int = Field(..., ge=15, le=180)


class Campaign(BaseModel):
    id: str
    name: str
    topic: str
    audience: str

    platform: Platform
    tone: ContentTone
    language: str

    duration_seconds: int

    ideas: List[Idea] = Field(default_factory=list)
    scripts: List[Script] = Field(default_factory=list)
