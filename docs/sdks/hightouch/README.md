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
* [get_sync_sequence_run](#get_sync_sequence_run) - Sync sequence status
* [list_destination](#list_destination) - List Destinations
* [list_model](#list_model) - List Models
* [list_source](#list_source) - List Sources
* [list_sync](#list_sync) - List Syncs
* [list_sync_runs](#list_sync_runs) - List Sync Runs
* [trigger_run](#trigger_run) - Trigger Sync
* [trigger_run_custom](#trigger_run_custom) - Trigger Sync From ID or Slug
* [trigger_run_id_graph](#trigger_run_id_graph)
* [trigger_sequence_run](#trigger_sequence_run) - Trigger Sync sequence
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
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = shared.DestinationCreate(
    configuration={
        'key': '<value>',
    },
    name='<value>',
    slug='<value>',
    type='<value>',
)

res = s.create_destination(req)

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.DestinationCreate](../../models/shared/destinationcreate.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateDestinationResponse](../../models/operations/createdestinationresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 409,422                  | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## create_model

Create a new model

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.CreateModelRequest(
    model_create=shared.ModelCreate(
        is_schema=False,
        name='<value>',
        primary_key='<value>',
        query_type='<value>',
        slug='<value>',
        source_id=8761.56,
    ),
)

res = s.create_model(req)

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.CreateModelRequest](../../models/operations/createmodelrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CreateModelResponse](../../models/operations/createmodelresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 409,422                  | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## create_source

Create a new source

### Example Usage

```python
import hightouch
from hightouch.models import shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = shared.SourceCreate(
    configuration={
        'key': '<value>',
    },
    name='<value>',
    slug='<value>',
    type='<value>',
)

res = s.create_source(req)

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.SourceCreate](../../models/shared/sourcecreate.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.CreateSourceResponse](../../models/operations/createsourceresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 409,422                  | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## create_sync

Create a new sync

### Example Usage

```python
import hightouch
from hightouch.models import shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = shared.SyncCreate(
    configuration={
        'key': '<value>',
    },
    destination_id=8797.77,
    disabled=False,
    model_id=2438.5,
    schedule=shared.SyncCreateSchedule(
        schedule=shared.CronSchedule(
            expression='<value>',
        ),
        type='<value>',
    ),
    slug='<value>',
)

res = s.create_sync(req)

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                              | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `request`                                              | [shared.SyncCreate](../../models/shared/synccreate.md) | :heavy_check_mark:                                     | The request object to use for the request.             |


### Response

**[operations.CreateSyncResponse](../../models/operations/createsyncresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 409,422                  | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## get_destination

Retrieve a destination based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.GetDestinationRequest(
    destination_id=4856.96,
)

res = s.get_destination(req)

if res.destination is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetDestinationRequest](../../models/operations/getdestinationrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetDestinationResponse](../../models/operations/getdestinationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_model

Retrieve models from model ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.GetModelRequest(
    model_id=7962.16,
)

res = s.get_model(req)

if res.model is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetModelRequest](../../models/operations/getmodelrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetModelResponse](../../models/operations/getmodelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_source

Retrieve source from source ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.GetSourceRequest(
    source_id=4378.62,
)

res = s.get_source(req)

if res.source is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetSourceRequest](../../models/operations/getsourcerequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetSourceResponse](../../models/operations/getsourceresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## get_sync

Retrieve sync from sync ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.GetSyncRequest(
    sync_id=7319.86,
)

res = s.get_sync(req)

if res.sync is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetSyncRequest](../../models/operations/getsyncrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetSyncResponse](../../models/operations/getsyncresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_sync_sequence_run

Get the status of a sync sequence run.

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.GetSyncSequenceRunRequest(
    sync_sequence_run_id='<value>',
)

res = s.get_sync_sequence_run(req)

if res.sync_sequence_status_output is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetSyncSequenceRunRequest](../../models/operations/getsyncsequencerunrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetSyncSequenceRunResponse](../../models/operations/getsyncsequencerunresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## list_destination

List the destinations in the user's workspace

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.ListDestinationRequest()

res = s.list_destination(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.ListDestinationRequest](../../models/operations/listdestinationrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.ListDestinationResponse](../../models/operations/listdestinationresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## list_model

List all the models in the current workspace including parent and related models

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.ListModelRequest()

res = s.list_model(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.ListModelRequest](../../models/operations/listmodelrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.ListModelResponse](../../models/operations/listmodelresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## list_source

List all the sources in the current workspace

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.ListSourceRequest()

res = s.list_source(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ListSourceRequest](../../models/operations/listsourcerequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ListSourceResponse](../../models/operations/listsourceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list_sync

List all the syncs in the current workspace

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.ListSyncRequest()

res = s.list_sync(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.ListSyncRequest](../../models/operations/listsyncrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.ListSyncResponse](../../models/operations/listsyncresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## list_sync_runs

List all sync runs under a sync

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.ListSyncRunsRequest(
    sync_id=8858.62,
)

res = s.list_sync_runs(req)

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListSyncRunsRequest](../../models/operations/listsyncrunsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListSyncRunsResponse](../../models/operations/listsyncrunsresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

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
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.TriggerRunRequest(
    sync_id='<value>',
)

res = s.trigger_run(req)

if res.trigger_run_output is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.TriggerRunRequest](../../models/operations/triggerrunrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.TriggerRunResponse](../../models/operations/triggerrunresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

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
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = shared.TriggerRunCustomInput()

res = s.trigger_run_custom(req)

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.TriggerRunCustomInput](../../models/shared/triggerruncustominput.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.TriggerRunCustomResponse](../../models/operations/triggerruncustomresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## trigger_run_id_graph

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.TriggerRunIDGraphRequest(
    graph_id='<value>',
)

res = s.trigger_run_id_graph(req)

if res.trigger_run_id_graph_output is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.TriggerRunIDGraphRequest](../../models/operations/triggerrunidgraphrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.TriggerRunIDGraphResponse](../../models/operations/triggerrunidgraphresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## trigger_sequence_run

Trigger a new run for the given sync sequence.

If a run is already in progress, this queues a sync sequence run that will be
executed immediately after the current run completes.

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.TriggerSequenceRunRequest(
    sync_sequence_id='<value>',
)

res = s.trigger_sequence_run(req)

if res.trigger_sequence_run_output is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.TriggerSequenceRunRequest](../../models/operations/triggersequencerunrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.TriggerSequenceRunResponse](../../models/operations/triggersequencerunresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## update_destination

Update an existing destination

Patch a destination based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.UpdateDestinationRequest(
    destination_update=shared.DestinationUpdate(),
    destination_id=8928.88,
)

res = s.update_destination(req)

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpdateDestinationRequest](../../models/operations/updatedestinationrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpdateDestinationResponse](../../models/operations/updatedestinationresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## update_model

Update an existing model

Patch a model based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.UpdateModelRequest(
    model_update=shared.ModelUpdate(),
    model_id=1027.03,
)

res = s.update_model(req)

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.UpdateModelRequest](../../models/operations/updatemodelrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.UpdateModelResponse](../../models/operations/updatemodelresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## update_source

Update an existing source

Patch a source based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.UpdateSourceRequest(
    source_update=shared.SourceUpdate(),
    source_id=6585.68,
)

res = s.update_source(req)

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.UpdateSourceRequest](../../models/operations/updatesourcerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.UpdateSourceResponse](../../models/operations/updatesourceresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |

## update_sync

Update an existing sync

Patch a sync based on its Hightouch ID

### Example Usage

```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ),
)

req = operations.UpdateSyncRequest(
    sync_update=shared.SyncUpdate(),
    sync_id=5066.51,
)

res = s.update_sync(req)

if res.one_of is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UpdateSyncRequest](../../models/operations/updatesyncrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UpdateSyncResponse](../../models/operations/updatesyncresponse.md)**
### Errors

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 422                      | application/json         |
| errors.SDKError          | 4x-5xx                   | */*                      |
