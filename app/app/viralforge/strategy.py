from typing import List

from .schemas import CampaignCreate, Idea


class StrategyEngine:
    """
    ViralForge strategy engine.

    Responsible for turning a campaign brief into content ideas.
    The actual LLM provider can be connected later.
    """

    def generate_ideas(
        self,
        campaign: CampaignCreate,
        count: int | None = None,
    ) -> List[Idea]:
        """
        Generate content ideas for a campaign.

        This MVP implementation creates deterministic placeholder
        ideas. The LLM provider will replace this logic later.
        """

        count = count or campaign.ideas_count

        ideas: List[Idea] = []

        for index in range(1, count + 1):
            ideas.append(
                Idea(
                    id=f"idea-{index}",
                    hook=f"The surprising truth about {campaign.topic} "
                         f"that most people don't know",
                    angle=(
                        f"Explain {campaign.topic} from a "
                        f"{campaign.tone.value} perspective"
                    ),
                    topic=campaign.topic,
                    emotion="curiosity",
                    cta="Follow for more",
                )
            )

        return ideas


def create_strategy(
    campaign: CampaignCreate,
    count: int | None = None,
) -> List[Idea]:
    """Convenience function for generating campaign ideas."""

    engine = StrategyEngine()

    return engine.generate_ideas(
        campaign=campaign,
        count=count,
    )
