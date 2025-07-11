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

from slurmrest_python_0_0_41.models.v0041_openapi_assocs_resp_associations_inner_accounting_inner_tres import V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES

class TestV0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES(unittest.TestCase):
    """V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES:
        """Test V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES`
        """
        model = V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES()
        if include_optional:
            return V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES(
                count = 56,
                id = 56,
                name = '',
                type = ''
            )
        else:
            return V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES(
                type = '',
        )
        """

    def testV0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES(self):
        """Test V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
