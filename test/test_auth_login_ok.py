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

from wot_api_client.models.auth_login_ok import AuthLoginOk

class TestAuthLoginOk(unittest.TestCase):
    """AuthLoginOk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthLoginOk:
        """Test AuthLoginOk
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthLoginOk`
        """
        model = AuthLoginOk()
        if include_optional:
            return AuthLoginOk(
                status = 'ok',
                meta = wot_api_client.models.auth_login_meta.auth_login_meta(
                    count = 56, ),
                data = wot_api_client.models.auth_login_data.auth_login_data(
                    location = '', )
            )
        else:
            return AuthLoginOk(
                status = 'ok',
                meta = wot_api_client.models.auth_login_meta.auth_login_meta(
                    count = 56, ),
                data = wot_api_client.models.auth_login_data.auth_login_data(
                    location = '', ),
        )
        """

    def testAuthLoginOk(self):
        """Test AuthLoginOk"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
