# V0041OpenapiNodesRespNodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_features** | **List[str]** | Currently active features | [optional] 
**address** | **str** | NodeAddr, used to establish a communication path | [optional] 
**alloc_cpus** | **int** | Total number of CPUs currently allocated for jobs | [optional] 
**alloc_idle_cpus** | **int** | Total number of idle CPUs | [optional] 
**alloc_memory** | **int** | Total memory in MB currently allocated for jobs | [optional] 
**architecture** | **str** | Computer architecture | [optional] 
**boards** | **int** | Number of Baseboards in nodes with a baseboard controller | [optional] 
**boot_time** | [**V0041OpenapiNodesRespNodesInnerBootTime**](V0041OpenapiNodesRespNodesInnerBootTime.md) |  | [optional] 
**burstbuffer_network_address** | **str** | Alternate network path to be used for sbcast network traffic | [optional] 
**cluster_name** | **str** | Cluster name (only set in federated environments) | [optional] 
**comment** | **str** | Arbitrary comment | [optional] 
**cores** | **int** | Number of cores in a single physical processor socket | [optional] 
**cpu_binding** | **int** | Default method for binding tasks to allocated CPUs | [optional] 
**cpu_load** | **int** | CPU load as reported by the OS | [optional] 
**cpus** | **int** | Total CPUs, including cores and threads | [optional] 
**effective_cpus** | **int** | Number of effective CPUs (excluding specialized CPUs) | [optional] 
**energy** | [**V0041OpenapiNodesRespNodesInnerEnergy**](V0041OpenapiNodesRespNodesInnerEnergy.md) |  | [optional] 
**external_sensors** | **object** |  | [optional] 
**extra** | **str** | Arbitrary string used for node filtering if extra constraints are enabled | [optional] 
**features** | **List[str]** | Available features | [optional] 
**free_mem** | [**V0041OpenapiNodesRespNodesInnerFreeMem**](V0041OpenapiNodesRespNodesInnerFreeMem.md) |  | [optional] 
**gpu_spec** | **str** | CPU cores reserved for jobs that also use a GPU | [optional] 
**gres** | **str** | Generic resources | [optional] 
**gres_drained** | **str** | Drained generic resources | [optional] 
**gres_used** | **str** | Generic resources currently in use | [optional] 
**hostname** | **str** | NodeHostname | [optional] 
**instance_id** | **str** | Cloud instance ID | [optional] 
**instance_type** | **str** | Cloud instance type | [optional] 
**last_busy** | [**V0041OpenapiNodesRespNodesInnerLastBusy**](V0041OpenapiNodesRespNodesInnerLastBusy.md) |  | [optional] 
**mcs_label** | **str** | Multi-Category Security label | [optional] 
**name** | **str** | NodeName | [optional] 
**next_state_after_reboot** | **List[str]** | The state the node will be assigned after rebooting | [optional] 
**operating_system** | **str** | Operating system reported by the node | [optional] 
**owner** | **str** | User allowed to run jobs on this node (unset if no restriction) | [optional] 
**partitions** | **List[str]** | Partitions containing this node | [optional] 
**port** | **int** | TCP port number of the slurmd | [optional] 
**power** | **object** |  | [optional] 
**real_memory** | **int** | Total memory in MB on the node | [optional] 
**reason** | **str** | Describes why the node is in a \&quot;DOWN\&quot;, \&quot;DRAINED\&quot;, \&quot;DRAINING\&quot;, \&quot;FAILING\&quot; or \&quot;FAIL\&quot; state | [optional] 
**reason_changed_at** | [**V0041OpenapiNodesRespNodesInnerReasonChangedAt**](V0041OpenapiNodesRespNodesInnerReasonChangedAt.md) |  | [optional] 
**reason_set_by_user** | **str** | User who set the reason | [optional] 
**res_cores_per_gpu** | **int** | Number of CPU cores per GPU restricted to GPU jobs | [optional] 
**reservation** | **str** | Name of reservation containing this node | [optional] 
**resume_after** | [**V0041OpenapiNodesRespNodesInnerResumeAfter**](V0041OpenapiNodesRespNodesInnerResumeAfter.md) |  | [optional] 
**slurmd_start_time** | [**V0041OpenapiNodesRespNodesInnerSlurmdStartTime**](V0041OpenapiNodesRespNodesInnerSlurmdStartTime.md) |  | [optional] 
**sockets** | **int** | Number of physical processor sockets/chips on the node | [optional] 
**specialized_cores** | **int** | Number of cores reserved for system use | [optional] 
**specialized_cpus** | **str** | Abstract CPU IDs on this node reserved for exclusive use by slurmd and slurmstepd | [optional] 
**specialized_memory** | **int** | Combined memory limit, in MB, for Slurm compute node daemons | [optional] 
**state** | **List[str]** | Node state(s) applicable to this node | [optional] 
**temporary_disk** | **int** | Total size in MB of temporary disk storage in TmpFS | [optional] 
**threads** | **int** | Number of logical threads in a single physical core | [optional] 
**tres** | **str** | Configured trackable resources | [optional] 
**tres_used** | **str** | Trackable resources currently allocated for jobs | [optional] 
**tres_weighted** | **float** | Weighted number of billable trackable resources allocated | [optional] 
**version** | **str** | Slurmd version | [optional] 
**weight** | **int** | Weight of the node for scheduling purposes | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_nodes_resp_nodes_inner import V0041OpenapiNodesRespNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiNodesRespNodesInner from a JSON string
v0041_openapi_nodes_resp_nodes_inner_instance = V0041OpenapiNodesRespNodesInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiNodesRespNodesInner.to_json())

# convert the object into a dict
v0041_openapi_nodes_resp_nodes_inner_dict = v0041_openapi_nodes_resp_nodes_inner_instance.to_dict()
# create an instance of V0041OpenapiNodesRespNodesInner from a dict
v0041_openapi_nodes_resp_nodes_inner_from_dict = V0041OpenapiNodesRespNodesInner.from_dict(v0041_openapi_nodes_resp_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


