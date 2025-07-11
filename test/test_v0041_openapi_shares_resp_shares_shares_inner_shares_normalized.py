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

from slurmrest_python_0_0_41.models.v0041_openapi_shares_resp_shares_shares_inner_shares_normalized import V0041OpenapiSharesRespSharesSharesInnerSharesNormalized

class TestV0041OpenapiSharesRespSharesSharesInnerSharesNormalized(unittest.TestCase):
    """V0041OpenapiSharesRespSharesSharesInnerSharesNormalized unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSharesRespSharesSharesInnerSharesNormalized:
        """Test V0041OpenapiSharesRespSharesSharesInnerSharesNormalized
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSharesRespSharesSharesInnerSharesNormalized`
        """
        model = V0041OpenapiSharesRespSharesSharesInnerSharesNormalized()
        if include_optional:
            return V0041OpenapiSharesRespSharesSharesInnerSharesNormalized(
                infinite = True,
                number = 1.337,
                set = True
            )
        else:
            return V0041OpenapiSharesRespSharesSharesInnerSharesNormalized(
        )
        """

    def testV0041OpenapiSharesRespSharesSharesInnerSharesNormalized(self):
        """Test V0041OpenapiSharesRespSharesSharesInnerSharesNormalized"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
