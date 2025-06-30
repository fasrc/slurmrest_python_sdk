# V0041OpenapiKillJobsRespStatusInnerError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Numeric error encountered signaling job | [optional] 
**message** | **str** | Error message why signaling job failed | [optional] 
**string** | **str** | String error encountered signaling job | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_kill_jobs_resp_status_inner_error import V0041OpenapiKillJobsRespStatusInnerError

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiKillJobsRespStatusInnerError from a JSON string
v0041_openapi_kill_jobs_resp_status_inner_error_instance = V0041OpenapiKillJobsRespStatusInnerError.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiKillJobsRespStatusInnerError.to_json())

# convert the object into a dict
v0041_openapi_kill_jobs_resp_status_inner_error_dict = v0041_openapi_kill_jobs_resp_status_inner_error_instance.to_dict()
# create an instance of V0041OpenapiKillJobsRespStatusInnerError from a dict
v0041_openapi_kill_jobs_resp_status_inner_error_from_dict = V0041OpenapiKillJobsRespStatusInnerError.from_dict(v0041_openapi_kill_jobs_resp_status_inner_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


