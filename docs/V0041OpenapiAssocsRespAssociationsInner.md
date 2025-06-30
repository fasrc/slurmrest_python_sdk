# V0041OpenapiAssocsRespAssociationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account | [optional] 
**accounting** | [**List[V0041OpenapiAssocsRespAssociationsInnerAccountingInner]**](V0041OpenapiAssocsRespAssociationsInnerAccountingInner.md) | Accounting records containing related resource usage | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**comment** | **str** | Arbitrary comment | [optional] 
**default** | [**V0041OpenapiAssocsRespAssociationsInnerDefault**](V0041OpenapiAssocsRespAssociationsInnerDefault.md) |  | [optional] 
**flags** | **List[str]** | Flags on the association | [optional] 
**id** | **int** | Unique ID | [optional] 
**is_default** | **bool** | Is default association for user | [optional] 
**lineage** | **str** | Complete path up the hierarchy to the root association | [optional] 
**max** | [**V0041OpenapiAssocsRespAssociationsInnerMax**](V0041OpenapiAssocsRespAssociationsInnerMax.md) |  | [optional] 
**min** | [**V0041OpenapiAssocsRespAssociationsInnerMin**](V0041OpenapiAssocsRespAssociationsInnerMin.md) |  | [optional] 
**parent_account** | **str** | Name of parent account | [optional] 
**partition** | **str** | Partition name | [optional] 
**priority** | [**V0041OpenapiAccountsAddCondRespAssociationConditionAssociationPriority**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationPriority.md) |  | [optional] 
**qos** | **List[str]** | List of available QOS names | [optional] 
**shares_raw** | **int** | Allocated shares used for fairshare calculation | [optional] 
**user** | **str** | User name | 

## Example

```python
from openapi_client.models.v0041_openapi_assocs_resp_associations_inner import V0041OpenapiAssocsRespAssociationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAssocsRespAssociationsInner from a JSON string
v0041_openapi_assocs_resp_associations_inner_instance = V0041OpenapiAssocsRespAssociationsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAssocsRespAssociationsInner.to_json())

# convert the object into a dict
v0041_openapi_assocs_resp_associations_inner_dict = v0041_openapi_assocs_resp_associations_inner_instance.to_dict()
# create an instance of V0041OpenapiAssocsRespAssociationsInner from a dict
v0041_openapi_assocs_resp_associations_inner_from_dict = V0041OpenapiAssocsRespAssociationsInner.from_dict(v0041_openapi_assocs_resp_associations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


