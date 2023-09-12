# Hightouch SDK

## Overview

Hightouch API: Hightouch Public Rest API to access syncs, models, sources and destinations

### Available Operations

* [create_destination](#create_destination) - Create Destination
* [create_model](#create_model) - Create Model
* [create_source](#create_source) - Create Source
* [create_sync](#create_sync) - Create Sync
* [get_destination](#get_destination) - Get Destination
* [get_model](#get_model) - Get Model
* [get_source](#get_source) - Get Source
* [get_sync](#get_sync) - Get Sync
* [list_destination](#list_destination) - List Destinations
* [list_model](#list_model) - List Models
* [list_source](#list_source) - List Sources
* [list_sync](#list_sync) - List Syncs
* [list_sync_runs](#list_sync_runs) - List Sync Runs
* [trigger_run](#trigger_run) - Trigger Sync
* [trigger_run_custom](#trigger_run_custom) - Trigger Sync From ID or Slug
* [trigger_run_id_graph](#trigger_run_id_graph)
* [update_destination](#update_destination) - Update Destination
* [update_model](#update_model) - Update Model
* [update_source](#update_source) - Update Source
* [update_sync](#update_sync) - Update Sync

## create_destination

Create a new destination

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = shared.DestinationCreate(
    configuration={
        "error": 'deserunt',
    },
    name='Willie Gulgowski DVM',
    slug='tempora',
    type='suscipit',
)

res = s.hightouch.create_destination(req, operations.CreateDestinationSecurity(
    bearer_auth="",
))

if res.create_destination_200_application_json_any_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.DestinationCreate](../../models/shared/destinationcreate.md)                         | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.CreateDestinationSecurity](../../models/operations/createdestinationsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.CreateDestinationResponse](../../models/operations/createdestinationresponse.md)**


## create_model

Create a new model

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = shared.ModelCreate(
    custom=shared.ModelCreateCustom(
        query='molestiae',
    ),
    dbt=shared.ModelCreateDbt(
        model_id='minus',
    ),
    is_schema=False,
    name='Ken Kshlerin',
    primary_key='recusandae',
    query_type='temporibus',
    raw=shared.ModelCreateRaw(
        sql='ab',
    ),
    slug='quis',
    source_id='veritatis',
    table=shared.ModelCreateTable(
        name='Christopher Hills',
    ),
    visual=shared.ModelCreateVisual(
        filter='quo',
        parent_id='odit',
        primary_label='at',
        secondary_label='at',
    ),
)

res = s.hightouch.create_model(req, operations.CreateModelSecurity(
    bearer_auth="",
))

if res.create_model_200_application_json_any_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.ModelCreate](../../models/shared/modelcreate.md)                         | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.CreateModelSecurity](../../models/operations/createmodelsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.CreateModelResponse](../../models/operations/createmodelresponse.md)**


## create_source

Create a new source

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = shared.SourceCreate(
    configuration={
        "maiores": 'molestiae',
    },
    name='Forrest Koepp',
    slug='dolorum',
    type='dicta',
)

res = s.hightouch.create_source(req, operations.CreateSourceSecurity(
    bearer_auth="",
))

if res.create_source_200_application_json_any_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.SourceCreate](../../models/shared/sourcecreate.md)                         | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.CreateSourceSecurity](../../models/operations/createsourcesecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.CreateSourceResponse](../../models/operations/createsourceresponse.md)**


## create_sync

Create a new sync

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = shared.SyncCreate(
    configuration={
        "nam": 'officia',
    },
    destination_id='occaecati',
    disabled=False,
    model_id='fugit',
    schedule=shared.SyncCreateSchedule(
        schedule=shared.VisualCronSchedule(
            expressions=[
                shared.VisualCronScheduleExpressions(
                    days=shared.RecordDayBooleanOrUndefined(
                        friday=False,
                        monday=False,
                        saturday=False,
                        sunday=False,
                        thursday=False,
                        tuesday=False,
                        wednesday=False,
                    ),
                    time='hic',
                ),
            ],
        ),
        type='optio',
    ),
    slug='totam',
)

res = s.hightouch.create_sync(req, operations.CreateSyncSecurity(
    bearer_auth="",
))

if res.create_sync_200_application_json_any_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.SyncCreate](../../models/shared/synccreate.md)                         | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.CreateSyncSecurity](../../models/operations/createsyncsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.CreateSyncResponse](../../models/operations/createsyncresponse.md)**


## get_destination

Retrieve a destination based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.GetDestinationRequest(
    destination_id=1059.07,
)

res = s.hightouch.get_destination(req, operations.GetDestinationSecurity(
    bearer_auth="",
))

if res.destination is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetDestinationRequest](../../models/operations/getdestinationrequest.md)   | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `security`                                                                             | [operations.GetDestinationSecurity](../../models/operations/getdestinationsecurity.md) | :heavy_check_mark:                                                                     | The security requirements to use for the request.                                      |


### Response

**[operations.GetDestinationResponse](../../models/operations/getdestinationresponse.md)**


## get_model

Retrieve models from model ID

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.GetModelRequest(
    model_id=4146.62,
)

res = s.hightouch.get_model(req, operations.GetModelSecurity(
    bearer_auth="",
))

if res.model is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetModelRequest](../../models/operations/getmodelrequest.md)   | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.GetModelSecurity](../../models/operations/getmodelsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.GetModelResponse](../../models/operations/getmodelresponse.md)**


## get_source

Retrieve source from source ID

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.GetSourceRequest(
    source_id=4736,
)

res = s.hightouch.get_source(req, operations.GetSourceSecurity(
    bearer_auth="",
))

if res.source is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetSourceRequest](../../models/operations/getsourcerequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.GetSourceSecurity](../../models/operations/getsourcesecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.GetSourceResponse](../../models/operations/getsourceresponse.md)**


## get_sync

Retrieve sync from sync ID

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.GetSyncRequest(
    sync_id=2645.55,
)

res = s.hightouch.get_sync(req, operations.GetSyncSecurity(
    bearer_auth="",
))

if res.sync is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetSyncRequest](../../models/operations/getsyncrequest.md)   | :heavy_check_mark:                                                       | The request object to use for the request.                               |
| `security`                                                               | [operations.GetSyncSecurity](../../models/operations/getsyncsecurity.md) | :heavy_check_mark:                                                       | The security requirements to use for the request.                        |


### Response

**[operations.GetSyncResponse](../../models/operations/getsyncresponse.md)**


## list_destination

List the destinations in the user's workspace

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.ListDestinationRequest(
    limit=1863.32,
    name='Jonathon Klocko',
    offset=1352.18,
    order_by=operations.ListDestinationOrderBy.ID,
    slug='ad',
)

res = s.hightouch.list_destination(req, operations.ListDestinationSecurity(
    bearer_auth="",
))

if res.list_destination_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListDestinationRequest](../../models/operations/listdestinationrequest.md)   | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `security`                                                                               | [operations.ListDestinationSecurity](../../models/operations/listdestinationsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |


### Response

**[operations.ListDestinationResponse](../../models/operations/listdestinationresponse.md)**


## list_model

List all the models in the current workspace including parent and related models

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.ListModelRequest(
    limit=6176.36,
    name='Sheryl Fadel',
    offset=9437.49,
    order_by=operations.ListModelOrderBy.UPDATED_AT,
    slug='fuga',
)

res = s.hightouch.list_model(req, operations.ListModelSecurity(
    bearer_auth="",
))

if res.list_model_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ListModelRequest](../../models/operations/listmodelrequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.ListModelSecurity](../../models/operations/listmodelsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.ListModelResponse](../../models/operations/listmodelresponse.md)**


## list_source

List all the sources in the current workspace

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.ListSourceRequest(
    limit=4499.5,
    name='Sheryl Kertzmann',
    offset=992.8,
    order_by=operations.ListSourceOrderBy.ID,
    slug='reiciendis',
)

res = s.hightouch.list_source(req, operations.ListSourceSecurity(
    bearer_auth="",
))

if res.list_source_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.ListSourceRequest](../../models/operations/listsourcerequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.ListSourceSecurity](../../models/operations/listsourcesecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.ListSourceResponse](../../models/operations/listsourceresponse.md)**


## list_sync

List all the syncs in the current workspace

### Example Usage

```python
import hightouch
import dateutil.parser
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.ListSyncRequest(
    after=dateutil.parser.isoparse('2021-09-11T04:59:11.542Z'),
    before=dateutil.parser.isoparse('2022-08-29T05:39:49.755Z'),
    limit=2103.82,
    model_id=3581.52,
    offset=1289.26,
    order_by=operations.ListSyncOrderBy.CREATED_AT,
    slug='enim',
)

res = s.hightouch.list_sync(req, operations.ListSyncSecurity(
    bearer_auth="",
))

if res.list_sync_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListSyncRequest](../../models/operations/listsyncrequest.md)   | :heavy_check_mark:                                                         | The request object to use for the request.                                 |
| `security`                                                                 | [operations.ListSyncSecurity](../../models/operations/listsyncsecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.ListSyncResponse](../../models/operations/listsyncresponse.md)**


## list_sync_runs

List all sync runs under a sync

### Example Usage

```python
import hightouch
import dateutil.parser
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.ListSyncRunsRequest(
    after=dateutil.parser.isoparse('2022-04-10T11:47:13.463Z'),
    before=dateutil.parser.isoparse('2022-06-06T21:04:34.044Z'),
    limit=384.25,
    offset=4386.01,
    order_by=operations.ListSyncRunsOrderBy.STARTED_AT,
    run_id=9883.74,
    sync_id=9589.5,
    within=1020.44,
)

res = s.hightouch.list_sync_runs(req, operations.ListSyncRunsSecurity(
    bearer_auth="",
))

if res.list_sync_runs_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.ListSyncRunsRequest](../../models/operations/listsyncrunsrequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.ListSyncRunsSecurity](../../models/operations/listsyncrunssecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.ListSyncRunsResponse](../../models/operations/listsyncrunsresponse.md)**


## trigger_run

Trigger a new run for the given sync.

If a run is already in progress, this queues a sync run that will get
executed immediately after the current run completes.

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = operations.TriggerRunRequest(
    trigger_run_input=shared.TriggerRunInput(
        full_resync=False,
    ),
    sync_id='mollitia',
)

res = s.hightouch.trigger_run(req, operations.TriggerRunSecurity(
    bearer_auth="",
))

if res.trigger_run_output is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.TriggerRunRequest](../../models/operations/triggerrunrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.TriggerRunSecurity](../../models/operations/triggerrunsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.TriggerRunResponse](../../models/operations/triggerrunresponse.md)**


## trigger_run_custom

Trigger a new run globally based on sync id or sync slug

If a run is already in progress, this queues a sync run that will get
executed immediately after the current run completes.

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = shared.TriggerRunCustomInput(
    full_resync=False,
    sync_id='dolorem',
    sync_slug='culpa',
)

res = s.hightouch.trigger_run_custom(req, operations.TriggerRunCustomSecurity(
    bearer_auth="",
))

if res.trigger_run_custom_200_application_json_any_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.TriggerRunCustomInput](../../models/shared/triggerruncustominput.md)               | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `security`                                                                                 | [operations.TriggerRunCustomSecurity](../../models/operations/triggerruncustomsecurity.md) | :heavy_check_mark:                                                                         | The security requirements to use for the request.                                          |


### Response

**[operations.TriggerRunCustomResponse](../../models/operations/triggerruncustomresponse.md)**


## trigger_run_id_graph

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = operations.TriggerRunIDGraphRequest(
    trigger_run_id_graph_input=shared.TriggerRunIDGraphInput(
        full_rerun=False,
    ),
    graph_id='consequuntur',
)

res = s.hightouch.trigger_run_id_graph(req, operations.TriggerRunIDGraphSecurity(
    bearer_auth="",
))

if res.trigger_run_id_graph_output is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.TriggerRunIDGraphRequest](../../models/operations/triggerrunidgraphrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.TriggerRunIDGraphSecurity](../../models/operations/triggerrunidgraphsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.TriggerRunIDGraphResponse](../../models/operations/triggerrunidgraphresponse.md)**


## update_destination

Update an existing destination

Patch a destination based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = operations.UpdateDestinationRequest(
    destination_update=shared.DestinationUpdate(
        configuration={
            "repellat": 'mollitia',
        },
        name='Francis Jerde',
    ),
    destination_id=2444.25,
)

res = s.hightouch.update_destination(req, operations.UpdateDestinationSecurity(
    bearer_auth="",
))

if res.update_destination_200_application_json_any_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateDestinationRequest](../../models/operations/updatedestinationrequest.md)   | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `security`                                                                                   | [operations.UpdateDestinationSecurity](../../models/operations/updatedestinationsecurity.md) | :heavy_check_mark:                                                                           | The security requirements to use for the request.                                            |


