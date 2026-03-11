# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter import M3ter, AsyncM3ter
from m3ter.types import CustomFieldsResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        custom_field = client.custom_fields.retrieve()
        assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.custom_fields.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = response.parse()
        assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.custom_fields.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = response.parse()
            assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: M3ter) -> None:
        custom_field = client.custom_fields.update()
        assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: M3ter) -> None:
        custom_field = client.custom_fields.update(
            account={},
            account_plan={"New CF Test": "Test Value"},
            aggregation={},
            compound_aggregation={},
            contract={"foo": "string"},
            meter={},
            organization={
                "Org Example 2": "Sample text 2.",
                "Org Example 1": "Sample text 1.",
            },
            plan={},
            plan_template={},
            product={"Product CF Example": 42},
            version=6,
        )
        assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: M3ter) -> None:
        response = client.custom_fields.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = response.parse()
        assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: M3ter) -> None:
        with client.custom_fields.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = response.parse()
            assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomFields:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        custom_field = await async_client.custom_fields.retrieve()
        assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.custom_fields.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = await response.parse()
        assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.custom_fields.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = await response.parse()
            assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncM3ter) -> None:
        custom_field = await async_client.custom_fields.update()
        assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncM3ter) -> None:
        custom_field = await async_client.custom_fields.update(
            account={},
            account_plan={"New CF Test": "Test Value"},
            aggregation={},
            compound_aggregation={},
            contract={"foo": "string"},
            meter={},
            organization={
                "Org Example 2": "Sample text 2.",
                "Org Example 1": "Sample text 1.",
            },
            plan={},
            plan_template={},
            product={"Product CF Example": 42},
            version=6,
        )
        assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncM3ter) -> None:
        response = await async_client.custom_fields.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = await response.parse()
        assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncM3ter) -> None:
        async with async_client.custom_fields.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = await response.parse()
            assert_matches_type(CustomFieldsResponse, custom_field, path=["response"])

        assert cast(Any, response.is_closed) is True
