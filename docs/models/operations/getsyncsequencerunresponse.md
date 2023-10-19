# GetSyncSequenceRunResponse


## Fields

| Field                                                                                        | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `content_type`                                                                               | *str*                                                                                        | :heavy_check_mark:                                                                           | HTTP response content type for this operation                                                |
| `status_code`                                                                                | *int*                                                                                        | :heavy_check_mark:                                                                           | HTTP response status code for this operation                                                 |
| `raw_response`                                                                               | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)        | :heavy_minus_sign:                                                                           | Raw HTTP response; suitable for custom response parsing                                      |
| `sync_sequence_status_output`                                                                | [Optional[shared.SyncSequenceStatusOutput]](../../models/shared/syncsequencestatusoutput.md) | :heavy_minus_sign:                                                                           | Ok                                                                                           |
| `validate_error_json`                                                                        | [Optional[shared.ValidateErrorJSON]](../../models/shared/validateerrorjson.md)               | :heavy_minus_sign:                                                                           | Validation Failed                                                                            |