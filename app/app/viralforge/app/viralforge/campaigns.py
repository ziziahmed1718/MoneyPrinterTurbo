from typing import Dict, List
from uuid import uuid4

from .schemas import Campaign, CampaignCreate, Idea
from .strategy import create_strategy
from .scoring import rank_ideas


class CampaignManager:
    """
    Manage ViralForge campaigns.

    The manager orchestrates strategy generation and idea scoring.
    """

    def __init__(self) -> None:
        self._campaigns: Dict[str, Campaign] = {}

    def create_campaign(self, data: CampaignCreate) -> Campaign:
        """Create and store a new campaign."""

        campaign_id = str(uuid4())

        campaign = Campaign(
            id=campaign_id,
            name=data.name,
            topic=data.topic,
            audience=data.audience,
            platform=data.platform,
            tone=data.tone,
            language=data.language,
            duration_seconds=data.duration_seconds,
        )

        self._campaigns[campaign_id] = campaign

        return campaign

    def get_campaign(self, campaign_id: str) -> Campaign | None:
        """Return a campaign by ID."""

        return self._campaigns.get(campaign_id)

    def generate_ideas(
        self,
        campaign_id: str,
        count: int | None = None,
    ) -> List[Idea]:
        """Generate and score ideas for a campaign."""

        campaign = self.get_campaign(campaign_id)

        if campaign is None:
            raise ValueError("Campaign not found")

        campaign_data = CampaignCreate(
            name=campaign.name,
            topic=campaign.topic,
            audience=campaign.audience,
            platform=campaign.platform,
            tone=campaign.tone,
            language=campaign.language,
            duration_seconds=campaign.duration_seconds,
            ideas_count=count or 20,
        )

        ideas = create_strategy(
            campaign=campaign_data,
            count=count,
        )

        ranked_ideas = rank_ideas(
            ideas,
            limit=5,
        )

        campaign.ideas = ranked_ideas

        return ranked_ideas


campaign_manager = CampaignManager()
