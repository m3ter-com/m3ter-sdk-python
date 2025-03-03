# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import (
    transaction_type_list_params,
    transaction_type_create_params,
    transaction_type_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursor, AsyncCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.transaction_type import TransactionType

__all__ = ["TransactionTypesResource", "AsyncTransactionTypesResource"]


class TransactionTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TransactionTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#with_streaming_response
        """
        return TransactionTypesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        org_id: str | None = None,
        name: str,
        archived: bool | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        version: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionType:
        """Create a new TransactionType for the specified Organization.

        Details of the new
        TransactionType should be included in the request body.

        Args:
          name: The name of the entity.

          archived: A Boolean TRUE / FALSE flag indicating whether the entity is archived. An entity
              can be archived if it is obsolete.

              - TRUE - the entity is in the archived state.
              - FALSE - the entity is not in the archived state.

          code: The short code for the entity.

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
        return self._post(
            f"/organizations/{org_id}/picklists/transactiontypes",
            body=maybe_transform(
                {
                    "name": name,
                    "archived": archived,
                    "code": code,
                    "version": version,
                },
                transaction_type_create_params.TransactionTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionType,
        )

    def retrieve(
        self,
        id: str,
        *,
        org_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionType:
        """
        Retrieves the TransactionType with the given UUID from the specified
        Organization.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/organizations/{org_id}/picklists/transactiontypes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionType,
        )

    def update(
        self,
        id: str,
        *,
        org_id: str | None = None,
        name: str,
        archived: bool | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        version: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionType:
        """
        Updates the TransactionType with the specified UUID for the specified
        Organization. Update details for the TransactionType should be included in the
        request body.

        Args:
          name: The name of the entity.

          archived: A Boolean TRUE / FALSE flag indicating whether the entity is archived. An entity
              can be archived if it is obsolete.

              - TRUE - the entity is in the archived state.
              - FALSE - the entity is not in the archived state.

          code: The short code for the entity.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/organizations/{org_id}/picklists/transactiontypes/{id}",
            body=maybe_transform(
                {
                    "name": name,
                    "archived": archived,
                    "code": code,
                    "version": version,
                },
                transaction_type_update_params.TransactionTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionType,
        )

    def list(
        self,
        *,
        org_id: str | None = None,
        archived: bool | NotGiven = NOT_GIVEN,
        codes: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        next_token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursor[TransactionType]:
        """Retrieves a list of TransactionType entities for the specified Organization.

        The
        list can be paginated for easier management, and supports filtering by various
        parameters.

        Args:
          archived: Filter with this Boolean flag whether to include TransactionTypes that are
              archived.

              - TRUE - include archived TransactionTypes in the list.
              - FALSE - exclude archived TransactionTypes.

          codes: A list of TransactionType short codes to retrieve.

          ids: A list of TransactionType unique identifiers (UUIDs) to retrieve.

          next_token: The `nextToken` for multi-page retrievals. It is used to fetch the next page of
              TransactionTypes in a paginated list.

          page_size: Specifies the maximum number of TransactionTypes to retrieve per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get_api_list(
            f"/organizations/{org_id}/picklists/transactiontypes",
            page=SyncCursor[TransactionType],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "codes": codes,
                        "ids": ids,
                        "next_token": next_token,
                        "page_size": page_size,
                    },
                    transaction_type_list_params.TransactionTypeListParams,
                ),
            ),
            model=TransactionType,
        )

    def delete(
        self,
        id: str,
        *,
        org_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionType:
        """
        Deletes the TransactionType with the given UUID from the specified Organization.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/organizations/{org_id}/picklists/transactiontypes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionType,
        )


class AsyncTransactionTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#with_streaming_response
        """
        return AsyncTransactionTypesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        org_id: str | None = None,
        name: str,
        archived: bool | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        version: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionType:
        """Create a new TransactionType for the specified Organization.

        Details of the new
        TransactionType should be included in the request body.

        Args:
          name: The name of the entity.

          archived: A Boolean TRUE / FALSE flag indicating whether the entity is archived. An entity
              can be archived if it is obsolete.

              - TRUE - the entity is in the archived state.
              - FALSE - the entity is not in the archived state.

          code: The short code for the entity.

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
        return await self._post(
            f"/organizations/{org_id}/picklists/transactiontypes",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "archived": archived,
                    "code": code,
                    "version": version,
                },
                transaction_type_create_params.TransactionTypeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionType,
        )

    async def retrieve(
        self,
        id: str,
        *,
        org_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionType:
        """
        Retrieves the TransactionType with the given UUID from the specified
        Organization.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/organizations/{org_id}/picklists/transactiontypes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionType,
        )

    async def update(
        self,
        id: str,
        *,
        org_id: str | None = None,
        name: str,
        archived: bool | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        version: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionType:
        """
        Updates the TransactionType with the specified UUID for the specified
        Organization. Update details for the TransactionType should be included in the
        request body.

        Args:
          name: The name of the entity.

          archived: A Boolean TRUE / FALSE flag indicating whether the entity is archived. An entity
              can be archived if it is obsolete.

              - TRUE - the entity is in the archived state.
              - FALSE - the entity is not in the archived state.

          code: The short code for the entity.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/organizations/{org_id}/picklists/transactiontypes/{id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "archived": archived,
                    "code": code,
                    "version": version,
                },
                transaction_type_update_params.TransactionTypeUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionType,
        )

    def list(
        self,
        *,
        org_id: str | None = None,
        archived: bool | NotGiven = NOT_GIVEN,
        codes: List[str] | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        next_token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TransactionType, AsyncCursor[TransactionType]]:
        """Retrieves a list of TransactionType entities for the specified Organization.

        The
        list can be paginated for easier management, and supports filtering by various
        parameters.

        Args:
          archived: Filter with this Boolean flag whether to include TransactionTypes that are
              archived.

              - TRUE - include archived TransactionTypes in the list.
              - FALSE - exclude archived TransactionTypes.

          codes: A list of TransactionType short codes to retrieve.

          ids: A list of TransactionType unique identifiers (UUIDs) to retrieve.

          next_token: The `nextToken` for multi-page retrievals. It is used to fetch the next page of
              TransactionTypes in a paginated list.

          page_size: Specifies the maximum number of TransactionTypes to retrieve per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get_api_list(
            f"/organizations/{org_id}/picklists/transactiontypes",
            page=AsyncCursor[TransactionType],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "codes": codes,
                        "ids": ids,
                        "next_token": next_token,
                        "page_size": page_size,
                    },
                    transaction_type_list_params.TransactionTypeListParams,
                ),
            ),
            model=TransactionType,
        )

    async def delete(
        self,
        id: str,
        *,
        org_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionType:
        """
        Deletes the TransactionType with the given UUID from the specified Organization.

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
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/organizations/{org_id}/picklists/transactiontypes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionType,
        )


