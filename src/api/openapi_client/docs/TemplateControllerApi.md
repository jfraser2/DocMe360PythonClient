# openapi_client.TemplateControllerApi

All URIs are relative to *http://localhost:8080/rest/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_templates**](TemplateControllerApi.md#all_templates) | **GET** /v1/all/templates | 
[**create_template**](TemplateControllerApi.md#create_template) | **POST** /v1/createTemplate | 
[**find_by_template_id**](TemplateControllerApi.md#find_by_template_id) | **GET** /v1/findByTemplateId/{id} | 
[**update_template**](TemplateControllerApi.md#update_template) | **PATCH** /v1/updateTemplate | 


# **all_templates**
> object all_templates()

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
    api_instance = openapi_client.TemplateControllerApi(api_client)

    try:
        api_response = api_instance.all_templates()
        print("The response of TemplateControllerApi->all_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateControllerApi->all_templates: %s\n" % e)
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

# **create_template**
> object create_template(create_template)

### Example


```python
import openapi_client
from openapi_client.models.create_template import CreateTemplate
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
    api_instance = openapi_client.TemplateControllerApi(api_client)
    create_template = openapi_client.CreateTemplate() # CreateTemplate | 

    try:
        api_response = api_instance.create_template(create_template)
        print("The response of TemplateControllerApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateControllerApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template** | [**CreateTemplate**](CreateTemplate.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_template_id**
> object find_by_template_id(id)

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
    api_instance = openapi_client.TemplateControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.find_by_template_id(id)
        print("The response of TemplateControllerApi->find_by_template_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateControllerApi->find_by_template_id: %s\n" % e)
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

# **update_template**
> object update_template(update_template)

### Example


```python
import openapi_client
from openapi_client.models.update_template import UpdateTemplate
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
    api_instance = openapi_client.TemplateControllerApi(api_client)
    update_template = openapi_client.UpdateTemplate() # UpdateTemplate | 

    try:
        api_response = api_instance.update_template(update_template)
        print("The response of TemplateControllerApi->update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateControllerApi->update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_template** | [**UpdateTemplate**](UpdateTemplate.md)|  | 

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
**200** | OK |  -  |
**400** | BAD_REQUEST |  -  |
**403** | FORBIDDEN |  -  |
**404** | NOT_FOUND |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

