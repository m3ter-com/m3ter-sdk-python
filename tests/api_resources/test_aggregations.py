# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter_sdk import M3ter, AsyncM3ter
from tests.utils import assert_matches_type
from m3ter_sdk.types import Aggregation
from m3ter_sdk.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAggregations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: M3ter) -> None:
        aggregation = client.aggregations.create(
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
        )
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: M3ter) -> None:
        aggregation = client.aggregations.create(
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
            code="x",
            custom_fields={"foo": "bar"},
            default_value=0,
            segmented_fields=["string"],
            segments=[{"foo": "string"}],
            version=0,
        )
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: M3ter) -> None:
        response = client.aggregations.with_raw_response.create(
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregation = response.parse()
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: M3ter) -> None:
        with client.aggregations.with_streaming_response.create(
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregation = response.parse()
            assert_matches_type(Aggregation, aggregation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.aggregations.with_raw_response.create(
                org_id="",
                aggregation="SUM",
                meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                name="x",
                quantity_per_unit=1,
                rounding="UP",
                target_field="x",
                unit="x",
            )

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        aggregation = client.aggregations.retrieve(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.aggregations.with_raw_response.retrieve(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregation = response.parse()
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.aggregations.with_streaming_response.retrieve(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregation = response.parse()
            assert_matches_type(Aggregation, aggregation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.aggregations.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aggregations.with_raw_response.retrieve(
                id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_update(self, client: M3ter) -> None:
        aggregation = client.aggregations.update(
            id="id",
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
        )
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: M3ter) -> None:
        aggregation = client.aggregations.update(
            id="id",
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
            code="x",
            custom_fields={"foo": "bar"},
            default_value=0,
            segmented_fields=["string"],
            segments=[{"foo": "string"}],
            version=0,
        )
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: M3ter) -> None:
        response = client.aggregations.with_raw_response.update(
            id="id",
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregation = response.parse()
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: M3ter) -> None:
        with client.aggregations.with_streaming_response.update(
            id="id",
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregation = response.parse()
            assert_matches_type(Aggregation, aggregation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.aggregations.with_raw_response.update(
                id="id",
                org_id="",
                aggregation="SUM",
                meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                name="x",
                quantity_per_unit=1,
                rounding="UP",
                target_field="x",
                unit="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.aggregations.with_raw_response.update(
                id="",
                org_id="orgId",
                aggregation="SUM",
                meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                name="x",
                quantity_per_unit=1,
                rounding="UP",
                target_field="x",
                unit="x",
            )

    @parametrize
    def test_method_list(self, client: M3ter) -> None:
        aggregation = client.aggregations.list(
            org_id="orgId",
        )
        assert_matches_type(SyncCursor[Aggregation], aggregation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: M3ter) -> None:
        aggregation = client.aggregations.list(
            org_id="orgId",
            codes=["string"],
            ids=["string"],
            next_token="nextToken",
            page_size=1,
            product_id=["string"],
        )
        assert_matches_type(SyncCursor[Aggregation], aggregation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: M3ter) -> None:
        response = client.aggregations.with_raw_response.list(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregation = response.parse()
        assert_matches_type(SyncCursor[Aggregation], aggregation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: M3ter) -> None:
        with client.aggregations.with_streaming_response.list(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregation = response.parse()
            assert_matches_type(SyncCursor[Aggregation], aggregation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.aggregations.with_raw_response.list(
                org_id="",
            )


class TestAsyncAggregations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncM3ter) -> None:
        aggregation = await async_client.aggregations.create(
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
        )
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncM3ter) -> None:
        aggregation = await async_client.aggregations.create(
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
            code="x",
            custom_fields={"foo": "bar"},
            default_value=0,
            segmented_fields=["string"],
            segments=[{"foo": "string"}],
            version=0,
        )
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncM3ter) -> None:
        response = await async_client.aggregations.with_raw_response.create(
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregation = await response.parse()
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncM3ter) -> None:
        async with async_client.aggregations.with_streaming_response.create(
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregation = await response.parse()
            assert_matches_type(Aggregation, aggregation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.aggregations.with_raw_response.create(
                org_id="",
                aggregation="SUM",
                meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                name="x",
                quantity_per_unit=1,
                rounding="UP",
                target_field="x",
                unit="x",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        aggregation = await async_client.aggregations.retrieve(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.aggregations.with_raw_response.retrieve(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregation = await response.parse()
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.aggregations.with_streaming_response.retrieve(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregation = await response.parse()
            assert_matches_type(Aggregation, aggregation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.aggregations.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aggregations.with_raw_response.retrieve(
                id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncM3ter) -> None:
        aggregation = await async_client.aggregations.update(
            id="id",
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
        )
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncM3ter) -> None:
        aggregation = await async_client.aggregations.update(
            id="id",
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
            code="x",
            custom_fields={"foo": "bar"},
            default_value=0,
            segmented_fields=["string"],
            segments=[{"foo": "string"}],
            version=0,
        )
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncM3ter) -> None:
        response = await async_client.aggregations.with_raw_response.update(
            id="id",
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregation = await response.parse()
        assert_matches_type(Aggregation, aggregation, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncM3ter) -> None:
        async with async_client.aggregations.with_streaming_response.update(
            id="id",
            org_id="orgId",
            aggregation="SUM",
            meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            name="x",
            quantity_per_unit=1,
            rounding="UP",
            target_field="x",
            unit="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregation = await response.parse()
            assert_matches_type(Aggregation, aggregation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.aggregations.with_raw_response.update(
                id="id",
                org_id="",
                aggregation="SUM",
                meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                name="x",
                quantity_per_unit=1,
                rounding="UP",
                target_field="x",
                unit="x",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.aggregations.with_raw_response.update(
                id="",
                org_id="orgId",
                aggregation="SUM",
                meter_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                name="x",
                quantity_per_unit=1,
                rounding="UP",
                target_field="x",
                unit="x",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncM3ter) -> None:
        aggregation = await async_client.aggregations.list(
            org_id="orgId",
        )
        assert_matches_type(AsyncCursor[Aggregation], aggregation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncM3ter) -> None:
        aggregation = await async_client.aggregations.list(
            org_id="orgId",
            codes=["string"],
            ids=["string"],
            next_token="nextToken",
            page_size=1,
            product_id=["string"],
        )
        assert_matches_type(AsyncCursor[Aggregation], aggregation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncM3ter) -> None:
        response = await async_client.aggregations.with_raw_response.list(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregation = await response.parse()
        assert_matches_type(AsyncCursor[Aggregation], aggregation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncM3ter) -> None:
        async with async_client.aggregations.with_streaming_response.list(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregation = await response.parse()
            assert_matches_type(AsyncCursor[Aggregation], aggregation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.aggregations.with_raw_response.list(
                org_id="",
            )
