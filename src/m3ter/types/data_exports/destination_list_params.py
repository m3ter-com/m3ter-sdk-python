# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DestinationListParams"]


class DestinationListParams(TypedDict, total=False):
    org_id: Annotated[str, PropertyInfo(alias="orgId")]

    ids: List[str]
    """List of Export Destination UUIDs to retrieve."""

    next_token: Annotated[str, PropertyInfo(alias="nextToken")]
    """nextToken for multi page retrievals"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Number of returned Export Destinations to list per page."""
