# coding: utf-8

"""
    World of Tanks

    OpenAPI specification for the Wargaming.net Public API. The official Wargaming.net Public API documentation can be found at the Wargaming [Developer's room](https://developers.wargaming.net/).

    The version of the OpenAPI document: 1.0.0
    Contact: contact@ace-tanker.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wot_api_client.models.globalmap_provinces_data_inner_active_battles_inner_clan_a import GlobalmapProvincesDataInnerActiveBattlesInnerClanA

class TestGlobalmapProvincesDataInnerActiveBattlesInnerClanA(unittest.TestCase):
    """GlobalmapProvincesDataInnerActiveBattlesInnerClanA unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GlobalmapProvincesDataInnerActiveBattlesInnerClanA:
        """Test GlobalmapProvincesDataInnerActiveBattlesInnerClanA
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GlobalmapProvincesDataInnerActiveBattlesInnerClanA`
        """
        model = GlobalmapProvincesDataInnerActiveBattlesInnerClanA()
        if include_optional:
            return GlobalmapProvincesDataInnerActiveBattlesInnerClanA(
                clan_id = 56,
                win_elo_delta = 56,
                loose_elo_delta = 56,
                battle_reward = 56
            )
        else:
            return GlobalmapProvincesDataInnerActiveBattlesInnerClanA(
                clan_id = 56,
                win_elo_delta = 56,
                loose_elo_delta = 56,
                battle_reward = 56,
        )
        """

    def testGlobalmapProvincesDataInnerActiveBattlesInnerClanA(self):
        """Test GlobalmapProvincesDataInnerActiveBattlesInnerClanA"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
