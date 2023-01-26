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