# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CounterResponse"]


class CounterResponse(BaseModel):
    id: str
    """The UUID of the entity."""

    version: int
    """The version number:

    - **Create:** On initial Create to insert a new entity, the version is set at 1
      in the response.
    - **Update:** On successful Update, the version is incremented by 1 in the
      response.
    """

    code: Optional[str] = None
    """Code of the Counter. A unique short code to identify the Counter."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """The ID of the user who created this item."""

    dt_created: Optional[datetime] = FieldInfo(alias="dtCreated", default=None)
    """The DateTime when this item was created _(in ISO-8601 format)_."""

    dt_last_modified: Optional[datetime] = FieldInfo(alias="dtLastModified", default=None)
    """The DateTime when this item was last modified _(in ISO-8601 format)_."""

    last_modified_by: Optional[str] = FieldInfo(alias="lastModifiedBy", default=None)
    """The ID of the user who last modified this item."""

    name: Optional[str] = None
    """Name of the Counter."""

    product_id: Optional[str] = FieldInfo(alias="productId", default=None)
    """UUID of the product the Counter belongs to.

    _(Optional)_ - if no `productId` is returned, the Counter is Global. A Global
    Counter can be used to price Plans or Plan Templates belonging to any Product.
    """

    unit: Optional[str] = None
    """
    Label for units shown on Bill line items, and indicating to customers what they
    are being charged for.
    """
