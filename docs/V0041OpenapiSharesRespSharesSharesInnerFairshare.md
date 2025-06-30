# V0041OpenapiSharesRespSharesSharesInnerFairshare


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor** | **float** | Fairshare factor | [optional] 
**level** | **float** | Fairshare factor at this level; stored on an assoc as a long double, but that is not needed for display in sshare | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner_fairshare import V0041OpenapiSharesRespSharesSharesInnerFairshare

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSharesRespSharesSharesInnerFairshare from a JSON string
v0041_openapi_shares_resp_shares_shares_inner_fairshare_instance = V0041OpenapiSharesRespSharesSharesInnerFairshare.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSharesRespSharesSharesInnerFairshare.to_json())

# convert the object into a dict
v0041_openapi_shares_resp_shares_shares_inner_fairshare_dict = v0041_openapi_shares_resp_shares_shares_inner_fairshare_instance.to_dict()
# create an instance of V0041OpenapiSharesRespSharesSharesInnerFairshare from a dict
v0041_openapi_shares_resp_shares_shares_inner_fairshare_from_dict = V0041OpenapiSharesRespSharesSharesInnerFairshare.from_dict(v0041_openapi_shares_resp_shares_shares_inner_fairshare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


