# V0041OpenapiSlurmdbdStatsRespStatistics

statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rpcs** | [**List[V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInner]**](V0041OpenapiSlurmdbdStatsRespStatisticsRPCsInner.md) | List of RPCs sent to the slurmdbd | [optional] 
**rollups** | [**V0041OpenapiSlurmdbdStatsRespStatisticsRollups**](V0041OpenapiSlurmdbdStatsRespStatisticsRollups.md) |  | [optional] 
**time_start** | **int** | When data collection started (UNIX timestamp) | [optional] 
**users** | [**List[V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner]**](V0041OpenapiSlurmdbdStatsRespStatisticsUsersInner.md) | List of users that issued RPCs | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_stats_resp_statistics import V0041OpenapiSlurmdbdStatsRespStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdStatsRespStatistics from a JSON string
v0041_openapi_slurmdbd_stats_resp_statistics_instance = V0041OpenapiSlurmdbdStatsRespStatistics.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdStatsRespStatistics.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_stats_resp_statistics_dict = v0041_openapi_slurmdbd_stats_resp_statistics_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdStatsRespStatistics from a dict
v0041_openapi_slurmdbd_stats_resp_statistics_from_dict = V0041OpenapiSlurmdbdStatsRespStatistics.from_dict(v0041_openapi_slurmdbd_stats_resp_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


