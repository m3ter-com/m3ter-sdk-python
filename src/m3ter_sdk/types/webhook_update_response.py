# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WebhookUpdateResponse", "Credentials"]


class Credentials:
    pass


class WebhookUpdateResponse(BaseModel):
    credentials: Credentials
    """The credentials required for the webhook."""

    description: str

    name: str

    url: str
    """The URL to which the webhook requests will be sent."""

    active: Optional[bool] = None

    code: Optional[str] = None

    version: Optional[int] = None
    """The version number of the entity:

    - **Create entity:** Not valid for initial insertion of new entity - _do not use
      for Create_. On initial Create, version is set at 1 and listed in the
      response.
    - **Update Entity:** On Update, version is required and must match the existing
      version because a check is performed to ensure sequential versioning is
      preserved. Version is incremented by 1 and listed in the response.
    """
