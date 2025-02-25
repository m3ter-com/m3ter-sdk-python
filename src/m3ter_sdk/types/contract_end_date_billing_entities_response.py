# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ContractEndDateBillingEntitiesResponse",
    "FailedEntities",
    "FailedEntitiesAccountplan",
    "FailedEntitiesContract",
    "FailedEntitiesCounterPricings",
    "FailedEntitiesPrepayment",
    "FailedEntitiesPricings",
    "UpdatedEntities",
    "UpdatedEntitiesAccountplan",
    "UpdatedEntitiesContract",
    "UpdatedEntitiesCounterPricings",
    "UpdatedEntitiesPrepayment",
    "UpdatedEntitiesPricings",
]


class FailedEntitiesAccountplan(BaseModel):
    empty: Optional[bool] = None


class FailedEntitiesContract(BaseModel):
    empty: Optional[bool] = None


class FailedEntitiesCounterPricings(BaseModel):
    empty: Optional[bool] = None


class FailedEntitiesPrepayment(BaseModel):
    empty: Optional[bool] = None


class FailedEntitiesPricings(BaseModel):
    empty: Optional[bool] = None


class FailedEntities(BaseModel):
    accountplan: Optional[FailedEntitiesAccountplan] = FieldInfo(alias="ACCOUNTPLAN", default=None)

    contract: Optional[FailedEntitiesContract] = FieldInfo(alias="CONTRACT", default=None)

    counter_pricings: Optional[FailedEntitiesCounterPricings] = FieldInfo(alias="COUNTER_PRICINGS", default=None)

    prepayment: Optional[FailedEntitiesPrepayment] = FieldInfo(alias="PREPAYMENT", default=None)

    pricings: Optional[FailedEntitiesPricings] = FieldInfo(alias="PRICINGS", default=None)


class UpdatedEntitiesAccountplan(BaseModel):
    empty: Optional[bool] = None


class UpdatedEntitiesContract(BaseModel):
    empty: Optional[bool] = None


class UpdatedEntitiesCounterPricings(BaseModel):
    empty: Optional[bool] = None


class UpdatedEntitiesPrepayment(BaseModel):
    empty: Optional[bool] = None


class UpdatedEntitiesPricings(BaseModel):
    empty: Optional[bool] = None


class UpdatedEntities(BaseModel):
    accountplan: Optional[UpdatedEntitiesAccountplan] = FieldInfo(alias="ACCOUNTPLAN", default=None)

    contract: Optional[UpdatedEntitiesContract] = FieldInfo(alias="CONTRACT", default=None)

    counter_pricings: Optional[UpdatedEntitiesCounterPricings] = FieldInfo(alias="COUNTER_PRICINGS", default=None)

    prepayment: Optional[UpdatedEntitiesPrepayment] = FieldInfo(alias="PREPAYMENT", default=None)

    pricings: Optional[UpdatedEntitiesPricings] = FieldInfo(alias="PRICINGS", default=None)


class ContractEndDateBillingEntitiesResponse(BaseModel):
    failed_entities: Optional[FailedEntities] = FieldInfo(alias="failedEntities", default=None)
    """
    A dictionary with keys as identifiers of billing entities and values as lists
    containing details of the entities for which the update failed.
    """

    status_message: Optional[str] = FieldInfo(alias="statusMessage", default=None)
    """A message indicating the status of the operation."""

    updated_entities: Optional[UpdatedEntities] = FieldInfo(alias="updatedEntities", default=None)
    """
    A dictionary with keys as identifiers of billing entities and values as lists
    containing details of the updated entities.
    """
