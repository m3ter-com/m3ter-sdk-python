# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter import M3ter, AsyncM3ter
from m3ter.types import (
    CreditReasonResponse,
)
from tests.utils import assert_matches_type
from m3ter.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditReasons:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: M3ter) -> None:
        credit_reason = client.credit_reasons.create(
            name="x",
        )
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: M3ter) -> None:
        credit_reason = client.credit_reasons.create(
            name="x",
            archived=True,
            code="code",
            version=0,
        )
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: M3ter) -> None:
        response = client.credit_reasons.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_reason = response.parse()
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: M3ter) -> None:
        with client.credit_reasons.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_reason = response.parse()
            assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        credit_reason = client.credit_reasons.retrieve(
            id="id",
        )
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.credit_reasons.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_reason = response.parse()
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.credit_reasons.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_reason = response.parse()
            assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.credit_reasons.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: M3ter) -> None:
        credit_reason = client.credit_reasons.update(
            id="id",
            name="x",
        )
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: M3ter) -> None:
        credit_reason = client.credit_reasons.update(
            id="id",
            name="x",
            archived=True,
            code="code",
            version=0,
        )
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: M3ter) -> None:
        response = client.credit_reasons.with_raw_response.update(
            id="id",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_reason = response.parse()
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: M3ter) -> None:
        with client.credit_reasons.with_streaming_response.update(
            id="id",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_reason = response.parse()
            assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.credit_reasons.with_raw_response.update(
                id="",
                name="x",
            )

    @parametrize
    def test_method_list(self, client: M3ter) -> None:
        credit_reason = client.credit_reasons.list()
        assert_matches_type(SyncCursor[CreditReasonResponse], credit_reason, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: M3ter) -> None:
        credit_reason = client.credit_reasons.list(
            archived=True,
            codes=["string"],
            ids=["string"],
            next_token="nextToken",
            page_size=1,
        )
        assert_matches_type(SyncCursor[CreditReasonResponse], credit_reason, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: M3ter) -> None:
        response = client.credit_reasons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_reason = response.parse()
        assert_matches_type(SyncCursor[CreditReasonResponse], credit_reason, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: M3ter) -> None:
        with client.credit_reasons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_reason = response.parse()
            assert_matches_type(SyncCursor[CreditReasonResponse], credit_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: M3ter) -> None:
        credit_reason = client.credit_reasons.delete(
            id="id",
        )
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: M3ter) -> None:
        response = client.credit_reasons.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_reason = response.parse()
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: M3ter) -> None:
        with client.credit_reasons.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_reason = response.parse()
            assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.credit_reasons.with_raw_response.delete(
                id="",
            )


class TestAsyncCreditReasons:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncM3ter) -> None:
        credit_reason = await async_client.credit_reasons.create(
            name="x",
        )
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncM3ter) -> None:
        credit_reason = await async_client.credit_reasons.create(
            name="x",
            archived=True,
            code="code",
            version=0,
        )
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncM3ter) -> None:
        response = await async_client.credit_reasons.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_reason = await response.parse()
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncM3ter) -> None:
        async with async_client.credit_reasons.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_reason = await response.parse()
            assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        credit_reason = await async_client.credit_reasons.retrieve(
            id="id",
        )
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.credit_reasons.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_reason = await response.parse()
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.credit_reasons.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_reason = await response.parse()
            assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.credit_reasons.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncM3ter) -> None:
        credit_reason = await async_client.credit_reasons.update(
            id="id",
            name="x",
        )
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncM3ter) -> None:
        credit_reason = await async_client.credit_reasons.update(
            id="id",
            name="x",
            archived=True,
            code="code",
            version=0,
        )
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncM3ter) -> None:
        response = await async_client.credit_reasons.with_raw_response.update(
            id="id",
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_reason = await response.parse()
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncM3ter) -> None:
        async with async_client.credit_reasons.with_streaming_response.update(
            id="id",
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_reason = await response.parse()
            assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.credit_reasons.with_raw_response.update(
                id="",
                name="x",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncM3ter) -> None:
        credit_reason = await async_client.credit_reasons.list()
        assert_matches_type(AsyncCursor[CreditReasonResponse], credit_reason, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncM3ter) -> None:
        credit_reason = await async_client.credit_reasons.list(
            archived=True,
            codes=["string"],
            ids=["string"],
            next_token="nextToken",
            page_size=1,
        )
        assert_matches_type(AsyncCursor[CreditReasonResponse], credit_reason, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncM3ter) -> None:
        response = await async_client.credit_reasons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_reason = await response.parse()
        assert_matches_type(AsyncCursor[CreditReasonResponse], credit_reason, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncM3ter) -> None:
        async with async_client.credit_reasons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_reason = await response.parse()
            assert_matches_type(AsyncCursor[CreditReasonResponse], credit_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncM3ter) -> None:
        credit_reason = await async_client.credit_reasons.delete(
            id="id",
        )
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncM3ter) -> None:
        response = await async_client.credit_reasons.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_reason = await response.parse()
        assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncM3ter) -> None:
        async with async_client.credit_reasons.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_reason = await response.parse()
            assert_matches_type(CreditReasonResponse, credit_reason, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.credit_reasons.with_raw_response.delete(
                id="",
            )
