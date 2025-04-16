# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter import M3ter, AsyncM3ter
from m3ter.types import (
    PlanTemplateResponse,
)
from tests.utils import assert_matches_type
from m3ter.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlanTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: M3ter) -> None:
        plan_template = client.plan_templates.create(
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
        )
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: M3ter) -> None:
        plan_template = client.plan_templates.create(
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
            bill_frequency_interval=1,
            code="JS!?Q0]r] ]$]",
            custom_fields={"foo": "string"},
            minimum_spend=0,
            minimum_spend_bill_in_advance=True,
            minimum_spend_description="minimumSpendDescription",
            ordinal=0,
            standing_charge_bill_in_advance=True,
            standing_charge_description="standingChargeDescription",
            standing_charge_interval=1,
            standing_charge_offset=0,
            version=0,
        )
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: M3ter) -> None:
        response = client.plan_templates.with_raw_response.create(
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_template = response.parse()
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: M3ter) -> None:
        with client.plan_templates.with_streaming_response.create(
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_template = response.parse()
            assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        plan_template = client.plan_templates.retrieve(
            id="id",
        )
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.plan_templates.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_template = response.parse()
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.plan_templates.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_template = response.parse()
            assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plan_templates.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: M3ter) -> None:
        plan_template = client.plan_templates.update(
            id="id",
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
        )
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: M3ter) -> None:
        plan_template = client.plan_templates.update(
            id="id",
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
            bill_frequency_interval=1,
            code="JS!?Q0]r] ]$]",
            custom_fields={"foo": "string"},
            minimum_spend=0,
            minimum_spend_bill_in_advance=True,
            minimum_spend_description="minimumSpendDescription",
            ordinal=0,
            standing_charge_bill_in_advance=True,
            standing_charge_description="standingChargeDescription",
            standing_charge_interval=1,
            standing_charge_offset=0,
            version=0,
        )
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: M3ter) -> None:
        response = client.plan_templates.with_raw_response.update(
            id="id",
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_template = response.parse()
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: M3ter) -> None:
        with client.plan_templates.with_streaming_response.update(
            id="id",
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_template = response.parse()
            assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plan_templates.with_raw_response.update(
                id="",
                bill_frequency="DAILY",
                currency="xxx",
                name="x",
                product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                standing_charge=0,
            )

    @parametrize
    def test_method_list(self, client: M3ter) -> None:
        plan_template = client.plan_templates.list()
        assert_matches_type(SyncCursor[PlanTemplateResponse], plan_template, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: M3ter) -> None:
        plan_template = client.plan_templates.list(
            ids=["string"],
            next_token="nextToken",
            page_size=1,
            product_id="productId",
        )
        assert_matches_type(SyncCursor[PlanTemplateResponse], plan_template, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: M3ter) -> None:
        response = client.plan_templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_template = response.parse()
        assert_matches_type(SyncCursor[PlanTemplateResponse], plan_template, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: M3ter) -> None:
        with client.plan_templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_template = response.parse()
            assert_matches_type(SyncCursor[PlanTemplateResponse], plan_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: M3ter) -> None:
        plan_template = client.plan_templates.delete(
            id="id",
        )
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: M3ter) -> None:
        response = client.plan_templates.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_template = response.parse()
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: M3ter) -> None:
        with client.plan_templates.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_template = response.parse()
            assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.plan_templates.with_raw_response.delete(
                id="",
            )


class TestAsyncPlanTemplates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncM3ter) -> None:
        plan_template = await async_client.plan_templates.create(
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
        )
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncM3ter) -> None:
        plan_template = await async_client.plan_templates.create(
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
            bill_frequency_interval=1,
            code="JS!?Q0]r] ]$]",
            custom_fields={"foo": "string"},
            minimum_spend=0,
            minimum_spend_bill_in_advance=True,
            minimum_spend_description="minimumSpendDescription",
            ordinal=0,
            standing_charge_bill_in_advance=True,
            standing_charge_description="standingChargeDescription",
            standing_charge_interval=1,
            standing_charge_offset=0,
            version=0,
        )
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncM3ter) -> None:
        response = await async_client.plan_templates.with_raw_response.create(
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_template = await response.parse()
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncM3ter) -> None:
        async with async_client.plan_templates.with_streaming_response.create(
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_template = await response.parse()
            assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        plan_template = await async_client.plan_templates.retrieve(
            id="id",
        )
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.plan_templates.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_template = await response.parse()
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.plan_templates.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_template = await response.parse()
            assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plan_templates.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncM3ter) -> None:
        plan_template = await async_client.plan_templates.update(
            id="id",
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
        )
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncM3ter) -> None:
        plan_template = await async_client.plan_templates.update(
            id="id",
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
            bill_frequency_interval=1,
            code="JS!?Q0]r] ]$]",
            custom_fields={"foo": "string"},
            minimum_spend=0,
            minimum_spend_bill_in_advance=True,
            minimum_spend_description="minimumSpendDescription",
            ordinal=0,
            standing_charge_bill_in_advance=True,
            standing_charge_description="standingChargeDescription",
            standing_charge_interval=1,
            standing_charge_offset=0,
            version=0,
        )
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncM3ter) -> None:
        response = await async_client.plan_templates.with_raw_response.update(
            id="id",
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_template = await response.parse()
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncM3ter) -> None:
        async with async_client.plan_templates.with_streaming_response.update(
            id="id",
            bill_frequency="DAILY",
            currency="xxx",
            name="x",
            product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            standing_charge=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_template = await response.parse()
            assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plan_templates.with_raw_response.update(
                id="",
                bill_frequency="DAILY",
                currency="xxx",
                name="x",
                product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                standing_charge=0,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncM3ter) -> None:
        plan_template = await async_client.plan_templates.list()
        assert_matches_type(AsyncCursor[PlanTemplateResponse], plan_template, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncM3ter) -> None:
        plan_template = await async_client.plan_templates.list(
            ids=["string"],
            next_token="nextToken",
            page_size=1,
            product_id="productId",
        )
        assert_matches_type(AsyncCursor[PlanTemplateResponse], plan_template, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncM3ter) -> None:
        response = await async_client.plan_templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_template = await response.parse()
        assert_matches_type(AsyncCursor[PlanTemplateResponse], plan_template, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncM3ter) -> None:
        async with async_client.plan_templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_template = await response.parse()
            assert_matches_type(AsyncCursor[PlanTemplateResponse], plan_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncM3ter) -> None:
        plan_template = await async_client.plan_templates.delete(
            id="id",
        )
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncM3ter) -> None:
        response = await async_client.plan_templates.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan_template = await response.parse()
        assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncM3ter) -> None:
        async with async_client.plan_templates.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan_template = await response.parse()
            assert_matches_type(PlanTemplateResponse, plan_template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.plan_templates.with_raw_response.delete(
                id="",
            )
