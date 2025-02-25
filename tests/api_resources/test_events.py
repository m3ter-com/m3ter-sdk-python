# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter_sdk import M3ter, AsyncM3ter
from tests.utils import assert_matches_type
from m3ter_sdk.types import (
    Event,
    EventGetTypesResponse,
    EventGetFieldsResponse,
)
from m3ter_sdk.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        event = client.events.retrieve(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.events.with_raw_response.retrieve(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.events.with_streaming_response.retrieve(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.events.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.events.with_raw_response.retrieve(
                id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_list(self, client: M3ter) -> None:
        event = client.events.list(
            org_id="orgId",
        )
        assert_matches_type(SyncCursor[Event], event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: M3ter) -> None:
        event = client.events.list(
            org_id="orgId",
            account_id="accountId",
            event_name="eventName",
            event_type="eventType",
            ids=["string"],
            include_actioned=True,
            next_token="nextToken",
            notification_code="notificationCode",
            notification_id="notificationId",
            page_size=1,
            resource_id="resourceId",
        )
        assert_matches_type(SyncCursor[Event], event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: M3ter) -> None:
        response = client.events.with_raw_response.list(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncCursor[Event], event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: M3ter) -> None:
        with client.events.with_streaming_response.list(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncCursor[Event], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.events.with_raw_response.list(
                org_id="",
            )

    @parametrize
    def test_method_get_fields(self, client: M3ter) -> None:
        event = client.events.get_fields(
            org_id="orgId",
        )
        assert_matches_type(EventGetFieldsResponse, event, path=["response"])

    @parametrize
    def test_method_get_fields_with_all_params(self, client: M3ter) -> None:
        event = client.events.get_fields(
            org_id="orgId",
            event_name="eventName",
        )
        assert_matches_type(EventGetFieldsResponse, event, path=["response"])

    @parametrize
    def test_raw_response_get_fields(self, client: M3ter) -> None:
        response = client.events.with_raw_response.get_fields(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventGetFieldsResponse, event, path=["response"])

    @parametrize
    def test_streaming_response_get_fields(self, client: M3ter) -> None:
        with client.events.with_streaming_response.get_fields(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventGetFieldsResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_fields(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.events.with_raw_response.get_fields(
                org_id="",
            )

    @parametrize
    def test_method_get_types(self, client: M3ter) -> None:
        event = client.events.get_types(
            org_id="orgId",
        )
        assert_matches_type(EventGetTypesResponse, event, path=["response"])

    @parametrize
    def test_raw_response_get_types(self, client: M3ter) -> None:
        response = client.events.with_raw_response.get_types(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventGetTypesResponse, event, path=["response"])

    @parametrize
    def test_streaming_response_get_types(self, client: M3ter) -> None:
        with client.events.with_streaming_response.get_types(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventGetTypesResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_types(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.events.with_raw_response.get_types(
                org_id="",
            )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        event = await async_client.events.retrieve(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.events.with_raw_response.retrieve(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.events.with_streaming_response.retrieve(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.events.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.events.with_raw_response.retrieve(
                id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncM3ter) -> None:
        event = await async_client.events.list(
            org_id="orgId",
        )
        assert_matches_type(AsyncCursor[Event], event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncM3ter) -> None:
        event = await async_client.events.list(
            org_id="orgId",
            account_id="accountId",
            event_name="eventName",
            event_type="eventType",
            ids=["string"],
            include_actioned=True,
            next_token="nextToken",
            notification_code="notificationCode",
            notification_id="notificationId",
            page_size=1,
            resource_id="resourceId",
        )
        assert_matches_type(AsyncCursor[Event], event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncM3ter) -> None:
        response = await async_client.events.with_raw_response.list(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(AsyncCursor[Event], event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncM3ter) -> None:
        async with async_client.events.with_streaming_response.list(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncCursor[Event], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.events.with_raw_response.list(
                org_id="",
            )

    @parametrize
    async def test_method_get_fields(self, async_client: AsyncM3ter) -> None:
        event = await async_client.events.get_fields(
            org_id="orgId",
        )
        assert_matches_type(EventGetFieldsResponse, event, path=["response"])

    @parametrize
    async def test_method_get_fields_with_all_params(self, async_client: AsyncM3ter) -> None:
        event = await async_client.events.get_fields(
            org_id="orgId",
            event_name="eventName",
        )
        assert_matches_type(EventGetFieldsResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_get_fields(self, async_client: AsyncM3ter) -> None:
        response = await async_client.events.with_raw_response.get_fields(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventGetFieldsResponse, event, path=["response"])

    @parametrize
    async def test_streaming_response_get_fields(self, async_client: AsyncM3ter) -> None:
        async with async_client.events.with_streaming_response.get_fields(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventGetFieldsResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_fields(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.events.with_raw_response.get_fields(
                org_id="",
            )

    @parametrize
    async def test_method_get_types(self, async_client: AsyncM3ter) -> None:
        event = await async_client.events.get_types(
            org_id="orgId",
        )
        assert_matches_type(EventGetTypesResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_get_types(self, async_client: AsyncM3ter) -> None:
        response = await async_client.events.with_raw_response.get_types(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventGetTypesResponse, event, path=["response"])

    @parametrize
    async def test_streaming_response_get_types(self, async_client: AsyncM3ter) -> None:
        async with async_client.events.with_streaming_response.get_types(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventGetTypesResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_types(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.events.with_raw_response.get_types(
                org_id="",
            )
