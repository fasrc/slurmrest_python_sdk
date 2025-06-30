# V0041OpenapiSlurmdbdJobsRespJobsInnerTimeUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microseconds** | **int** | User CPU time used by the job in microseconds | [optional] 
**seconds** | **int** | User CPU time used by the job in seconds | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_user import V0041OpenapiSlurmdbdJobsRespJobsInnerTimeUser

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTimeUser from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_user_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerTimeUser.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerTimeUser.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_user_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_user_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTimeUser from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_user_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerTimeUser.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


