# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CounterCreateParams"]


class CounterCreateParams(TypedDict, total=False):
    version: int
    """The version number of the entity:

    - **Create entity:** Not valid for initial insertion of new entity - _do not use
      for Create_. On initial Create, version is set at 1 and listed in the
      response.
    - **Update Entity:** On Update, version is required and must match the existing
      version because a check is performed to ensure sequential versioning is
      preserved. Version is incremented by 1 and listed in the response.
    """
