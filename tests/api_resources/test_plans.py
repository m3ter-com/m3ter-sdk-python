# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter_sdk import M3ter, AsyncM3ter
from tests.utils import assert_matches_type
from m3ter_sdk.types import Plan
from m3ter_sdk.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: M3ter) -> None:
        plan = client.plans.create(
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: M3ter) -> None:
        plan = client.plans.create(
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            bespoke=True,
            custom_fields={"foo": "string"},
            minimum_spend=0,
            minimum_spend_bill_in_advance=True,
            minimum_spend_description="minimumSpendDescription",
            ordinal=0,
            standing_charge=0,
            standing_charge_bill_in_advance=True,
            standing_charge_description="standingChargeDescription",
            version=0,
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: M3ter) -> None:
        response = client.plans.with_raw_response.create(
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: M3ter) -> None:
        with client.plans.with_streaming_response.create(
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.plans.with_raw_response.create(
                org_id="",
                code="JS!?Q0]r] ]$]",
                name="x",
                plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        plan = client.plans.retrieve(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.plans.with_raw_response.retrieve(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.plans.with_streaming_response.retrieve(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.plans.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plans.with_raw_response.retrieve(
                id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_update(self, client: M3ter) -> None:
        plan = client.plans.update(
            id="id",
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: M3ter) -> None:
        plan = client.plans.update(
            id="id",
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            bespoke=True,
            custom_fields={"foo": "string"},
            minimum_spend=0,
            minimum_spend_bill_in_advance=True,
            minimum_spend_description="minimumSpendDescription",
            ordinal=0,
            standing_charge=0,
            standing_charge_bill_in_advance=True,
            standing_charge_description="standingChargeDescription",
            version=0,
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: M3ter) -> None:
        response = client.plans.with_raw_response.update(
            id="id",
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: M3ter) -> None:
        with client.plans.with_streaming_response.update(
            id="id",
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.plans.with_raw_response.update(
                id="id",
                org_id="",
                code="JS!?Q0]r] ]$]",
                name="x",
                plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plans.with_raw_response.update(
                id="",
                org_id="orgId",
                code="JS!?Q0]r] ]$]",
                name="x",
                plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    def test_method_list(self, client: M3ter) -> None:
        plan = client.plans.list(
            org_id="orgId",
        )
        assert_matches_type(SyncCursor[Plan], plan, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: M3ter) -> None:
        plan = client.plans.list(
            org_id="orgId",
            account_id=["string"],
            ids=["string"],
            next_token="nextToken",
            page_size=1,
            product_id="productId",
        )
        assert_matches_type(SyncCursor[Plan], plan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: M3ter) -> None:
        response = client.plans.with_raw_response.list(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncCursor[Plan], plan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: M3ter) -> None:
        with client.plans.with_streaming_response.list(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncCursor[Plan], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.plans.with_raw_response.list(
                org_id="",
            )

    @parametrize
    def test_method_delete(self, client: M3ter) -> None:
        plan = client.plans.delete(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: M3ter) -> None:
        response = client.plans.with_raw_response.delete(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: M3ter) -> None:
        with client.plans.with_streaming_response.delete(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.plans.with_raw_response.delete(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plans.with_raw_response.delete(
                id="",
                org_id="orgId",
            )


class TestAsyncPlans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncM3ter) -> None:
        plan = await async_client.plans.create(
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncM3ter) -> None:
        plan = await async_client.plans.create(
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            bespoke=True,
            custom_fields={"foo": "string"},
            minimum_spend=0,
            minimum_spend_bill_in_advance=True,
            minimum_spend_description="minimumSpendDescription",
            ordinal=0,
            standing_charge=0,
            standing_charge_bill_in_advance=True,
            standing_charge_description="standingChargeDescription",
            version=0,
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncM3ter) -> None:
        response = await async_client.plans.with_raw_response.create(
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncM3ter) -> None:
        async with async_client.plans.with_streaming_response.create(
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.plans.with_raw_response.create(
                org_id="",
                code="JS!?Q0]r] ]$]",
                name="x",
                plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        plan = await async_client.plans.retrieve(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.plans.with_raw_response.retrieve(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.plans.with_streaming_response.retrieve(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.plans.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plans.with_raw_response.retrieve(
                id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncM3ter) -> None:
        plan = await async_client.plans.update(
            id="id",
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncM3ter) -> None:
        plan = await async_client.plans.update(
            id="id",
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            bespoke=True,
            custom_fields={"foo": "string"},
            minimum_spend=0,
            minimum_spend_bill_in_advance=True,
            minimum_spend_description="minimumSpendDescription",
            ordinal=0,
            standing_charge=0,
            standing_charge_bill_in_advance=True,
            standing_charge_description="standingChargeDescription",
            version=0,
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncM3ter) -> None:
        response = await async_client.plans.with_raw_response.update(
            id="id",
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncM3ter) -> None:
        async with async_client.plans.with_streaming_response.update(
            id="id",
            org_id="orgId",
            code="JS!?Q0]r] ]$]",
            name="x",
            plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.plans.with_raw_response.update(
                id="id",
                org_id="",
                code="JS!?Q0]r] ]$]",
                name="x",
                plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plans.with_raw_response.update(
                id="",
                org_id="orgId",
                code="JS!?Q0]r] ]$]",
                name="x",
                plan_template_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncM3ter) -> None:
        plan = await async_client.plans.list(
            org_id="orgId",
        )
        assert_matches_type(AsyncCursor[Plan], plan, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncM3ter) -> None:
        plan = await async_client.plans.list(
            org_id="orgId",
            account_id=["string"],
            ids=["string"],
            next_token="nextToken",
            page_size=1,
            product_id="productId",
        )
        assert_matches_type(AsyncCursor[Plan], plan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncM3ter) -> None:
        response = await async_client.plans.with_raw_response.list(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AsyncCursor[Plan], plan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncM3ter) -> None:
        async with async_client.plans.with_streaming_response.list(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncCursor[Plan], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.plans.with_raw_response.list(
                org_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncM3ter) -> None:
        plan = await async_client.plans.delete(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncM3ter) -> None:
        response = await async_client.plans.with_raw_response.delete(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(Plan, plan, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncM3ter) -> None:
        async with async_client.plans.with_streaming_response.delete(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(Plan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.plans.with_raw_response.delete(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plans.with_raw_response.delete(
                id="",
                org_id="orgId",
            )
