# V0041OpenapiJobInfoRespJobsInnerDerivedExitCode

Highest exit code of all job steps

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_code** | [**V0041OpenapiJobInfoRespJobsInnerDerivedExitCodeReturnCode**](V0041OpenapiJobInfoRespJobsInnerDerivedExitCodeReturnCode.md) |  | [optional] 
**signal** | [**V0041OpenapiJobInfoRespJobsInnerDerivedExitCodeSignal**](V0041OpenapiJobInfoRespJobsInnerDerivedExitCodeSignal.md) |  | [optional] 
**status** | **List[str]** | Status given by return code | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_job_info_resp_jobs_inner_derived_exit_code import V0041OpenapiJobInfoRespJobsInnerDerivedExitCode

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobInfoRespJobsInnerDerivedExitCode from a JSON string
v0041_openapi_job_info_resp_jobs_inner_derived_exit_code_instance = V0041OpenapiJobInfoRespJobsInnerDerivedExitCode.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobInfoRespJobsInnerDerivedExitCode.to_json())

# convert the object into a dict
v0041_openapi_job_info_resp_jobs_inner_derived_exit_code_dict = v0041_openapi_job_info_resp_jobs_inner_derived_exit_code_instance.to_dict()
# create an instance of V0041OpenapiJobInfoRespJobsInnerDerivedExitCode from a dict
v0041_openapi_job_info_resp_jobs_inner_derived_exit_code_from_dict = V0041OpenapiJobInfoRespJobsInnerDerivedExitCode.from_dict(v0041_openapi_job_info_resp_jobs_inner_derived_exit_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