### Response

**[operations.UpdateDestinationResponse](../../models/operations/updatedestinationresponse.md)**


## update_model

Update an existing model

Patch a model based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = operations.UpdateModelRequest(
    model_update=shared.ModelUpdate(
        custom=shared.ModelUpdateCustom(
            query='error',
        ),
        dbt=shared.ModelUpdateDbt(
            model_id='quia',
        ),
        is_schema=False,
        name='Gloria Padberg',
        primary_key='odit',
        raw=shared.ModelUpdateRaw(
            sql='quo',
        ),
        table=shared.ModelUpdateTable(
            name='Mandy Hills',
        ),
        visual=shared.ModelUpdateVisual(
            filter='aut',
            parent_id='quasi',
            primary_label='error',
            secondary_label='temporibus',
        ),
    ),
    model_id=6736.6,
)

res = s.hightouch.update_model(req, operations.UpdateModelSecurity(
    bearer_auth="",
))

if res.update_model_200_application_json_any_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateModelRequest](../../models/operations/updatemodelrequest.md)   | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `security`                                                                       | [operations.UpdateModelSecurity](../../models/operations/updatemodelsecurity.md) | :heavy_check_mark:                                                               | The security requirements to use for the request.                                |


### Response

**[operations.UpdateModelResponse](../../models/operations/updatemodelresponse.md)**


