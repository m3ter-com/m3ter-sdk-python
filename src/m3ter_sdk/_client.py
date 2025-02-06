# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._models import FinalRequestOptions
from ._version import __version__
from .resources import (
    plans,
    meters,
    accounts,
    counters,
    pricings,
    products,
    contracts,
    currencies,
    bill_config,
    commitments,
    plan_groups,
    aggregations,
    account_plans,
    debit_reasons,
    authentication,
    credit_reasons,
    plan_templates,
    counter_pricings,
    plan_group_links,
    transaction_types,
    counter_adjustments,
    organization_config,
    compound_aggregations,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import M3terError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.balances import balances

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "M3ter", "AsyncM3ter", "Client", "AsyncClient"]

from .types import AuthenticationGetBearerTokenResponse


class M3ter(SyncAPIClient):
    authentication: authentication.AuthenticationResource
    accounts: accounts.AccountsResource
    account_plans: account_plans.AccountPlansResource
    aggregations: aggregations.AggregationsResource
    balances: balances.BalancesResource
    bill_config: bill_config.BillConfigResource
    commitments: commitments.CommitmentsResource
    compound_aggregations: compound_aggregations.CompoundAggregationsResource
    contracts: contracts.ContractsResource
    counters: counters.CountersResource
    counter_adjustments: counter_adjustments.CounterAdjustmentsResource
    counter_pricings: counter_pricings.CounterPricingsResource
    credit_reasons: credit_reasons.CreditReasonsResource
    currencies: currencies.CurrenciesResource
    debit_reasons: debit_reasons.DebitReasonsResource
    meters: meters.MetersResource
    organization_config: organization_config.OrganizationConfigResource
    plans: plans.PlansResource
    plan_groups: plan_groups.PlanGroupsResource
    plan_group_links: plan_group_links.PlanGroupLinksResource
    plan_templates: plan_templates.PlanTemplatesResource
    pricings: pricings.PricingsResource
    products: products.ProductsResource
    transaction_types: transaction_types.TransactionTypesResource
    with_raw_response: M3terWithRawResponse
    with_streaming_response: M3terWithStreamedResponse

    # client options
    api_key: str
    api_secret: str
    token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_secret: str | None = None,
        token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous m3ter client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `M3TER_API_KEY`
        - `api_secret` from `M3TER_API_SECRET`
        - `token` from `M3TER_API_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("M3TER_API_KEY")
        if api_key is None:
            raise M3terError(
                "The api_key client option must be set either by passing api_key to the client or by setting the M3TER_API_KEY environment variable"
            )
        self.api_key = api_key

        if api_secret is None:
            api_secret = os.environ.get("M3TER_API_SECRET")
        if api_secret is None:
            raise M3terError(
                "The api_secret client option must be set either by passing api_secret to the client or by setting the M3TER_API_SECRET environment variable"
            )
        self.api_secret = api_secret

        if token is None:
            token = os.environ.get("M3TER_API_TOKEN")
        self.token = token

        if base_url is None:
            base_url = os.environ.get("M3TER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.m3ter.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.authentication = authentication.AuthenticationResource(self)
        self.accounts = accounts.AccountsResource(self)
        self.account_plans = account_plans.AccountPlansResource(self)
        self.aggregations = aggregations.AggregationsResource(self)
        self.balances = balances.BalancesResource(self)
        self.bill_config = bill_config.BillConfigResource(self)
        self.commitments = commitments.CommitmentsResource(self)
        self.compound_aggregations = compound_aggregations.CompoundAggregationsResource(self)
        self.contracts = contracts.ContractsResource(self)
        self.counters = counters.CountersResource(self)
        self.counter_adjustments = counter_adjustments.CounterAdjustmentsResource(self)
        self.counter_pricings = counter_pricings.CounterPricingsResource(self)
        self.credit_reasons = credit_reasons.CreditReasonsResource(self)
        self.currencies = currencies.CurrenciesResource(self)
        self.debit_reasons = debit_reasons.DebitReasonsResource(self)
        self.meters = meters.MetersResource(self)
        self.organization_config = organization_config.OrganizationConfigResource(self)
        self.plans = plans.PlansResource(self)
        self.plan_groups = plan_groups.PlanGroupsResource(self)
        self.plan_group_links = plan_group_links.PlanGroupLinksResource(self)
        self.plan_templates = plan_templates.PlanTemplatesResource(self)
        self.pricings = pricings.PricingsResource(self)
        self.products = products.ProductsResource(self)
        self.transaction_types = transaction_types.TransactionTypesResource(self)
        self.with_raw_response = M3terWithRawResponse(self)
        self.with_streaming_response = M3terWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        token = self.token
        if token is None:
            return {}
        return {"Authorization": f"Bearer {token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if custom_headers.get("Authorization"):
            return
        if self.token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    @override
    def _prepare_options(
        self,
        options: FinalRequestOptions,  # noqa: ARG002
    ) -> FinalRequestOptions:
        if not options.url.endswith("/oauth/token"):
            if not self.token:
                auth: str = base64.b64encode(f"{self.api_key}:{self.api_secret}".encode("utf8")).decode("utf8")
                token: AuthenticationGetBearerTokenResponse = self.authentication.get_bearer_token(
                    grant_type="client_credentials", extra_headers={"Authorization": f"Basic {auth}"}
                )
                self.token = token.access_token
        return options

    def copy(
        self,
        *,
        api_key: str | None = None,
        api_secret: str | None = None,
        token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            api_secret=api_secret or self.api_secret,
            token=token or self.token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncM3ter(AsyncAPIClient):
    authentication: authentication.AsyncAuthenticationResource
    accounts: accounts.AsyncAccountsResource
    account_plans: account_plans.AsyncAccountPlansResource
    aggregations: aggregations.AsyncAggregationsResource
    balances: balances.AsyncBalancesResource
    bill_config: bill_config.AsyncBillConfigResource
    commitments: commitments.AsyncCommitmentsResource
    compound_aggregations: compound_aggregations.AsyncCompoundAggregationsResource
    contracts: contracts.AsyncContractsResource
    counters: counters.AsyncCountersResource
    counter_adjustments: counter_adjustments.AsyncCounterAdjustmentsResource
    counter_pricings: counter_pricings.AsyncCounterPricingsResource
    credit_reasons: credit_reasons.AsyncCreditReasonsResource
    currencies: currencies.AsyncCurrenciesResource
    debit_reasons: debit_reasons.AsyncDebitReasonsResource
    meters: meters.AsyncMetersResource
    organization_config: organization_config.AsyncOrganizationConfigResource
    plans: plans.AsyncPlansResource
    plan_groups: plan_groups.AsyncPlanGroupsResource
    plan_group_links: plan_group_links.AsyncPlanGroupLinksResource
    plan_templates: plan_templates.AsyncPlanTemplatesResource
    pricings: pricings.AsyncPricingsResource
    products: products.AsyncProductsResource
    transaction_types: transaction_types.AsyncTransactionTypesResource
    with_raw_response: AsyncM3terWithRawResponse
    with_streaming_response: AsyncM3terWithStreamedResponse

    # client options
    api_key: str
    api_secret: str
    token: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_secret: str | None = None,
        token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async m3ter client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `M3TER_API_KEY`
        - `api_secret` from `M3TER_API_SECRET`
        - `token` from `M3TER_API_TOKEN`
        """
        if api_key is None:
            api_key = os.environ.get("M3TER_API_KEY")
        if api_key is None:
            raise M3terError(
                "The api_key client option must be set either by passing api_key to the client or by setting the M3TER_API_KEY environment variable"
            )
        self.api_key = api_key

        if api_secret is None:
            api_secret = os.environ.get("M3TER_API_SECRET")
        if api_secret is None:
            raise M3terError(
                "The api_secret client option must be set either by passing api_secret to the client or by setting the M3TER_API_SECRET environment variable"
            )
        self.api_secret = api_secret

        if token is None:
            token = os.environ.get("M3TER_API_TOKEN")
        self.token = token

        if base_url is None:
            base_url = os.environ.get("M3TER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.m3ter.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.authentication = authentication.AsyncAuthenticationResource(self)
        self.accounts = accounts.AsyncAccountsResource(self)
        self.account_plans = account_plans.AsyncAccountPlansResource(self)
        self.aggregations = aggregations.AsyncAggregationsResource(self)
        self.balances = balances.AsyncBalancesResource(self)
        self.bill_config = bill_config.AsyncBillConfigResource(self)
        self.commitments = commitments.AsyncCommitmentsResource(self)
        self.compound_aggregations = compound_aggregations.AsyncCompoundAggregationsResource(self)
        self.contracts = contracts.AsyncContractsResource(self)
        self.counters = counters.AsyncCountersResource(self)
        self.counter_adjustments = counter_adjustments.AsyncCounterAdjustmentsResource(self)
        self.counter_pricings = counter_pricings.AsyncCounterPricingsResource(self)
        self.credit_reasons = credit_reasons.AsyncCreditReasonsResource(self)
        self.currencies = currencies.AsyncCurrenciesResource(self)
        self.debit_reasons = debit_reasons.AsyncDebitReasonsResource(self)
        self.meters = meters.AsyncMetersResource(self)
        self.organization_config = organization_config.AsyncOrganizationConfigResource(self)
        self.plans = plans.AsyncPlansResource(self)
        self.plan_groups = plan_groups.AsyncPlanGroupsResource(self)
        self.plan_group_links = plan_group_links.AsyncPlanGroupLinksResource(self)
        self.plan_templates = plan_templates.AsyncPlanTemplatesResource(self)
        self.pricings = pricings.AsyncPricingsResource(self)
        self.products = products.AsyncProductsResource(self)
        self.transaction_types = transaction_types.AsyncTransactionTypesResource(self)
        self.with_raw_response = AsyncM3terWithRawResponse(self)
        self.with_streaming_response = AsyncM3terWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        token = self.token
        if token is None:
            return {}
        return {"Authorization": f"Bearer {token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.token and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        api_secret: str | None = None,
        token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            api_secret=api_secret or self.api_secret,
            token=token or self.token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class M3terWithRawResponse:
    def __init__(self, client: M3ter) -> None:
        self.authentication = authentication.AuthenticationResourceWithRawResponse(client.authentication)
        self.accounts = accounts.AccountsResourceWithRawResponse(client.accounts)
        self.account_plans = account_plans.AccountPlansResourceWithRawResponse(client.account_plans)
        self.aggregations = aggregations.AggregationsResourceWithRawResponse(client.aggregations)
        self.balances = balances.BalancesResourceWithRawResponse(client.balances)
        self.bill_config = bill_config.BillConfigResourceWithRawResponse(client.bill_config)
        self.commitments = commitments.CommitmentsResourceWithRawResponse(client.commitments)
        self.compound_aggregations = compound_aggregations.CompoundAggregationsResourceWithRawResponse(
            client.compound_aggregations
        )
        self.contracts = contracts.ContractsResourceWithRawResponse(client.contracts)
        self.counters = counters.CountersResourceWithRawResponse(client.counters)
        self.counter_adjustments = counter_adjustments.CounterAdjustmentsResourceWithRawResponse(
            client.counter_adjustments
        )
        self.counter_pricings = counter_pricings.CounterPricingsResourceWithRawResponse(client.counter_pricings)
        self.credit_reasons = credit_reasons.CreditReasonsResourceWithRawResponse(client.credit_reasons)
        self.currencies = currencies.CurrenciesResourceWithRawResponse(client.currencies)
        self.debit_reasons = debit_reasons.DebitReasonsResourceWithRawResponse(client.debit_reasons)
        self.meters = meters.MetersResourceWithRawResponse(client.meters)
        self.organization_config = organization_config.OrganizationConfigResourceWithRawResponse(
            client.organization_config
        )
        self.plans = plans.PlansResourceWithRawResponse(client.plans)
        self.plan_groups = plan_groups.PlanGroupsResourceWithRawResponse(client.plan_groups)
        self.plan_group_links = plan_group_links.PlanGroupLinksResourceWithRawResponse(client.plan_group_links)
        self.plan_templates = plan_templates.PlanTemplatesResourceWithRawResponse(client.plan_templates)
        self.pricings = pricings.PricingsResourceWithRawResponse(client.pricings)
        self.products = products.ProductsResourceWithRawResponse(client.products)
        self.transaction_types = transaction_types.TransactionTypesResourceWithRawResponse(client.transaction_types)


class AsyncM3terWithRawResponse:
    def __init__(self, client: AsyncM3ter) -> None:
        self.authentication = authentication.AsyncAuthenticationResourceWithRawResponse(client.authentication)
        self.accounts = accounts.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.account_plans = account_plans.AsyncAccountPlansResourceWithRawResponse(client.account_plans)
        self.aggregations = aggregations.AsyncAggregationsResourceWithRawResponse(client.aggregations)
        self.balances = balances.AsyncBalancesResourceWithRawResponse(client.balances)
        self.bill_config = bill_config.AsyncBillConfigResourceWithRawResponse(client.bill_config)
        self.commitments = commitments.AsyncCommitmentsResourceWithRawResponse(client.commitments)
        self.compound_aggregations = compound_aggregations.AsyncCompoundAggregationsResourceWithRawResponse(
            client.compound_aggregations
        )
        self.contracts = contracts.AsyncContractsResourceWithRawResponse(client.contracts)
        self.counters = counters.AsyncCountersResourceWithRawResponse(client.counters)
        self.counter_adjustments = counter_adjustments.AsyncCounterAdjustmentsResourceWithRawResponse(
            client.counter_adjustments
        )
        self.counter_pricings = counter_pricings.AsyncCounterPricingsResourceWithRawResponse(client.counter_pricings)
        self.credit_reasons = credit_reasons.AsyncCreditReasonsResourceWithRawResponse(client.credit_reasons)
        self.currencies = currencies.AsyncCurrenciesResourceWithRawResponse(client.currencies)
        self.debit_reasons = debit_reasons.AsyncDebitReasonsResourceWithRawResponse(client.debit_reasons)
        self.meters = meters.AsyncMetersResourceWithRawResponse(client.meters)
        self.organization_config = organization_config.AsyncOrganizationConfigResourceWithRawResponse(
            client.organization_config
        )
        self.plans = plans.AsyncPlansResourceWithRawResponse(client.plans)
        self.plan_groups = plan_groups.AsyncPlanGroupsResourceWithRawResponse(client.plan_groups)
        self.plan_group_links = plan_group_links.AsyncPlanGroupLinksResourceWithRawResponse(client.plan_group_links)
        self.plan_templates = plan_templates.AsyncPlanTemplatesResourceWithRawResponse(client.plan_templates)
        self.pricings = pricings.AsyncPricingsResourceWithRawResponse(client.pricings)
        self.products = products.AsyncProductsResourceWithRawResponse(client.products)
        self.transaction_types = transaction_types.AsyncTransactionTypesResourceWithRawResponse(
            client.transaction_types
        )


class M3terWithStreamedResponse:
    def __init__(self, client: M3ter) -> None:
        self.authentication = authentication.AuthenticationResourceWithStreamingResponse(client.authentication)
        self.accounts = accounts.AccountsResourceWithStreamingResponse(client.accounts)
        self.account_plans = account_plans.AccountPlansResourceWithStreamingResponse(client.account_plans)
        self.aggregations = aggregations.AggregationsResourceWithStreamingResponse(client.aggregations)
        self.balances = balances.BalancesResourceWithStreamingResponse(client.balances)
        self.bill_config = bill_config.BillConfigResourceWithStreamingResponse(client.bill_config)
        self.commitments = commitments.CommitmentsResourceWithStreamingResponse(client.commitments)
        self.compound_aggregations = compound_aggregations.CompoundAggregationsResourceWithStreamingResponse(
            client.compound_aggregations
        )
        self.contracts = contracts.ContractsResourceWithStreamingResponse(client.contracts)
        self.counters = counters.CountersResourceWithStreamingResponse(client.counters)
        self.counter_adjustments = counter_adjustments.CounterAdjustmentsResourceWithStreamingResponse(
            client.counter_adjustments
        )
        self.counter_pricings = counter_pricings.CounterPricingsResourceWithStreamingResponse(client.counter_pricings)
        self.credit_reasons = credit_reasons.CreditReasonsResourceWithStreamingResponse(client.credit_reasons)
        self.currencies = currencies.CurrenciesResourceWithStreamingResponse(client.currencies)
        self.debit_reasons = debit_reasons.DebitReasonsResourceWithStreamingResponse(client.debit_reasons)
        self.meters = meters.MetersResourceWithStreamingResponse(client.meters)
        self.organization_config = organization_config.OrganizationConfigResourceWithStreamingResponse(
            client.organization_config
        )
        self.plans = plans.PlansResourceWithStreamingResponse(client.plans)
        self.plan_groups = plan_groups.PlanGroupsResourceWithStreamingResponse(client.plan_groups)
        self.plan_group_links = plan_group_links.PlanGroupLinksResourceWithStreamingResponse(client.plan_group_links)
        self.plan_templates = plan_templates.PlanTemplatesResourceWithStreamingResponse(client.plan_templates)
        self.pricings = pricings.PricingsResourceWithStreamingResponse(client.pricings)
        self.products = products.ProductsResourceWithStreamingResponse(client.products)
        self.transaction_types = transaction_types.TransactionTypesResourceWithStreamingResponse(
            client.transaction_types
        )


class AsyncM3terWithStreamedResponse:
    def __init__(self, client: AsyncM3ter) -> None:
        self.authentication = authentication.AsyncAuthenticationResourceWithStreamingResponse(client.authentication)
        self.accounts = accounts.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.account_plans = account_plans.AsyncAccountPlansResourceWithStreamingResponse(client.account_plans)
        self.aggregations = aggregations.AsyncAggregationsResourceWithStreamingResponse(client.aggregations)
        self.balances = balances.AsyncBalancesResourceWithStreamingResponse(client.balances)
        self.bill_config = bill_config.AsyncBillConfigResourceWithStreamingResponse(client.bill_config)
        self.commitments = commitments.AsyncCommitmentsResourceWithStreamingResponse(client.commitments)
        self.compound_aggregations = compound_aggregations.AsyncCompoundAggregationsResourceWithStreamingResponse(
            client.compound_aggregations
        )
        self.contracts = contracts.AsyncContractsResourceWithStreamingResponse(client.contracts)
        self.counters = counters.AsyncCountersResourceWithStreamingResponse(client.counters)
        self.counter_adjustments = counter_adjustments.AsyncCounterAdjustmentsResourceWithStreamingResponse(
            client.counter_adjustments
        )
        self.counter_pricings = counter_pricings.AsyncCounterPricingsResourceWithStreamingResponse(
            client.counter_pricings
        )
        self.credit_reasons = credit_reasons.AsyncCreditReasonsResourceWithStreamingResponse(client.credit_reasons)
        self.currencies = currencies.AsyncCurrenciesResourceWithStreamingResponse(client.currencies)
        self.debit_reasons = debit_reasons.AsyncDebitReasonsResourceWithStreamingResponse(client.debit_reasons)
        self.meters = meters.AsyncMetersResourceWithStreamingResponse(client.meters)
        self.organization_config = organization_config.AsyncOrganizationConfigResourceWithStreamingResponse(
            client.organization_config
        )
        self.plans = plans.AsyncPlansResourceWithStreamingResponse(client.plans)
        self.plan_groups = plan_groups.AsyncPlanGroupsResourceWithStreamingResponse(client.plan_groups)
        self.plan_group_links = plan_group_links.AsyncPlanGroupLinksResourceWithStreamingResponse(
            client.plan_group_links
        )
        self.plan_templates = plan_templates.AsyncPlanTemplatesResourceWithStreamingResponse(client.plan_templates)
        self.pricings = pricings.AsyncPricingsResourceWithStreamingResponse(client.pricings)
        self.products = products.AsyncProductsResourceWithStreamingResponse(client.products)
        self.transaction_types = transaction_types.AsyncTransactionTypesResourceWithStreamingResponse(
            client.transaction_types
        )


Client = M3ter

AsyncClient = AsyncM3ter
