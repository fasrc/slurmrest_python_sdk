# V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpjobsaccrue

Maximum number of pending jobs able to accrue age priority in this association and its children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 
**set** | **bool** | True if number has been set; False if number is unset | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_accounts_add_cond_resp_association_condition_association_grpjobsaccrue import V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpjobsaccrue

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpjobsaccrue from a JSON string
v0041_openapi_accounts_add_cond_resp_association_condition_association_grpjobsaccrue_instance = V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpjobsaccrue.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpjobsaccrue.to_json())

# convert the object into a dict
v0041_openapi_accounts_add_cond_resp_association_condition_association_grpjobsaccrue_dict = v0041_openapi_accounts_add_cond_resp_association_condition_association_grpjobsaccrue_instance.to_dict()
# create an instance of V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpjobsaccrue from a dict
v0041_openapi_accounts_add_cond_resp_association_condition_association_grpjobsaccrue_from_dict = V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpjobsaccrue.from_dict(v0041_openapi_accounts_add_cond_resp_association_condition_association_grpjobsaccrue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


