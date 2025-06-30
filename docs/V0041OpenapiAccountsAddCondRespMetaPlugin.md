# V0041OpenapiAccountsAddCondRespMetaPlugin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_storage** | **str** | Slurm accounting plugin | [optional] 
**data_parser** | **str** | Slurm data_parser plugin | [optional] 
**name** | **str** | Slurm plugin name (if applicable) | [optional] 
**type** | **str** | Slurm plugin type (if applicable) | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_accounts_add_cond_resp_meta_plugin import V0041OpenapiAccountsAddCondRespMetaPlugin

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsAddCondRespMetaPlugin from a JSON string
v0041_openapi_accounts_add_cond_resp_meta_plugin_instance = V0041OpenapiAccountsAddCondRespMetaPlugin.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsAddCondRespMetaPlugin.to_json())

# convert the object into a dict
v0041_openapi_accounts_add_cond_resp_meta_plugin_dict = v0041_openapi_accounts_add_cond_resp_meta_plugin_instance.to_dict()
# create an instance of V0041OpenapiAccountsAddCondRespMetaPlugin from a dict
v0041_openapi_accounts_add_cond_resp_meta_plugin_from_dict = V0041OpenapiAccountsAddCondRespMetaPlugin.from_dict(v0041_openapi_accounts_add_cond_resp_meta_plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


