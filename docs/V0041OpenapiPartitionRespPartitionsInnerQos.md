# V0041OpenapiPartitionRespPartitionsInnerQos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **str** | AllowQOS | [optional] 
**assigned** | **str** | QOS | [optional] 
**deny** | **str** | DenyQOS | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_partition_resp_partitions_inner_qos import V0041OpenapiPartitionRespPartitionsInnerQos

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiPartitionRespPartitionsInnerQos from a JSON string
v0041_openapi_partition_resp_partitions_inner_qos_instance = V0041OpenapiPartitionRespPartitionsInnerQos.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiPartitionRespPartitionsInnerQos.to_json())

# convert the object into a dict
v0041_openapi_partition_resp_partitions_inner_qos_dict = v0041_openapi_partition_resp_partitions_inner_qos_instance.to_dict()
# create an instance of V0041OpenapiPartitionRespPartitionsInnerQos from a dict
v0041_openapi_partition_resp_partitions_inner_qos_from_dict = V0041OpenapiPartitionRespPartitionsInnerQos.from_dict(v0041_openapi_partition_resp_partitions_inner_qos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


