# V0041OpenapiSlurmdbdConfigRespQosInnerPreempt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exempt_time** | [**V0041OpenapiSlurmdbdConfigRespQosInnerPreemptExemptTime**](V0041OpenapiSlurmdbdConfigRespQosInnerPreemptExemptTime.md) |  | [optional] 
**list** | **List[str]** | Other QOS&#39;s this QOS can preempt | [optional] 
**mode** | **List[str]** | PreemptMode | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_config_resp_qos_inner_preempt import V0041OpenapiSlurmdbdConfigRespQosInnerPreempt

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerPreempt from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_preempt_instance = V0041OpenapiSlurmdbdConfigRespQosInnerPreempt.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInnerPreempt.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_preempt_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_preempt_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerPreempt from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_preempt_from_dict = V0041OpenapiSlurmdbdConfigRespQosInnerPreempt.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_preempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


