<div align="center">
  <img src="https://user-images.githubusercontent.com/6267663/221538828-de1343f2-b249-4ba2-85e3-a2e43cc5f265.svg">
  <h1>Python SDK</h1>
  <p>Hightouch exposes a REST API that lets users interact with resources like syncs, models, sources and destinations.</p>
  <a href="https://hightouch.com/docs/api-reference"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000000&style=for-the-badge" /></a>
  <a href="https://github.com/speakeasy-sdks/hightouch-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/hightouch-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
  <a href="https://github.com/speakeasy-sdks/hightouch-python-sdk/releases"><img src="https://img.shields.io/github/v/release/speakeasy-sdks/hightouch-python-sdk?sort=semver&style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/hightouch-python-sdk.git
```
<!-- End SDK Installation [installation] -->

## Authentication

- Create an [API key](https://app.hightouch.com/settings/api-keys)
- From the API keys tab on the Settings page, select Add API key.
- Enter a descriptive Name for your key.
- Copy your API key and store it in a safe location. The key will only be displayed once.
- Click Create API key.

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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
        'key': 'string',
    },
    name='string',
    slug='string',
    type='string',
)

res = s.create_destination(req)

if res.one_of is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [Hightouch SDK](docs/sdks/hightouch/README.md)

* [create_destination](docs/sdks/hightouch/README.md#create_destination) - Create Destination
* [create_model](docs/sdks/hightouch/README.md#create_model) - Create Model
* [create_source](docs/sdks/hightouch/README.md#create_source) - Create Source
* [create_sync](docs/sdks/hightouch/README.md#create_sync) - Create Sync
* [get_destination](docs/sdks/hightouch/README.md#get_destination) - Get Destination
* [get_model](docs/sdks/hightouch/README.md#get_model) - Get Model
* [get_source](docs/sdks/hightouch/README.md#get_source) - Get Source
* [get_sync](docs/sdks/hightouch/README.md#get_sync) - Get Sync
* [get_sync_sequence_run](docs/sdks/hightouch/README.md#get_sync_sequence_run) - Sync sequence status
* [list_destination](docs/sdks/hightouch/README.md#list_destination) - List Destinations
* [list_model](docs/sdks/hightouch/README.md#list_model) - List Models
* [list_source](docs/sdks/hightouch/README.md#list_source) - List Sources
* [list_sync](docs/sdks/hightouch/README.md#list_sync) - List Syncs
* [list_sync_runs](docs/sdks/hightouch/README.md#list_sync_runs) - List Sync Runs
* [trigger_run](docs/sdks/hightouch/README.md#trigger_run) - Trigger Sync
* [trigger_run_custom](docs/sdks/hightouch/README.md#trigger_run_custom) - Trigger Sync From ID or Slug
* [trigger_run_id_graph](docs/sdks/hightouch/README.md#trigger_run_id_graph)
* [trigger_sequence_run](docs/sdks/hightouch/README.md#trigger_sequence_run) - Trigger Sync sequence
* [update_destination](docs/sdks/hightouch/README.md#update_destination) - Update Destination
* [update_model](docs/sdks/hightouch/README.md#update_model) - Update Model
* [update_source](docs/sdks/hightouch/README.md#update_source) - Update Source
* [update_sync](docs/sdks/hightouch/README.md#update_sync) - Update Sync
<!-- End Available Resources and Operations [operations] -->







<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object             | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ValidateErrorJSON | 409,422                  | application/json         |
| errors.SDKError          | 400-600                  | */*                      |

### Example

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
        'key': 'string',
    },
    name='string',
    slug='string',
    type='string',
)

res = None
try:
    res = s.create_destination(req)
except errors.ValidateErrorJSON as e:
    print(e)  # handle exception
    raise(e)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.one_of is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->



<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.hightouch.com/api/v1` | None |

#### Example

```python
import hightouch
from hightouch.models import shared

s = hightouch.Hightouch(
    server_idx=0,
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.DestinationCreate(
    configuration={
        'key': 'string',
    },
    name='string',
    slug='string',
    type='string',
)

res = s.create_destination(req)

if res.one_of is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import hightouch
from hightouch.models import shared

s = hightouch.Hightouch(
    server_url="https://api.hightouch.com/api/v1",
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.DestinationCreate(
    configuration={
        'key': 'string',
    },
    name='string',
    slug='string',
    type='string',
)

res = s.create_destination(req)

if res.one_of is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->



<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import hightouch
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = hightouch.Hightouch(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->



<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
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
        'key': 'string',
    },
    name='string',
    slug='string',
    type='string',
)

res = s.create_destination(req)

if res.one_of is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->



### SDK Generated by [Speakeasy](https://speakeasyapi.dev/)
