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

from wot_api_client.models.encyclopedia_achievements_data_value_options_inner import EncyclopediaAchievementsDataValueOptionsInner

class TestEncyclopediaAchievementsDataValueOptionsInner(unittest.TestCase):
    """EncyclopediaAchievementsDataValueOptionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EncyclopediaAchievementsDataValueOptionsInner:
        """Test EncyclopediaAchievementsDataValueOptionsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EncyclopediaAchievementsDataValueOptionsInner`
        """
        model = EncyclopediaAchievementsDataValueOptionsInner()
        if include_optional:
            return EncyclopediaAchievementsDataValueOptionsInner(
                name_i18n = '',
                image = '',
                image_big = '',
                nation_images = wot_api_client.models.encyclopedia_achievements_data_value_options_inner_nation_images.encyclopedia_achievements_data_value_options_inner_nation_images(
                    x71 = {
                        'key' : ''
                        }, 
                    x85 = {
                        'key' : ''
                        }, 
                    x180 = {
                        'key' : ''
                        }, ),
                description = ''
            )
        else:
            return EncyclopediaAchievementsDataValueOptionsInner(
                name_i18n = '',
                image = '',
                image_big = '',
                nation_images = wot_api_client.models.encyclopedia_achievements_data_value_options_inner_nation_images.encyclopedia_achievements_data_value_options_inner_nation_images(
                    x71 = {
                        'key' : ''
                        }, 
                    x85 = {
                        'key' : ''
                        }, 
                    x180 = {
                        'key' : ''
                        }, ),
                description = '',
        )
        """

    def testEncyclopediaAchievementsDataValueOptionsInner(self):
        """Test EncyclopediaAchievementsDataValueOptionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
