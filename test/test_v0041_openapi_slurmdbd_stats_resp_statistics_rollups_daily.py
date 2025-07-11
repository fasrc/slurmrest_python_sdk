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

from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily import V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily

class TestV0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily(unittest.TestCase):
    """V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily:
        """Test V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily`
        """
        model = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily()
        if include_optional:
            return V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily(
                count = 56,
                duration = slurmrest_python_0_0_41.models.v0_0_41_openapi_slurmdbd_stats_resp_statistics_rollups_daily_duration.v0_0_41_openapi_slurmdbd_stats_resp_statistics_rollups_daily_duration(
                    last = 56, 
                    max = 56, 
                    time = 56, ),
                last_run = 56
            )
        else:
            return V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily(
        )
        """

    def testV0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily(self):
        """Test V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
