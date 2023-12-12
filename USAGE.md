<!-- Start SDK Example Usage [usage] -->
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