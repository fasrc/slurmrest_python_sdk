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

from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobs

class TestV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobs(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobs:
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobs
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobs`
        """
        model = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobs()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobs(
                per = slurmrest_python_0_0_41.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per(
                    account = slurmrest_python_0_0_41.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_account.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_account(
                        infinite = True, 
                        number = 56, 
                        set = True, ), 
                    user = slurmrest_python_0_0_41.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_user.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_user(
                        infinite = True, 
                        number = 56, 
                        set = True, ), )
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobs(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobs(self):
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
