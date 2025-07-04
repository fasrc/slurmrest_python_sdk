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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from slurmrest_python_0_0_41.models.v0041_job_desc_msg import V0041JobDescMsg
from typing import Optional, Set
from typing_extensions import Self

class V0041JobSubmitReq(BaseModel):
    """
    V0041JobSubmitReq
    """ # noqa: E501
    job: Optional[V0041JobDescMsg] = None
    jobs: Optional[List[V0041JobDescMsg]] = Field(default=None, description="HetJob description")
    script: Optional[StrictStr] = Field(default=None, description="Deprecated; Populate script field in jobs[0] or job")
    __properties: ClassVar[List[str]] = ["job", "jobs", "script"]

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
        """Create an instance of V0041JobSubmitReq from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of job
        if self.job:
            _dict['job'] = self.job.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in jobs (list)
        _items = []
        if self.jobs:
            for _item_jobs in self.jobs:
                if _item_jobs:
                    _items.append(_item_jobs.to_dict())
            _dict['jobs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041JobSubmitReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "job": V0041JobDescMsg.from_dict(obj["job"]) if obj.get("job") is not None else None,
            "jobs": [V0041JobDescMsg.from_dict(_item) for _item in obj["jobs"]] if obj.get("jobs") is not None else None,
            "script": obj.get("script")
        })
        return _obj


