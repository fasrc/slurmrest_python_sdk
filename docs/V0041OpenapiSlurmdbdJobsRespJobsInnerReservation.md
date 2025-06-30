# V0041OpenapiSlurmdbdJobsRespJobsInnerReservation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of requested reservation | [optional] 
**name** | **str** | Name of reservation to use | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_reservation import V0041OpenapiSlurmdbdJobsRespJobsInnerReservation

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerReservation from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_reservation_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerReservation.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerReservation.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_reservation_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_reservation_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerReservation from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_reservation_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerReservation.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


