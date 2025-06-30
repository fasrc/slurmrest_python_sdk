# V0041OpenapiAccountsAddCondRespMeta

Slurm meta values

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | [**V0041OpenapiAccountsAddCondRespMetaClient**](V0041OpenapiAccountsAddCondRespMetaClient.md) |  | [optional] 
**command** | **List[str]** | CLI command (if applicable) | [optional] 
**plugin** | [**V0041OpenapiAccountsAddCondRespMetaPlugin**](V0041OpenapiAccountsAddCondRespMetaPlugin.md) |  | [optional] 
**slurm** | [**V0041OpenapiAccountsAddCondRespMetaSlurm**](V0041OpenapiAccountsAddCondRespMetaSlurm.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_accounts_add_cond_resp_meta import V0041OpenapiAccountsAddCondRespMeta

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsAddCondRespMeta from a JSON string
v0041_openapi_accounts_add_cond_resp_meta_instance = V0041OpenapiAccountsAddCondRespMeta.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsAddCondRespMeta.to_json())

# convert the object into a dict
v0041_openapi_accounts_add_cond_resp_meta_dict = v0041_openapi_accounts_add_cond_resp_meta_instance.to_dict()
# create an instance of V0041OpenapiAccountsAddCondRespMeta from a dict
v0041_openapi_accounts_add_cond_resp_meta_from_dict = V0041OpenapiAccountsAddCondRespMeta.from_dict(v0041_openapi_accounts_add_cond_resp_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


