# V0041OpenapiUsersResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[V0041OpenapiAccountsAddCondRespErrorsInner]**](V0041OpenapiAccountsAddCondRespErrorsInner.md) | Query errors | [optional] 
**meta** | [**V0041OpenapiAccountsAddCondRespMeta**](V0041OpenapiAccountsAddCondRespMeta.md) |  | [optional] 
**users** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInner]**](V0041OpenapiSlurmdbdConfigRespUsersInner.md) | users | 
**warnings** | [**List[V0041OpenapiAccountsAddCondRespWarningsInner]**](V0041OpenapiAccountsAddCondRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_users_resp import V0041OpenapiUsersResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiUsersResp from a JSON string
v0041_openapi_users_resp_instance = V0041OpenapiUsersResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiUsersResp.to_json())

# convert the object into a dict
v0041_openapi_users_resp_dict = v0041_openapi_users_resp_instance.to_dict()
# create an instance of V0041OpenapiUsersResp from a dict
v0041_openapi_users_resp_from_dict = V0041OpenapiUsersResp.from_dict(v0041_openapi_users_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


