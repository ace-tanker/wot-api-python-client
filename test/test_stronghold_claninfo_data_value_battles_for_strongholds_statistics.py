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

from wot_api_client.models.stronghold_claninfo_data_value_battles_for_strongholds_statistics import StrongholdClaninfoDataValueBattlesForStrongholdsStatistics

class TestStrongholdClaninfoDataValueBattlesForStrongholdsStatistics(unittest.TestCase):
    """StrongholdClaninfoDataValueBattlesForStrongholdsStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StrongholdClaninfoDataValueBattlesForStrongholdsStatistics:
        """Test StrongholdClaninfoDataValueBattlesForStrongholdsStatistics
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StrongholdClaninfoDataValueBattlesForStrongholdsStatistics`
        """
        model = StrongholdClaninfoDataValueBattlesForStrongholdsStatistics()
        if include_optional:
            return StrongholdClaninfoDataValueBattlesForStrongholdsStatistics(
                total_10 = 56,
                win_10 = 56,
                lose_10 = 56,
                total_10_in_28d = 56,
                win_10_in_28d = 56,
                last_time_10 = 56
            )
        else:
            return StrongholdClaninfoDataValueBattlesForStrongholdsStatistics(
                total_10 = 56,
                win_10 = 56,
                lose_10 = 56,
                total_10_in_28d = 56,
                win_10_in_28d = 56,
                last_time_10 = 56,
        )
        """

    def testStrongholdClaninfoDataValueBattlesForStrongholdsStatistics(self):
        """Test StrongholdClaninfoDataValueBattlesForStrongholdsStatistics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
