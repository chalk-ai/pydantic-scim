from enum import Enum
from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Field


class GroupMemberKind(Enum):
    User = "User"
    Group = "Group"


class Member(BaseModel):
    value: Optional[str] = Field(
        None, description="Identifier of the member of this Group."
    )
    _ref: Optional[AnyUrl] = Field(
        None,
        alias="$ref",
        description="The URI corresponding to a SCIM resource that is a member of this Group.",
    )
    type: Optional[GroupMemberKind] = Field(
        None,
        description="A label indicating the type of resource, e.g., 'User' or 'Group'.",
    )


class Group(BaseModel):
    displayName: str = Field(
        ..., description="A human-readable name for the Group. REQUIRED."
    )
    members: Optional[List[Member]] = Field(
        None, description="A list of members of the Group."
    )
