# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BillSearchParams"]


class BillSearchParams(TypedDict, total=False):
    org_id: Annotated[str, PropertyInfo(alias="orgId")]

    from_document: Annotated[int, PropertyInfo(alias="fromDocument")]
    """fromDocument for multi page retrievals"""

    operator: Literal["AND", "OR"]
    """Search Operator to be used while querying search"""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Number of Commitments to retrieve per page"""

    search_query: Annotated[str, PropertyInfo(alias="searchQuery")]
    """Query for data using special syntax.

    Query parameters should be delimited using
    $.Allowed comparators are > (greater than), >= (grater than or equal), : (equal), < (less than), <= (less than or equal), ~ (contains). Allowed parameters: accountId, locked, billDate, startDate, endDate, dueDate, billingFrequency, externalInvoiceDateStart, externalInvoiceDateEnd, id, createdBy, dtCreated, lastModifiedBy, ids.Query example: searchQuery=startDate>2023-01-01$accountId:999cb15f-3e8a-4146-b4be-28d0aaedf275.
    This query is translated into: find bills that startDate is older than
    2023-01-01 AND accountId is equal to 999cb15f-3e8a-4146-b4be-28d0aaedf275.
    """

    sort_by: Annotated[str, PropertyInfo(alias="sortBy")]
    """Name of the parameter on which sorting is performed"""

    sort_order: Annotated[Literal["ASC", "DESC"], PropertyInfo(alias="sortOrder")]
    """Sorting order"""
