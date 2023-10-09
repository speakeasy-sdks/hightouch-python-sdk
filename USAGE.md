<!-- Start SDK Example Usage -->


```python
import hightouch
from hightouch.models import shared

s = hightouch.Hightouch(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = {
    "optical": 'Sid',
}

res = s.create_destination(req)

if res.create_destination_200_application_json_one_of is not None:
    # handle response
```
<!-- End SDK Example Usage -->