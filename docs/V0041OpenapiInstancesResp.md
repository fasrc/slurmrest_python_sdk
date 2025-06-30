# V0041OpenapiInstancesResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[V0041OpenapiAccountsAddCondRespErrorsInner]**](V0041OpenapiAccountsAddCondRespErrorsInner.md) | Query errors | [optional] 
**instances** | [**List[V0041OpenapiInstancesRespInstancesInner]**](V0041OpenapiInstancesRespInstancesInner.md) | instances | 
**meta** | [**V0041OpenapiAccountsAddCondRespMeta**](V0041OpenapiAccountsAddCondRespMeta.md) |  | [optional] 
**warnings** | [**List[V0041OpenapiAccountsAddCondRespWarningsInner]**](V0041OpenapiAccountsAddCondRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_instances_resp import V0041OpenapiInstancesResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiInstancesResp from a JSON string
v0041_openapi_instances_resp_instance = V0041OpenapiInstancesResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiInstancesResp.to_json())

# convert the object into a dict
v0041_openapi_instances_resp_dict = v0041_openapi_instances_resp_instance.to_dict()
# create an instance of V0041OpenapiInstancesResp from a dict
v0041_openapi_instances_resp_from_dict = V0041OpenapiInstancesResp.from_dict(v0041_openapi_instances_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


