<!-- Start SDK Example Usage -->
```python
import hightouch
from hightouch.models import operations, shared

s = hightouch.Hightouch()


req = shared.DestinationCreate(
    configuration={
        "provident": "distinctio",
        "quibusdam": "unde",
        "nulla": "corrupti",
    },
    name="illum",
    slug="vel",
    type="error",
)
    
res = s.create_destination(req, operations.CreateDestinationSecurity(
    bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.create_destination_200_application_json_any_of is not None:
    # handle response
```
<!-- End SDK Example Usage -->