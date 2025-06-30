# V0041OpenapiDiagRespStatisticsPendingRpcsInner

Pending RPCs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of pending RPCs queued | 
**message_type** | **str** | Message type as string | 
**type_id** | **int** | Message type as integer | 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_diag_resp_statistics_pending_rpcs_inner import V0041OpenapiDiagRespStatisticsPendingRpcsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiDiagRespStatisticsPendingRpcsInner from a JSON string
v0041_openapi_diag_resp_statistics_pending_rpcs_inner_instance = V0041OpenapiDiagRespStatisticsPendingRpcsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiDiagRespStatisticsPendingRpcsInner.to_json())

# convert the object into a dict
v0041_openapi_diag_resp_statistics_pending_rpcs_inner_dict = v0041_openapi_diag_resp_statistics_pending_rpcs_inner_instance.to_dict()
# create an instance of V0041OpenapiDiagRespStatisticsPendingRpcsInner from a dict
v0041_openapi_diag_resp_statistics_pending_rpcs_inner_from_dict = V0041OpenapiDiagRespStatisticsPendingRpcsInner.from_dict(v0041_openapi_diag_resp_statistics_pending_rpcs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


