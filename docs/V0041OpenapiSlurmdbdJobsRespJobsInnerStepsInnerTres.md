# V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | Trackable resources allocated to the step | [optional] 
**consumed** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresConsumed**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresConsumed.md) |  | [optional] 
**requested** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequested**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequested.md) |  | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTres from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTres.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTres.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTres from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTres.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


