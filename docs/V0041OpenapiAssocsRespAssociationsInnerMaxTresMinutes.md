# V0041OpenapiAssocsRespAssociationsInnerMaxTresMinutes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per** | [**V0041OpenapiAssocsRespAssociationsInnerMaxTresMinutesPer**](V0041OpenapiAssocsRespAssociationsInnerMaxTresMinutesPer.md) |  | [optional] 
**total** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | MaxTRESMinsPerJob | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_assocs_resp_associations_inner_max_tres_minutes import V0041OpenapiAssocsRespAssociationsInnerMaxTresMinutes

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAssocsRespAssociationsInnerMaxTresMinutes from a JSON string
v0041_openapi_assocs_resp_associations_inner_max_tres_minutes_instance = V0041OpenapiAssocsRespAssociationsInnerMaxTresMinutes.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAssocsRespAssociationsInnerMaxTresMinutes.to_json())

# convert the object into a dict
v0041_openapi_assocs_resp_associations_inner_max_tres_minutes_dict = v0041_openapi_assocs_resp_associations_inner_max_tres_minutes_instance.to_dict()
# create an instance of V0041OpenapiAssocsRespAssociationsInnerMaxTresMinutes from a dict
v0041_openapi_assocs_resp_associations_inner_max_tres_minutes_from_dict = V0041OpenapiAssocsRespAssociationsInnerMaxTresMinutes.from_dict(v0041_openapi_assocs_resp_associations_inner_max_tres_minutes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


