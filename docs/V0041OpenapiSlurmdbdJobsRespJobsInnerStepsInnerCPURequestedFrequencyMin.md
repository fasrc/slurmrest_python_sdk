# V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequencyMin

Minimum requested CPU frequency in kHz

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 
**set** | **bool** | True if number has been set; False if number is unset | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency_min import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequencyMin

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequencyMin from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency_min_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequencyMin.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequencyMin.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency_min_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency_min_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequencyMin from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency_min_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerCPURequestedFrequencyMin.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency_min_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


