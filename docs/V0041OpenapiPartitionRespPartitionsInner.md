# V0041OpenapiPartitionRespPartitionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**V0041OpenapiPartitionRespPartitionsInnerAccounts**](V0041OpenapiPartitionRespPartitionsInnerAccounts.md) |  | [optional] 
**alternate** | **str** | Alternate | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**cpus** | [**V0041OpenapiPartitionRespPartitionsInnerCpus**](V0041OpenapiPartitionRespPartitionsInnerCpus.md) |  | [optional] 
**defaults** | [**V0041OpenapiPartitionRespPartitionsInnerDefaults**](V0041OpenapiPartitionRespPartitionsInnerDefaults.md) |  | [optional] 
**grace_time** | **int** | GraceTime | [optional] 
**groups** | [**V0041OpenapiPartitionRespPartitionsInnerGroups**](V0041OpenapiPartitionRespPartitionsInnerGroups.md) |  | [optional] 
**maximums** | [**V0041OpenapiPartitionRespPartitionsInnerMaximums**](V0041OpenapiPartitionRespPartitionsInnerMaximums.md) |  | [optional] 
**minimums** | [**V0041OpenapiPartitionRespPartitionsInnerMinimums**](V0041OpenapiPartitionRespPartitionsInnerMinimums.md) |  | [optional] 
**name** | **str** | PartitionName | [optional] 
**node_sets** | **str** | NodeSets | [optional] 
**nodes** | [**V0041OpenapiPartitionRespPartitionsInnerNodes**](V0041OpenapiPartitionRespPartitionsInnerNodes.md) |  | [optional] 
**partition** | [**V0041OpenapiPartitionRespPartitionsInnerPartition**](V0041OpenapiPartitionRespPartitionsInnerPartition.md) |  | [optional] 
**priority** | [**V0041OpenapiPartitionRespPartitionsInnerPriority**](V0041OpenapiPartitionRespPartitionsInnerPriority.md) |  | [optional] 
**qos** | [**V0041OpenapiPartitionRespPartitionsInnerQos**](V0041OpenapiPartitionRespPartitionsInnerQos.md) |  | [optional] 
**select_type** | **List[str]** | Scheduler consumable resource selection type | [optional] 
**suspend_time** | [**V0041OpenapiPartitionRespPartitionsInnerSuspendTime**](V0041OpenapiPartitionRespPartitionsInnerSuspendTime.md) |  | [optional] 
**timeouts** | [**V0041OpenapiPartitionRespPartitionsInnerTimeouts**](V0041OpenapiPartitionRespPartitionsInnerTimeouts.md) |  | [optional] 
**tres** | [**V0041OpenapiPartitionRespPartitionsInnerTres**](V0041OpenapiPartitionRespPartitionsInnerTres.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner import V0041OpenapiPartitionRespPartitionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiPartitionRespPartitionsInner from a JSON string
v0041_openapi_partition_resp_partitions_inner_instance = V0041OpenapiPartitionRespPartitionsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiPartitionRespPartitionsInner.to_json())

# convert the object into a dict
v0041_openapi_partition_resp_partitions_inner_dict = v0041_openapi_partition_resp_partitions_inner_instance.to_dict()
# create an instance of V0041OpenapiPartitionRespPartitionsInner from a dict
v0041_openapi_partition_resp_partitions_inner_from_dict = V0041OpenapiPartitionRespPartitionsInner.from_dict(v0041_openapi_partition_resp_partitions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


