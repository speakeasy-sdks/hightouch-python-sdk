# SyncSequenceStatusOutput

The status of a given sync sequence run at both a high level and the individual
sync-run level.


## Fields

| Field                                                                                | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `id`                                                                                 | *str*                                                                                | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `status`                                                                             | [shared.SyncSequenceRequestStatus](../../models/shared/syncsequencerequeststatus.md) | :heavy_check_mark:                                                                   | N/A                                                                                  |
| `sync_runs`                                                                          | List[[shared.SyncRuns](../../models/shared/syncruns.md)]                             | :heavy_check_mark:                                                                   | N/A                                                                                  |