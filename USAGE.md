<!-- Start SDK Example Usage -->
```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()
   
req = operations.CreateDestinationRequest(
    security=operations.CreateDestinationSecurity(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
    request=shared.DestinationCreate(
        configuration={
            "deserunt": "porro",
            "nulla": "id",
            "vero": "perspiciatis",
        },
        name="nulla",
        slug="nihil",
        type="fuga",
    ),
)
    
res = s.create_destination(req)

if res.create_destination_200_application_json_any_of is not None:
    # handle response
```
<!-- End SDK Example Usage -->