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

from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes

class TestV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes(unittest.TestCase):
    """V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes:
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes`
        """
        model = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes()
        if include_optional:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes(
                count = 56,
                list = [
                    ''
                    ],
                range = ''
            )
        else:
            return V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes(
        )
        """

    def testV0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes(self):
        """Test V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerNodes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
