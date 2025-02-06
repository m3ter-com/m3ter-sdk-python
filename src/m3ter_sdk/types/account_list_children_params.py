# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountListChildrenParams"]


class AccountListChildrenParams(TypedDict, total=False):
    org_id: Required[Annotated[str, PropertyInfo(alias="orgId")]]

    next_token: Annotated[Optional[str], PropertyInfo(alias="nextToken")]

    page_size: Annotated[Optional[int], PropertyInfo(alias="pageSize")]
