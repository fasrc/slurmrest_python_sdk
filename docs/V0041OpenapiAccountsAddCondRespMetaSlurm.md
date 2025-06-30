# V0041OpenapiAccountsAddCondRespMetaSlurm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** | Slurm cluster name | [optional] 
**release** | **str** | Slurm release string | [optional] 
**version** | [**V0041OpenapiAccountsAddCondRespMetaSlurmVersion**](V0041OpenapiAccountsAddCondRespMetaSlurmVersion.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_accounts_add_cond_resp_meta_slurm import V0041OpenapiAccountsAddCondRespMetaSlurm

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsAddCondRespMetaSlurm from a JSON string
v0041_openapi_accounts_add_cond_resp_meta_slurm_instance = V0041OpenapiAccountsAddCondRespMetaSlurm.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsAddCondRespMetaSlurm.to_json())

# convert the object into a dict
v0041_openapi_accounts_add_cond_resp_meta_slurm_dict = v0041_openapi_accounts_add_cond_resp_meta_slurm_instance.to_dict()
# create an instance of V0041OpenapiAccountsAddCondRespMetaSlurm from a dict
v0041_openapi_accounts_add_cond_resp_meta_slurm_from_dict = V0041OpenapiAccountsAddCondRespMetaSlurm.from_dict(v0041_openapi_accounts_add_cond_resp_meta_slurm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


