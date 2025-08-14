# openapi_client.NotificationControllerApi

All URIs are relative to *http://localhost:8080/rest/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_notifications**](NotificationControllerApi.md#all_notifications) | **GET** /v1/all/notifications | 
[**create_notification**](NotificationControllerApi.md#create_notification) | **POST** /v1/createNotification | 
[**find_by_notification_id**](NotificationControllerApi.md#find_by_notification_id) | **GET** /v1/findByNotificationId/{id} | 


# **all_notifications**
> object all_notifications()

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/rest/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/rest/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotificationControllerApi(api_client)

    try:
        api_response = api_instance.all_notifications()
        print("The response of NotificationControllerApi->all_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationControllerApi->all_notifications: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | FORBIDDEN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_notification**
> object create_notification(create_notification)

### Example


```python
import openapi_client
from openapi_client.models.create_notification import CreateNotification
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/rest/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/rest/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotificationControllerApi(api_client)
    create_notification = openapi_client.CreateNotification() # CreateNotification | 

    try:
        api_response = api_instance.create_notification(create_notification)
        print("The response of NotificationControllerApi->create_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationControllerApi->create_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_notification** | [**CreateNotification**](CreateNotification.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**400** | BAD_REQUEST |  -  |
**403** | FORBIDDEN |  -  |
**404** | NOT_FOUND |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_notification_id**
> object find_by_notification_id(id)

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/rest/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/rest/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotificationControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.find_by_notification_id(id)
        print("The response of NotificationControllerApi->find_by_notification_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationControllerApi->find_by_notification_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BAD_REQUEST |  -  |
**403** | FORBIDDEN |  -  |
**404** | NOT_FOUND |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

