# V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**V0041OpenapiAssocsRespAssociationsInnerMaxJobsPerWallClock**](V0041OpenapiAssocsRespAssociationsInnerMaxJobsPerWallClock.md) |  | [optional] 
**qos** | [**V0041OpenapiAssocsRespAssociationsInnerMaxPerAccountWallClock**](V0041OpenapiAssocsRespAssociationsInnerMaxPerAccountWallClock.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_instance = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_from_dict = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPer.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


