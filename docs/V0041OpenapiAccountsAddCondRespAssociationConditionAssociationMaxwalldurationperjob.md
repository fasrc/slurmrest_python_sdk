# V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxwalldurationperjob

Maximum wall clock time each job is able to use in this association

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 
**set** | **bool** | True if number has been set; False if number is unset | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_accounts_add_cond_resp_association_condition_association_maxwalldurationperjob import V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxwalldurationperjob

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxwalldurationperjob from a JSON string
v0041_openapi_accounts_add_cond_resp_association_condition_association_maxwalldurationperjob_instance = V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxwalldurationperjob.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxwalldurationperjob.to_json())

# convert the object into a dict
v0041_openapi_accounts_add_cond_resp_association_condition_association_maxwalldurationperjob_dict = v0041_openapi_accounts_add_cond_resp_association_condition_association_maxwalldurationperjob_instance.to_dict()
# create an instance of V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxwalldurationperjob from a dict
v0041_openapi_accounts_add_cond_resp_association_condition_association_maxwalldurationperjob_from_dict = V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxwalldurationperjob.from_dict(v0041_openapi_accounts_add_cond_resp_association_condition_association_maxwalldurationperjob_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


