from enum import Enum
from typing import Tuple, List, Optional, Dict

from pydantic import BaseModel

from pydanticscim.group import Group
from pydanticscim.user import User


class SCIMError(BaseModel):
    detail: str
    status: int
    schemas: Tuple[str] = ("urn:ietf:params:scim:api:messages:2.0:Error",)

    @classmethod
    def not_found(cls, detail: str = "Not found") -> "SCIMError":
        return cls(detail=detail, status=404)


class PatchOp(Enum):
    replace = "replace"
    remove = "remove"
    add = "add"


class PatchOperation(BaseModel):
    op: PatchOp
    path: str
    value: Optional[Dict] = None


class PatchRequest(BaseModel):
    Operations: List[PatchOperation]


class ListResponse(BaseModel):
    totalResults: int
    startIndex: int
    itemsPerPage: int
    Resources: List[BaseModel]
    schemas: Tuple[str] = ("urn:ietf:params:scim:api:messages:2.0:ListResponse",)

    @classmethod
    def for_users(
        cls,
        users: List[User],
        start_index: int = 0,
        items_per_page: int | None = None,
    ) -> "ListResponse":
        return cls(
            Resources=users,
            totalResults=len(users),
            itemsPerPage=items_per_page or len(users),
            startIndex=start_index,
        )

    @classmethod
    def for_groups(
        cls,
        groups: List[Group],
        start_index: int = 0,
        items_per_page: int | None = None,
    ) -> "ListResponse":
        return cls(
            Resources=groups,
            totalResults=len(groups),
            itemsPerPage=items_per_page or len(groups),
            startIndex=start_index,
        )