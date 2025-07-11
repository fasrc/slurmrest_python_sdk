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

from slurmrest_python_0_0_41.models.v0041_job_desc_msg_rlimits_stack import V0041JobDescMsgRlimitsStack

class TestV0041JobDescMsgRlimitsStack(unittest.TestCase):
    """V0041JobDescMsgRlimitsStack unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041JobDescMsgRlimitsStack:
        """Test V0041JobDescMsgRlimitsStack
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041JobDescMsgRlimitsStack`
        """
        model = V0041JobDescMsgRlimitsStack()
        if include_optional:
            return V0041JobDescMsgRlimitsStack(
                infinite = True,
                number = 56,
                set = True
            )
        else:
            return V0041JobDescMsgRlimitsStack(
        )
        """

    def testV0041JobDescMsgRlimitsStack(self):
        """Test V0041JobDescMsgRlimitsStack"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
