# V0041OpenapiKillJobsRespStatusInner

List of jobs signal responses

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**V0041OpenapiKillJobsRespStatusInnerError**](V0041OpenapiKillJobsRespStatusInnerError.md) |  | [optional] 
**federation** | [**V0041OpenapiKillJobsRespStatusInnerFederation**](V0041OpenapiKillJobsRespStatusInnerFederation.md) |  | [optional] 
**job_id** | [**V0041OpenapiKillJobsRespStatusInnerJobId**](V0041OpenapiKillJobsRespStatusInnerJobId.md) |  | 
**step_id** | **str** | Job or Step ID that signaling failed | 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_kill_jobs_resp_status_inner import V0041OpenapiKillJobsRespStatusInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiKillJobsRespStatusInner from a JSON string
v0041_openapi_kill_jobs_resp_status_inner_instance = V0041OpenapiKillJobsRespStatusInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiKillJobsRespStatusInner.to_json())

# convert the object into a dict
v0041_openapi_kill_jobs_resp_status_inner_dict = v0041_openapi_kill_jobs_resp_status_inner_instance.to_dict()
# create an instance of V0041OpenapiKillJobsRespStatusInner from a dict
v0041_openapi_kill_jobs_resp_status_inner_from_dict = V0041OpenapiKillJobsRespStatusInner.from_dict(v0041_openapi_kill_jobs_resp_status_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


