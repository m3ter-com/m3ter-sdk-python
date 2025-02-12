# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .account import Account
from .._models import BaseModel

__all__ = ["AccountSearchResponse"]


class AccountSearchResponse(BaseModel):
    data: Optional[List[Account]] = None

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
