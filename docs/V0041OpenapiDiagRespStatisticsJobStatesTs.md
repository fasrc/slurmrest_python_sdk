# V0041OpenapiDiagRespStatisticsJobStatesTs

When the job state counts were gathered (UNIX timestamp)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 
**set** | **bool** | True if number has been set; False if number is unset | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_diag_resp_statistics_job_states_ts import V0041OpenapiDiagRespStatisticsJobStatesTs

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiDiagRespStatisticsJobStatesTs from a JSON string
v0041_openapi_diag_resp_statistics_job_states_ts_instance = V0041OpenapiDiagRespStatisticsJobStatesTs.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiDiagRespStatisticsJobStatesTs.to_json())

# convert the object into a dict
v0041_openapi_diag_resp_statistics_job_states_ts_dict = v0041_openapi_diag_resp_statistics_job_states_ts_instance.to_dict()
# create an instance of V0041OpenapiDiagRespStatisticsJobStatesTs from a dict
v0041_openapi_diag_resp_statistics_job_states_ts_from_dict = V0041OpenapiDiagRespStatisticsJobStatesTs.from_dict(v0041_openapi_diag_resp_statistics_job_states_ts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


