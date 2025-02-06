# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountSearchParams"]


class AccountSearchParams(TypedDict, total=False):
    from_document: Annotated[int, PropertyInfo(alias="fromDocument")]
    """fromDocument for multi page retrievals"""

    operator: Literal["AND", "OR"]
    """Search Operator to be used while querying search"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Number of Accounts to retrieve per page"""

    search_query: Annotated[str, PropertyInfo(alias="searchQuery")]
    """Query for data using special syntax.

    Query parameters should be delimited using $ Allowed comparators are > (greater
    than), >= (grater or equal than), : (equal), < (less than), <= (less than or
    equal), ~ (contains). Allowed parameters: name, code, currency,
    purchaseOrderNumber, parentAccountId, codes, id, createdBy, dtCreated,
    lastModifiedBy, ids.Query example: searchQuery=name~test$currency:USD. This
    query is translated into: find accounts that name contains 'test' AND currency
    is USD.
    """

    sort_by: Annotated[str, PropertyInfo(alias="sortBy")]
    """Name of the parameter on which sorting is performed"""

    sort_order: Annotated[Literal["ASC", "DESC"], PropertyInfo(alias="sortOrder")]
    """Sorting order"""
