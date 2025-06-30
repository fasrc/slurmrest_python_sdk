# V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minutes** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes.md) |  | [optional] 
**per** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresPer**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresPer.md) |  | [optional] 
**total** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | GrpTRES | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTres from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_instance = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTres.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTres.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTres from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_from_dict = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTres.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


