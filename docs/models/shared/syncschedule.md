# SyncSchedule

The scheduling configuration. It can be triggerd based on several ways:

Interval: the sync will be trigged based on certain interval(minutes/hours/days/weeks)

Cron: the sync will be trigged based on cron expression https://en.wikipedia.org/wiki/Cron.

Visual: the sync will be trigged based a visual cron configuration on UI

DBT-cloud: the sync will be trigged based on a dbt cloud job


## Fields

| Field                                                                                                                                                           | Type                                                                                                                                                            | Required                                                                                                                                                        | Description                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `schedule`                                                                                                                                                      | [Optional[Union[shared.IntervalSchedule, shared.CronSchedule, shared.VisualCronSchedule, shared.DBTSchedule]]](undefined/models/shared/syncscheduleschedule.md) | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |
| `type`                                                                                                                                                          | *Optional[str]*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                              | N/A                                                                                                                                                             |