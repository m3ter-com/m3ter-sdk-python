# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MeterUpdateParams", "DataField", "DerivedField"]


class MeterUpdateParams(TypedDict, total=False):
    org_id: Required[Annotated[str, PropertyInfo(alias="orgId")]]

    code: Required[str]
    """Code of the Meter - unique short code used to identify the Meter.

    **NOTE:** Code has a maximum length of 80 characters and must not contain
    non-printable or whitespace characters (except space), and cannot start/end with
    whitespace.
    """

    data_fields: Required[Annotated[Iterable[DataField], PropertyInfo(alias="dataFields")]]
    """
    Used to submit categorized raw usage data values for ingest into the platform -
    either numeric quantitative values or non-numeric data values. At least one
    required per Meter; maximum 15 per Meter.
    """

    derived_fields: Required[Annotated[Iterable[DerivedField], PropertyInfo(alias="derivedFields")]]
    """
    Used to submit usage data values for ingest into the platform that are the
    result of a calculation performed on `dataFields`, `customFields`, or system
    `Timestamp` fields. Raw usage data is not submitted using `derivedFields`.
    Maximum 15 per Meter. _(Optional)_.

    **Note:** Required parameter. If you want to create a Meter without Derived
    Fields, use an empty array `[]`. If you use a `null`, you'll receive an error.
    """

    name: Required[str]
    """Descriptive name for the Meter."""

    custom_fields: Annotated[Dict[str, object], PropertyInfo(alias="customFields")]
    """User defined fields enabling you to attach custom data.

    The value for a custom field can be either a string or a number.

    If `customFields` can also be defined for this entity at the Organizational
    level, `customField` values defined at individual level override values of
    `customFields` with the same name defined at Organization level.

    See
    [Working with Custom Fields](https://www.m3ter.com/docs/guides/creating-and-managing-products/working-with-custom-fields)
    in the m3ter documentation for more information.
    """

    group_id: Annotated[str, PropertyInfo(alias="groupId")]
    """UUID of the group the Meter belongs to. _(Optional)_."""

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """UUID of the product the Meter belongs to.

    _(Optional)_ - if left blank, the Meter is global.
    """

    version: int
    """The version number of the entity:

    - **Create entity:** Not valid for initial insertion of new entity - _do not use
      for Create_. On initial Create, version is set at 1 and listed in the
      response.
    - **Update Entity:** On Update, version is required and must match the existing
      version because a check is performed to ensure sequential versioning is
      preserved. Version is incremented by 1 and listed in the response.
    """


class DataField(TypedDict, total=False):
    category: Required[Literal["WHO", "WHERE", "WHAT", "OTHER", "METADATA", "MEASURE", "INCOME", "COST"]]
    """The type of field (WHO, WHAT, WHERE, MEASURE, METADATA, INCOME, COST, OTHER)."""

    code: Required[str]
    """Short code to identify the field

    **NOTE:** Code has a maximum length of 80 characters and can only contain
    letters, numbers, underscore, and the dollar character, and must not start with
    a number.
    """

    name: Required[str]
    """Descriptive name of the field."""

    unit: str
    """The units to measure the data with.

    Should conform to _Unified Code for Units of Measure_ (UCUM). Required only for
    numeric field categories.
    """


class DerivedField(TypedDict, total=False):
    category: Required[Literal["WHO", "WHERE", "WHAT", "OTHER", "METADATA", "MEASURE", "INCOME", "COST"]]
    """The type of field (WHO, WHAT, WHERE, MEASURE, METADATA, INCOME, COST, OTHER)."""

    code: Required[str]
    """Short code to identify the field

    **NOTE:** Code has a maximum length of 80 characters and can only contain
    letters, numbers, underscore, and the dollar character, and must not start with
    a number.
    """

    name: Required[str]
    """Descriptive name of the field."""

    unit: str
    """The units to measure the data with.

    Should conform to _Unified Code for Units of Measure_ (UCUM). Required only for
    numeric field categories.
    """
