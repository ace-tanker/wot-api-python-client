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

from wot_api_client.models.clans_memberhistory_ok import ClansMemberhistoryOk

class TestClansMemberhistoryOk(unittest.TestCase):
    """ClansMemberhistoryOk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClansMemberhistoryOk:
        """Test ClansMemberhistoryOk
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClansMemberhistoryOk`
        """
        model = ClansMemberhistoryOk()
        if include_optional:
            return ClansMemberhistoryOk(
                status = 'ok',
                meta = wot_api_client.models.clans_memberhistory_meta.clans_memberhistory_meta(
                    count = 56, ),
                data = {
                    'key' : [
                        wot_api_client.models.clans_memberhistory_data_value_inner.clans_memberhistory_data_value_inner(
                            account_id = 56, 
                            clan_id = 56, 
                            joined_at = 56, 
                            left_at = 56, 
                            role = '', )
                        ]
                    }
            )
        else:
            return ClansMemberhistoryOk(
                status = 'ok',
                meta = wot_api_client.models.clans_memberhistory_meta.clans_memberhistory_meta(
                    count = 56, ),
                data = {
                    'key' : [
                        wot_api_client.models.clans_memberhistory_data_value_inner.clans_memberhistory_data_value_inner(
                            account_id = 56, 
                            clan_id = 56, 
                            joined_at = 56, 
                            left_at = 56, 
                            role = '', )
                        ]
                    },
        )
        """

    def testClansMemberhistoryOk(self):
        """Test ClansMemberhistoryOk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
