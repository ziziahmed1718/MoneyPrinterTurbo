from typing import List

from fastapi import APIRouter, HTTPException

from .campaigns import campaign_manager
from .schemas import Campaign, CampaignCreate, Idea


router = APIRouter(
    prefix="/api/v1/viralforge",
    tags=["ViralForge"],
)


@router.post(
    "/campaigns",
    response_model=Campaign,
)
def create_campaign(data: CampaignCreate) -> Campaign:
    """Create a new ViralForge campaign."""

    return campaign_manager.create_campaign(data)


@router.get(
    "/campaigns/{campaign_id}",
    response_model=Campaign,
)
def get_campaign(campaign_id: str) -> Campaign:
    """Get a ViralForge campaign."""

    campaign = campaign_manager.get_campaign(campaign_id)

    if campaign is None:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found",
        )

    return campaign


@router.post(
    "/campaigns/{campaign_id}/ideas",
    response_model=List[Idea],
)
def generate_campaign_ideas(
    campaign_id: str,
) -> List[Idea]:
    """Generate and rank ideas for a campaign."""

    try:
        return campaign_manager.generate_ideas(
            campaign_id=campaign_id,
        )

    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found",
        )
