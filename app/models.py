from dataclasses import dataclass, asdict
from typing import Optional, Any
@dataclass
class SourceRef:
    document:str; page:Optional[int]=None; sheet:Optional[str]=None; cell:Optional[str]=None; quote:str=""
@dataclass
class Requirement:
    requirement_id:str; category:str; text:str; mandatory:Optional[bool]; quantity:Any=None; unit:Optional[str]=None; threshold:Optional[str]=None; deadline:Optional[str]=None; status:str="active"; source:dict=None; amendment:Optional[str]=None; supersedes:Optional[str]=None
    def to_dict(self): return asdict(self)
