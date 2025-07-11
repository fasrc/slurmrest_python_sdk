# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.11.5&openapi/slurmdbd&openapi/slurmctld
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_accruing import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobs
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobs
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTres
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClock
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax(BaseModel):
    """
    V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax
    """ # noqa: E501
    accruing: Optional[V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing] = None
    active_jobs: Optional[V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobs] = None
    jobs: Optional[V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobs] = None
    tres: Optional[V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTres] = None
    wall_clock: Optional[V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClock] = None
    __properties: ClassVar[List[str]] = ["accruing", "active_jobs", "jobs", "tres", "wall_clock"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of accruing
        if self.accruing:
            _dict['accruing'] = self.accruing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of active_jobs
        if self.active_jobs:
            _dict['active_jobs'] = self.active_jobs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of jobs
        if self.jobs:
            _dict['jobs'] = self.jobs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tres
        if self.tres:
            _dict['tres'] = self.tres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wall_clock
        if self.wall_clock:
            _dict['wall_clock'] = self.wall_clock.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMax from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accruing": V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxAccruing.from_dict(obj["accruing"]) if obj.get("accruing") is not None else None,
            "active_jobs": V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobs.from_dict(obj["active_jobs"]) if obj.get("active_jobs") is not None else None,
            "jobs": V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobs.from_dict(obj["jobs"]) if obj.get("jobs") is not None else None,
            "tres": V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTres.from_dict(obj["tres"]) if obj.get("tres") is not None else None,
            "wall_clock": V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClock.from_dict(obj["wall_clock"]) if obj.get("wall_clock") is not None else None
        })
        return _obj


