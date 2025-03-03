# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DebitReason"]


class DebitReason(BaseModel):
    id: str
    """The UUID of the entity."""

    version: int
    """The version number:

    - **Create:** On initial Create to insert a new entity, the version is set at 1
      in the response.
    - **Update:** On successful Update, the version is incremented by 1 in the
      response.
    """

    archived: Optional[bool] = None
    """TRUE / FALSE flag indicating whether the data entity is archived.

    An entity can be archived if it is obsolete.
    """

    code: Optional[str] = None
    """The short code of the data entity."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """The id of the user who created this debit reason."""

    dt_created: Optional[datetime] = FieldInfo(alias="dtCreated", default=None)
    """The DateTime when the debit reason was created _(in ISO-8601 format)_."""

    dt_last_modified: Optional[datetime] = FieldInfo(alias="dtLastModified", default=None)
    """The DateTime when the debit reason was last modified _(in ISO-8601 format)_."""

    last_modified_by: Optional[str] = FieldInfo(alias="lastModifiedBy", default=None)
    """The id of the user who last modified this debit reason."""

    name: Optional[str] = None
    """The name of the data entity."""
