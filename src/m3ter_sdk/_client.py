# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
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
from ._version import __version__
from .resources import meters, counters, products, aggregations, authentication, compound_aggregations
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import M3terError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "M3ter", "AsyncM3ter", "Client", "AsyncClient"]


class M3ter(SyncAPIClient):
    authentication: authentication.AuthenticationResource
    aggregations: aggregations.AggregationsResource
    compound_aggregations: compound_aggregations.CompoundAggregationsResource
    counters: counters.CountersResource
    meters: meters.MetersResource
    products: products.ProductsResource
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
        self.aggregations = aggregations.AggregationsResource(self)
        self.compound_aggregations = compound_aggregations.CompoundAggregationsResource(self)
        self.counters = counters.CountersResource(self)
        self.meters = meters.MetersResource(self)
        self.products = products.ProductsResource(self)
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
    aggregations: aggregations.AsyncAggregationsResource
    compound_aggregations: compound_aggregations.AsyncCompoundAggregationsResource
    counters: counters.AsyncCountersResource
    meters: meters.AsyncMetersResource
    products: products.AsyncProductsResource
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
        self.aggregations = aggregations.AsyncAggregationsResource(self)
        self.compound_aggregations = compound_aggregations.AsyncCompoundAggregationsResource(self)
        self.counters = counters.AsyncCountersResource(self)
        self.meters = meters.AsyncMetersResource(self)
        self.products = products.AsyncProductsResource(self)
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
        self.aggregations = aggregations.AggregationsResourceWithRawResponse(client.aggregations)
        self.compound_aggregations = compound_aggregations.CompoundAggregationsResourceWithRawResponse(
            client.compound_aggregations
        )
        self.counters = counters.CountersResourceWithRawResponse(client.counters)
        self.meters = meters.MetersResourceWithRawResponse(client.meters)
        self.products = products.ProductsResourceWithRawResponse(client.products)


class AsyncM3terWithRawResponse:
    def __init__(self, client: AsyncM3ter) -> None:
        self.authentication = authentication.AsyncAuthenticationResourceWithRawResponse(client.authentication)
        self.aggregations = aggregations.AsyncAggregationsResourceWithRawResponse(client.aggregations)
        self.compound_aggregations = compound_aggregations.AsyncCompoundAggregationsResourceWithRawResponse(
            client.compound_aggregations
        )
        self.counters = counters.AsyncCountersResourceWithRawResponse(client.counters)
        self.meters = meters.AsyncMetersResourceWithRawResponse(client.meters)
        self.products = products.AsyncProductsResourceWithRawResponse(client.products)


class M3terWithStreamedResponse:
    def __init__(self, client: M3ter) -> None:
        self.authentication = authentication.AuthenticationResourceWithStreamingResponse(client.authentication)
        self.aggregations = aggregations.AggregationsResourceWithStreamingResponse(client.aggregations)
        self.compound_aggregations = compound_aggregations.CompoundAggregationsResourceWithStreamingResponse(
            client.compound_aggregations
        )
        self.counters = counters.CountersResourceWithStreamingResponse(client.counters)
        self.meters = meters.MetersResourceWithStreamingResponse(client.meters)
        self.products = products.ProductsResourceWithStreamingResponse(client.products)


class AsyncM3terWithStreamedResponse:
    def __init__(self, client: AsyncM3ter) -> None:
        self.authentication = authentication.AsyncAuthenticationResourceWithStreamingResponse(client.authentication)
        self.aggregations = aggregations.AsyncAggregationsResourceWithStreamingResponse(client.aggregations)
        self.compound_aggregations = compound_aggregations.AsyncCompoundAggregationsResourceWithStreamingResponse(
            client.compound_aggregations
        )
        self.counters = counters.AsyncCountersResourceWithStreamingResponse(client.counters)
        self.meters = meters.AsyncMetersResourceWithStreamingResponse(client.meters)
        self.products = products.AsyncProductsResourceWithStreamingResponse(client.products)


Client = M3ter

AsyncClient = AsyncM3ter
