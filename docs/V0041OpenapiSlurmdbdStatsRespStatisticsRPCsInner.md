# V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of RPCs processed | [optional] 
**rpc** | **str** | RPC type | [optional] 
**time** | [**V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInnerTime**](V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInnerTime.md) |  | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_stats_resp_statistics_rpcs_inner import V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInner from a JSON string
v0041_openapi_slurmdbd_stats_resp_statistics_rpcs_inner_instance = V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rpcs_inner_dict = v0041_openapi_slurmdbd_stats_resp_statistics_rpcs_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInner from a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rpcs_inner_from_dict = V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInner.from_dict(v0041_openapi_slurmdbd_stats_resp_statistics_rpcs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


