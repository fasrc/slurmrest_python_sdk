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

from slurmrest_python_0_0_41.models.v0041_openapi_clusters_resp_clusters_inner_controller import V0041OpenapiClustersRespClustersInnerController

class TestV0041OpenapiClustersRespClustersInnerController(unittest.TestCase):
    """V0041OpenapiClustersRespClustersInnerController unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiClustersRespClustersInnerController:
        """Test V0041OpenapiClustersRespClustersInnerController
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiClustersRespClustersInnerController`
        """
        model = V0041OpenapiClustersRespClustersInnerController()
        if include_optional:
            return V0041OpenapiClustersRespClustersInnerController(
                host = '',
                port = 56
            )
        else:
            return V0041OpenapiClustersRespClustersInnerController(
        )
        """

    def testV0041OpenapiClustersRespClustersInnerController(self):
        """Test V0041OpenapiClustersRespClustersInnerController"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
