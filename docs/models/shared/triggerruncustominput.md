# TriggerRunCustomInput

The input of a trigger action to run syncs based on sync ID, slug or other filters


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `full_resync`                                                                       | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Whether to resync all the rows in the query (i.e. ignoring previously<br/>synced rows). |
| `sync_id`                                                                           | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Trigger run based on sync id                                                        |
| `sync_slug`                                                                         | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | Trigger run based on sync slug                                                      |