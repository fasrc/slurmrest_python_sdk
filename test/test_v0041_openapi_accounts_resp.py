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

from slurmrest_python_0_0_41.models.v0041_openapi_accounts_resp import V0041OpenapiAccountsResp

class TestV0041OpenapiAccountsResp(unittest.TestCase):
    """V0041OpenapiAccountsResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiAccountsResp:
        """Test V0041OpenapiAccountsResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiAccountsResp`
        """
        model = V0041OpenapiAccountsResp()
        if include_optional:
            return V0041OpenapiAccountsResp(
                accounts = [
                    slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_resp_accounts_inner.v0_0_41_openapi_accounts_resp_accounts_inner(
                        associations = [
                            slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_resp_accounts_inner_associations_inner.v0_0_41_openapi_accounts_resp_accounts_inner_associations_inner(
                                account = '', 
                                cluster = '', 
                                id = 56, 
                                partition = '', 
                                user = '', )
                            ], 
                        coordinators = [
                            slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_resp_accounts_inner_coordinators_inner.v0_0_41_openapi_accounts_resp_accounts_inner_coordinators_inner(
                                direct = True, 
                                name = '', )
                            ], 
                        description = '', 
                        flags = [
                            'DELETED'
                            ], 
                        name = '', 
                        organization = '', )
                    ],
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
                warnings = [
                    slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_add_cond_resp_warnings_inner.v0_0_41_openapi_accounts_add_cond_resp_warnings_inner(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0041OpenapiAccountsResp(
                accounts = [
                    slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_resp_accounts_inner.v0_0_41_openapi_accounts_resp_accounts_inner(
                        associations = [
                            slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_resp_accounts_inner_associations_inner.v0_0_41_openapi_accounts_resp_accounts_inner_associations_inner(
                                account = '', 
                                cluster = '', 
                                id = 56, 
                                partition = '', 
                                user = '', )
                            ], 
                        coordinators = [
                            slurmrest_python_0_0_41.models.v0_0_41_openapi_accounts_resp_accounts_inner_coordinators_inner.v0_0_41_openapi_accounts_resp_accounts_inner_coordinators_inner(
                                direct = True, 
                                name = '', )
                            ], 
                        description = '', 
                        flags = [
                            'DELETED'
                            ], 
                        name = '', 
                        organization = '', )
                    ],
        )
        """

    def testV0041OpenapiAccountsResp(self):
        """Test V0041OpenapiAccountsResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
