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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from slurmrest_python_0_0_41.models.v0041_openapi_nodes_resp_nodes_inner_boot_time import V0041OpenapiNodesRespNodesInnerBootTime
from slurmrest_python_0_0_41.models.v0041_openapi_nodes_resp_nodes_inner_energy import V0041OpenapiNodesRespNodesInnerEnergy
from slurmrest_python_0_0_41.models.v0041_openapi_nodes_resp_nodes_inner_free_mem import V0041OpenapiNodesRespNodesInnerFreeMem
from slurmrest_python_0_0_41.models.v0041_openapi_nodes_resp_nodes_inner_last_busy import V0041OpenapiNodesRespNodesInnerLastBusy
from slurmrest_python_0_0_41.models.v0041_openapi_nodes_resp_nodes_inner_reason_changed_at import V0041OpenapiNodesRespNodesInnerReasonChangedAt
from slurmrest_python_0_0_41.models.v0041_openapi_nodes_resp_nodes_inner_resume_after import V0041OpenapiNodesRespNodesInnerResumeAfter
from slurmrest_python_0_0_41.models.v0041_openapi_nodes_resp_nodes_inner_slurmd_start_time import V0041OpenapiNodesRespNodesInnerSlurmdStartTime
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiNodesRespNodesInner(BaseModel):
    """
    V0041OpenapiNodesRespNodesInner
    """ # noqa: E501
    active_features: Optional[List[StrictStr]] = Field(default=None, description="Currently active features")
    address: Optional[StrictStr] = Field(default=None, description="NodeAddr, used to establish a communication path")
    alloc_cpus: Optional[StrictInt] = Field(default=None, description="Total number of CPUs currently allocated for jobs")
    alloc_idle_cpus: Optional[StrictInt] = Field(default=None, description="Total number of idle CPUs")
    alloc_memory: Optional[StrictInt] = Field(default=None, description="Total memory in MB currently allocated for jobs")
    architecture: Optional[StrictStr] = Field(default=None, description="Computer architecture")
    boards: Optional[StrictInt] = Field(default=None, description="Number of Baseboards in nodes with a baseboard controller")
    boot_time: Optional[V0041OpenapiNodesRespNodesInnerBootTime] = None
    burstbuffer_network_address: Optional[StrictStr] = Field(default=None, description="Alternate network path to be used for sbcast network traffic")
    cluster_name: Optional[StrictStr] = Field(default=None, description="Cluster name (only set in federated environments)")
    comment: Optional[StrictStr] = Field(default=None, description="Arbitrary comment")
    cores: Optional[StrictInt] = Field(default=None, description="Number of cores in a single physical processor socket")
    cpu_binding: Optional[StrictInt] = Field(default=None, description="Default method for binding tasks to allocated CPUs")
    cpu_load: Optional[StrictInt] = Field(default=None, description="CPU load as reported by the OS")
    cpus: Optional[StrictInt] = Field(default=None, description="Total CPUs, including cores and threads")
    effective_cpus: Optional[StrictInt] = Field(default=None, description="Number of effective CPUs (excluding specialized CPUs)")
    energy: Optional[V0041OpenapiNodesRespNodesInnerEnergy] = None
    external_sensors: Optional[Dict[str, Any]] = None
    extra: Optional[StrictStr] = Field(default=None, description="Arbitrary string used for node filtering if extra constraints are enabled")
    features: Optional[List[StrictStr]] = Field(default=None, description="Available features")
    free_mem: Optional[V0041OpenapiNodesRespNodesInnerFreeMem] = None
    gpu_spec: Optional[StrictStr] = Field(default=None, description="CPU cores reserved for jobs that also use a GPU")
    gres: Optional[StrictStr] = Field(default=None, description="Generic resources")
    gres_drained: Optional[StrictStr] = Field(default=None, description="Drained generic resources")
    gres_used: Optional[StrictStr] = Field(default=None, description="Generic resources currently in use")
    hostname: Optional[StrictStr] = Field(default=None, description="NodeHostname")
    instance_id: Optional[StrictStr] = Field(default=None, description="Cloud instance ID")
    instance_type: Optional[StrictStr] = Field(default=None, description="Cloud instance type")
    last_busy: Optional[V0041OpenapiNodesRespNodesInnerLastBusy] = None
    mcs_label: Optional[StrictStr] = Field(default=None, description="Multi-Category Security label")
    name: Optional[StrictStr] = Field(default=None, description="NodeName")
    next_state_after_reboot: Optional[List[StrictStr]] = Field(default=None, description="The state the node will be assigned after rebooting")
    operating_system: Optional[StrictStr] = Field(default=None, description="Operating system reported by the node")
    owner: Optional[StrictStr] = Field(default=None, description="User allowed to run jobs on this node (unset if no restriction)")
    partitions: Optional[List[StrictStr]] = Field(default=None, description="Partitions containing this node")
    port: Optional[StrictInt] = Field(default=None, description="TCP port number of the slurmd")
    power: Optional[Dict[str, Any]] = None
    real_memory: Optional[StrictInt] = Field(default=None, description="Total memory in MB on the node")
    reason: Optional[StrictStr] = Field(default=None, description="Describes why the node is in a \"DOWN\", \"DRAINED\", \"DRAINING\", \"FAILING\" or \"FAIL\" state")
    reason_changed_at: Optional[V0041OpenapiNodesRespNodesInnerReasonChangedAt] = None
    reason_set_by_user: Optional[StrictStr] = Field(default=None, description="User who set the reason")
    res_cores_per_gpu: Optional[StrictInt] = Field(default=None, description="Number of CPU cores per GPU restricted to GPU jobs")
    reservation: Optional[StrictStr] = Field(default=None, description="Name of reservation containing this node")
    resume_after: Optional[V0041OpenapiNodesRespNodesInnerResumeAfter] = None
    slurmd_start_time: Optional[V0041OpenapiNodesRespNodesInnerSlurmdStartTime] = None
    sockets: Optional[StrictInt] = Field(default=None, description="Number of physical processor sockets/chips on the node")
    specialized_cores: Optional[StrictInt] = Field(default=None, description="Number of cores reserved for system use")
    specialized_cpus: Optional[StrictStr] = Field(default=None, description="Abstract CPU IDs on this node reserved for exclusive use by slurmd and slurmstepd")
    specialized_memory: Optional[StrictInt] = Field(default=None, description="Combined memory limit, in MB, for Slurm compute node daemons")
    state: Optional[List[StrictStr]] = Field(default=None, description="Node state(s) applicable to this node")
    temporary_disk: Optional[StrictInt] = Field(default=None, description="Total size in MB of temporary disk storage in TmpFS")
    threads: Optional[StrictInt] = Field(default=None, description="Number of logical threads in a single physical core")
    tres: Optional[StrictStr] = Field(default=None, description="Configured trackable resources")
    tres_used: Optional[StrictStr] = Field(default=None, description="Trackable resources currently allocated for jobs")
    tres_weighted: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Weighted number of billable trackable resources allocated")
    version: Optional[StrictStr] = Field(default=None, description="Slurmd version")
    weight: Optional[StrictInt] = Field(default=None, description="Weight of the node for scheduling purposes")
    __properties: ClassVar[List[str]] = ["active_features", "address", "alloc_cpus", "alloc_idle_cpus", "alloc_memory", "architecture", "boards", "boot_time", "burstbuffer_network_address", "cluster_name", "comment", "cores", "cpu_binding", "cpu_load", "cpus", "effective_cpus", "energy", "external_sensors", "extra", "features", "free_mem", "gpu_spec", "gres", "gres_drained", "gres_used", "hostname", "instance_id", "instance_type", "last_busy", "mcs_label", "name", "next_state_after_reboot", "operating_system", "owner", "partitions", "port", "power", "real_memory", "reason", "reason_changed_at", "reason_set_by_user", "res_cores_per_gpu", "reservation", "resume_after", "slurmd_start_time", "sockets", "specialized_cores", "specialized_cpus", "specialized_memory", "state", "temporary_disk", "threads", "tres", "tres_used", "tres_weighted", "version", "weight"]

    @field_validator('next_state_after_reboot')
    def next_state_after_reboot_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['INVALID', 'UNKNOWN', 'DOWN', 'IDLE', 'ALLOCATED', 'ERROR', 'MIXED', 'FUTURE', 'RESERVED', 'UNDRAIN', 'CLOUD', 'RESUME', 'DRAIN', 'COMPLETING', 'NOT_RESPONDING', 'POWERED_DOWN', 'FAIL', 'POWERING_UP', 'MAINTENANCE', 'REBOOT_REQUESTED', 'REBOOT_CANCELED', 'POWERING_DOWN', 'DYNAMIC_FUTURE', 'REBOOT_ISSUED', 'PLANNED', 'INVALID_REG', 'POWER_DOWN', 'POWER_UP', 'POWER_DRAIN', 'DYNAMIC_NORM']):
                raise ValueError("each list item must be one of ('INVALID', 'UNKNOWN', 'DOWN', 'IDLE', 'ALLOCATED', 'ERROR', 'MIXED', 'FUTURE', 'RESERVED', 'UNDRAIN', 'CLOUD', 'RESUME', 'DRAIN', 'COMPLETING', 'NOT_RESPONDING', 'POWERED_DOWN', 'FAIL', 'POWERING_UP', 'MAINTENANCE', 'REBOOT_REQUESTED', 'REBOOT_CANCELED', 'POWERING_DOWN', 'DYNAMIC_FUTURE', 'REBOOT_ISSUED', 'PLANNED', 'INVALID_REG', 'POWER_DOWN', 'POWER_UP', 'POWER_DRAIN', 'DYNAMIC_NORM')")
        return value

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['INVALID', 'UNKNOWN', 'DOWN', 'IDLE', 'ALLOCATED', 'ERROR', 'MIXED', 'FUTURE', 'RESERVED', 'UNDRAIN', 'CLOUD', 'RESUME', 'DRAIN', 'COMPLETING', 'NOT_RESPONDING', 'POWERED_DOWN', 'FAIL', 'POWERING_UP', 'MAINTENANCE', 'REBOOT_REQUESTED', 'REBOOT_CANCELED', 'POWERING_DOWN', 'DYNAMIC_FUTURE', 'REBOOT_ISSUED', 'PLANNED', 'INVALID_REG', 'POWER_DOWN', 'POWER_UP', 'POWER_DRAIN', 'DYNAMIC_NORM']):
                raise ValueError("each list item must be one of ('INVALID', 'UNKNOWN', 'DOWN', 'IDLE', 'ALLOCATED', 'ERROR', 'MIXED', 'FUTURE', 'RESERVED', 'UNDRAIN', 'CLOUD', 'RESUME', 'DRAIN', 'COMPLETING', 'NOT_RESPONDING', 'POWERED_DOWN', 'FAIL', 'POWERING_UP', 'MAINTENANCE', 'REBOOT_REQUESTED', 'REBOOT_CANCELED', 'POWERING_DOWN', 'DYNAMIC_FUTURE', 'REBOOT_ISSUED', 'PLANNED', 'INVALID_REG', 'POWER_DOWN', 'POWER_UP', 'POWER_DRAIN', 'DYNAMIC_NORM')")
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
        """Create an instance of V0041OpenapiNodesRespNodesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of boot_time
        if self.boot_time:
            _dict['boot_time'] = self.boot_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of energy
        if self.energy:
            _dict['energy'] = self.energy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of free_mem
        if self.free_mem:
            _dict['free_mem'] = self.free_mem.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_busy
        if self.last_busy:
            _dict['last_busy'] = self.last_busy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reason_changed_at
        if self.reason_changed_at:
            _dict['reason_changed_at'] = self.reason_changed_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resume_after
        if self.resume_after:
            _dict['resume_after'] = self.resume_after.to_dict()
        # override the default output from pydantic by calling `to_dict()` of slurmd_start_time
        if self.slurmd_start_time:
            _dict['slurmd_start_time'] = self.slurmd_start_time.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiNodesRespNodesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active_features": obj.get("active_features"),
            "address": obj.get("address"),
            "alloc_cpus": obj.get("alloc_cpus"),
            "alloc_idle_cpus": obj.get("alloc_idle_cpus"),
            "alloc_memory": obj.get("alloc_memory"),
            "architecture": obj.get("architecture"),
            "boards": obj.get("boards"),
            "boot_time": V0041OpenapiNodesRespNodesInnerBootTime.from_dict(obj["boot_time"]) if obj.get("boot_time") is not None else None,
            "burstbuffer_network_address": obj.get("burstbuffer_network_address"),
            "cluster_name": obj.get("cluster_name"),
            "comment": obj.get("comment"),
            "cores": obj.get("cores"),
            "cpu_binding": obj.get("cpu_binding"),
            "cpu_load": obj.get("cpu_load"),
            "cpus": obj.get("cpus"),
            "effective_cpus": obj.get("effective_cpus"),
            "energy": V0041OpenapiNodesRespNodesInnerEnergy.from_dict(obj["energy"]) if obj.get("energy") is not None else None,
            "external_sensors": obj.get("external_sensors"),
            "extra": obj.get("extra"),
            "features": obj.get("features"),
            "free_mem": V0041OpenapiNodesRespNodesInnerFreeMem.from_dict(obj["free_mem"]) if obj.get("free_mem") is not None else None,
            "gpu_spec": obj.get("gpu_spec"),
            "gres": obj.get("gres"),
            "gres_drained": obj.get("gres_drained"),
            "gres_used": obj.get("gres_used"),
            "hostname": obj.get("hostname"),
            "instance_id": obj.get("instance_id"),
            "instance_type": obj.get("instance_type"),
            "last_busy": V0041OpenapiNodesRespNodesInnerLastBusy.from_dict(obj["last_busy"]) if obj.get("last_busy") is not None else None,
            "mcs_label": obj.get("mcs_label"),
            "name": obj.get("name"),
            "next_state_after_reboot": obj.get("next_state_after_reboot"),
            "operating_system": obj.get("operating_system"),
            "owner": obj.get("owner"),
            "partitions": obj.get("partitions"),
            "port": obj.get("port"),
            "power": obj.get("power"),
            "real_memory": obj.get("real_memory"),
            "reason": obj.get("reason"),
            "reason_changed_at": V0041OpenapiNodesRespNodesInnerReasonChangedAt.from_dict(obj["reason_changed_at"]) if obj.get("reason_changed_at") is not None else None,
            "reason_set_by_user": obj.get("reason_set_by_user"),
            "res_cores_per_gpu": obj.get("res_cores_per_gpu"),
            "reservation": obj.get("reservation"),
            "resume_after": V0041OpenapiNodesRespNodesInnerResumeAfter.from_dict(obj["resume_after"]) if obj.get("resume_after") is not None else None,
            "slurmd_start_time": V0041OpenapiNodesRespNodesInnerSlurmdStartTime.from_dict(obj["slurmd_start_time"]) if obj.get("slurmd_start_time") is not None else None,
            "sockets": obj.get("sockets"),
            "specialized_cores": obj.get("specialized_cores"),
            "specialized_cpus": obj.get("specialized_cpus"),
            "specialized_memory": obj.get("specialized_memory"),
            "state": obj.get("state"),
            "temporary_disk": obj.get("temporary_disk"),
            "threads": obj.get("threads"),
            "tres": obj.get("tres"),
            "tres_used": obj.get("tres_used"),
            "tres_weighted": obj.get("tres_weighted"),
            "version": obj.get("version"),
            "weight": obj.get("weight")
        })
        return _obj


