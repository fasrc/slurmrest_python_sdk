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

from openapi_client.models.v0041_job_desc_msg_rlimits import V0041JobDescMsgRlimits

class TestV0041JobDescMsgRlimits(unittest.TestCase):
    """V0041JobDescMsgRlimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041JobDescMsgRlimits:
        """Test V0041JobDescMsgRlimits
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041JobDescMsgRlimits`
        """
        model = V0041JobDescMsgRlimits()
        if include_optional:
            return V0041JobDescMsgRlimits(
                var_as = openapi_client.models.v0_0_41_job_desc_msg_rlimits_as.v0_0_41_job_desc_msg_rlimits_as(
                    infinite = True, 
                    number = 56, 
                    set = True, ),
                core = openapi_client.models.v0_0_41_job_desc_msg_rlimits_core.v0_0_41_job_desc_msg_rlimits_core(
                    infinite = True, 
                    number = 56, 
                    set = True, ),
                cpu = openapi_client.models.v0_0_41_job_desc_msg_rlimits_cpu.v0_0_41_job_desc_msg_rlimits_cpu(
                    infinite = True, 
                    number = 56, 
                    set = True, ),
                data = openapi_client.models.v0_0_41_job_desc_msg_rlimits_data.v0_0_41_job_desc_msg_rlimits_data(
                    infinite = True, 
                    number = 56, 
                    set = True, ),
                fsize = openapi_client.models.v0_0_41_job_desc_msg_rlimits_fsize.v0_0_41_job_desc_msg_rlimits_fsize(
                    infinite = True, 
                    number = 56, 
                    set = True, ),
                memlock = openapi_client.models.v0_0_41_job_desc_msg_rlimits_memlock.v0_0_41_job_desc_msg_rlimits_memlock(
                    infinite = True, 
                    number = 56, 
                    set = True, ),
                nofile = openapi_client.models.v0_0_41_job_desc_msg_rlimits_nofile.v0_0_41_job_desc_msg_rlimits_nofile(
                    infinite = True, 
                    number = 56, 
                    set = True, ),
                nproc = openapi_client.models.v0_0_41_job_desc_msg_rlimits_nproc.v0_0_41_job_desc_msg_rlimits_nproc(
                    infinite = True, 
                    number = 56, 
                    set = True, ),
                rss = openapi_client.models.v0_0_41_job_desc_msg_rlimits_rss.v0_0_41_job_desc_msg_rlimits_rss(
                    infinite = True, 
                    number = 56, 
                    set = True, ),
                stack = openapi_client.models.v0_0_41_job_desc_msg_rlimits_stack.v0_0_41_job_desc_msg_rlimits_stack(
                    infinite = True, 
                    number = 56, 
                    set = True, )
            )
        else:
            return V0041JobDescMsgRlimits(
        )
        """

    def testV0041JobDescMsgRlimits(self):
        """Test V0041JobDescMsgRlimits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
