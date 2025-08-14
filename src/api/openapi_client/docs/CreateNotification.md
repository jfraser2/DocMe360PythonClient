# CreateNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** |  | 
**personalization** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**template_text** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_notification import CreateNotification

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNotification from a JSON string
create_notification_instance = CreateNotification.from_json(json)
# print the JSON string representation of the object
print(CreateNotification.to_json())

# convert the object into a dict
create_notification_dict = create_notification_instance.to_dict()
# create an instance of CreateNotification from a dict
create_notification_from_dict = CreateNotification.from_dict(create_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


