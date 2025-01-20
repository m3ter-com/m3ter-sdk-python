# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CounterListParams"]


class CounterListParams(TypedDict, total=False):
    codes: List[str]
    """List of Counter codes to retrieve.

    These are unique short codes to identify each Counter.
    """

    ids: List[str]
    """List of Counter IDs to retrieve."""

    next_token: Annotated[str, PropertyInfo(alias="nextToken")]
    """NextToken for multi page retrievals."""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Number of Counters to retrieve per page"""

    product_id: Annotated[Optional[List[str]], PropertyInfo(alias="productId")]
    """List of Products UUIDs to retrieve Counters for."""
