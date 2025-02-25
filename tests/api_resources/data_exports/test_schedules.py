# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter_sdk import M3ter, AsyncM3ter
from tests.utils import assert_matches_type
from m3ter_sdk.pagination import SyncCursor, AsyncCursor
from m3ter_sdk.types.data_exports import (
    ScheduleListResponse,
    ScheduleCreateResponse,
    ScheduleDeleteResponse,
    ScheduleUpdateResponse,
    ScheduleRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: M3ter) -> None:
        schedule = client.data_exports.schedules.create(
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: M3ter) -> None:
        schedule = client.data_exports.schedules.create(
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
            version=0,
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: M3ter) -> None:
        response = client.data_exports.schedules.with_raw_response.create(
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: M3ter) -> None:
        with client.data_exports.schedules.with_streaming_response.create(
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.data_exports.schedules.with_raw_response.create(
                org_id="",
                operational_data_types=["BILLS"],
                source_type="USAGE",
            )

    @parametrize
    def test_method_create_overload_2(self, client: M3ter) -> None:
        schedule = client.data_exports.schedules.create(
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: M3ter) -> None:
        schedule = client.data_exports.schedules.create(
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
            account_ids=["string"],
            aggregation="SUM",
            meter_ids=["string"],
            version=0,
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: M3ter) -> None:
        response = client.data_exports.schedules.with_raw_response.create(
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: M3ter) -> None:
        with client.data_exports.schedules.with_streaming_response.create(
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.data_exports.schedules.with_raw_response.create(
                org_id="",
                aggregation_frequency="ORIGINAL",
                source_type="USAGE",
                time_period="TODAY",
            )

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        schedule = client.data_exports.schedules.retrieve(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.data_exports.schedules.with_raw_response.retrieve(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.data_exports.schedules.with_streaming_response.retrieve(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.data_exports.schedules.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.data_exports.schedules.with_raw_response.retrieve(
                id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_update_overload_1(self, client: M3ter) -> None:
        schedule = client.data_exports.schedules.update(
            id="id",
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
        )
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: M3ter) -> None:
        schedule = client.data_exports.schedules.update(
            id="id",
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
            version=0,
        )
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: M3ter) -> None:
        response = client.data_exports.schedules.with_raw_response.update(
            id="id",
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: M3ter) -> None:
        with client.data_exports.schedules.with_streaming_response.update(
            id="id",
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.data_exports.schedules.with_raw_response.update(
                id="id",
                org_id="",
                operational_data_types=["BILLS"],
                source_type="USAGE",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.data_exports.schedules.with_raw_response.update(
                id="",
                org_id="orgId",
                operational_data_types=["BILLS"],
                source_type="USAGE",
            )

    @parametrize
    def test_method_update_overload_2(self, client: M3ter) -> None:
        schedule = client.data_exports.schedules.update(
            id="id",
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
        )
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: M3ter) -> None:
        schedule = client.data_exports.schedules.update(
            id="id",
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
            account_ids=["string"],
            aggregation="SUM",
            meter_ids=["string"],
            version=0,
        )
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: M3ter) -> None:
        response = client.data_exports.schedules.with_raw_response.update(
            id="id",
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: M3ter) -> None:
        with client.data_exports.schedules.with_streaming_response.update(
            id="id",
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.data_exports.schedules.with_raw_response.update(
                id="id",
                org_id="",
                aggregation_frequency="ORIGINAL",
                source_type="USAGE",
                time_period="TODAY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.data_exports.schedules.with_raw_response.update(
                id="",
                org_id="orgId",
                aggregation_frequency="ORIGINAL",
                source_type="USAGE",
                time_period="TODAY",
            )

    @parametrize
    def test_method_list(self, client: M3ter) -> None:
        schedule = client.data_exports.schedules.list(
            org_id="orgId",
        )
        assert_matches_type(SyncCursor[ScheduleListResponse], schedule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: M3ter) -> None:
        schedule = client.data_exports.schedules.list(
            org_id="orgId",
            ids=["string"],
            next_token="nextToken",
            page_size=1,
        )
        assert_matches_type(SyncCursor[ScheduleListResponse], schedule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: M3ter) -> None:
        response = client.data_exports.schedules.with_raw_response.list(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(SyncCursor[ScheduleListResponse], schedule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: M3ter) -> None:
        with client.data_exports.schedules.with_streaming_response.list(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(SyncCursor[ScheduleListResponse], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.data_exports.schedules.with_raw_response.list(
                org_id="",
            )

    @parametrize
    def test_method_delete(self, client: M3ter) -> None:
        schedule = client.data_exports.schedules.delete(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: M3ter) -> None:
        response = client.data_exports.schedules.with_raw_response.delete(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: M3ter) -> None:
        with client.data_exports.schedules.with_streaming_response.delete(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.data_exports.schedules.with_raw_response.delete(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.data_exports.schedules.with_raw_response.delete(
                id="",
                org_id="orgId",
            )


class TestAsyncSchedules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncM3ter) -> None:
        schedule = await async_client.data_exports.schedules.create(
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncM3ter) -> None:
        schedule = await async_client.data_exports.schedules.create(
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
            version=0,
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncM3ter) -> None:
        response = await async_client.data_exports.schedules.with_raw_response.create(
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncM3ter) -> None:
        async with async_client.data_exports.schedules.with_streaming_response.create(
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.data_exports.schedules.with_raw_response.create(
                org_id="",
                operational_data_types=["BILLS"],
                source_type="USAGE",
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncM3ter) -> None:
        schedule = await async_client.data_exports.schedules.create(
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncM3ter) -> None:
        schedule = await async_client.data_exports.schedules.create(
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
            account_ids=["string"],
            aggregation="SUM",
            meter_ids=["string"],
            version=0,
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncM3ter) -> None:
        response = await async_client.data_exports.schedules.with_raw_response.create(
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncM3ter) -> None:
        async with async_client.data_exports.schedules.with_streaming_response.create(
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.data_exports.schedules.with_raw_response.create(
                org_id="",
                aggregation_frequency="ORIGINAL",
                source_type="USAGE",
                time_period="TODAY",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        schedule = await async_client.data_exports.schedules.retrieve(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.data_exports.schedules.with_raw_response.retrieve(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.data_exports.schedules.with_streaming_response.retrieve(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.data_exports.schedules.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.data_exports.schedules.with_raw_response.retrieve(
                id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncM3ter) -> None:
        schedule = await async_client.data_exports.schedules.update(
            id="id",
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
        )
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncM3ter) -> None:
        schedule = await async_client.data_exports.schedules.update(
            id="id",
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
            version=0,
        )
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncM3ter) -> None:
        response = await async_client.data_exports.schedules.with_raw_response.update(
            id="id",
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncM3ter) -> None:
        async with async_client.data_exports.schedules.with_streaming_response.update(
            id="id",
            org_id="orgId",
            operational_data_types=["BILLS"],
            source_type="USAGE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.data_exports.schedules.with_raw_response.update(
                id="id",
                org_id="",
                operational_data_types=["BILLS"],
                source_type="USAGE",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.data_exports.schedules.with_raw_response.update(
                id="",
                org_id="orgId",
                operational_data_types=["BILLS"],
                source_type="USAGE",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncM3ter) -> None:
        schedule = await async_client.data_exports.schedules.update(
            id="id",
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
        )
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncM3ter) -> None:
        schedule = await async_client.data_exports.schedules.update(
            id="id",
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
            account_ids=["string"],
            aggregation="SUM",
            meter_ids=["string"],
            version=0,
        )
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncM3ter) -> None:
        response = await async_client.data_exports.schedules.with_raw_response.update(
            id="id",
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncM3ter) -> None:
        async with async_client.data_exports.schedules.with_streaming_response.update(
            id="id",
            org_id="orgId",
            aggregation_frequency="ORIGINAL",
            source_type="USAGE",
            time_period="TODAY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleUpdateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.data_exports.schedules.with_raw_response.update(
                id="id",
                org_id="",
                aggregation_frequency="ORIGINAL",
                source_type="USAGE",
                time_period="TODAY",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.data_exports.schedules.with_raw_response.update(
                id="",
                org_id="orgId",
                aggregation_frequency="ORIGINAL",
                source_type="USAGE",
                time_period="TODAY",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncM3ter) -> None:
        schedule = await async_client.data_exports.schedules.list(
            org_id="orgId",
        )
        assert_matches_type(AsyncCursor[ScheduleListResponse], schedule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncM3ter) -> None:
        schedule = await async_client.data_exports.schedules.list(
            org_id="orgId",
            ids=["string"],
            next_token="nextToken",
            page_size=1,
        )
        assert_matches_type(AsyncCursor[ScheduleListResponse], schedule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncM3ter) -> None:
        response = await async_client.data_exports.schedules.with_raw_response.list(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(AsyncCursor[ScheduleListResponse], schedule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncM3ter) -> None:
        async with async_client.data_exports.schedules.with_streaming_response.list(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(AsyncCursor[ScheduleListResponse], schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.data_exports.schedules.with_raw_response.list(
                org_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncM3ter) -> None:
        schedule = await async_client.data_exports.schedules.delete(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncM3ter) -> None:
        response = await async_client.data_exports.schedules.with_raw_response.delete(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncM3ter) -> None:
        async with async_client.data_exports.schedules.with_streaming_response.delete(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.data_exports.schedules.with_raw_response.delete(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.data_exports.schedules.with_raw_response.delete(
                id="",
                org_id="orgId",
            )
