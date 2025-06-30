# V0041OpenapiInstancesRespInstancesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** | Cluster name | [optional] 
**extra** | **str** | Arbitrary string used for node filtering if extra constraints are enabled | [optional] 
**instance_id** | **str** | Cloud instance ID | [optional] 
**instance_type** | **str** | Cloud instance type | [optional] 
**node_name** | **str** | NodeName | [optional] 
**time** | [**V0041OpenapiInstancesRespInstancesInnerTime**](V0041OpenapiInstancesRespInstancesInnerTime.md) |  | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_instances_resp_instances_inner import V0041OpenapiInstancesRespInstancesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiInstancesRespInstancesInner from a JSON string
v0041_openapi_instances_resp_instances_inner_instance = V0041OpenapiInstancesRespInstancesInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiInstancesRespInstancesInner.to_json())

# convert the object into a dict
v0041_openapi_instances_resp_instances_inner_dict = v0041_openapi_instances_resp_instances_inner_instance.to_dict()
# create an instance of V0041OpenapiInstancesRespInstancesInner from a dict
v0041_openapi_instances_resp_instances_inner_from_dict = V0041OpenapiInstancesRespInstancesInner.from_dict(v0041_openapi_instances_resp_instances_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


