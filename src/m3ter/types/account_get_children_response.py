# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .account_response import AccountResponse

__all__ = ["AccountGetChildrenResponse"]


class AccountGetChildrenResponse(BaseModel):
    data: Optional[List[AccountResponse]] = None

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
