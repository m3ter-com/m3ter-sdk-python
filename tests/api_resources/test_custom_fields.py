# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter_sdk import M3ter, AsyncM3ter
from tests.utils import assert_matches_type
from m3ter_sdk.types import CustomFields

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        custom_field = client.custom_fields.retrieve(
            org_id="orgId",
        )
        assert_matches_type(CustomFields, custom_field, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.custom_fields.with_raw_response.retrieve(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = response.parse()
        assert_matches_type(CustomFields, custom_field, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.custom_fields.with_streaming_response.retrieve(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = response.parse()
            assert_matches_type(CustomFields, custom_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.custom_fields.with_raw_response.retrieve(
                org_id="",
            )

    @parametrize
    def test_method_update(self, client: M3ter) -> None:
        custom_field = client.custom_fields.update(
            org_id="orgId",
        )
        assert_matches_type(CustomFields, custom_field, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: M3ter) -> None:
        custom_field = client.custom_fields.update(
            org_id="orgId",
            account={"foo": "bar"},
            account_plan={"foo": "bar"},
            aggregation={"foo": "bar"},
            compound_aggregation={"foo": "bar"},
            meter={"foo": "bar"},
            organization={"foo": "bar"},
            plan={"foo": "bar"},
            plan_template={"foo": "bar"},
            product={"foo": "bar"},
            version=0,
        )
        assert_matches_type(CustomFields, custom_field, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: M3ter) -> None:
        response = client.custom_fields.with_raw_response.update(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = response.parse()
        assert_matches_type(CustomFields, custom_field, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: M3ter) -> None:
        with client.custom_fields.with_streaming_response.update(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = response.parse()
            assert_matches_type(CustomFields, custom_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.custom_fields.with_raw_response.update(
                org_id="",
            )


class TestAsyncCustomFields:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        custom_field = await async_client.custom_fields.retrieve(
            org_id="orgId",
        )
        assert_matches_type(CustomFields, custom_field, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.custom_fields.with_raw_response.retrieve(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = await response.parse()
        assert_matches_type(CustomFields, custom_field, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.custom_fields.with_streaming_response.retrieve(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = await response.parse()
            assert_matches_type(CustomFields, custom_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.custom_fields.with_raw_response.retrieve(
                org_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncM3ter) -> None:
        custom_field = await async_client.custom_fields.update(
            org_id="orgId",
        )
        assert_matches_type(CustomFields, custom_field, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncM3ter) -> None:
        custom_field = await async_client.custom_fields.update(
            org_id="orgId",
            account={"foo": "bar"},
            account_plan={"foo": "bar"},
            aggregation={"foo": "bar"},
            compound_aggregation={"foo": "bar"},
            meter={"foo": "bar"},
            organization={"foo": "bar"},
            plan={"foo": "bar"},
            plan_template={"foo": "bar"},
            product={"foo": "bar"},
            version=0,
        )
        assert_matches_type(CustomFields, custom_field, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncM3ter) -> None:
        response = await async_client.custom_fields.with_raw_response.update(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_field = await response.parse()
        assert_matches_type(CustomFields, custom_field, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncM3ter) -> None:
        async with async_client.custom_fields.with_streaming_response.update(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_field = await response.parse()
            assert_matches_type(CustomFields, custom_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.custom_fields.with_raw_response.update(
                org_id="",
            )