class TransactionTypesResourceWithRawResponse:
    def __init__(self, transaction_types: TransactionTypesResource) -> None:
        self._transaction_types = transaction_types

        self.create = to_raw_response_wrapper(
            transaction_types.create,
        )
        self.retrieve = to_raw_response_wrapper(
            transaction_types.retrieve,
        )
        self.update = to_raw_response_wrapper(
            transaction_types.update,
        )
        self.list = to_raw_response_wrapper(
            transaction_types.list,
        )
        self.delete = to_raw_response_wrapper(
            transaction_types.delete,
        )


class AsyncTransactionTypesResourceWithRawResponse:
    def __init__(self, transaction_types: AsyncTransactionTypesResource) -> None:
        self._transaction_types = transaction_types

        self.create = async_to_raw_response_wrapper(
            transaction_types.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            transaction_types.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            transaction_types.update,
        )
        self.list = async_to_raw_response_wrapper(
            transaction_types.list,
        )
        self.delete = async_to_raw_response_wrapper(
            transaction_types.delete,
        )


class TransactionTypesResourceWithStreamingResponse:
    def __init__(self, transaction_types: TransactionTypesResource) -> None:
        self._transaction_types = transaction_types

        self.create = to_streamed_response_wrapper(
            transaction_types.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            transaction_types.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            transaction_types.update,
        )
        self.list = to_streamed_response_wrapper(
            transaction_types.list,
        )
        self.delete = to_streamed_response_wrapper(
            transaction_types.delete,
        )


class AsyncTransactionTypesResourceWithStreamingResponse:
    def __init__(self, transaction_types: AsyncTransactionTypesResource) -> None:
        self._transaction_types = transaction_types

        self.create = async_to_streamed_response_wrapper(
            transaction_types.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            transaction_types.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            transaction_types.update,
        )
        self.list = async_to_streamed_response_wrapper(
            transaction_types.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            transaction_types.delete,
        )
