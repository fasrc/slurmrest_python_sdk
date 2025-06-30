# V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES

Trackable resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | TRES count (0 if listed generically) | [optional] 
**id** | **int** | ID used in database | [optional] 
**name** | **str** | TRES name (if applicable) | [optional] 
**type** | **str** | TRES type (CPU, MEM, etc) | 

## Example

```python
from openapi_client.models.v0041_openapi_assocs_resp_associations_inner_accounting_inner_tres import V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES from a JSON string
v0041_openapi_assocs_resp_associations_inner_accounting_inner_tres_instance = V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES.to_json())

# convert the object into a dict
v0041_openapi_assocs_resp_associations_inner_accounting_inner_tres_dict = v0041_openapi_assocs_resp_associations_inner_accounting_inner_tres_instance.to_dict()
# create an instance of V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES from a dict
v0041_openapi_assocs_resp_associations_inner_accounting_inner_tres_from_dict = V0041OpenapiAssocsRespAssociationsInnerAccountingInnerTRES.from_dict(v0041_openapi_assocs_resp_associations_inner_accounting_inner_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


