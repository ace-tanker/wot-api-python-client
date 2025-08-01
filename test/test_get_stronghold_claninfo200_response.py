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

from wot_api_client.models.get_stronghold_claninfo200_response import GetStrongholdClaninfo200Response

class TestGetStrongholdClaninfo200Response(unittest.TestCase):
    """GetStrongholdClaninfo200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetStrongholdClaninfo200Response:
        """Test GetStrongholdClaninfo200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetStrongholdClaninfo200Response`
        """
        model = GetStrongholdClaninfo200Response()
        if include_optional:
            return GetStrongholdClaninfo200Response(
                status = 'error',
                meta = wot_api_client.models.stronghold_claninfo_meta.stronghold_claninfo_meta(
                    count = 56, ),
                data = {
                    'key' : wot_api_client.models.stronghold_claninfo_data_value.stronghold_claninfo_data_value(
                        clan_id = 56, 
                        clan_name = '', 
                        clan_tag = '', 
                        stronghold_level = 56, 
                        stronghold_buildings_level = 56, 
                        command_center_arena_id = '', 
                        building_slots = [
                            wot_api_client.models.stronghold_claninfo_data_value_building_slots_inner.stronghold_claninfo_data_value_building_slots_inner(
                                position = '', 
                                direction = '', 
                                arena_id = '', 
                                building_title = '', 
                                building_level = 56, 
                                reserve_title = '', )
                            ], 
                        skirmish_statistics = wot_api_client.models.stronghold_claninfo_data_value_skirmish_statistics.stronghold_claninfo_data_value_skirmish_statistics(
                            total_10 = 56, 
                            win_10 = 56, 
                            lose_10 = 56, 
                            total_8 = 56, 
                            win_8 = 56, 
                            lose_8 = 56, 
                            total_6 = 56, 
                            win_6 = 56, 
                            lose_6 = 56, 
                            total_10_in_28d = 56, 
                            win_10_in_28d = 56, 
                            total_8_in_28d = 56, 
                            win_8_in_28d = 56, 
                            total_6_in_28d = 56, 
                            win_6_in_28d = 56, 
                            last_time_10 = 56, 
                            last_time_8 = 56, 
                            last_time_6 = 56, ), 
                        battles_for_strongholds_statistics = wot_api_client.models.stronghold_claninfo_data_value_battles_for_strongholds_statistics.stronghold_claninfo_data_value_battles_for_strongholds_statistics(
                            total_10 = 56, 
                            win_10 = 56, 
                            lose_10 = 56, 
                            total_10_in_28d = 56, 
                            win_10_in_28d = 56, 
                            last_time_10 = 56, ), 
                        battles_series_for_strongholds_statistics = wot_api_client.models.stronghold_claninfo_data_value_battles_series_for_strongholds_statistics.stronghold_claninfo_data_value_battles_series_for_strongholds_statistics(
                            total_10 = 56, 
                            win_10 = 56, 
                            lose_10 = 56, 
                            total_10_in_28d = 56, 
                            win_10_in_28d = 56, ), )
                    },
                error = wot_api_client.models.error.error()
            )
        else:
            return GetStrongholdClaninfo200Response(
                status = 'error',
                meta = wot_api_client.models.stronghold_claninfo_meta.stronghold_claninfo_meta(
                    count = 56, ),
                data = {
                    'key' : wot_api_client.models.stronghold_claninfo_data_value.stronghold_claninfo_data_value(
                        clan_id = 56, 
                        clan_name = '', 
                        clan_tag = '', 
                        stronghold_level = 56, 
                        stronghold_buildings_level = 56, 
                        command_center_arena_id = '', 
                        building_slots = [
                            wot_api_client.models.stronghold_claninfo_data_value_building_slots_inner.stronghold_claninfo_data_value_building_slots_inner(
                                position = '', 
                                direction = '', 
                                arena_id = '', 
                                building_title = '', 
                                building_level = 56, 
                                reserve_title = '', )
                            ], 
                        skirmish_statistics = wot_api_client.models.stronghold_claninfo_data_value_skirmish_statistics.stronghold_claninfo_data_value_skirmish_statistics(
                            total_10 = 56, 
                            win_10 = 56, 
                            lose_10 = 56, 
                            total_8 = 56, 
                            win_8 = 56, 
                            lose_8 = 56, 
                            total_6 = 56, 
                            win_6 = 56, 
                            lose_6 = 56, 
                            total_10_in_28d = 56, 
                            win_10_in_28d = 56, 
                            total_8_in_28d = 56, 
                            win_8_in_28d = 56, 
                            total_6_in_28d = 56, 
                            win_6_in_28d = 56, 
                            last_time_10 = 56, 
                            last_time_8 = 56, 
                            last_time_6 = 56, ), 
                        battles_for_strongholds_statistics = wot_api_client.models.stronghold_claninfo_data_value_battles_for_strongholds_statistics.stronghold_claninfo_data_value_battles_for_strongholds_statistics(
                            total_10 = 56, 
                            win_10 = 56, 
                            lose_10 = 56, 
                            total_10_in_28d = 56, 
                            win_10_in_28d = 56, 
                            last_time_10 = 56, ), 
                        battles_series_for_strongholds_statistics = wot_api_client.models.stronghold_claninfo_data_value_battles_series_for_strongholds_statistics.stronghold_claninfo_data_value_battles_series_for_strongholds_statistics(
                            total_10 = 56, 
                            win_10 = 56, 
                            lose_10 = 56, 
                            total_10_in_28d = 56, 
                            win_10_in_28d = 56, ), )
                    },
                error = wot_api_client.models.error.error(),
        )
        """

    def testGetStrongholdClaninfo200Response(self):
        """Test GetStrongholdClaninfo200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
