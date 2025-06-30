# V0041OpenapiSlurmdbdConfigResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[V0041OpenapiAccountsRespAccountsInner]**](V0041OpenapiAccountsRespAccountsInner.md) | Accounts | [optional] 
**associations** | [**List[V0041OpenapiAssocsRespAssociationsInner]**](V0041OpenapiAssocsRespAssociationsInner.md) | Associations | [optional] 
**clusters** | [**List[V0041OpenapiClustersRespClustersInner]**](V0041OpenapiClustersRespClustersInner.md) | Clusters | [optional] 
**errors** | [**List[V0041OpenapiAccountsAddCondRespErrorsInner]**](V0041OpenapiAccountsAddCondRespErrorsInner.md) | Query errors | [optional] 
**instances** | [**List[V0041OpenapiInstancesRespInstancesInner]**](V0041OpenapiInstancesRespInstancesInner.md) | Instances | [optional] 
**meta** | [**V0041OpenapiAccountsAddCondRespMeta**](V0041OpenapiAccountsAddCondRespMeta.md) |  | [optional] 
**qos** | [**List[V0041OpenapiSlurmdbdConfigRespQosInner]**](V0041OpenapiSlurmdbdConfigRespQosInner.md) | QOS | [optional] 
**tres** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | TRES | [optional] 
**users** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInner]**](V0041OpenapiSlurmdbdConfigRespUsersInner.md) | Users | [optional] 
**warnings** | [**List[V0041OpenapiAccountsAddCondRespWarningsInner]**](V0041OpenapiAccountsAddCondRespWarningsInner.md) | Query warnings | [optional] 
**wckeys** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner]**](V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner.md) | WCKeys | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_config_resp import V0041OpenapiSlurmdbdConfigResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigResp from a JSON string
v0041_openapi_slurmdbd_config_resp_instance = V0041OpenapiSlurmdbdConfigResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigResp.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_dict = v0041_openapi_slurmdbd_config_resp_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigResp from a dict
v0041_openapi_slurmdbd_config_resp_from_dict = V0041OpenapiSlurmdbdConfigResp.from_dict(v0041_openapi_slurmdbd_config_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


