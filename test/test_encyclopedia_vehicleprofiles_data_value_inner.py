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

from wot_api_client.models.encyclopedia_vehicleprofiles_data_value_inner import EncyclopediaVehicleprofilesDataValueInner

class TestEncyclopediaVehicleprofilesDataValueInner(unittest.TestCase):
    """EncyclopediaVehicleprofilesDataValueInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EncyclopediaVehicleprofilesDataValueInner:
        """Test EncyclopediaVehicleprofilesDataValueInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EncyclopediaVehicleprofilesDataValueInner`
        """
        model = EncyclopediaVehicleprofilesDataValueInner()
        if include_optional:
            return EncyclopediaVehicleprofilesDataValueInner(
                profile_id = '',
                tank_id = 56,
                is_default = True,
                price_credit = 56
            )
        else:
            return EncyclopediaVehicleprofilesDataValueInner(
                profile_id = '',
                tank_id = 56,
                is_default = True,
                price_credit = 56,
        )
        """

    def testEncyclopediaVehicleprofilesDataValueInner(self):
        """Test EncyclopediaVehicleprofilesDataValueInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
