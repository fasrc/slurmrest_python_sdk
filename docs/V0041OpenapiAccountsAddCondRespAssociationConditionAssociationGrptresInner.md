# V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | TRES count (0 if listed generically) | [optional] 
**id** | **int** | ID used in database | [optional] 
**name** | **str** | TRES name (if applicable) | [optional] 
**type** | **str** | TRES type (CPU, MEM, etc) | 

## Example

```python
from openapi_client.models.v0041_openapi_accounts_add_cond_resp_association_condition_association_grptres_inner import V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner from a JSON string
v0041_openapi_accounts_add_cond_resp_association_condition_association_grptres_inner_instance = V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.to_json())

# convert the object into a dict
v0041_openapi_accounts_add_cond_resp_association_condition_association_grptres_inner_dict = v0041_openapi_accounts_add_cond_resp_association_condition_association_grptres_inner_instance.to_dict()
# create an instance of V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner from a dict
v0041_openapi_accounts_add_cond_resp_association_condition_association_grptres_inner_from_dict = V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.from_dict(v0041_openapi_accounts_add_cond_resp_association_condition_association_grptres_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


