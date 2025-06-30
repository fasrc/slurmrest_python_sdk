# V0041OpenapiAccountsAddCondRespAssociationConditionAssociation

Association limits and options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Arbitrary comment | [optional] 
**defaultqos** | **str** | Default QOS | [optional] 
**fairshare** | **int** | Allocated shares used for fairshare calculation | [optional] 
**grpjobs** | [**V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpjobs**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpjobs.md) |  | [optional] 
**grpjobsaccrue** | [**V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpjobsaccrue**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpjobsaccrue.md) |  | [optional] 
**grpsubmitjobs** | [**V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpsubmitjobs**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpsubmitjobs.md) |  | [optional] 
**grptres** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | Maximum number of TRES able to be allocated by running jobs in this association and its children | [optional] 
**grptresmins** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | Total number of TRES minutes that can possibly be used by past, present and future jobs in this association and its children | [optional] 
**grptresrunmins** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | Maximum number of TRES minutes able to be allocated by running jobs in this association and its children | [optional] 
**grpwall** | [**V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpwall**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrpwall.md) |  | [optional] 
**maxjobs** | [**V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxjobs**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxjobs.md) |  | [optional] 
**maxjobsaccrue** | [**V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxjobsaccrue**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxjobsaccrue.md) |  | [optional] 
**maxsubmitjobs** | [**V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxsubmitjobs**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxsubmitjobs.md) |  | [optional] 
**maxtresminsperjob** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | Maximum number of TRES minutes each job is able to use in this association | [optional] 
**maxtresperjob** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | Maximum number of TRES each job is able to use in this association | [optional] 
**maxtrespernode** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | Maximum number of TRES each node is able to use | [optional] 
**maxtresrunmins** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | Maximum number of TRES minutes able to be allocated by running jobs in this association | [optional] 
**maxwalldurationperjob** | [**V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxwalldurationperjob**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMaxwalldurationperjob.md) |  | [optional] 
**minpriothresh** | [**V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMinpriothresh**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationMinpriothresh.md) |  | [optional] 
**parent** | **str** | Name of parent account | [optional] 
**priority** | [**V0041OpenapiAccountsAddCondRespAssociationConditionAssociationPriority**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationPriority.md) |  | [optional] 
**qoslevel** | **List[str]** | List of available QOS names | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_accounts_add_cond_resp_association_condition_association import V0041OpenapiAccountsAddCondRespAssociationConditionAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsAddCondRespAssociationConditionAssociation from a JSON string
v0041_openapi_accounts_add_cond_resp_association_condition_association_instance = V0041OpenapiAccountsAddCondRespAssociationConditionAssociation.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsAddCondRespAssociationConditionAssociation.to_json())

# convert the object into a dict
v0041_openapi_accounts_add_cond_resp_association_condition_association_dict = v0041_openapi_accounts_add_cond_resp_association_condition_association_instance.to_dict()
# create an instance of V0041OpenapiAccountsAddCondRespAssociationConditionAssociation from a dict
v0041_openapi_accounts_add_cond_resp_association_condition_association_from_dict = V0041OpenapiAccountsAddCondRespAssociationConditionAssociation.from_dict(v0041_openapi_accounts_add_cond_resp_association_condition_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


