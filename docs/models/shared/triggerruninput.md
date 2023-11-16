# TriggerRunInput

The input of a trigger action to run syncs


## Fields

| Field                                                                                   | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `full_resync`                                                                           | *Optional[bool]*                                                                        | :heavy_minus_sign:                                                                      | Whether to resync all the rows in the query (i.e. ignoring previously<br/>synced rows). |
| `reset_cdc`                                                                             | *Optional[bool]*                                                                        | :heavy_minus_sign:                                                                      | Whether to sync all the rows in the query without executing changes on the destination. |