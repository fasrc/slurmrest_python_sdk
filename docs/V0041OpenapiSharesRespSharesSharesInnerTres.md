# V0041OpenapiSharesRespSharesSharesInnerTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_minutes** | [**List[V0041OpenapiSharesRespSharesSharesInnerTresGroupMinutesInner]**](V0041OpenapiSharesRespSharesSharesInnerTresGroupMinutesInner.md) | TRES-minute limit | [optional] 
**run_seconds** | [**List[V0041OpenapiSharesRespSharesSharesInnerTresGroupMinutesInner]**](V0041OpenapiSharesRespSharesSharesInnerTresGroupMinutesInner.md) | Currently running tres-secs &#x3D; grp_used_tres_run_secs | [optional] 
**usage** | [**List[V0041OpenapiSharesRespSharesSharesInnerTresUsageInner]**](V0041OpenapiSharesRespSharesSharesInnerTresUsageInner.md) | Measure of each TRES usage | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_shares_resp_shares_shares_inner_tres import V0041OpenapiSharesRespSharesSharesInnerTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSharesRespSharesSharesInnerTres from a JSON string
v0041_openapi_shares_resp_shares_shares_inner_tres_instance = V0041OpenapiSharesRespSharesSharesInnerTres.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSharesRespSharesSharesInnerTres.to_json())

# convert the object into a dict
v0041_openapi_shares_resp_shares_shares_inner_tres_dict = v0041_openapi_shares_resp_shares_shares_inner_tres_instance.to_dict()
# create an instance of V0041OpenapiSharesRespSharesSharesInnerTres from a dict
v0041_openapi_shares_resp_shares_shares_inner_tres_from_dict = V0041OpenapiSharesRespSharesSharesInnerTres.from_dict(v0041_openapi_shares_resp_shares_shares_inner_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


