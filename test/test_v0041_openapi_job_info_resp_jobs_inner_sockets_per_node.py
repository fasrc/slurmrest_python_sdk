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

from slurmrest_python_0_0_41.models.v0041_openapi_job_info_resp_jobs_inner_sockets_per_node import V0041OpenapiJobInfoRespJobsInnerSocketsPerNode

class TestV0041OpenapiJobInfoRespJobsInnerSocketsPerNode(unittest.TestCase):
    """V0041OpenapiJobInfoRespJobsInnerSocketsPerNode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiJobInfoRespJobsInnerSocketsPerNode:
        """Test V0041OpenapiJobInfoRespJobsInnerSocketsPerNode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiJobInfoRespJobsInnerSocketsPerNode`
        """
        model = V0041OpenapiJobInfoRespJobsInnerSocketsPerNode()
        if include_optional:
            return V0041OpenapiJobInfoRespJobsInnerSocketsPerNode(
                infinite = True,
                number = 56,
                set = True
            )
        else:
            return V0041OpenapiJobInfoRespJobsInnerSocketsPerNode(
        )
        """

    def testV0041OpenapiJobInfoRespJobsInnerSocketsPerNode(self):
        """Test V0041OpenapiJobInfoRespJobsInnerSocketsPerNode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
