<!-- Start SDK Example Usage -->


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
        "optical": 'Sid',
    },
    name='Ergonomic mumble blue',
    slug='hollow Southeast Mobility',
    type='Jaguar Ford',
)

res = s.hightouch.create_destination(req)

if res.create_destination_200_application_json_one_of is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->