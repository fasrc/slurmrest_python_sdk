# V0041OpenapiAccountsAddCondRespErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Long form error description | [optional] 
**error** | **str** | Short form error description | [optional] 
**error_number** | **int** | Slurm numeric error identifier | [optional] 
**source** | **str** | Source of error or where error was first detected | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_accounts_add_cond_resp_errors_inner import V0041OpenapiAccountsAddCondRespErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsAddCondRespErrorsInner from a JSON string
v0041_openapi_accounts_add_cond_resp_errors_inner_instance = V0041OpenapiAccountsAddCondRespErrorsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsAddCondRespErrorsInner.to_json())

# convert the object into a dict
v0041_openapi_accounts_add_cond_resp_errors_inner_dict = v0041_openapi_accounts_add_cond_resp_errors_inner_instance.to_dict()
# create an instance of V0041OpenapiAccountsAddCondRespErrorsInner from a dict
v0041_openapi_accounts_add_cond_resp_errors_inner_from_dict = V0041OpenapiAccountsAddCondRespErrorsInner.from_dict(v0041_openapi_accounts_add_cond_resp_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


