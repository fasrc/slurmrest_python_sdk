# V0041OpenapiSlurmdbdJobsRespJobsInnerTimeTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**microseconds** | **int** | Sum of System and User CPU time used by the job in microseconds | [optional] 
**seconds** | **int** | Sum of System and User CPU time used by the job in seconds | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_total import V0041OpenapiSlurmdbdJobsRespJobsInnerTimeTotal

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTimeTotal from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_total_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerTimeTotal.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerTimeTotal.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_total_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_total_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTimeTotal from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_total_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerTimeTotal.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


