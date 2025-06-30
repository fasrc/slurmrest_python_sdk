# slurmrest_python_0_0_41.SlurmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slurm_v0041_delete_job**](SlurmApi.md#slurm_v0041_delete_job) | **DELETE** /slurm/v0.0.41/job/{job_id} | cancel or signal job
[**slurm_v0041_delete_jobs**](SlurmApi.md#slurm_v0041_delete_jobs) | **DELETE** /slurm/v0.0.41/jobs/ | send signal to list of jobs
[**slurm_v0041_delete_node**](SlurmApi.md#slurm_v0041_delete_node) | **DELETE** /slurm/v0.0.41/node/{node_name} | delete node
[**slurm_v0041_get_diag**](SlurmApi.md#slurm_v0041_get_diag) | **GET** /slurm/v0.0.41/diag/ | get diagnostics
[**slurm_v0041_get_job**](SlurmApi.md#slurm_v0041_get_job) | **GET** /slurm/v0.0.41/job/{job_id} | get job info
[**slurm_v0041_get_jobs**](SlurmApi.md#slurm_v0041_get_jobs) | **GET** /slurm/v0.0.41/jobs/ | get list of jobs
[**slurm_v0041_get_jobs_state**](SlurmApi.md#slurm_v0041_get_jobs_state) | **GET** /slurm/v0.0.41/jobs/state/ | get list of job states
[**slurm_v0041_get_licenses**](SlurmApi.md#slurm_v0041_get_licenses) | **GET** /slurm/v0.0.41/licenses/ | get all Slurm tracked license info
[**slurm_v0041_get_node**](SlurmApi.md#slurm_v0041_get_node) | **GET** /slurm/v0.0.41/node/{node_name} | get node info
[**slurm_v0041_get_nodes**](SlurmApi.md#slurm_v0041_get_nodes) | **GET** /slurm/v0.0.41/nodes/ | get node(s) info
[**slurm_v0041_get_partition**](SlurmApi.md#slurm_v0041_get_partition) | **GET** /slurm/v0.0.41/partition/{partition_name} | get partition info
[**slurm_v0041_get_partitions**](SlurmApi.md#slurm_v0041_get_partitions) | **GET** /slurm/v0.0.41/partitions/ | get all partition info
[**slurm_v0041_get_ping**](SlurmApi.md#slurm_v0041_get_ping) | **GET** /slurm/v0.0.41/ping/ | ping test
[**slurm_v0041_get_reconfigure**](SlurmApi.md#slurm_v0041_get_reconfigure) | **GET** /slurm/v0.0.41/reconfigure/ | request slurmctld reconfigure
[**slurm_v0041_get_reservation**](SlurmApi.md#slurm_v0041_get_reservation) | **GET** /slurm/v0.0.41/reservation/{reservation_name} | get reservation info
[**slurm_v0041_get_reservations**](SlurmApi.md#slurm_v0041_get_reservations) | **GET** /slurm/v0.0.41/reservations/ | get all reservation info
[**slurm_v0041_get_shares**](SlurmApi.md#slurm_v0041_get_shares) | **GET** /slurm/v0.0.41/shares | get fairshare info
[**slurm_v0041_post_job**](SlurmApi.md#slurm_v0041_post_job) | **POST** /slurm/v0.0.41/job/{job_id} | update job
[**slurm_v0041_post_job_allocate**](SlurmApi.md#slurm_v0041_post_job_allocate) | **POST** /slurm/v0.0.41/job/allocate | submit new job allocation without any steps that must be signaled to stop
[**slurm_v0041_post_job_submit**](SlurmApi.md#slurm_v0041_post_job_submit) | **POST** /slurm/v0.0.41/job/submit | submit new job
[**slurm_v0041_post_node**](SlurmApi.md#slurm_v0041_post_node) | **POST** /slurm/v0.0.41/node/{node_name} | update node properties
[**slurm_v0041_post_nodes**](SlurmApi.md#slurm_v0041_post_nodes) | **POST** /slurm/v0.0.41/nodes/ | batch update node(s)


# **slurm_v0041_delete_job**
> V0041OpenapiResp slurm_v0041_delete_job(job_id, signal=signal, flags=flags)

cancel or signal job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    signal = 'signal_example' # str | Signal to send to Job (optional)
    flags = 'flags_example' # str | Signalling flags (optional)

    try:
        # cancel or signal job
        api_response = api_instance.slurm_v0041_delete_job(job_id, signal=signal, flags=flags)
        print("The response of SlurmApi->slurm_v0041_delete_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_delete_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **signal** | **str**| Signal to send to Job | [optional] 
 **flags** | **str**| Signalling flags | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job signal result |  -  |
**0** | job signal result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_delete_jobs**
> V0041OpenapiKillJobsResp slurm_v0041_delete_jobs(v0041_kill_jobs_msg=v0041_kill_jobs_msg)

send signal to list of jobs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_kill_jobs_msg import V0041KillJobsMsg
from slurmrest_python_0_0_41.models.v0041_openapi_kill_jobs_resp import V0041OpenapiKillJobsResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    v0041_kill_jobs_msg = slurmrest_python_0_0_41.V0041KillJobsMsg() # V0041KillJobsMsg | Signal or cancel jobs (optional)

    try:
        # send signal to list of jobs
        api_response = api_instance.slurm_v0041_delete_jobs(v0041_kill_jobs_msg=v0041_kill_jobs_msg)
        print("The response of SlurmApi->slurm_v0041_delete_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_delete_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0041_kill_jobs_msg** | [**V0041KillJobsMsg**](V0041KillJobsMsg.md)| Signal or cancel jobs | [optional] 

### Return type

[**V0041OpenapiKillJobsResp**](V0041OpenapiKillJobsResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | description of jobs to signal |  -  |
**0** | description of jobs to signal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_delete_node**
> V0041OpenapiResp slurm_v0041_delete_node(node_name)

delete node

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name

    try:
        # delete node
        api_response = api_instance.slurm_v0041_delete_node(node_name)
        print("The response of SlurmApi->slurm_v0041_delete_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_delete_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node delete request result |  -  |
**0** | node delete request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_diag**
> V0041OpenapiDiagResp slurm_v0041_get_diag()

get diagnostics

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_diag_resp import V0041OpenapiDiagResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)

    try:
        # get diagnostics
        api_response = api_instance.slurm_v0041_get_diag()
        print("The response of SlurmApi->slurm_v0041_get_diag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_diag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0041OpenapiDiagResp**](V0041OpenapiDiagResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | diagnostic results |  -  |
**0** | diagnostic results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_job**
> V0041OpenapiJobInfoResp slurm_v0041_get_job(job_id, update_time=update_time, flags=flags)

get job info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_job_info_resp import V0041OpenapiJobInfoResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get job info
        api_response = api_instance.slurm_v0041_get_job(job_id, update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiJobInfoResp**](V0041OpenapiJobInfoResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_jobs**
> V0041OpenapiJobInfoResp slurm_v0041_get_jobs(update_time=update_time, flags=flags)

get list of jobs

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_job_info_resp import V0041OpenapiJobInfoResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get list of jobs
        api_response = api_instance.slurm_v0041_get_jobs(update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiJobInfoResp**](V0041OpenapiJobInfoResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) information |  -  |
**0** | job(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_jobs_state**
> V0041OpenapiJobInfoResp slurm_v0041_get_jobs_state(job_id=job_id)

get list of job states

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_job_info_resp import V0041OpenapiJobInfoResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Search for CSV list of Job IDs (optional)

    try:
        # get list of job states
        api_response = api_instance.slurm_v0041_get_jobs_state(job_id=job_id)
        print("The response of SlurmApi->slurm_v0041_get_jobs_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_jobs_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Search for CSV list of Job IDs | [optional] 

### Return type

[**V0041OpenapiJobInfoResp**](V0041OpenapiJobInfoResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job(s) state information |  -  |
**0** | job(s) state information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_licenses**
> V0041OpenapiLicensesResp slurm_v0041_get_licenses()

get all Slurm tracked license info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_licenses_resp import V0041OpenapiLicensesResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)

    try:
        # get all Slurm tracked license info
        api_response = api_instance.slurm_v0041_get_licenses()
        print("The response of SlurmApi->slurm_v0041_get_licenses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_licenses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0041OpenapiLicensesResp**](V0041OpenapiLicensesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of get all licenses |  -  |
**0** | results of get all licenses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_node**
> V0041OpenapiNodesResp slurm_v0041_get_node(node_name, update_time=update_time, flags=flags)

get node info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_nodes_resp import V0041OpenapiNodesResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node info
        api_response = api_instance.slurm_v0041_get_node(node_name, update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiNodesResp**](V0041OpenapiNodesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node information |  -  |
**0** | node information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_nodes**
> V0041OpenapiNodesResp slurm_v0041_get_nodes(update_time=update_time, flags=flags)

get node(s) info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_nodes_resp import V0041OpenapiNodesResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter jobs since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get node(s) info
        api_response = api_instance.slurm_v0041_get_nodes(update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter jobs since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiNodesResp**](V0041OpenapiNodesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node(s) information |  -  |
**0** | node(s) information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_partition**
> V0041OpenapiPartitionResp slurm_v0041_get_partition(partition_name, update_time=update_time, flags=flags)

get partition info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_partition_resp import V0041OpenapiPartitionResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    partition_name = 'partition_name_example' # str | Partition name
    update_time = 'update_time_example' # str | Filter partitions since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get partition info
        api_response = api_instance.slurm_v0041_get_partition(partition_name, update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_partition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_partition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partition_name** | **str**| Partition name | 
 **update_time** | **str**| Filter partitions since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiPartitionResp**](V0041OpenapiPartitionResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | partition information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_partitions**
> V0041OpenapiPartitionResp slurm_v0041_get_partitions(update_time=update_time, flags=flags)

get all partition info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_partition_resp import V0041OpenapiPartitionResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter partitions since update timestamp (optional)
    flags = 'flags_example' # str | Query flags (optional)

    try:
        # get all partition info
        api_response = api_instance.slurm_v0041_get_partitions(update_time=update_time, flags=flags)
        print("The response of SlurmApi->slurm_v0041_get_partitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_partitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter partitions since update timestamp | [optional] 
 **flags** | **str**| Query flags | [optional] 

### Return type

[**V0041OpenapiPartitionResp**](V0041OpenapiPartitionResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | partition information |  -  |
**0** | partition information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_ping**
> V0041OpenapiPingArrayResp slurm_v0041_get_ping()

ping test

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_ping_array_resp import V0041OpenapiPingArrayResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)

    try:
        # ping test
        api_response = api_instance.slurm_v0041_get_ping()
        print("The response of SlurmApi->slurm_v0041_get_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0041OpenapiPingArrayResp**](V0041OpenapiPingArrayResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | results of ping test |  -  |
**0** | results of ping test |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_reconfigure**
> V0041OpenapiResp slurm_v0041_get_reconfigure()

request slurmctld reconfigure

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)

    try:
        # request slurmctld reconfigure
        api_response = api_instance.slurm_v0041_get_reconfigure()
        print("The response of SlurmApi->slurm_v0041_get_reconfigure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_reconfigure: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reconfigure request result |  -  |
**0** | reconfigure request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_reservation**
> V0041OpenapiReservationResp slurm_v0041_get_reservation(reservation_name, update_time=update_time)

get reservation info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_reservation_resp import V0041OpenapiReservationResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    reservation_name = 'reservation_name_example' # str | Reservation name
    update_time = 'update_time_example' # str | Filter reservations since update timestamp (optional)

    try:
        # get reservation info
        api_response = api_instance.slurm_v0041_get_reservation(reservation_name, update_time=update_time)
        print("The response of SlurmApi->slurm_v0041_get_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_reservation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_name** | **str**| Reservation name | 
 **update_time** | **str**| Filter reservations since update timestamp | [optional] 

### Return type

[**V0041OpenapiReservationResp**](V0041OpenapiReservationResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | reservation information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_reservations**
> V0041OpenapiReservationResp slurm_v0041_get_reservations(update_time=update_time)

get all reservation info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_reservation_resp import V0041OpenapiReservationResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    update_time = 'update_time_example' # str | Filter reservations since update timestamp (optional)

    try:
        # get all reservation info
        api_response = api_instance.slurm_v0041_get_reservations(update_time=update_time)
        print("The response of SlurmApi->slurm_v0041_get_reservations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_reservations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_time** | **str**| Filter reservations since update timestamp | [optional] 

### Return type

[**V0041OpenapiReservationResp**](V0041OpenapiReservationResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | reservation information |  -  |
**0** | reservation information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_get_shares**
> V0041OpenapiSharesResp slurm_v0041_get_shares(accounts=accounts, users=users)

get fairshare info

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_shares_resp import V0041OpenapiSharesResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    accounts = 'accounts_example' # str | Accounts to query (optional)
    users = 'users_example' # str | Users to query (optional)

    try:
        # get fairshare info
        api_response = api_instance.slurm_v0041_get_shares(accounts=accounts, users=users)
        print("The response of SlurmApi->slurm_v0041_get_shares:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_get_shares: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounts** | **str**| Accounts to query | [optional] 
 **users** | **str**| Users to query | [optional] 

### Return type

[**V0041OpenapiSharesResp**](V0041OpenapiSharesResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | shares information |  -  |
**0** | shares information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_post_job**
> V0041OpenapiJobPostResponse slurm_v0041_post_job(job_id, v0041_job_desc_msg=v0041_job_desc_msg)

update job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_job_desc_msg import V0041JobDescMsg
from slurmrest_python_0_0_41.models.v0041_openapi_job_post_response import V0041OpenapiJobPostResponse
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    job_id = 'job_id_example' # str | Job ID
    v0041_job_desc_msg = slurmrest_python_0_0_41.V0041JobDescMsg() # V0041JobDescMsg | Job update description (optional)

    try:
        # update job
        api_response = api_instance.slurm_v0041_post_job(job_id, v0041_job_desc_msg=v0041_job_desc_msg)
        print("The response of SlurmApi->slurm_v0041_post_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_post_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 
 **v0041_job_desc_msg** | [**V0041JobDescMsg**](V0041JobDescMsg.md)| Job update description | [optional] 

### Return type

[**V0041OpenapiJobPostResponse**](V0041OpenapiJobPostResponse.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job update result |  -  |
**0** | job update result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_post_job_allocate**
> V0041OpenapiJobAllocResp slurm_v0041_post_job_allocate(v0041_job_alloc_req=v0041_job_alloc_req)

submit new job allocation without any steps that must be signaled to stop

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_job_alloc_req import V0041JobAllocReq
from slurmrest_python_0_0_41.models.v0041_openapi_job_alloc_resp import V0041OpenapiJobAllocResp
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    v0041_job_alloc_req = slurmrest_python_0_0_41.V0041JobAllocReq() # V0041JobAllocReq | Job allocation description (optional)

    try:
        # submit new job allocation without any steps that must be signaled to stop
        api_response = api_instance.slurm_v0041_post_job_allocate(v0041_job_alloc_req=v0041_job_alloc_req)
        print("The response of SlurmApi->slurm_v0041_post_job_allocate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_post_job_allocate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0041_job_alloc_req** | [**V0041JobAllocReq**](V0041JobAllocReq.md)| Job allocation description | [optional] 

### Return type

[**V0041OpenapiJobAllocResp**](V0041OpenapiJobAllocResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job allocation response |  -  |
**0** | job allocation response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_post_job_submit**
> V0041OpenapiJobSubmitResponse slurm_v0041_post_job_submit(v0041_job_submit_req=v0041_job_submit_req)

submit new job

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_job_submit_req import V0041JobSubmitReq
from slurmrest_python_0_0_41.models.v0041_openapi_job_submit_response import V0041OpenapiJobSubmitResponse
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    v0041_job_submit_req = slurmrest_python_0_0_41.V0041JobSubmitReq() # V0041JobSubmitReq | Job description (optional)

    try:
        # submit new job
        api_response = api_instance.slurm_v0041_post_job_submit(v0041_job_submit_req=v0041_job_submit_req)
        print("The response of SlurmApi->slurm_v0041_post_job_submit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_post_job_submit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0041_job_submit_req** | [**V0041JobSubmitReq**](V0041JobSubmitReq.md)| Job description | [optional] 

### Return type

[**V0041OpenapiJobSubmitResponse**](V0041OpenapiJobSubmitResponse.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | job submission response |  -  |
**0** | job submission response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_post_node**
> V0041OpenapiResp slurm_v0041_post_node(node_name, v0041_update_node_msg=v0041_update_node_msg)

update node properties

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrest_python_0_0_41.models.v0041_update_node_msg import V0041UpdateNodeMsg
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    node_name = 'node_name_example' # str | Node name
    v0041_update_node_msg = slurmrest_python_0_0_41.V0041UpdateNodeMsg() # V0041UpdateNodeMsg | Node update description (optional)

    try:
        # update node properties
        api_response = api_instance.slurm_v0041_post_node(node_name, v0041_update_node_msg=v0041_update_node_msg)
        print("The response of SlurmApi->slurm_v0041_post_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_post_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| Node name | 
 **v0041_update_node_msg** | [**V0041UpdateNodeMsg**](V0041UpdateNodeMsg.md)| Node update description | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | node update request result |  -  |
**0** | node update request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **slurm_v0041_post_nodes**
> V0041OpenapiResp slurm_v0041_post_nodes(v0041_update_node_msg=v0041_update_node_msg)

batch update node(s)

### Example

* Api Key Authentication (user):
* Bearer (JWT) Authentication (bearerAuth):
* Api Key Authentication (token):

```python
import slurmrest_python_0_0_41
from slurmrest_python_0_0_41.models.v0041_openapi_resp import V0041OpenapiResp
from slurmrest_python_0_0_41.models.v0041_update_node_msg import V0041UpdateNodeMsg
from slurmrest_python_0_0_41.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = slurmrest_python_0_0_41.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: user
configuration.api_key['user'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['user'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = slurmrest_python_0_0_41.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Configure API key authorization: token
configuration.api_key['token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with slurmrest_python_0_0_41.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = slurmrest_python_0_0_41.SlurmApi(api_client)
    v0041_update_node_msg = slurmrest_python_0_0_41.V0041UpdateNodeMsg() # V0041UpdateNodeMsg | Nodelist update description (optional)

    try:
        # batch update node(s)
        api_response = api_instance.slurm_v0041_post_nodes(v0041_update_node_msg=v0041_update_node_msg)
        print("The response of SlurmApi->slurm_v0041_post_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SlurmApi->slurm_v0041_post_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v0041_update_node_msg** | [**V0041UpdateNodeMsg**](V0041UpdateNodeMsg.md)| Nodelist update description | [optional] 

### Return type

[**V0041OpenapiResp**](V0041OpenapiResp.md)

### Authorization

[user](../README.md#user), [bearerAuth](../README.md#bearerAuth), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml
 - **Accept**: application/json, application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | batch node update request result |  -  |
**0** | batch node update request result |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

