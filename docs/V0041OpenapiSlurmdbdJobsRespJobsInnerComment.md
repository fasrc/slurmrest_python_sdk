# V0041OpenapiSlurmdbdJobsRespJobsInnerComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator** | **str** | Arbitrary comment made by administrator | [optional] 
**job** | **str** | Arbitrary comment made by user | [optional] 
**system** | **str** | Arbitrary comment from slurmctld | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_comment import V0041OpenapiSlurmdbdJobsRespJobsInnerComment

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerComment from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_comment_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerComment.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerComment.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_comment_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_comment_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerComment from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_comment_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerComment.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


