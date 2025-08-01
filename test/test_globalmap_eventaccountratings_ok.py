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

from wot_api_client.models.globalmap_eventaccountratings_ok import GlobalmapEventaccountratingsOk

class TestGlobalmapEventaccountratingsOk(unittest.TestCase):
    """GlobalmapEventaccountratingsOk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GlobalmapEventaccountratingsOk:
        """Test GlobalmapEventaccountratingsOk
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GlobalmapEventaccountratingsOk`
        """
        model = GlobalmapEventaccountratingsOk()
        if include_optional:
            return GlobalmapEventaccountratingsOk(
                status = 'ok',
                meta = wot_api_client.models.globalmap_eventaccountratings_meta.globalmap_eventaccountratings_meta(
                    count = 56, 
                    page_total = 56, 
                    page = 56, ),
                data = [
                    wot_api_client.models.globalmap_eventaccountratings_data_inner.globalmap_eventaccountratings_data_inner(
                        event_id = '', 
                        account_id = 56, 
                        clan_id = 56, 
                        clan_rank = 56, 
                        battles = 56, 
                        battles_to_award = 56, 
                        award_level = '', 
                        updated_at = 56, 
                        fame_points = 56, 
                        fame_points_to_improve_award = 56, 
                        front_id = '', 
                        url = '', 
                        rank = 56, 
                        rank_delta = 56, )
                    ]
            )
        else:
            return GlobalmapEventaccountratingsOk(
                status = 'ok',
                meta = wot_api_client.models.globalmap_eventaccountratings_meta.globalmap_eventaccountratings_meta(
                    count = 56, 
                    page_total = 56, 
                    page = 56, ),
                data = [
                    wot_api_client.models.globalmap_eventaccountratings_data_inner.globalmap_eventaccountratings_data_inner(
                        event_id = '', 
                        account_id = 56, 
                        clan_id = 56, 
                        clan_rank = 56, 
                        battles = 56, 
                        battles_to_award = 56, 
                        award_level = '', 
                        updated_at = 56, 
                        fame_points = 56, 
                        fame_points_to_improve_award = 56, 
                        front_id = '', 
                        url = '', 
                        rank = 56, 
                        rank_delta = 56, )
                    ],
        )
        """

    def testGlobalmapEventaccountratingsOk(self):
        """Test GlobalmapEventaccountratingsOk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
