# V0041OpenapiClustersRespClustersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associations** | [**V0041OpenapiClustersRespClustersInnerAssociations**](V0041OpenapiClustersRespClustersInnerAssociations.md) |  | [optional] 
**controller** | [**V0041OpenapiClustersRespClustersInnerController**](V0041OpenapiClustersRespClustersInnerController.md) |  | [optional] 
**flags** | **List[str]** | Flags | [optional] 
**name** | **str** | ClusterName | [optional] 
**nodes** | **str** | Node names | [optional] 
**rpc_version** | **int** | RPC version used in the cluster | [optional] 
**select_plugin** | **str** |  | [optional] 
**tres** | [**List[V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner]**](V0041OpenapiAccountsAddCondRespAssociationConditionAssociationGrptresInner.md) | Trackable resources | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_clusters_resp_clusters_inner import V0041OpenapiClustersRespClustersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiClustersRespClustersInner from a JSON string
v0041_openapi_clusters_resp_clusters_inner_instance = V0041OpenapiClustersRespClustersInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiClustersRespClustersInner.to_json())

# convert the object into a dict
v0041_openapi_clusters_resp_clusters_inner_dict = v0041_openapi_clusters_resp_clusters_inner_instance.to_dict()
# create an instance of V0041OpenapiClustersRespClustersInner from a dict
v0041_openapi_clusters_resp_clusters_inner_from_dict = V0041OpenapiClustersRespClustersInner.from_dict(v0041_openapi_clusters_resp_clusters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


