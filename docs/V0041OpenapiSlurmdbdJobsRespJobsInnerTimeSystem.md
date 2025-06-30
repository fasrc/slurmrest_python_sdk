# V0041OpenapiSlurmdbdJobsRespJobsInnerTimeSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microseconds** | **int** | System CPU time used by the job in microseconds | [optional] 
**seconds** | **int** | System CPU time used by the job in seconds | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_system import V0041OpenapiSlurmdbdJobsRespJobsInnerTimeSystem

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTimeSystem from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_system_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerTimeSystem.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerTimeSystem.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_system_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_system_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTimeSystem from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_system_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerTimeSystem.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


