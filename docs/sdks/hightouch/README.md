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
from hightouch.models import shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.DestinationCreate(
    configuration={
        "dignissimos": 'Bugatti',
    },
    name='greatly',
    slug='kilogram Southwest',
    type='blue wilt',
)

res = s.hightouch.create_destination(req)

if res.create_destination_200_application_json_one_of is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.DestinationCreate](../../models/shared/destinationcreate.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateDestinationResponse](../../models/operations/createdestinationresponse.md)**


## create_model

Create a new model

### Example Usage

```python
import hightouch
from hightouch.models import shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.ModelCreate(
    custom=shared.ModelCreateCustom(
        query='zesty',
    ),
    dbt=shared.ModelCreateDbt(
        model_id='Northwest enterprise',
    ),
    folder_id='Libyan Data Non',
    is_schema=False,
    name='Dakota',
    primary_key='success Rochester Non',
    query_type='Metal',
    raw=shared.ModelCreateRaw(
        sql='payment',
    ),
    slug='Division',
    source_id='application unloosen yahoo',
    table=shared.ModelCreateTable(
        name='Practical Bike',
    ),
    visual=shared.ModelCreateVisual(
        filter='Bugatti',
        parent_id='invoice',
        primary_label='Usability',
        secondary_label='hack AI instead',
    ),
)

res = s.hightouch.create_model(req)

if res.create_model_200_application_json_one_of is not None:
    # handle response
```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `request`                                                | [shared.ModelCreate](../../models/shared/modelcreate.md) | :heavy_check_mark:                                       | The request object to use for the request.               |


### Response

**[operations.CreateModelResponse](../../models/operations/createmodelresponse.md)**


## create_source

Create a new source

### Example Usage

```python
import hightouch
from hightouch.models import shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.SourceCreate(
    configuration={
        "aut": 'Vermont',
    },
    name='Van deposit Lamborghini',
    slug='York ouch Northwest',
    type='Porsche Cadillac',
)

res = s.hightouch.create_source(req)

if res.create_source_200_application_json_one_of is not None:
    # handle response
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.SourceCreate](../../models/shared/sourcecreate.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.CreateSourceResponse](../../models/operations/createsourceresponse.md)**


## create_sync

Create a new sync

### Example Usage

```python
import hightouch
from hightouch.models import shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.SyncCreate(
    configuration={
        "accusamus": 'Concrete',
    },
    destination_id='North synergies Cambridgeshire',
    disabled=False,
    model_id='orchid Applications disintermediate',
    schedule=shared.SyncCreateSchedule(
        schedule=[],
        type='meanwhile',
    ),
    slug='Electric SDD',
)

res = s.hightouch.create_sync(req)

if res.create_sync_200_application_json_one_of is not None:
    # handle response
```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.SyncCreate](../../models/shared/synccreate.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.CreateSyncResponse](../../models/operations/createsyncresponse.md)**


## get_destination

Retrieve a destination based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetDestinationRequest(
    destination_id=4856.96,
)

res = s.hightouch.get_destination(req)

if res.destination is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetDestinationRequest](../../models/operations/getdestinationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetDestinationResponse](../../models/operations/getdestinationresponse.md)**


## get_model

Retrieve models from model ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetModelRequest(
    model_id=7962.16,
)

res = s.hightouch.get_model(req)

if res.model is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetModelRequest](../../models/operations/getmodelrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetModelResponse](../../models/operations/getmodelresponse.md)**


## get_source

Retrieve source from source ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetSourceRequest(
    source_id=4378.62,
)

res = s.hightouch.get_source(req)

if res.source is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetSourceRequest](../../models/operations/getsourcerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetSourceResponse](../../models/operations/getsourceresponse.md)**


## get_sync

Retrieve sync from sync ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetSyncRequest(
    sync_id=7319.86,
)

res = s.hightouch.get_sync(req)

if res.sync is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetSyncRequest](../../models/operations/getsyncrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetSyncResponse](../../models/operations/getsyncresponse.md)**


## list_destination

List the destinations in the user's workspace

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListDestinationRequest(
    limit=898.03,
    name='Alaska',
    offset=1026.89,
    order_by=operations.ListDestinationOrderBy.CREATED_AT,
    slug='quas',
)

res = s.hightouch.list_destination(req)

if res.list_destination_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListDestinationRequest](../../models/operations/listdestinationrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ListDestinationResponse](../../models/operations/listdestinationresponse.md)**


## list_model

List all the models in the current workspace including parent and related models

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListModelRequest(
    limit=4556.79,
    name='times Automated portal',
    offset=1772.52,
    order_by=operations.ListModelOrderBy.SLUG,
    slug='deposit definite',
)

res = s.hightouch.list_model(req)

if res.list_model_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListModelRequest](../../models/operations/listmodelrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.ListModelResponse](../../models/operations/listmodelresponse.md)**


## list_source

List all the sources in the current workspace

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListSourceRequest(
    limit=3667.48,
    name='facilis',
    offset=7285.7,
    order_by=operations.ListSourceOrderBy.NAME,
    slug='Francium spread Outdoors',
)

res = s.hightouch.list_source(req)

if res.list_source_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ListSourceRequest](../../models/operations/listsourcerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ListSourceResponse](../../models/operations/listsourceresponse.md)**


## list_sync

List all the syncs in the current workspace

### Example Usage

```python
import hightouch
import dateutil.parser
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListSyncRequest(
    after=dateutil.parser.isoparse('2021-12-29T02:44:53.348Z'),
    before=dateutil.parser.isoparse('2023-03-08T22:11:11.682Z'),
    limit=8056.73,
    model_id=2244.55,
    offset=5024.07,
    order_by=operations.ListSyncOrderBy.SLUG,
    slug='Automated Sausages',
)

