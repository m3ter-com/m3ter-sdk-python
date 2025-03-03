# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomFieldUpdateParams"]


class CustomFieldUpdateParams(TypedDict, total=False):
    org_id: Annotated[str, PropertyInfo(alias="orgId")]

    account: Dict[str, object]
    """Updates to Account entity CustomFields."""

    account_plan: Annotated[Dict[str, object], PropertyInfo(alias="accountPlan")]
    """Updates to accountPlan entity CustomFields."""

    aggregation: Dict[str, object]
    """Updates to simple Aggregation entity CustomFields."""

    compound_aggregation: Annotated[Dict[str, object], PropertyInfo(alias="compoundAggregation")]
    """Updates to Compound Aggregation entity CustomFields."""

    meter: Dict[str, object]
    """Updates to Meter entity CustomFields."""

    organization: Dict[str, object]
    """Updates to Organization CustomFields."""

    plan: Dict[str, object]
    """Updates to Plan entity CustomFields."""

    plan_template: Annotated[Dict[str, object], PropertyInfo(alias="planTemplate")]
    """Updates to planTemplate entity CustomFields."""

    product: Dict[str, object]
    """Updates to Product entity CustomFields."""

    version: int
    """The version number of the entity:

    - **Create entity:** Not valid for initial insertion of new entity - _do not use
      for Create_. On initial Create, version is set at 1 and listed in the
      response.
    - **Update Entity:** On Update, version is required and must match the existing
      version because a check is performed to ensure sequential versioning is
      preserved. Version is incremented by 1 and listed in the response.
    """
