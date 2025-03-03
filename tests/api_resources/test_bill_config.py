# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter_sdk import M3ter, AsyncM3ter
from tests.utils import assert_matches_type
from m3ter_sdk.types import BillConfig
from m3ter_sdk._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBillConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        bill_config = client.bill_config.retrieve(
            org_id="orgId",
        )
        assert_matches_type(BillConfig, bill_config, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.bill_config.with_raw_response.retrieve(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_config = response.parse()
        assert_matches_type(BillConfig, bill_config, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.bill_config.with_streaming_response.retrieve(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_config = response.parse()
            assert_matches_type(BillConfig, bill_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.bill_config.with_raw_response.retrieve(
                org_id="",
            )

    @parametrize
    def test_method_update(self, client: M3ter) -> None:
        bill_config = client.bill_config.update(
            org_id="orgId",
        )
        assert_matches_type(BillConfig, bill_config, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: M3ter) -> None:
        bill_config = client.bill_config.update(
            org_id="orgId",
            bill_lock_date=parse_date("2019-12-27"),
            version=0,
        )
        assert_matches_type(BillConfig, bill_config, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: M3ter) -> None:
        response = client.bill_config.with_raw_response.update(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_config = response.parse()
        assert_matches_type(BillConfig, bill_config, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: M3ter) -> None:
        with client.bill_config.with_streaming_response.update(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_config = response.parse()
            assert_matches_type(BillConfig, bill_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.bill_config.with_raw_response.update(
                org_id="",
            )


class TestAsyncBillConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        bill_config = await async_client.bill_config.retrieve(
            org_id="orgId",
        )
        assert_matches_type(BillConfig, bill_config, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.bill_config.with_raw_response.retrieve(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_config = await response.parse()
        assert_matches_type(BillConfig, bill_config, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.bill_config.with_streaming_response.retrieve(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_config = await response.parse()
            assert_matches_type(BillConfig, bill_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.bill_config.with_raw_response.retrieve(
                org_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncM3ter) -> None:
        bill_config = await async_client.bill_config.update(
            org_id="orgId",
        )
        assert_matches_type(BillConfig, bill_config, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncM3ter) -> None:
        bill_config = await async_client.bill_config.update(
            org_id="orgId",
            bill_lock_date=parse_date("2019-12-27"),
            version=0,
        )
        assert_matches_type(BillConfig, bill_config, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncM3ter) -> None:
        response = await async_client.bill_config.with_raw_response.update(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill_config = await response.parse()
        assert_matches_type(BillConfig, bill_config, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncM3ter) -> None:
        async with async_client.bill_config.with_streaming_response.update(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill_config = await response.parse()
            assert_matches_type(BillConfig, bill_config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.bill_config.with_raw_response.update(
                org_id="",
            )
