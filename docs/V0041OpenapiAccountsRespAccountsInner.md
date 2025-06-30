# V0041OpenapiAccountsRespAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associations** | [**List[V0041OpenapiAccountsRespAccountsInnerAssociationsInner]**](V0041OpenapiAccountsRespAccountsInnerAssociationsInner.md) | Associations involving this account (only populated if requested) | [optional] 
**coordinators** | [**List[V0041OpenapiAccountsRespAccountsInnerCoordinatorsInner]**](V0041OpenapiAccountsRespAccountsInnerCoordinatorsInner.md) | List of users that are a coordinator of this account (only populated if requested) | [optional] 
**description** | **str** | Arbitrary string describing the account | 
**flags** | **List[str]** | Flags associated with the account | [optional] 
**name** | **str** | Account name | 
**organization** | **str** | Organization to which the account belongs | 

## Example

```python
from openapi_client.models.v0041_openapi_accounts_resp_accounts_inner import V0041OpenapiAccountsRespAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsRespAccountsInner from a JSON string
v0041_openapi_accounts_resp_accounts_inner_instance = V0041OpenapiAccountsRespAccountsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsRespAccountsInner.to_json())

# convert the object into a dict
v0041_openapi_accounts_resp_accounts_inner_dict = v0041_openapi_accounts_resp_accounts_inner_instance.to_dict()
# create an instance of V0041OpenapiAccountsRespAccountsInner from a dict
v0041_openapi_accounts_resp_accounts_inner_from_dict = V0041OpenapiAccountsRespAccountsInner.from_dict(v0041_openapi_accounts_resp_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


