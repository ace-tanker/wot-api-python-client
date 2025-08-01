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

from wot_api_client.models.auth_login_error_error_one_of1 import AuthLoginErrorErrorOneOf1

class TestAuthLoginErrorErrorOneOf1(unittest.TestCase):
    """AuthLoginErrorErrorOneOf1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthLoginErrorErrorOneOf1:
        """Test AuthLoginErrorErrorOneOf1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthLoginErrorErrorOneOf1`
        """
        model = AuthLoginErrorErrorOneOf1()
        if include_optional:
            return AuthLoginErrorErrorOneOf1(
                code = 403,
                message = 'AUTH_EXPIRED',
                var_field = '',
                value = ''
            )
        else:
            return AuthLoginErrorErrorOneOf1(
                code = 403,
                message = 'AUTH_EXPIRED',
                var_field = '',
                value = '',
        )
        """

    def testAuthLoginErrorErrorOneOf1(self):
        """Test AuthLoginErrorErrorOneOf1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
