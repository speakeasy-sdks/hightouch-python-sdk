# ListDestinationRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `limit`                                                            | *Optional[float]*                                                  | :heavy_minus_sign:                                                 | limit the number of objects returned (default is 100)              |
| `name`                                                             | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Filter based on the destination's name                             |
| `offset`                                                           | *Optional[float]*                                                  | :heavy_minus_sign:                                                 | set the offset on results (for pagination)                         |
| `order_by`                                                         | [Optional[operations.OrderBy]](../../models/operations/orderby.md) | :heavy_minus_sign:                                                 | Order the returned destinations                                    |
| `slug`                                                             | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | Filter based on destination's slug                                 |