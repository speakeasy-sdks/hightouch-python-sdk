<!-- Start SDK Example Usage -->


```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()

req = shared.DestinationCreate(
    configuration={
        "corrupti": 'provident',
    },
    name='Ellis Mitchell',
    slug='illum',
    type='vel',
)

res = s.create_destination(req, operations.CreateDestinationSecurity(
    bearer_auth="",
))

if res.create_destination_200_application_json_any_of is not None:
    # handle response
```
<!-- End SDK Example Usage -->