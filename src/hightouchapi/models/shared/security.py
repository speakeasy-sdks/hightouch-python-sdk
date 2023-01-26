import dataclasses



@dataclasses.dataclass
class SchemeBearerAuth:
    authorization: str = dataclasses.field(metadata={'security': { 'field_name': 'Authorization' }})
    
