# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.11.5&openapi/slurmdbd&openapi/slurmctld
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from slurmrest_python_0_0_41.models.v0041_openapi_assocs_resp_associations_inner_min import V0041OpenapiAssocsRespAssociationsInnerMin

class TestV0041OpenapiAssocsRespAssociationsInnerMin(unittest.TestCase):
    """V0041OpenapiAssocsRespAssociationsInnerMin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiAssocsRespAssociationsInnerMin:
        """Test V0041OpenapiAssocsRespAssociationsInnerMin
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiAssocsRespAssociationsInnerMin`
        """
        model = V0041OpenapiAssocsRespAssociationsInnerMin()
        if include_optional:
            return V0041OpenapiAssocsRespAssociationsInnerMin(
                priority_threshold = slurmrest_python_0_0_41.models.v0_0_41_openapi_assocs_resp_associations_inner_min_priority_threshold.v0_0_41_openapi_assocs_resp_associations_inner_min_priority_threshold(
                    infinite = True, 
                    number = 56, 
                    set = True, )
            )
        else:
            return V0041OpenapiAssocsRespAssociationsInnerMin(
        )
        """

    def testV0041OpenapiAssocsRespAssociationsInnerMin(self):
        """Test V0041OpenapiAssocsRespAssociationsInnerMin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
