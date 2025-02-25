# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .permission_policy import PermissionPolicy

__all__ = ["ResourceGroupListPermissionsResponse"]


class ResourceGroupListPermissionsResponse(BaseModel):
    data: Optional[List[PermissionPolicy]] = None

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
