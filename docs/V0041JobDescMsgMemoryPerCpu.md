# V0041JobDescMsgMemoryPerCpu

Minimum memory in megabytes per allocated CPU

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 
**set** | **bool** | True if number has been set; False if number is unset | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_job_desc_msg_memory_per_cpu import V0041JobDescMsgMemoryPerCpu

# TODO update the JSON string below
json = "{}"
# create an instance of V0041JobDescMsgMemoryPerCpu from a JSON string
v0041_job_desc_msg_memory_per_cpu_instance = V0041JobDescMsgMemoryPerCpu.from_json(json)
# print the JSON string representation of the object
print(V0041JobDescMsgMemoryPerCpu.to_json())

# convert the object into a dict
v0041_job_desc_msg_memory_per_cpu_dict = v0041_job_desc_msg_memory_per_cpu_instance.to_dict()
# create an instance of V0041JobDescMsgMemoryPerCpu from a dict
v0041_job_desc_msg_memory_per_cpu_from_dict = V0041JobDescMsgMemoryPerCpu.from_dict(v0041_job_desc_msg_memory_per_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


