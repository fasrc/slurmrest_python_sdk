# V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **List[str]** | Flags applicable to the OverSubscribe setting | [optional] 
**jobs** | **int** | Maximum number of jobs allowed to oversubscribe resources | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_partition_resp_partitions_inner_maximums_oversubscribe import V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe from a JSON string
v0041_openapi_partition_resp_partitions_inner_maximums_oversubscribe_instance = V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe.to_json())

# convert the object into a dict
v0041_openapi_partition_resp_partitions_inner_maximums_oversubscribe_dict = v0041_openapi_partition_resp_partitions_inner_maximums_oversubscribe_instance.to_dict()
# create an instance of V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe from a dict
v0041_openapi_partition_resp_partitions_inner_maximums_oversubscribe_from_dict = V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe.from_dict(v0041_openapi_partition_resp_partitions_inner_maximums_oversubscribe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


