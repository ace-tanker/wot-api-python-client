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

from wot_api_client.models.activateclanreserve200_response import Activateclanreserve200Response

class TestActivateclanreserve200Response(unittest.TestCase):
    """Activateclanreserve200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Activateclanreserve200Response:
        """Test Activateclanreserve200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Activateclanreserve200Response`
        """
        model = Activateclanreserve200Response()
        if include_optional:
            return Activateclanreserve200Response(
                status = 'error',
                meta = wot_api_client.models.stronghold_activateclanreserve_meta.stronghold_activateclanreserve_meta(
                    count = 56, ),
                data = wot_api_client.models.stronghold_activateclanreserve_data.stronghold_activateclanreserve_data(
                    activated_at = 56, ),
                error = wot_api_client.models.stronghold_activateclanreserve_error_error.stronghold_activateclanreserve_error_error(
                    code = 409, 
                    message = 'RESERVE_ACTIVATION_ERROR', 
                    field = '', 
                    value = '', )
            )
        else:
            return Activateclanreserve200Response(
                status = 'error',
                meta = wot_api_client.models.stronghold_activateclanreserve_meta.stronghold_activateclanreserve_meta(
                    count = 56, ),
                data = wot_api_client.models.stronghold_activateclanreserve_data.stronghold_activateclanreserve_data(
                    activated_at = 56, ),
                error = wot_api_client.models.stronghold_activateclanreserve_error_error.stronghold_activateclanreserve_error_error(
                    code = 409, 
                    message = 'RESERVE_ACTIVATION_ERROR', 
                    field = '', 
                    value = '', ),
        )
        """

    def testActivateclanreserve200Response(self):
        """Test Activateclanreserve200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
