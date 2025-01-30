# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MeterListParams"]


class MeterListParams(TypedDict, total=False):
    codes: List[str]
    """list of codes to retrieve"""

    ids: List[str]
    """list of ids to retrieve"""

    next_token: Annotated[str, PropertyInfo(alias="nextToken")]
    """nextToken for multi page retrievals"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Number of Meters to retrieve per page"""

    product_id: Annotated[List[str], PropertyInfo(alias="productId")]
    """The UUIDs of the products to retrieve meters for"""
