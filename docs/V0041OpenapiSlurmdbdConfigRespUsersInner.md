# V0041OpenapiSlurmdbdConfigRespUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator_level** | **List[str]** | AdminLevel granted to the user | [optional] 
**associations** | [**List[V0041OpenapiAccountsRespAccountsInnerAssociationsInner]**](V0041OpenapiAccountsRespAccountsInnerAssociationsInner.md) | Associations created for this user | [optional] 
**coordinators** | [**List[V0041OpenapiAccountsRespAccountsInnerCoordinatorsInner]**](V0041OpenapiAccountsRespAccountsInnerCoordinatorsInner.md) | Accounts this user is a coordinator for | [optional] 
**default** | [**V0041OpenapiSlurmdbdConfigRespUsersInnerDefault**](V0041OpenapiSlurmdbdConfigRespUsersInnerDefault.md) |  | [optional] 
**flags** | **List[str]** | Flags associated with user | [optional] 
**name** | **str** | User name | 
**old_name** | **str** | Previous user name | [optional] 
**wckeys** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner]**](V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner.md) | List of available WCKeys | [optional] 

## Example

```python
from slurmrest_python_0_0_41.models.v0041_openapi_slurmdbd_config_resp_users_inner import V0041OpenapiSlurmdbdConfigRespUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespUsersInner from a JSON string
v0041_openapi_slurmdbd_config_resp_users_inner_instance = V0041OpenapiSlurmdbdConfigRespUsersInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespUsersInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_users_inner_dict = v0041_openapi_slurmdbd_config_resp_users_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespUsersInner from a dict
v0041_openapi_slurmdbd_config_resp_users_inner_from_dict = V0041OpenapiSlurmdbdConfigRespUsersInner.from_dict(v0041_openapi_slurmdbd_config_resp_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


