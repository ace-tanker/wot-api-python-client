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

from wot_api_client.models.globalmap_eventratingneighbors_error import GlobalmapEventratingneighborsError

class TestGlobalmapEventratingneighborsError(unittest.TestCase):
    """GlobalmapEventratingneighborsError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GlobalmapEventratingneighborsError:
        """Test GlobalmapEventratingneighborsError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GlobalmapEventratingneighborsError`
        """
        model = GlobalmapEventratingneighborsError()
        if include_optional:
            return GlobalmapEventratingneighborsError(
                status = 'error',
                error = wot_api_client.models.globalmap_seasonratingneighbors_error_error.globalmap_seasonratingneighbors_error_error(
                    code = 404, 
                    message = 'RATINGS_NOT_FOUND', 
                    field = '', 
                    value = '', )
            )
        else:
            return GlobalmapEventratingneighborsError(
                status = 'error',
                error = wot_api_client.models.globalmap_seasonratingneighbors_error_error.globalmap_seasonratingneighbors_error_error(
                    code = 404, 
                    message = 'RATINGS_NOT_FOUND', 
                    field = '', 
                    value = '', ),
        )
        """

    def testGlobalmapEventratingneighborsError(self):
        """Test GlobalmapEventratingneighborsError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