## update_source

Update an existing source

Patch a source based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = operations.UpdateSourceRequest(
    source_update=shared.SourceUpdate(
        configuration={
            "quasi": 'reiciendis',
        },
        name='Caleb Koss',
    ),
    source_id=557.14,
)

res = s.hightouch.update_source(req, operations.UpdateSourceSecurity(
    bearer_auth="",
))

if res.update_source_200_application_json_any_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateSourceRequest](../../models/operations/updatesourcerequest.md)   | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `security`                                                                         | [operations.UpdateSourceSecurity](../../models/operations/updatesourcesecurity.md) | :heavy_check_mark:                                                                 | The security requirements to use for the request.                                  |


### Response

**[operations.UpdateSourceResponse](../../models/operations/updatesourceresponse.md)**


## update_sync

Update an existing sync

Patch a sync based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = operations.UpdateSyncRequest(
    sync_update=shared.SyncUpdate(
        configuration={
            "omnis": 'voluptate',
        },
        disabled=False,
        schedule=shared.SyncUpdateSchedule(
            schedule=shared.VisualCronSchedule(
                expressions=[
                    shared.VisualCronScheduleExpressions(
                        days=shared.RecordDayBooleanOrUndefined(
                            friday=False,
                            monday=False,
                            saturday=False,
                            sunday=False,
                            thursday=False,
                            tuesday=False,
                            wednesday=False,
                        ),
                        time='perferendis',
                    ),
                ],
            ),
            type='doloremque',
        ),
    ),
    sync_id=4417.11,
)

res = s.hightouch.update_sync(req, operations.UpdateSyncSecurity(
    bearer_auth="",
))

if res.update_sync_200_application_json_any_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.UpdateSyncRequest](../../models/operations/updatesyncrequest.md)   | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `security`                                                                     | [operations.UpdateSyncSecurity](../../models/operations/updatesyncsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |


### Response

**[operations.UpdateSyncResponse](../../models/operations/updatesyncresponse.md)**

