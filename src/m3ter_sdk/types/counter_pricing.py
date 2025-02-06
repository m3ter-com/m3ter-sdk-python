# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CounterPricing", "PricingBand"]


class PricingBand(BaseModel):
    fixed_price: float = FieldInfo(alias="fixedPrice")
    """Fixed price charged for the Pricing band."""

    lower_limit: float = FieldInfo(alias="lowerLimit")
    """Lower limit for the Pricing band."""

    unit_price: float = FieldInfo(alias="unitPrice")
    """Unit price charged for the Pricing band."""

    id: Optional[str] = None
    """The ID for the Pricing band."""

    credit_type_id: Optional[str] = FieldInfo(alias="creditTypeId", default=None)
    """**OBSOLETE - this is deprecated and no longer used.**"""


class CounterPricing(BaseModel):
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
    """Unique short code for the Pricing."""

    counter_id: Optional[str] = FieldInfo(alias="counterId", default=None)
    """UUID of the Counter used to create the pricing."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """The ID of the user who created this item."""

    cumulative: Optional[bool] = None
    """
    Controls whether or not charge rates under a set of pricing bands configured for
    a Pricing are applied according to each separate band or at the highest band
    reached.

    The default value is **TRUE**.

    - When TRUE, at billing charge rates are applied according to each separate
      band.

    - When FALSE, at billing charge rates are applied according to highest band
      reached.
    """

    description: Optional[str] = None
    """Displayed on Bill line items."""

    dt_created: Optional[datetime] = FieldInfo(alias="dtCreated", default=None)
    """The DateTime when this item was created _(in ISO-8601 format)_."""

    dt_last_modified: Optional[datetime] = FieldInfo(alias="dtLastModified", default=None)
    """The DateTime when this item was last modified _(in ISO-8601 format)_."""

    end_date: Optional[datetime] = FieldInfo(alias="endDate", default=None)
    """
    The end date _(in ISO-8601 format)_ for when the Pricing ceases to be active for
    the Plan or Plan Template.

    If not specified, the Pricing remains active indefinitely.
    """

    last_modified_by: Optional[str] = FieldInfo(alias="lastModifiedBy", default=None)
    """The ID of the user who last modified this item."""

    plan_id: Optional[str] = FieldInfo(alias="planId", default=None)
    """UUID of the Plan the Pricing is created for."""

    plan_template_id: Optional[str] = FieldInfo(alias="planTemplateId", default=None)
    """UUID of the Plan Template the Pricing was created for."""

    pricing_bands: Optional[List[PricingBand]] = FieldInfo(alias="pricingBands", default=None)

    pro_rate_adjustment_credit: Optional[bool] = FieldInfo(alias="proRateAdjustmentCredit", default=None)
    """The default value is **TRUE**.

    - When TRUE, counter adjustment credits are prorated and are billed according to
      the number of days in billing period.

    - When FALSE, counter adjustment credits are not prorated and are billed for the
      entire billing period.
    """

    pro_rate_adjustment_debit: Optional[bool] = FieldInfo(alias="proRateAdjustmentDebit", default=None)
    """The default value is **TRUE**.

    - When TRUE, counter adjustment debits are prorated and are billed according to
      the number of days in billing period.

    - When FALSE, counter adjustment debits are not prorated and are billed for the
      entire billing period.
    """

    pro_rate_running_total: Optional[bool] = FieldInfo(alias="proRateRunningTotal", default=None)
    """The default value is **TRUE**.

    - When TRUE, counter running total charges are prorated and are billed according
      to the number of days in billing period.

    - When FALSE, counter running total charges are not prorated and are billed for
      the entire billing period.
    """

    running_total_bill_in_advance: Optional[bool] = FieldInfo(alias="runningTotalBillInAdvance", default=None)
    """The default value is **TRUE**.

    - When TRUE, running totals are billed at the start of each billing period.

    - When FALSE, running totals are billed at the end of each billing period.
    """

    start_date: Optional[datetime] = FieldInfo(alias="startDate", default=None)
    """
    The start date _(in ISO-8601 format)_ for when the Pricing starts to be active
    for the Plan of Plan Template.
    """
