# V0041OpenapiAssocsRespAssociationsInnerMaxTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**V0041OpenapiAssocsRespAssociationsInnerMaxTresGroup**](V0041OpenapiAssocsRespAssociationsInnerMaxTresGroup.md) |  | [optional] 
**minutes** | [**V0041OpenapiAssocsRespAssociationsInnerMaxTresMinutes**](V0041OpenapiAssocsRespAssociationsInnerMaxTresMinutes.md) |  | [optional] 
**per** | [**V0041OpenapiAssocsRespAssociationsInnerMaxTresPer**](V0041OpenapiAssocsRespAssociationsInnerMaxTresPer.md) |  | [optional] 
**total** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | GrpTRES | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_assocs_resp_associations_inner_max_tres import V0041OpenapiAssocsRespAssociationsInnerMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAssocsRespAssociationsInnerMaxTres from a JSON string
v0041_openapi_assocs_resp_associations_inner_max_tres_instance = V0041OpenapiAssocsRespAssociationsInnerMaxTres.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAssocsRespAssociationsInnerMaxTres.to_json())

# convert the object into a dict
v0041_openapi_assocs_resp_associations_inner_max_tres_dict = v0041_openapi_assocs_resp_associations_inner_max_tres_instance.to_dict()
# create an instance of V0041OpenapiAssocsRespAssociationsInnerMaxTres from a dict
v0041_openapi_assocs_resp_associations_inner_max_tres_from_dict = V0041OpenapiAssocsRespAssociationsInnerMaxTres.from_dict(v0041_openapi_assocs_resp_associations_inner_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


