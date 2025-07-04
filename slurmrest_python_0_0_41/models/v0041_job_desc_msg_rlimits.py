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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from slurmrest_python_0_0_41.models.v0041_job_desc_msg_rlimits_as import V0041JobDescMsgRlimitsAs
from slurmrest_python_0_0_41.models.v0041_job_desc_msg_rlimits_core import V0041JobDescMsgRlimitsCore
from slurmrest_python_0_0_41.models.v0041_job_desc_msg_rlimits_cpu import V0041JobDescMsgRlimitsCpu
from slurmrest_python_0_0_41.models.v0041_job_desc_msg_rlimits_data import V0041JobDescMsgRlimitsData
from slurmrest_python_0_0_41.models.v0041_job_desc_msg_rlimits_fsize import V0041JobDescMsgRlimitsFsize
from slurmrest_python_0_0_41.models.v0041_job_desc_msg_rlimits_memlock import V0041JobDescMsgRlimitsMemlock
from slurmrest_python_0_0_41.models.v0041_job_desc_msg_rlimits_nofile import V0041JobDescMsgRlimitsNofile
from slurmrest_python_0_0_41.models.v0041_job_desc_msg_rlimits_nproc import V0041JobDescMsgRlimitsNproc
from slurmrest_python_0_0_41.models.v0041_job_desc_msg_rlimits_rss import V0041JobDescMsgRlimitsRss
from slurmrest_python_0_0_41.models.v0041_job_desc_msg_rlimits_stack import V0041JobDescMsgRlimitsStack
from typing import Optional, Set
from typing_extensions import Self

class V0041JobDescMsgRlimits(BaseModel):
    """
    V0041JobDescMsgRlimits
    """ # noqa: E501
    var_as: Optional[V0041JobDescMsgRlimitsAs] = Field(default=None, alias="as")
    core: Optional[V0041JobDescMsgRlimitsCore] = None
    cpu: Optional[V0041JobDescMsgRlimitsCpu] = None
    data: Optional[V0041JobDescMsgRlimitsData] = None
    fsize: Optional[V0041JobDescMsgRlimitsFsize] = None
    memlock: Optional[V0041JobDescMsgRlimitsMemlock] = None
    nofile: Optional[V0041JobDescMsgRlimitsNofile] = None
    nproc: Optional[V0041JobDescMsgRlimitsNproc] = None
    rss: Optional[V0041JobDescMsgRlimitsRss] = None
    stack: Optional[V0041JobDescMsgRlimitsStack] = None
    __properties: ClassVar[List[str]] = ["as", "core", "cpu", "data", "fsize", "memlock", "nofile", "nproc", "rss", "stack"]

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
        """Create an instance of V0041JobDescMsgRlimits from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_as
        if self.var_as:
            _dict['as'] = self.var_as.to_dict()
        # override the default output from pydantic by calling `to_dict()` of core
        if self.core:
            _dict['core'] = self.core.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpu
        if self.cpu:
            _dict['cpu'] = self.cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fsize
        if self.fsize:
            _dict['fsize'] = self.fsize.to_dict()
        # override the default output from pydantic by calling `to_dict()` of memlock
        if self.memlock:
            _dict['memlock'] = self.memlock.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nofile
        if self.nofile:
            _dict['nofile'] = self.nofile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nproc
        if self.nproc:
            _dict['nproc'] = self.nproc.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rss
        if self.rss:
            _dict['rss'] = self.rss.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stack
        if self.stack:
            _dict['stack'] = self.stack.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041JobDescMsgRlimits from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "as": V0041JobDescMsgRlimitsAs.from_dict(obj["as"]) if obj.get("as") is not None else None,
            "core": V0041JobDescMsgRlimitsCore.from_dict(obj["core"]) if obj.get("core") is not None else None,
            "cpu": V0041JobDescMsgRlimitsCpu.from_dict(obj["cpu"]) if obj.get("cpu") is not None else None,
            "data": V0041JobDescMsgRlimitsData.from_dict(obj["data"]) if obj.get("data") is not None else None,
            "fsize": V0041JobDescMsgRlimitsFsize.from_dict(obj["fsize"]) if obj.get("fsize") is not None else None,
            "memlock": V0041JobDescMsgRlimitsMemlock.from_dict(obj["memlock"]) if obj.get("memlock") is not None else None,
            "nofile": V0041JobDescMsgRlimitsNofile.from_dict(obj["nofile"]) if obj.get("nofile") is not None else None,
            "nproc": V0041JobDescMsgRlimitsNproc.from_dict(obj["nproc"]) if obj.get("nproc") is not None else None,
            "rss": V0041JobDescMsgRlimitsRss.from_dict(obj["rss"]) if obj.get("rss") is not None else None,
            "stack": V0041JobDescMsgRlimitsStack.from_dict(obj["stack"]) if obj.get("stack") is not None else None
        })
        return _obj


