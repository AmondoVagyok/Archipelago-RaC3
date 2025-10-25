from Rac3Addresses import RAC3ITEM, RAC3REGION
from worlds.rac3.test import RAC3TestBase


class TestBiobliterator(RAC3TestBase):

    def test_logic(self):
        state = self.multiworld.state
        self.assertTrue(self.can_reach_region(RAC3REGION.VELDIN), "Can't start on Veldin")
        self.assertFalse(self.can_reach_region(RAC3REGION.FLORANA), "Florana reachable without coordinates")
        self.assertFalse(self.can_reach_region(RAC3REGION.STARSHIP_PHOENIX),
                         "Starship Phoenix reachable without coordinates")
        self.assertFalse(self.can_reach_region(RAC3REGION.COMMAND_CENTER), "Command Center reachable from Veldin")
        self.assertFalse(self.can_reach_location("Command Center: Biobliterator Defeated!"),
                         "Goal reachable from Veldin")

        state.sweep_for_advancements()
        self.assertTrue(self.can_reach_region(RAC3REGION.FLORANA), "Can't reach Florana from Veldin")
        self.assertTrue(self.can_reach_region(RAC3REGION.STARSHIP_PHOENIX), "Can't reach Starship Phoenix from Veldin")
        self.assertFalse(self.can_reach_region(RAC3REGION.COMMAND_CENTER), "Command Center reachable from Florana")
        self.assertFalse(self.can_reach_location("Command Center: Biobliterator Defeated!"),
                         "Goal reachable from Florana")

        self.collect_by_name(RAC3ITEM.COMMAND_CENTER)
        self.assertTrue(self.can_reach_region(RAC3REGION.COMMAND_CENTER), "Can't reach Command Center with coordinates")
        self.assertFalse(self.can_reach_location("Command Center: Biobliterator Defeated!"),
                         "Goal reachable with no items")

        self.collect_by_name([RAC3ITEM.HYPERSHOT, RAC3ITEM.GRAV_BOOTS, RAC3ITEM.TYHRRA_GUISE, RAC3ITEM.HACKER,
                              RAC3ITEM.REFRACTOR])
        self.assertTrue(self.can_reach_location("Command Center: Biobliterator Defeated!"),
                        "Goal not reachable with items")
