# ListDestinationResponse


## Fields

| Field                                                                                                       | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                              | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `list_destination_200_application_json_object`                                                              | [Optional[ListDestination200ApplicationJSON]](../../models/operations/listdestination200applicationjson.md) | :heavy_minus_sign:                                                                                          | Ok                                                                                                          |
| `status_code`                                                                                               | *int*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `raw_response`                                                                                              | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                       | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `validate_error_json`                                                                                       | [Optional[shared.ValidateErrorJSON]](../../models/shared/validateerrorjson.md)                              | :heavy_minus_sign:                                                                                          | Validation Failed                                                                                           |