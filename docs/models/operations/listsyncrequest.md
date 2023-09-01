# ListSyncRequest


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `after`                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)    | :heavy_minus_sign:                                                      | select syncs that were run after given ISO timestamp                    |
| `before`                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)    | :heavy_minus_sign:                                                      | select syncs that were run before given ISO timestamp                   |
| `limit`                                                                 | *Optional[float]*                                                       | :heavy_minus_sign:                                                      | limit the number of objects returned (default is 100)                   |
| `model_id`                                                              | *Optional[float]*                                                       | :heavy_minus_sign:                                                      | filter based on modelId                                                 |
| `offset`                                                                | *Optional[float]*                                                       | :heavy_minus_sign:                                                      | set the offset on results (for pagination)                              |
| `order_by`                                                              | [Optional[ListSyncOrderBy]](../../models/operations/listsyncorderby.md) | :heavy_minus_sign:                                                      | specify the order                                                       |
| `slug`                                                                  | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | filter based on slug                                                    |