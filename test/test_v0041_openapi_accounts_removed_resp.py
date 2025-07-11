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

from slurmrest_python_0_0_41.models.v0041_openapi_accounts_removed_resp import V0041OpenapiAccountsRemovedResp

class TestV0041OpenapiAccountsRemovedResp(unittest.TestCase):
    """V0041OpenapiAccountsRemovedResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiAccountsRemovedResp:
        """Test V0041OpenapiAccountsRemovedResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiAccountsRemovedResp`
        """
        model = V0041OpenapiAccountsRemovedResp()
        if include_optional:
            return V0041OpenapiAccountsRemovedResp(
                errors = [
                    slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_add_cond_resp_errors_inner.v0_0_41_openapi_accounts_add_cond_resp_errors_inner(
                        description = '', 
                        error = '', 
                        error_number = 56, 
                        source = '', )
                    ],
                meta = slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_add_cond_resp_meta.v0_0_41_openapi_accounts_add_cond_resp_meta(
                    client = slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_add_cond_resp_meta_client.v0_0_41_openapi_accounts_add_cond_resp_meta_client(
                        group = '', 
                        source = '', 
                        user = '', ), 
                    command = [
                        ''
                        ], 
                    plugin = slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_add_cond_resp_meta_plugin.v0_0_41_openapi_accounts_add_cond_resp_meta_plugin(
                        accounting_storage = '', 
                        data_parser = '', 
                        name = '', 
                        type = '', ), 
                    slurm = slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_add_cond_resp_meta_slurm.v0_0_41_openapi_accounts_add_cond_resp_meta_slurm(
                        cluster = '', 
                        release = '', 
                        version = slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_add_cond_resp_meta_slurm_version.v0_0_41_openapi_accounts_add_cond_resp_meta_slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), ), ),
                removed_accounts = [
                    ''
                    ],
                warnings = [
                    slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_add_cond_resp_warnings_inner.v0_0_41_openapi_accounts_add_cond_resp_warnings_inner(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0041OpenapiAccountsRemovedResp(
                removed_accounts = [
                    ''
                    ],
        )
        """

    def testV0041OpenapiAccountsRemovedResp(self):
        """Test V0041OpenapiAccountsRemovedResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
