# V0041OpenapiAssocsRespAssociationsInnerAccountingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tres** | [**V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES**](V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES.md) |  | [optional] 
**allocated** | [**V0041OpenapiAssocsRespAssociationsInnerAccountingInnerAllocated**](V0041OpenapiAssocsRespAssociationsInnerAccountingInnerAllocated.md) |  | [optional] 
**id** | **int** | Association ID or Workload characterization key ID | [optional] 
**start** | **int** | When the record was started | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_assocs_resp_associations_inner_accounting_inner import V0041OpenapiAssocsRespAssociationsInnerAccountingInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAssocsRespAssociationsInnerAccountingInner from a JSON string
v0041_openapi_assocs_resp_associations_inner_accounting_inner_instance = V0041OpenapiAssocsRespAssociationsInnerAccountingInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAssocsRespAssociationsInnerAccountingInner.to_json())

# convert the object into a dict
v0041_openapi_assocs_resp_associations_inner_accounting_inner_dict = v0041_openapi_assocs_resp_associations_inner_accounting_inner_instance.to_dict()
# create an instance of V0041OpenapiAssocsRespAssociationsInnerAccountingInner from a dict
v0041_openapi_assocs_resp_associations_inner_accounting_inner_from_dict = V0041OpenapiAssocsRespAssociationsInnerAccountingInner.from_dict(v0041_openapi_assocs_resp_associations_inner_accounting_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


