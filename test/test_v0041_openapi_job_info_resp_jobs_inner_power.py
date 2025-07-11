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

from slurmrest_python_0_0_41.models.v0041_openapi_job_info_resp_jobs_inner_power import V0041OpenapiJobInfoRespJobsInnerPower

class TestV0041OpenapiJobInfoRespJobsInnerPower(unittest.TestCase):
    """V0041OpenapiJobInfoRespJobsInnerPower unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiJobInfoRespJobsInnerPower:
        """Test V0041OpenapiJobInfoRespJobsInnerPower
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiJobInfoRespJobsInnerPower`
        """
        model = V0041OpenapiJobInfoRespJobsInnerPower()
        if include_optional:
            return V0041OpenapiJobInfoRespJobsInnerPower(
                flags = [
                    null
                    ]
            )
        else:
            return V0041OpenapiJobInfoRespJobsInnerPower(
        )
        """

    def testV0041OpenapiJobInfoRespJobsInnerPower(self):
        """Test V0041OpenapiJobInfoRespJobsInnerPower"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
