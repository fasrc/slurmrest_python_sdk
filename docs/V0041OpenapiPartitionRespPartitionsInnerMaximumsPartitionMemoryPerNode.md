# V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerNode

MaxMemPerNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 
**set** | **bool** | True if number has been set; False if number is unset | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_partition_resp_partitions_inner_maximums_partition_memory_per_node import V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerNode

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerNode from a JSON string
v0041_openapi_partition_resp_partitions_inner_maximums_partition_memory_per_node_instance = V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerNode.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerNode.to_json())

# convert the object into a dict
v0041_openapi_partition_resp_partitions_inner_maximums_partition_memory_per_node_dict = v0041_openapi_partition_resp_partitions_inner_maximums_partition_memory_per_node_instance.to_dict()
# create an instance of V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerNode from a dict
v0041_openapi_partition_resp_partitions_inner_maximums_partition_memory_per_node_from_dict = V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerNode.from_dict(v0041_openapi_partition_resp_partitions_inner_maximums_partition_memory_per_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


