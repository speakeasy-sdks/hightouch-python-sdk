# PlannedRows

The number of planned rows that this sync run was supposed to execute.

Note that the counts for `successfulRows` and `failedRows` may not add up
to `plannedRows` if the sync was cancelled.


## Fields

| Field                       | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `added_count`               | *float*                     | :heavy_check_mark:          | The number of added rows.   |
| `changed_count`             | *float*                     | :heavy_check_mark:          | The number of changed rows. |
| `removed_count`             | *float*                     | :heavy_check_mark:          | The number of removed rows. |