# Hightouch SDK

## Overview

Hightouch Public Rest API to access syncs, models, sources and destinations

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
        "ipsa": 'delectus',
        "tempora": 'suscipit',
        "molestiae": 'minus',
        "placeat": 'voluptatum',
    },
    name='Miriam Huel',
    slug='ab',
    type='quis',
)

res = s.hightouch.create_destination(req, operations.CreateDestinationSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.create_destination_200_application_json_any_of is not None:
    # handle response
```

## create_model

Create a new model

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = shared.ModelCreate(
    custom=shared.ModelCreateCustom(
        query='veritatis',
    ),
    dbt=shared.ModelCreateDbt(
        model_id='deserunt',
    ),
    is_schema=False,
    name='Roberta Sipes',
    primary_key='odit',
    query_type='at',
    raw=shared.ModelCreateRaw(
        sql='at',
    ),
    slug='maiores',
    source_id='molestiae',
    table=shared.ModelCreateTable(
        name='Forrest Koepp',
    ),
    visual=shared.ModelCreateVisual(
        filter='dolorum',
        parent_id='dicta',
        primary_label='nam',
        secondary_label='officia',
    ),
)

res = s.hightouch.create_model(req, operations.CreateModelSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.create_model_200_application_json_any_of is not None:
    # handle response
```

## create_source

Create a new source

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = shared.SourceCreate(
    configuration={
        "fugit": 'deleniti',
        "hic": 'optio',
        "totam": 'beatae',
    },
    name='Tanya Gleason',
    slug='cum',
    type='esse',
)

res = s.hightouch.create_source(req, operations.CreateSourceSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.create_source_200_application_json_any_of is not None:
    # handle response
```

## create_sync

Create a new sync

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = shared.SyncCreate(
    configuration={
        "excepturi": 'aspernatur',
    },
    destination_id='perferendis',
    disabled=False,
    model_id='ad',
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
                    time='iste',
                ),
            ],
        ),
        type='dolor',
    ),
    slug='natus',
)

res = s.hightouch.create_sync(req, operations.CreateSyncSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.create_sync_200_application_json_any_of is not None:
    # handle response
```

## get_destination

Retrieve a destination based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.GetDestinationRequest(
    destination_id=3864.89,
)

res = s.hightouch.get_destination(req, operations.GetDestinationSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.destination is not None:
    # handle response
```

## get_model

Retrieve models from model ID

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.GetModelRequest(
    model_id=9437.49,
)

res = s.hightouch.get_model(req, operations.GetModelSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.model is not None:
    # handle response
```

## get_source

Retrieve source from source ID

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.GetSourceRequest(
    source_id=9025.99,
)

res = s.hightouch.get_source(req, operations.GetSourceSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.source is not None:
    # handle response
```

## get_sync

Retrieve sync from sync ID

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.GetSyncRequest(
    sync_id=6818.2,
)

res = s.hightouch.get_sync(req, operations.GetSyncSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.sync is not None:
    # handle response
```

## list_destination

List the destinations in the user's workspace

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.ListDestinationRequest(
    limit=4499.5,
    name='Sheryl Kertzmann',
    offset=992.8,
    order_by=operations.ListDestinationOrderByEnum.ID,
    slug='reiciendis',
)

res = s.hightouch.list_destination(req, operations.ListDestinationSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.list_destination_200_application_json_object is not None:
    # handle response
```

## list_model

List all the models in the current workspace including parent and related models

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.ListModelRequest(
    limit=6667.67,
    name='Cameron Dach',
    offset=1289.26,
    order_by=operations.ListModelOrderByEnum.CREATED_AT,
    slug='enim',
)

res = s.hightouch.list_model(req, operations.ListModelSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.list_model_200_application_json_object is not None:
    # handle response
```

## list_source

List all the sources in the current workspace

### Example Usage

```python
import hightouch
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.ListSourceRequest(
    limit=6078.31,
    name='Ms. Cathy Marks',
    offset=9883.74,
    order_by=operations.ListSourceOrderByEnum.UPDATED_AT,
    slug='architecto',
)

res = s.hightouch.list_source(req, operations.ListSourceSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.list_source_200_application_json_object is not None:
    # handle response
```

## list_sync

List all the syncs in the current workspace

### Example Usage

```python
import hightouch
import dateutil.parser
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.ListSyncRequest(
    after=dateutil.parser.isoparse('2022-08-01T12:28:44.292Z'),
    before=dateutil.parser.isoparse('2022-09-05T05:51:25.673Z'),
    limit=9953,
    model_id=6531.08,
    offset=5818.5,
    order_by=operations.ListSyncOrderByEnum.NAME,
    slug='commodi',
)

res = s.hightouch.list_sync(req, operations.ListSyncSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.list_sync_200_application_json_object is not None:
    # handle response
```

## list_sync_runs

List all sync runs under a sync

### Example Usage

```python
import hightouch
import dateutil.parser
from hightouch.models import operations

s = hightouch.Hightouch()

req = operations.ListSyncRunsRequest(
    after=dateutil.parser.isoparse('2022-07-11T17:38:58.953Z'),
    before=dateutil.parser.isoparse('2022-05-18T10:03:04.921Z'),
    limit=1589.69,
    offset=3380.07,
    order_by=operations.ListSyncRunsOrderByEnum.ID,
    run_id=6747.52,
    sync_id=6563.3,
    within=3172.02,
)

res = s.hightouch.list_sync_runs(req, operations.ListSyncRunsSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.list_sync_runs_200_application_json_object is not None:
    # handle response
```

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
    sync_id='odit',
)

res = s.hightouch.trigger_run(req, operations.TriggerRunSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.trigger_run_output is not None:
    # handle response
```

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
    sync_id='quo',
    sync_slug='sequi',
)

res = s.hightouch.trigger_run_custom(req, operations.TriggerRunCustomSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.trigger_run_custom_200_application_json_any_of is not None:
    # handle response
```

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
            "ipsam": 'id',
            "possimus": 'aut',
            "quasi": 'error',
            "temporibus": 'laborum',
        },
        name='Johanna Wolf',
    ),
    destination_id=5096.24,
)

res = s.hightouch.update_destination(req, operations.UpdateDestinationSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.update_destination_200_application_json_any_of is not None:
    # handle response
```

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
            query='voluptatibus',
        ),
        dbt=shared.ModelUpdateDbt(
            model_id='ipsa',
        ),
        is_schema=False,
        name='Mr. Jared Ritchie',
        primary_key='ut',
        raw=shared.ModelUpdateRaw(
            sql='maiores',
        ),
        table=shared.ModelUpdateTable(
            name='Stacy Gulgowski MD',
        ),
        visual=shared.ModelUpdateVisual(
            filter='enim',
            parent_id='accusamus',
            primary_label='commodi',
            secondary_label='repudiandae',
        ),
    ),
    model_id=641.47,
)

res = s.hightouch.update_model(req, operations.UpdateModelSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.update_model_200_application_json_any_of is not None:
    # handle response
```

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
            "quidem": 'molestias',
        },
        name='Ervin Gleason',
    ),
    source_id=9167.23,
)

res = s.hightouch.update_source(req, operations.UpdateSourceSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.update_source_200_application_json_any_of is not None:
    # handle response
```

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
            "repudiandae": 'sint',
        },
        disabled=False,
        schedule=shared.SyncUpdateSchedule(
            schedule=shared.IntervalSchedule(
                interval=shared.Interval(
                    quantity=9292.97,
                    unit=shared.IntervalUnitEnum.HOUR,
                ),
            ),
            type='enim',
        ),
    ),
    sync_id=93.56,
)

res = s.hightouch.update_sync(req, operations.UpdateSyncSecurity(
    bearer_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.update_sync_200_application_json_any_of is not None:
    # handle response
```
