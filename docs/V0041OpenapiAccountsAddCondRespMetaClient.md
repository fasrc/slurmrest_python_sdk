# V0041OpenapiAccountsAddCondRespMetaClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Client group (if known) | [optional] 
**source** | **str** | Client source description | [optional] 
**user** | **str** | Client user (if known) | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_accounts_add_cond_resp_meta_client import V0041OpenapiAccountsAddCondRespMetaClient

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsAddCondRespMetaClient from a JSON string
v0041_openapi_accounts_add_cond_resp_meta_client_instance = V0041OpenapiAccountsAddCondRespMetaClient.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsAddCondRespMetaClient.to_json())

# convert the object into a dict
v0041_openapi_accounts_add_cond_resp_meta_client_dict = v0041_openapi_accounts_add_cond_resp_meta_client_instance.to_dict()
# create an instance of V0041OpenapiAccountsAddCondRespMetaClient from a dict
v0041_openapi_accounts_add_cond_resp_meta_client_from_dict = V0041OpenapiAccountsAddCondRespMetaClient.from_dict(v0041_openapi_accounts_add_cond_resp_meta_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


