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

from openapi_client.models.v0041_openapi_slurmdbd_qos_resp import V0041OpenapiSlurmdbdQosResp

class TestV0041OpenapiSlurmdbdQosResp(unittest.TestCase):
    """V0041OpenapiSlurmdbdQosResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdQosResp:
        """Test V0041OpenapiSlurmdbdQosResp
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdQosResp`
        """
        model = V0041OpenapiSlurmdbdQosResp()
        if include_optional:
            return V0041OpenapiSlurmdbdQosResp(
                errors = [
                    openapi_client.models.v0_0_41_openapi_accounts_add_cond_resp_errors_inner.v0_0_41_openapi_accounts_add_cond_resp_errors_inner(
                        description = '', 
                        error = '', 
                        error_number = 56, 
                        source = '', )
                    ],
                meta = openapi_client.models.v0_0_41_openapi_accounts_add_cond_resp_meta.v0_0_41_openapi_accounts_add_cond_resp_meta(
                    client = openapi_client.models.v0_0_41_openapi_accounts_add_cond_resp_meta_client.v0_0_41_openapi_accounts_add_cond_resp_meta_client(
                        group = '', 
                        source = '', 
                        user = '', ), 
                    command = [
                        ''
                        ], 
                    plugin = openapi_client.models.v0_0_41_openapi_accounts_add_cond_resp_meta_plugin.v0_0_41_openapi_accounts_add_cond_resp_meta_plugin(
                        accounting_storage = '', 
                        data_parser = '', 
                        name = '', 
                        type = '', ), 
                    slurm = openapi_client.models.v0_0_41_openapi_accounts_add_cond_resp_meta_slurm.v0_0_41_openapi_accounts_add_cond_resp_meta_slurm(
                        cluster = '', 
                        release = '', 
                        version = openapi_client.models.v0_0_41_openapi_accounts_add_cond_resp_meta_slurm_version.v0_0_41_openapi_accounts_add_cond_resp_meta_slurm_version(
                            major = '', 
                            micro = '', 
                            minor = '', ), ), ),
                qos = [
                    openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner.v0_0_41_openapi_slurmdbd_config_resp_qos_inner(
                        description = '', 
                        flags = [
                            'NOT_SET'
                            ], 
                        id = 56, 
                        limits = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits(
                            factor = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor(
                                infinite = True, 
                                number = 1.337, 
                                set = True, ), 
                            grace_time = 56, 
                            max = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max(
                                accruing = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing(
                                    per = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per(
                                        account = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_account.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_account(
                                            infinite = True, 
                                            number = 56, 
                                            set = True, ), 
                                        user = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_user.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_user(
                                            infinite = True, 
                                            number = 56, 
                                            set = True, ), ), ), 
                                active_jobs = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs(
                                    count = openapi_client.models.v0_0_41_openapi_assocs_resp_associations_inner_max_jobs_per_count.v0_0_41_openapi_assocs_resp_associations_inner_max_jobs_per_count(
                                        infinite = True, 
                                        number = 56, 
                                        set = True, ), ), 
                                jobs = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs(), 
                                tres = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres(
                                    minutes = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes(), 
                                    total = [
                                        openapi_client.models.v0_0_41_openapi_accounts_add_cond_resp_association_condition_association_grptres_inner.v0_0_41_openapi_accounts_add_cond_resp_association_condition_association_grptres_inner(
                                            id = 56, 
                                            name = '', 
                                            type = '', )
                                        ], ), 
                                wall_clock = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock(), ), 
                            min = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min(
                                priority_threshold = openapi_client.models.v0_0_41_openapi_assocs_resp_associations_inner_min_priority_threshold.v0_0_41_openapi_assocs_resp_associations_inner_min_priority_threshold(
                                    infinite = True, 
                                    number = 56, 
                                    set = True, ), ), ), 
                        name = '', 
                        preempt = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt(
                            exempt_time = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt_exempt_time.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt_exempt_time(
                                infinite = True, 
                                number = 56, 
                                set = True, ), 
                            list = [
                                ''
                                ], 
                            mode = [
                                'DISABLED'
                                ], ), 
                        priority = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_priority.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_priority(
                            infinite = True, 
                            number = 56, 
                            set = True, ), 
                        usage_factor = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_factor.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_factor(
                            infinite = True, 
                            number = 1.337, 
                            set = True, ), 
                        usage_threshold = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_threshold.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_threshold(
                            infinite = True, 
                            number = 1.337, 
                            set = True, ), )
                    ],
                warnings = [
                    openapi_client.models.v0_0_41_openapi_accounts_add_cond_resp_warnings_inner.v0_0_41_openapi_accounts_add_cond_resp_warnings_inner(
                        description = '', 
                        source = '', )
                    ]
            )
        else:
            return V0041OpenapiSlurmdbdQosResp(
                qos = [
                    openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner.v0_0_41_openapi_slurmdbd_config_resp_qos_inner(
                        description = '', 
                        flags = [
                            'NOT_SET'
                            ], 
                        id = 56, 
                        limits = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits(
                            factor = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_factor(
                                infinite = True, 
                                number = 1.337, 
                                set = True, ), 
                            grace_time = 56, 
                            max = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max(
                                accruing = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing(
                                    per = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per(
                                        account = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_account.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_account(
                                            infinite = True, 
                                            number = 56, 
                                            set = True, ), 
                                        user = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_user.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing_per_user(
                                            infinite = True, 
                                            number = 56, 
                                            set = True, ), ), ), 
                                active_jobs = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs(
                                    count = openapi_client.models.v0_0_41_openapi_assocs_resp_associations_inner_max_jobs_per_count.v0_0_41_openapi_assocs_resp_associations_inner_max_jobs_per_count(
                                        infinite = True, 
                                        number = 56, 
                                        set = True, ), ), 
                                jobs = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs(), 
                                tres = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres(
                                    minutes = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes(), 
                                    total = [
                                        openapi_client.models.v0_0_41_openapi_accounts_add_cond_resp_association_condition_association_grptres_inner.v0_0_41_openapi_accounts_add_cond_resp_association_condition_association_grptres_inner(
                                            id = 56, 
                                            name = '', 
                                            type = '', )
                                        ], ), 
                                wall_clock = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock(), ), 
                            min = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_min(
                                priority_threshold = openapi_client.models.v0_0_41_openapi_assocs_resp_associations_inner_min_priority_threshold.v0_0_41_openapi_assocs_resp_associations_inner_min_priority_threshold(
                                    infinite = True, 
                                    number = 56, 
                                    set = True, ), ), ), 
                        name = '', 
                        preempt = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt(
                            exempt_time = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt_exempt_time.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_preempt_exempt_time(
                                infinite = True, 
                                number = 56, 
                                set = True, ), 
                            list = [
                                ''
                                ], 
                            mode = [
                                'DISABLED'
                                ], ), 
                        priority = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_priority.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_priority(
                            infinite = True, 
                            number = 56, 
                            set = True, ), 
                        usage_factor = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_factor.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_factor(
                            infinite = True, 
                            number = 1.337, 
                            set = True, ), 
                        usage_threshold = openapi_client.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_threshold.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_usage_threshold(
                            infinite = True, 
                            number = 1.337, 
                            set = True, ), )
                    ],
        )
        """

    def testV0041OpenapiSlurmdbdQosResp(self):
        """Test V0041OpenapiSlurmdbdQosResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
