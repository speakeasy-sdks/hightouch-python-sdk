# Hightouch Python SDK

Hightouch exposes a REST API that lets users interact with resources like syncs, models, sources and destinations. 

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install hightouchapi
```
<!-- End SDK Installation -->

## Authentication

- Create an [API key](https://app.hightouch.com/settings/api-keys)
- From the API keys tab on the Settings page, select Add API key.
- Enter a descriptive Name for your key.
- Copy your API key and store it in a safe location. The key will only be displayed once.
- Click Create API key.

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import hightouchapi
from hightouchapi.models import operations, shared

s = hightouchapi.Hightouchapi()
    
req = operations.CreateDestinationRequest(
    security=operations.CreateDestinationSecurity(
        bearer_auth=shared.SchemeBearerAuth(
            authorization="Bearer YOUR_BEARER_TOKEN_HERE",
        ),
    ),
    request=shared.DestinationCreate(
        configuration={
            "voluptas": "culpa",
        },
        name="expedita",
        slug="consequuntur",
        type="dolor",
    ),
)
    
res = s.create_destination(req)

if res.create_destination_200_application_json_any_of is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations

### Hightouchapi SDK

* `create_destination` - Create Destination
* `create_model` - Create Model
* `create_source` - Create Source
* `create_sync` - Create Sync
* `get_destination` - Get Destination
* `get_model` - Get Model
* `get_source` - Get Source
* `get_sync` - Get Sync
* `list_destination` - List Destinations
* `list_model` - List Models
* `list_source` - List Sources
* `list_sync` - List Syncs
* `list_sync_runs` - List Sync Runs
* `trigger_run` - Trigger Sync
* `trigger_run_custom` - Trigger Sync From ID or Slug
* `update_destination` - Update Destination
* `update_model` - Update Model
* `update_source` - Update Source
* `update_sync` - Update Sync

<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
