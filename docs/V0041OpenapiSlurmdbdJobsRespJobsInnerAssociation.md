# V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation

Unique identifier for the association

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
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association import V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


