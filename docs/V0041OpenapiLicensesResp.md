# V0041OpenapiLicensesResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[V0041OpenapiAccountsAddCondRespErrorsInner]**](V0041OpenapiAccountsAddCondRespErrorsInner.md) | Query errors | [optional] 
**last_update** | [**V0041OpenapiLicensesRespLastUpdate**](V0041OpenapiLicensesRespLastUpdate.md) |  | 
**licenses** | [**List[V0041OpenapiLicensesRespLicensesInner]**](V0041OpenapiLicensesRespLicensesInner.md) | List of licenses | 
**meta** | [**V0041OpenapiAccountsAddCondRespMeta**](V0041OpenapiAccountsAddCondRespMeta.md) |  | [optional] 
**warnings** | [**List[V0041OpenapiAccountsAddCondRespWarningsInner]**](V0041OpenapiAccountsAddCondRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_licenses_resp import V0041OpenapiLicensesResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiLicensesResp from a JSON string
v0041_openapi_licenses_resp_instance = V0041OpenapiLicensesResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiLicensesResp.to_json())

# convert the object into a dict
v0041_openapi_licenses_resp_dict = v0041_openapi_licenses_resp_instance.to_dict()
# create an instance of V0041OpenapiLicensesResp from a dict
v0041_openapi_licenses_resp_from_dict = V0041OpenapiLicensesResp.from_dict(v0041_openapi_licenses_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


