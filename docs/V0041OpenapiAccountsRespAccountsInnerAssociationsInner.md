# V0041OpenapiAccountsRespAccountsInnerAssociationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account | [optional] 
**cluster** | **str** | Cluster | [optional] 
**id** | **int** | Numeric association ID | [optional] 
**partition** | **str** | Partition | [optional] 
**user** | **str** | User name | 

## Example

```python
from openapi_client.models.v0041_openapi_accounts_resp_accounts_inner_associations_inner import V0041OpenapiAccountsRespAccountsInnerAssociationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsRespAccountsInnerAssociationsInner from a JSON string
v0041_openapi_accounts_resp_accounts_inner_associations_inner_instance = V0041OpenapiAccountsRespAccountsInnerAssociationsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsRespAccountsInnerAssociationsInner.to_json())

# convert the object into a dict
v0041_openapi_accounts_resp_accounts_inner_associations_inner_dict = v0041_openapi_accounts_resp_accounts_inner_associations_inner_instance.to_dict()
# create an instance of V0041OpenapiAccountsRespAccountsInnerAssociationsInner from a dict
v0041_openapi_accounts_resp_accounts_inner_associations_inner_from_dict = V0041OpenapiAccountsRespAccountsInnerAssociationsInner.from_dict(v0041_openapi_accounts_resp_accounts_inner_associations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


