# V0041OpenapiSlurmdbdStatsRespStatisticsRollups

Rollup statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily** | [**V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily**](V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily.md) |  | [optional] 
**hourly** | [**V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly**](V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly.md) |  | [optional] 
**monthly** | [**V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly**](V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly.md) |  | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups import V0041OpenapiSlurmdbdStatsRespStatisticsRollups

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollups from a JSON string
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_instance = V0041OpenapiSlurmdbdStatsRespStatisticsRollups.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdStatsRespStatisticsRollups.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_dict = v0041_openapi_slurmdbd_stats_resp_statistics_rollups_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollups from a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_from_dict = V0041OpenapiSlurmdbdStatsRespStatisticsRollups.from_dict(v0041_openapi_slurmdbd_stats_resp_statistics_rollups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


