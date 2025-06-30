# V0041OpenapiAssocsRespAssociationsInnerMaxJobsPerCount

GrpJobs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 
**set** | **bool** | True if number has been set; False if number is unset | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_assocs_resp_associations_inner_max_jobs_per_count import V0041OpenapiAssocsRespAssociationsInnerMaxJobsPerCount

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAssocsRespAssociationsInnerMaxJobsPerCount from a JSON string
v0041_openapi_assocs_resp_associations_inner_max_jobs_per_count_instance = V0041OpenapiAssocsRespAssociationsInnerMaxJobsPerCount.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAssocsRespAssociationsInnerMaxJobsPerCount.to_json())

# convert the object into a dict
v0041_openapi_assocs_resp_associations_inner_max_jobs_per_count_dict = v0041_openapi_assocs_resp_associations_inner_max_jobs_per_count_instance.to_dict()
# create an instance of V0041OpenapiAssocsRespAssociationsInnerMaxJobsPerCount from a dict
v0041_openapi_assocs_resp_associations_inner_max_jobs_per_count_from_dict = V0041OpenapiAssocsRespAssociationsInnerMaxJobsPerCount.from_dict(v0041_openapi_assocs_resp_associations_inner_max_jobs_per_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


