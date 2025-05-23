# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScheduledEventConfigurationUpdateParams"]


class ScheduledEventConfigurationUpdateParams(TypedDict, total=False):
    org_id: Annotated[str, PropertyInfo(alias="orgId")]

    entity: Required[str]
    """
    The referenced configuration or billing entity for which the desired scheduled
    Event will trigger.
    """

    field: Required[str]
    """
    A DateTime field for which the desired scheduled Event will trigger - this must
    be a DateTime field on the referenced billing or configuration entity.
    """

    name: Required[str]
    """The name of the custom Scheduled Event Configuration.

    This must be in the format:

    - scheduled._name of entity_._custom event name_

    For example:

    - `scheduled.bill.endDateEvent`
    """

    offset: Required[int]
    """
    The offset in days from the specified DateTime field on the referenced entity
    when the scheduled Event will trigger.
    """

    version: int
    """The version number of the scheduled event configuration:

    - **Create entity**: Not valid for initial insertion - do not use for Create. On
      initial Create, version is set at 1 and listed in the response.
    - **Update Entity**: On Update, version is required and must match the existing
      version because a check is performed to ensure sequential versioning is
      preserved. Version is incremented by 1 and listed in the response.
    """
