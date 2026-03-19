# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursor, AsyncCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.balances import transaction_list_params, transaction_create_params
from ...types.balances.transaction_response import TransactionResponse
from ...types.balances.transaction_summary_response import TransactionSummaryResponse

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    """Endpoints for creating/retrieving/updating/deleting Balances on Accounts.

    When you have created a Balance for an Account, you can create a positive or negative Transaction amounts for the Balance. To do this, you must first define Transaction Types for your Organization, and then use one of these Transaction Types when you add a specific Transaction to a Balance - see the [Create TransactionType](https://www.m3ter.com/docs/api#tag/TransactionType/operation/CreateTransactionType) call in the Transaction Type section in this API Reference for more details.

    Balances are typically used when a customer prepays an amount to add a credit to their Account, which can then be draw-down against charges due for product or service consumption. You can include options to top-up the original Balance.

    Examples of how Balances for end customer Accounts can be used:

    * Onboarding Balance/Free Trials. Offering an onboarding incentive to new customers as an initial free credit Balance on their Account.

    * Balance as initial commitment. Add a Balance amount to a new customer Account. This acts as an initial commitment, which allows them to use the service and gain an accurate insight into their usage level.

    * Managing Customer Satisfaction. Use Balance as credits that will be applied to subsequent Bills as compensation for acknowledged service delivery issues.

    * Facilitating Balance Adjustments:
        * Apply negative amounts to immediately write-off outstanding Balances.

    #### What is the difference between Balances and Commitments/Prepayments?

    To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

    Commitments - also referred to as Prepayments - are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the commitment or prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

    In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

    You can use Commitments/Prepayments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Commitment credit on an Account is drawn-down - Balance amounts first or Commitment/Prepayment amounts first.
    """

    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#with_streaming_response
        """
        return TransactionsResourceWithStreamingResponse(self)

    def create(
        self,
        balance_id: str,
        *,
        org_id: str | None = None,
        amount: float,
        applied_date: Union[str, datetime] | Omit = omit,
        currency_paid: str | Omit = omit,
        description: str | Omit = omit,
        paid: float | Omit = omit,
        transaction_date: Union[str, datetime] | Omit = omit,
        transaction_type_id: str | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionResponse:
        """Add a Transaction to a Balance.

        This endpoint allows you to create a new
        Transaction amount for a Balance. This amount then becomes available at billing
        for draw-down to cover charges due. The Transaction details should be provided
        in the request body.

        Before you can add a Transaction amount, you must first set up Transaction Types
        at the Organization Level - see the
        [Transaction Type](https://www.m3ter.com/docs/api#tag/TransactionType) section
        in this API Reference for more details. You can then use this call to add an
        instance of a Transaction Type to a Balance.

        **Note:** If you have a customer whose payment is in a different currency to the
        Balance currency, you can use the `paid` and `paidCurrency` request parameters
        to record the amount paid and alternative currency respectively. For example,
        you might add a Transaction amount of 200 USD to a Balance on a customer Account
        where the customer actually paid you 50 units in virtual currency X.

        Args:
          amount: The financial value of the transaction.

          applied_date: The date _(in ISO 8601 format)_ when the Balance transaction was applied.

          currency_paid: The currency code of the payment if it differs from the Balance currency. For
              example: USD, GBP or EUR.

          description: A brief description explaining the purpose and context of the transaction.

          paid: The payment amount if the payment currency differs from the Balance currency.

          transaction_date: The date _(in ISO 8601 format)_ when the transaction occurred.

          transaction_type_id: The unique identifier (UUID) of the transaction type. This is obtained from the
              list of created Transaction Types within the Organization Configuration.

          version:
              The version number of the entity:

              - **Create entity:** Not valid for initial insertion of new entity - _do not use
                for Create_. On initial Create, version is set at 1 and listed in the
                response.
              - **Update Entity:** On Update, version is required and must match the existing
                version because a check is performed to ensure sequential versioning is
                preserved. Version is incremented by 1 and listed in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not balance_id:
            raise ValueError(f"Expected a non-empty value for `balance_id` but received {balance_id!r}")
        return self._post(
            path_template(
                "/organizations/{org_id}/balances/{balance_id}/transactions", org_id=org_id, balance_id=balance_id
            ),
            body=maybe_transform(
                {
                    "amount": amount,
                    "applied_date": applied_date,
                    "currency_paid": currency_paid,
                    "description": description,
                    "paid": paid,
                    "transaction_date": transaction_date,
                    "transaction_type_id": transaction_type_id,
                    "version": version,
                },
                transaction_create_params.TransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionResponse,
        )

    def list(
        self,
        balance_id: str,
        *,
        org_id: str | None = None,
        entity_id: Optional[str] | Omit = omit,
        entity_type: Optional[Literal["BILL", "COMMITMENT", "USER", "SERVICE_USER", "SCHEDULER"]] | Omit = omit,
        next_token: str | Omit = omit,
        page_size: int | Omit = omit,
        transaction_type_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[TransactionResponse]:
        """
        Retrieve all Transactions for a specific Balance.

        This endpoint returns a list of all Transactions associated with a specific
        Balance. You can paginate through the Transactions by using the `pageSize` and
        `nextToken` parameters.

        Args:
          entity_type

          next_token: `nextToken` for multi page retrievals. A token for retrieving the next page of
              transactions. You'll get this from the response to your request.

          page_size: The maximum number of transactions to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not balance_id:
            raise ValueError(f"Expected a non-empty value for `balance_id` but received {balance_id!r}")
        return self._get_api_list(
            path_template(
                "/organizations/{org_id}/balances/{balance_id}/transactions", org_id=org_id, balance_id=balance_id
            ),
            page=SyncCursor[TransactionResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_id": entity_id,
                        "entity_type": entity_type,
                        "next_token": next_token,
                        "page_size": page_size,
                        "transaction_type_id": transaction_type_id,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            model=TransactionResponse,
        )

    def summary(
        self,
        balance_id: str,
        *,
        org_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionSummaryResponse:
        """
        Retrieves the Balance Transactions Summary for a given Balance.

        The response contains useful recorded and calculated Transaction amounts created
        for a Balance during the time it is active for the Account, including amounts
        relevant to any rollover amount configured for a Balance:

        - `totalCreditAmount`. The sum of all credits amounts created for the Balance.
        - `totalDebitAmount`. The sum of all debit amounts created for the Balance.
        - `initialCreditAmount`. The initial credit amount created for the Balance.
        - `expiredBalanceAmount`. The amount of the Balance remaining at the time the
          Balance expires and which is not included in any configured Rollover amount.
          For example, suppose a Balance reaches its end date and $1000 credit remains
          unused. If the Balance is configured to rollover $800, then the
          `expiredBalanceAmount` is calculated as $1000 - $800 = $200.
        - `rolloverConsumed`. The sum of debits made against the configured rollover
          amount. Note that this amount is dynamic relative to when the API call is made
          until either the rollover end date is reached or the cap configured for the
          rollover amount is reached, after which it will be unchanged. If no rollover
          is configured for a Balance, then this is ignored.
        - `balanceConsumed`. The sum of debits made against the Balance. Note that this
          amount is dynamic relative to when the API call is made until either the
          Balance end date is reached or the available Balance amount reaches zero,
          after which it will be unchanged.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not balance_id:
            raise ValueError(f"Expected a non-empty value for `balance_id` but received {balance_id!r}")
        return self._get(
            path_template(
                "/organizations/{org_id}/balances/{balance_id}/transactions/summary",
                org_id=org_id,
                balance_id=balance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSummaryResponse,
        )


class AsyncTransactionsResource(AsyncAPIResource):
    """Endpoints for creating/retrieving/updating/deleting Balances on Accounts.

    When you have created a Balance for an Account, you can create a positive or negative Transaction amounts for the Balance. To do this, you must first define Transaction Types for your Organization, and then use one of these Transaction Types when you add a specific Transaction to a Balance - see the [Create TransactionType](https://www.m3ter.com/docs/api#tag/TransactionType/operation/CreateTransactionType) call in the Transaction Type section in this API Reference for more details.

    Balances are typically used when a customer prepays an amount to add a credit to their Account, which can then be draw-down against charges due for product or service consumption. You can include options to top-up the original Balance.

    Examples of how Balances for end customer Accounts can be used:

    * Onboarding Balance/Free Trials. Offering an onboarding incentive to new customers as an initial free credit Balance on their Account.

    * Balance as initial commitment. Add a Balance amount to a new customer Account. This acts as an initial commitment, which allows them to use the service and gain an accurate insight into their usage level.

    * Managing Customer Satisfaction. Use Balance as credits that will be applied to subsequent Bills as compensation for acknowledged service delivery issues.

    * Facilitating Balance Adjustments:
        * Apply negative amounts to immediately write-off outstanding Balances.

    #### What is the difference between Balances and Commitments/Prepayments?

    To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

    Commitments - also referred to as Prepayments - are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the commitment or prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

    In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

    You can use Commitments/Prepayments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Commitment credit on an Account is drawn-down - Balance amounts first or Commitment/Prepayment amounts first.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#with_streaming_response
        """
        return AsyncTransactionsResourceWithStreamingResponse(self)

    async def create(
        self,
        balance_id: str,
        *,
        org_id: str | None = None,
        amount: float,
        applied_date: Union[str, datetime] | Omit = omit,
        currency_paid: str | Omit = omit,
        description: str | Omit = omit,
        paid: float | Omit = omit,
        transaction_date: Union[str, datetime] | Omit = omit,
        transaction_type_id: str | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionResponse:
        """Add a Transaction to a Balance.

        This endpoint allows you to create a new
        Transaction amount for a Balance. This amount then becomes available at billing
        for draw-down to cover charges due. The Transaction details should be provided
        in the request body.

        Before you can add a Transaction amount, you must first set up Transaction Types
        at the Organization Level - see the
        [Transaction Type](https://www.m3ter.com/docs/api#tag/TransactionType) section
        in this API Reference for more details. You can then use this call to add an
        instance of a Transaction Type to a Balance.

        **Note:** If you have a customer whose payment is in a different currency to the
        Balance currency, you can use the `paid` and `paidCurrency` request parameters
        to record the amount paid and alternative currency respectively. For example,
        you might add a Transaction amount of 200 USD to a Balance on a customer Account
        where the customer actually paid you 50 units in virtual currency X.

        Args:
          amount: The financial value of the transaction.

          applied_date: The date _(in ISO 8601 format)_ when the Balance transaction was applied.

          currency_paid: The currency code of the payment if it differs from the Balance currency. For
              example: USD, GBP or EUR.

          description: A brief description explaining the purpose and context of the transaction.

          paid: The payment amount if the payment currency differs from the Balance currency.

          transaction_date: The date _(in ISO 8601 format)_ when the transaction occurred.

          transaction_type_id: The unique identifier (UUID) of the transaction type. This is obtained from the
              list of created Transaction Types within the Organization Configuration.

          version:
              The version number of the entity:

              - **Create entity:** Not valid for initial insertion of new entity - _do not use
                for Create_. On initial Create, version is set at 1 and listed in the
                response.
              - **Update Entity:** On Update, version is required and must match the existing
                version because a check is performed to ensure sequential versioning is
                preserved. Version is incremented by 1 and listed in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not balance_id:
            raise ValueError(f"Expected a non-empty value for `balance_id` but received {balance_id!r}")
        return await self._post(
            path_template(
                "/organizations/{org_id}/balances/{balance_id}/transactions", org_id=org_id, balance_id=balance_id
            ),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "applied_date": applied_date,
                    "currency_paid": currency_paid,
                    "description": description,
                    "paid": paid,
                    "transaction_date": transaction_date,
                    "transaction_type_id": transaction_type_id,
                    "version": version,
                },
                transaction_create_params.TransactionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionResponse,
        )

    def list(
        self,
        balance_id: str,
        *,
        org_id: str | None = None,
        entity_id: Optional[str] | Omit = omit,
        entity_type: Optional[Literal["BILL", "COMMITMENT", "USER", "SERVICE_USER", "SCHEDULER"]] | Omit = omit,
        next_token: str | Omit = omit,
        page_size: int | Omit = omit,
        transaction_type_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TransactionResponse, AsyncCursor[TransactionResponse]]:
        """
        Retrieve all Transactions for a specific Balance.

        This endpoint returns a list of all Transactions associated with a specific
        Balance. You can paginate through the Transactions by using the `pageSize` and
        `nextToken` parameters.

        Args:
          entity_type

          next_token: `nextToken` for multi page retrievals. A token for retrieving the next page of
              transactions. You'll get this from the response to your request.

          page_size: The maximum number of transactions to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not balance_id:
            raise ValueError(f"Expected a non-empty value for `balance_id` but received {balance_id!r}")
        return self._get_api_list(
            path_template(
                "/organizations/{org_id}/balances/{balance_id}/transactions", org_id=org_id, balance_id=balance_id
            ),
            page=AsyncCursor[TransactionResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "entity_id": entity_id,
                        "entity_type": entity_type,
                        "next_token": next_token,
                        "page_size": page_size,
                        "transaction_type_id": transaction_type_id,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            model=TransactionResponse,
        )

    async def summary(
        self,
        balance_id: str,
        *,
        org_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TransactionSummaryResponse:
        """
        Retrieves the Balance Transactions Summary for a given Balance.

        The response contains useful recorded and calculated Transaction amounts created
        for a Balance during the time it is active for the Account, including amounts
        relevant to any rollover amount configured for a Balance:

        - `totalCreditAmount`. The sum of all credits amounts created for the Balance.
        - `totalDebitAmount`. The sum of all debit amounts created for the Balance.
        - `initialCreditAmount`. The initial credit amount created for the Balance.
        - `expiredBalanceAmount`. The amount of the Balance remaining at the time the
          Balance expires and which is not included in any configured Rollover amount.
          For example, suppose a Balance reaches its end date and $1000 credit remains
          unused. If the Balance is configured to rollover $800, then the
          `expiredBalanceAmount` is calculated as $1000 - $800 = $200.
        - `rolloverConsumed`. The sum of debits made against the configured rollover
          amount. Note that this amount is dynamic relative to when the API call is made
          until either the rollover end date is reached or the cap configured for the
          rollover amount is reached, after which it will be unchanged. If no rollover
          is configured for a Balance, then this is ignored.
        - `balanceConsumed`. The sum of debits made against the Balance. Note that this
          amount is dynamic relative to when the API call is made until either the
          Balance end date is reached or the available Balance amount reaches zero,
          after which it will be unchanged.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not balance_id:
            raise ValueError(f"Expected a non-empty value for `balance_id` but received {balance_id!r}")
        return await self._get(
            path_template(
                "/organizations/{org_id}/balances/{balance_id}/transactions/summary",
                org_id=org_id,
                balance_id=balance_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSummaryResponse,
        )


class TransactionsResourceWithRawResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.create = to_raw_response_wrapper(
            transactions.create,
        )
        self.list = to_raw_response_wrapper(
            transactions.list,
        )
        self.summary = to_raw_response_wrapper(
            transactions.summary,
        )


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.create = async_to_raw_response_wrapper(
            transactions.create,
        )
        self.list = async_to_raw_response_wrapper(
            transactions.list,
        )
        self.summary = async_to_raw_response_wrapper(
            transactions.summary,
        )


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.create = to_streamed_response_wrapper(
            transactions.create,
        )
        self.list = to_streamed_response_wrapper(
            transactions.list,
        )
        self.summary = to_streamed_response_wrapper(
            transactions.summary,
        )


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.create = async_to_streamed_response_wrapper(
            transactions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            transactions.list,
        )
        self.summary = async_to_streamed_response_wrapper(
            transactions.summary,
        )
