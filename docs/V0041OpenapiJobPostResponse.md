# V0041OpenapiJobPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[V0041OpenapiAccountsAddCondRespErrorsInner]**](V0041OpenapiAccountsAddCondRespErrorsInner.md) | Query errors | [optional] 
**job_id** | **str** | First updated Job ID - Use results instead | [optional] 
**job_submit_user_msg** | **str** | First updated Job submission user message - Use results instead | [optional] 
**meta** | [**V0041OpenapiAccountsAddCondRespMeta**](V0041OpenapiAccountsAddCondRespMeta.md) |  | [optional] 
**results** | [**List[V0041OpenapiJobPostResponseResultsInner]**](V0041OpenapiJobPostResponseResultsInner.md) | Job update results | [optional] 
**step_id** | **str** | First updated Step ID - Use results instead | [optional] 
**warnings** | [**List[V0041OpenapiAccountsAddCondRespWarningsInner]**](V0041OpenapiAccountsAddCondRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_job_post_response import V0041OpenapiJobPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobPostResponse from a JSON string
v0041_openapi_job_post_response_instance = V0041OpenapiJobPostResponse.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobPostResponse.to_json())

# convert the object into a dict
v0041_openapi_job_post_response_dict = v0041_openapi_job_post_response_instance.to_dict()
# create an instance of V0041OpenapiJobPostResponse from a dict
v0041_openapi_job_post_response_from_dict = V0041OpenapiJobPostResponse.from_dict(v0041_openapi_job_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


