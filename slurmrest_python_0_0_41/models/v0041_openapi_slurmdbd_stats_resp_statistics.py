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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups import V0041OpenapiSlurmdbdStatsRespStatisticsRollups
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_stats_resp_statistics_rpcs_inner import V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInner
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_stats_resp_statistics_users_inner import V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiSlurmdbdStatsRespStatistics(BaseModel):
    """
    statistics
    """ # noqa: E501
    rpcs: Optional[List[V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInner]] = Field(default=None, description="List of RPCs sent to the slurmdbd", alias="RPCs")
    rollups: Optional[V0041OpenapiSlurmdbdStatsRespStatisticsRollups] = None
    time_start: Optional[StrictInt] = Field(default=None, description="When data collection started (UNIX timestamp)")
    users: Optional[List[V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner]] = Field(default=None, description="List of users that issued RPCs")
    __properties: ClassVar[List[str]] = ["RPCs", "rollups", "time_start", "users"]

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
        """Create an instance of V0041OpenapiSlurmdbdStatsRespStatistics from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rpcs (list)
        _items = []
        if self.rpcs:
            for _item_rpcs in self.rpcs:
                if _item_rpcs:
                    _items.append(_item_rpcs.to_dict())
            _dict['RPCs'] = _items
        # override the default output from pydantic by calling `to_dict()` of rollups
        if self.rollups:
            _dict['rollups'] = self.rollups.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item_users in self.users:
                if _item_users:
                    _items.append(_item_users.to_dict())
            _dict['users'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiSlurmdbdStatsRespStatistics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "RPCs": [V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInner.from_dict(_item) for _item in obj["RPCs"]] if obj.get("RPCs") is not None else None,
            "rollups": V0041OpenapiSlurmdbdStatsRespStatisticsRollups.from_dict(obj["rollups"]) if obj.get("rollups") is not None else None,
            "time_start": obj.get("time_start"),
            "users": [V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner.from_dict(_item) for _item in obj["users"]] if obj.get("users") is not None else None
        })
        return _obj


