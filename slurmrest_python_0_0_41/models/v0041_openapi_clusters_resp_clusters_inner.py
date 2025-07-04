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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from slurmrest_python_0_0_41.models.v0041_openapi_accounts_add_cond_resp_association_condition_association_grptres_inner import V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner
from slurmrest_python_0_0_41.models.v0041_openapi_clusters_resp_clusters_inner_associations import V0041OpenapiClustersRespClustersInnerAssociations
from slurmrest_python_0_0_41.models.v0041_openapi_clusters_resp_clusters_inner_controller import V0041OpenapiClustersRespClustersInnerController
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiClustersRespClustersInner(BaseModel):
    """
    V0041OpenapiClustersRespClustersInner
    """ # noqa: E501
    associations: Optional[V0041OpenapiClustersRespClustersInnerAssociations] = None
    controller: Optional[V0041OpenapiClustersRespClustersInnerController] = None
    flags: Optional[List[StrictStr]] = Field(default=None, description="Flags")
    name: Optional[StrictStr] = Field(default=None, description="ClusterName")
    nodes: Optional[StrictStr] = Field(default=None, description="Node names")
    rpc_version: Optional[StrictInt] = Field(default=None, description="RPC version used in the cluster")
    select_plugin: Optional[StrictStr] = None
    tres: Optional[List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]] = Field(default=None, description="Trackable resources")
    __properties: ClassVar[List[str]] = ["associations", "controller", "flags", "name", "nodes", "rpc_version", "select_plugin", "tres"]

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['REGISTERING', 'MULTIPLE_SLURMD', 'FRONT_END', 'FEDERATION', 'EXTERNAL']):
                raise ValueError("each list item must be one of ('REGISTERING', 'MULTIPLE_SLURMD', 'FRONT_END', 'FEDERATION', 'EXTERNAL')")
        return value

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
        """Create an instance of V0041OpenapiClustersRespClustersInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of associations
        if self.associations:
            _dict['associations'] = self.associations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of controller
        if self.controller:
            _dict['controller'] = self.controller.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tres (list)
        _items = []
        if self.tres:
            for _item_tres in self.tres:
                if _item_tres:
                    _items.append(_item_tres.to_dict())
            _dict['tres'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiClustersRespClustersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associations": V0041OpenapiClustersRespClustersInnerAssociations.from_dict(obj["associations"]) if obj.get("associations") is not None else None,
            "controller": V0041OpenapiClustersRespClustersInnerController.from_dict(obj["controller"]) if obj.get("controller") is not None else None,
            "flags": obj.get("flags"),
            "name": obj.get("name"),
            "nodes": obj.get("nodes"),
            "rpc_version": obj.get("rpc_version"),
            "select_plugin": obj.get("select_plugin"),
            "tres": [V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.from_dict(_item) for _item in obj["tres"]] if obj.get("tres") is not None else None
        })
        return _obj


