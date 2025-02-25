# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .bill import Bill
from .._models import BaseModel

__all__ = ["BillSearchResponse"]


class BillSearchResponse(BaseModel):
    data: Optional[List[Bill]] = None
    """An array containing the list of requested Bills."""

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
    """The `nextToken` for multi-page retrievals.

    It is used to fetch the next page of Bills in a paginated list.
    """