res = s.hightouch.list_sync(req)

if res.list_sync_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.ListSyncRequest](../../models/operations/listsyncrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.ListSyncResponse](../../models/operations/listsyncresponse.md)**


## list_sync_runs

List all sync runs under a sync

### Example Usage

```python
import hightouch
import dateutil.parser
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListSyncRunsRequest(
    after=dateutil.parser.isoparse('2023-08-29T00:26:30.425Z'),
    before=dateutil.parser.isoparse('2022-11-28T13:12:20.353Z'),
    limit=3202.39,
    offset=771.35,
    order_by=operations.ListSyncRunsOrderBy.STARTED_AT,
    run_id=2963.65,
    sync_id=7146.37,
    within=4058.13,
)

res = s.hightouch.list_sync_runs(req)

if res.list_sync_runs_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListSyncRunsRequest](../../models/operations/listsyncrunsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


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

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TriggerRunRequest(
    trigger_run_input=shared.TriggerRunInput(
        full_resync=False,
    ),
    sync_id='Digitized withdrawal Midland',
)

res = s.hightouch.trigger_run(req)

if res.trigger_run_output is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.TriggerRunRequest](../../models/operations/triggerrunrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.TriggerRunResponse](../../models/operations/triggerrunresponse.md)**


## trigger_run_custom

Trigger a new run globally based on sync id or sync slug

If a run is already in progress, this queues a sync run that will get
executed immediately after the current run completes.

### Example Usage

```python
import hightouch
from hightouch.models import shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.TriggerRunCustomInput(
    full_resync=False,
    sync_id='female',
    sync_slug='Tellurium core',
)

res = s.hightouch.trigger_run_custom(req)

if res.trigger_run_custom_200_application_json_one_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.TriggerRunCustomInput](../../models/shared/triggerruncustominput.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.TriggerRunCustomResponse](../../models/operations/triggerruncustomresponse.md)**


## trigger_run_id_graph

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.TriggerRunIDGraphRequest(
    trigger_run_id_graph_input=shared.TriggerRunIDGraphInput(
        full_rerun=False,
    ),
    graph_id='hop Bentley AI',
)

res = s.hightouch.trigger_run_id_graph(req)

if res.trigger_run_id_graph_output is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.TriggerRunIDGraphRequest](../../models/operations/triggerrunidgraphrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.TriggerRunIDGraphResponse](../../models/operations/triggerrunidgraphresponse.md)**


## update_destination

Update an existing destination

Patch a destination based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateDestinationRequest(
    destination_update=shared.DestinationUpdate(
        configuration={
            "debitis": 'copying',
        },
        name='enable Northwest woot',
    ),
    destination_id=8585.6,
)

res = s.hightouch.update_destination(req)

if res.update_destination_200_application_json_one_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateDestinationRequest](../../models/operations/updatedestinationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateDestinationResponse](../../models/operations/updatedestinationresponse.md)**


## update_model

Update an existing model

Patch a model based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateModelRequest(
    model_update=shared.ModelUpdate(
        custom=shared.ModelUpdateCustom(
            query='Northwest',
        ),
        dbt=shared.ModelUpdateDbt(
            model_id='Ford till Customer',
        ),
        folder_id='users content',
        is_schema=False,
        name='New',
        primary_key='reinvent male indigo',
        raw=shared.ModelUpdateRaw(
            sql='Rhodium mint Steel',
        ),
        table=shared.ModelUpdateTable(
            name='systematic Gasoline',
        ),
        visual=shared.ModelUpdateVisual(
            filter='Paradigm',
            parent_id='Accountability whenever Palladium',
            primary_label='Metal green becquerel',
            secondary_label='Hyundai bluetooth',
        ),
    ),
    model_id=8592.48,
)

res = s.hightouch.update_model(req)

if res.update_model_200_application_json_one_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.UpdateModelRequest](../../models/operations/updatemodelrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.UpdateModelResponse](../../models/operations/updatemodelresponse.md)**


## update_source

Update an existing source

Patch a source based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateSourceRequest(
    source_update=shared.SourceUpdate(
        configuration={
            "animi": 'Land',
        },
        name='Bismuth Bedfordshire Northwest',
    ),
    source_id=2452.92,
)

res = s.hightouch.update_source(req)

if res.update_source_200_application_json_one_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateSourceRequest](../../models/operations/updatesourcerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateSourceResponse](../../models/operations/updatesourceresponse.md)**


## update_sync

Update an existing sync

Patch a sync based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateSyncRequest(
    sync_update=shared.SyncUpdate(
        configuration={
            "praesentium": 'Carolanne',
        },
        disabled=False,
        schedule=shared.SyncUpdateSchedule(
            schedule=[],
            type='Bedfordshire Chlorine',
        ),
    ),
    sync_id=6235.37,
)

res = s.hightouch.update_sync(req)

if res.update_sync_200_application_json_one_of is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UpdateSyncRequest](../../models/operations/updatesyncrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UpdateSyncResponse](../../models/operations/updatesyncresponse.md)**

