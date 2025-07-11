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

from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime

class TestV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime(unittest.TestCase):
    """V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime:
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime`
        """
        model = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime()
        if include_optional:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime(
                elapsed = 56,
                end = slurmrest_python_0_0_41.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_end.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_end(
                    infinite = True, 
                    number = 56, 
                    set = True, ),
                start = slurmrest_python_0_0_41.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_start.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_start(
                    infinite = True, 
                    number = 56, 
                    set = True, ),
                suspended = 56,
                system = slurmrest_python_0_0_41.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_system.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_system(
                    microseconds = 56, 
                    seconds = 56, ),
                total = slurmrest_python_0_0_41.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_total.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_total(
                    microseconds = 56, 
                    seconds = 56, ),
                user = slurmrest_python_0_0_41.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_user.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_user(
                    microseconds = 56, 
                    seconds = 56, )
            )
        else:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime(
        )
        """

    def testV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime(self):
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
