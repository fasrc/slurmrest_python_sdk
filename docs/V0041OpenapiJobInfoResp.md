# V0041OpenapiJobInfoResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[V0041OpenapiAccountsAddCondRespErrorsInner]**](V0041OpenapiAccountsAddCondRespErrorsInner.md) | Query errors | [optional] 
**jobs** | [**List[V0041OpenapiJobInfoRespJobsInner]**](V0041OpenapiJobInfoRespJobsInner.md) | List of jobs | 
**last_backfill** | [**V0041OpenapiJobInfoRespLastBackfill**](V0041OpenapiJobInfoRespLastBackfill.md) |  | 
**last_update** | [**V0041OpenapiJobInfoRespLastUpdate**](V0041OpenapiJobInfoRespLastUpdate.md) |  | 
**meta** | [**V0041OpenapiAccountsAddCondRespMeta**](V0041OpenapiAccountsAddCondRespMeta.md) |  | [optional] 
**warnings** | [**List[V0041OpenapiAccountsAddCondRespWarningsInner]**](V0041OpenapiAccountsAddCondRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_job_info_resp import V0041OpenapiJobInfoResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobInfoResp from a JSON string
v0041_openapi_job_info_resp_instance = V0041OpenapiJobInfoResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobInfoResp.to_json())

# convert the object into a dict
v0041_openapi_job_info_resp_dict = v0041_openapi_job_info_resp_instance.to_dict()
# create an instance of V0041OpenapiJobInfoResp from a dict
v0041_openapi_job_info_resp_from_dict = V0041OpenapiJobInfoResp.from_dict(v0041_openapi_job_info_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


