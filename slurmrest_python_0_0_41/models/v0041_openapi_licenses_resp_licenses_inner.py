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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiLicensesRespLicensesInner(BaseModel):
    """
    V0041OpenapiLicensesRespLicensesInner
    """ # noqa: E501
    free: Optional[StrictInt] = Field(default=None, description="Number of licenses currently available", alias="Free")
    last_consumed: Optional[StrictInt] = Field(default=None, description="Last known number of licenses that were consumed in the license manager (Remote Only)", alias="LastConsumed")
    last_deficit: Optional[StrictInt] = Field(default=None, description="Number of \"missing licenses\" from the cluster's perspective", alias="LastDeficit")
    last_update: Optional[StrictInt] = Field(default=None, description="When the license information was last updated (UNIX Timestamp)", alias="LastUpdate")
    license_name: Optional[StrictStr] = Field(default=None, description="Name of the license", alias="LicenseName")
    remote: Optional[StrictBool] = Field(default=None, description="Indicates whether licenses are served by the database", alias="Remote")
    reserved: Optional[StrictInt] = Field(default=None, description="Number of licenses reserved", alias="Reserved")
    total: Optional[StrictInt] = Field(default=None, description="Total number of licenses present", alias="Total")
    used: Optional[StrictInt] = Field(default=None, description="Number of licenses in use", alias="Used")
    __properties: ClassVar[List[str]] = ["Free", "LastConsumed", "LastDeficit", "LastUpdate", "LicenseName", "Remote", "Reserved", "Total", "Used"]

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
        """Create an instance of V0041OpenapiLicensesRespLicensesInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiLicensesRespLicensesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Free": obj.get("Free"),
            "LastConsumed": obj.get("LastConsumed"),
            "LastDeficit": obj.get("LastDeficit"),
            "LastUpdate": obj.get("LastUpdate"),
            "LicenseName": obj.get("LicenseName"),
            "Remote": obj.get("Remote"),
            "Reserved": obj.get("Reserved"),
            "Total": obj.get("Total"),
            "Used": obj.get("Used")
        })
        return _obj


