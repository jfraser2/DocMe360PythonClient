# ApiValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] 
**var_field** | **str** |  | [optional] 
**rejected_value** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.api_validation_error import ApiValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ApiValidationError from a JSON string
api_validation_error_instance = ApiValidationError.from_json(json)
# print the JSON string representation of the object
print(ApiValidationError.to_json())

# convert the object into a dict
api_validation_error_dict = api_validation_error_instance.to_dict()
# create an instance of ApiValidationError from a dict
api_validation_error_from_dict = ApiValidationError.from_dict(api_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


