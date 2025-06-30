# V0041OpenapiAssocsRespAssociationsInnerMaxJobsActive

MaxJobs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 
**set** | **bool** | True if number has been set; False if number is unset | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_assocs_resp_associations_inner_max_jobs_active import V0041OpenapiAssocsRespAssociationsInnerMaxJobsActive

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAssocsRespAssociationsInnerMaxJobsActive from a JSON string
v0041_openapi_assocs_resp_associations_inner_max_jobs_active_instance = V0041OpenapiAssocsRespAssociationsInnerMaxJobsActive.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAssocsRespAssociationsInnerMaxJobsActive.to_json())

# convert the object into a dict
v0041_openapi_assocs_resp_associations_inner_max_jobs_active_dict = v0041_openapi_assocs_resp_associations_inner_max_jobs_active_instance.to_dict()
# create an instance of V0041OpenapiAssocsRespAssociationsInnerMaxJobsActive from a dict
v0041_openapi_assocs_resp_associations_inner_max_jobs_active_from_dict = V0041OpenapiAssocsRespAssociationsInnerMaxJobsActive.from_dict(v0041_openapi_assocs_resp_associations_inner_max_jobs_active_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


