# ListModelRequest


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `limit`                                                                   | *Optional[float]*                                                         | :heavy_minus_sign:                                                        | limit the number of objects returned (default is 100)                     |
| `name`                                                                    | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | filter based on name                                                      |
| `offset`                                                                  | *Optional[float]*                                                         | :heavy_minus_sign:                                                        | set the offset on results (for pagination)                                |
| `order_by`                                                                | [Optional[ListModelOrderBy]](../../models/operations/listmodelorderby.md) | :heavy_minus_sign:                                                        | specify the order                                                         |
| `slug`                                                                    | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | filter based on slug                                                      |