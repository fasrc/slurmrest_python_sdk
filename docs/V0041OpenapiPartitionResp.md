# V0041OpenapiPartitionResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[V0041OpenapiAccountsAddCondRespErrorsInner]**](V0041OpenapiAccountsAddCondRespErrorsInner.md) | Query errors | [optional] 
**last_update** | [**V0041OpenapiPartitionRespLastUpdate**](V0041OpenapiPartitionRespLastUpdate.md) |  | 
**meta** | [**V0041OpenapiAccountsAddCondRespMeta**](V0041OpenapiAccountsAddCondRespMeta.md) |  | [optional] 
**partitions** | [**List[V0041OpenapiPartitionRespPartitionsInner]**](V0041OpenapiPartitionRespPartitionsInner.md) | List of partitions | 
**warnings** | [**List[V0041OpenapiAccountsAddCondRespWarningsInner]**](V0041OpenapiAccountsAddCondRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_partition_resp import V0041OpenapiPartitionResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiPartitionResp from a JSON string
v0041_openapi_partition_resp_instance = V0041OpenapiPartitionResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiPartitionResp.to_json())

# convert the object into a dict
v0041_openapi_partition_resp_dict = v0041_openapi_partition_resp_instance.to_dict()
# create an instance of V0041OpenapiPartitionResp from a dict
v0041_openapi_partition_resp_from_dict = V0041OpenapiPartitionResp.from_dict(v0041_openapi_partition_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


