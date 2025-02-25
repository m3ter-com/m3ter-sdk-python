# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .external_mapping import ExternalMapping

__all__ = ["ExternalMappingListByExternalEntityResponse"]


class ExternalMappingListByExternalEntityResponse(BaseModel):
    data: Optional[List[ExternalMapping]] = None
    """An array containing the list of requested External Mapping entities."""

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
    """The `nextToken` for multi-page retrievals.

    It is used to fetch the next page of External Mappings in a paginated list.
    """
