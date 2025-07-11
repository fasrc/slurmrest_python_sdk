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

from slurmrest_python_0_0_41.models.v0041_openapi_accounts_add_cond_resp_meta_slurm import V0041OpenapiAccountsAddCondRespMetaSlurm

class TestV0041OpenapiAccountsAddCondRespMetaSlurm(unittest.TestCase):
    """V0041OpenapiAccountsAddCondRespMetaSlurm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiAccountsAddCondRespMetaSlurm:
        """Test V0041OpenapiAccountsAddCondRespMetaSlurm
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiAccountsAddCondRespMetaSlurm`
        """
        model = V0041OpenapiAccountsAddCondRespMetaSlurm()
        if include_optional:
            return V0041OpenapiAccountsAddCondRespMetaSlurm(
                cluster = '',
                release = '',
                version = slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_add_cond_resp_meta_slurm_version.v0_0_41_openapi_accounts_add_cond_resp_meta_slurm_version(
                    major = '', 
                    micro = '', 
                    minor = '', )
            )
        else:
            return V0041OpenapiAccountsAddCondRespMetaSlurm(
        )
        """

    def testV0041OpenapiAccountsAddCondRespMetaSlurm(self):
        """Test V0041OpenapiAccountsAddCondRespMetaSlurm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
