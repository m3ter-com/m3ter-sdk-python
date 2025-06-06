# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter import M3ter, AsyncM3ter
from m3ter.types import Balance
from tests.utils import assert_matches_type
from m3ter._utils import parse_datetime
from m3ter.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: M3ter) -> None:
        balance = client.balances.create(
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: M3ter) -> None:
        balance = client.balances.create(
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            balance_draw_down_description="balanceDrawDownDescription",
            code="JS!?Q0]r] ]$]",
            consumptions_accounting_product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            contract_id="contractId",
            description="description",
            fees_accounting_product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            line_item_types=["STANDING_CHARGE"],
            name="name",
            overage_description="overageDescription",
            overage_surcharge_percent=0,
            product_ids=["string"],
            rollover_amount=0,
            rollover_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            version=0,
        )
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: M3ter) -> None:
        response = client.balances.with_raw_response.create(
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: M3ter) -> None:
        with client.balances.with_streaming_response.create(
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(Balance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        balance = client.balances.retrieve(
            id="id",
        )
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.balances.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.balances.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(Balance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.balances.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: M3ter) -> None:
        balance = client.balances.update(
            id="id",
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: M3ter) -> None:
        balance = client.balances.update(
            id="id",
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            balance_draw_down_description="balanceDrawDownDescription",
            code="JS!?Q0]r] ]$]",
            consumptions_accounting_product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            contract_id="contractId",
            description="description",
            fees_accounting_product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            line_item_types=["STANDING_CHARGE"],
            name="name",
            overage_description="overageDescription",
            overage_surcharge_percent=0,
            product_ids=["string"],
            rollover_amount=0,
            rollover_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            version=0,
        )
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: M3ter) -> None:
        response = client.balances.with_raw_response.update(
            id="id",
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: M3ter) -> None:
        with client.balances.with_streaming_response.update(
            id="id",
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(Balance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.balances.with_raw_response.update(
                id="",
                account_id="x",
                currency="x",
                end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
                start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @parametrize
    def test_method_list(self, client: M3ter) -> None:
        balance = client.balances.list()
        assert_matches_type(SyncCursor[Balance], balance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: M3ter) -> None:
        balance = client.balances.list(
            account_id="accountId",
            end_date_end="endDateEnd",
            end_date_start="endDateStart",
            next_token="nextToken",
            page_size=1,
        )
        assert_matches_type(SyncCursor[Balance], balance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: M3ter) -> None:
        response = client.balances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(SyncCursor[Balance], balance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: M3ter) -> None:
        with client.balances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(SyncCursor[Balance], balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: M3ter) -> None:
        balance = client.balances.delete(
            id="id",
        )
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: M3ter) -> None:
        response = client.balances.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: M3ter) -> None:
        with client.balances.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(Balance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.balances.with_raw_response.delete(
                id="",
            )


class TestAsyncBalances:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncM3ter) -> None:
        balance = await async_client.balances.create(
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncM3ter) -> None:
        balance = await async_client.balances.create(
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            balance_draw_down_description="balanceDrawDownDescription",
            code="JS!?Q0]r] ]$]",
            consumptions_accounting_product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            contract_id="contractId",
            description="description",
            fees_accounting_product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            line_item_types=["STANDING_CHARGE"],
            name="name",
            overage_description="overageDescription",
            overage_surcharge_percent=0,
            product_ids=["string"],
            rollover_amount=0,
            rollover_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            version=0,
        )
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncM3ter) -> None:
        response = await async_client.balances.with_raw_response.create(
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncM3ter) -> None:
        async with async_client.balances.with_streaming_response.create(
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(Balance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        balance = await async_client.balances.retrieve(
            id="id",
        )
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.balances.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.balances.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(Balance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.balances.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncM3ter) -> None:
        balance = await async_client.balances.update(
            id="id",
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncM3ter) -> None:
        balance = await async_client.balances.update(
            id="id",
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            balance_draw_down_description="balanceDrawDownDescription",
            code="JS!?Q0]r] ]$]",
            consumptions_accounting_product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            contract_id="contractId",
            description="description",
            fees_accounting_product_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            line_item_types=["STANDING_CHARGE"],
            name="name",
            overage_description="overageDescription",
            overage_surcharge_percent=0,
            product_ids=["string"],
            rollover_amount=0,
            rollover_end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            version=0,
        )
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncM3ter) -> None:
        response = await async_client.balances.with_raw_response.update(
            id="id",
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncM3ter) -> None:
        async with async_client.balances.with_streaming_response.update(
            id="id",
            account_id="x",
            currency="x",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(Balance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.balances.with_raw_response.update(
                id="",
                account_id="x",
                currency="x",
                end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
                start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncM3ter) -> None:
        balance = await async_client.balances.list()
        assert_matches_type(AsyncCursor[Balance], balance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncM3ter) -> None:
        balance = await async_client.balances.list(
            account_id="accountId",
            end_date_end="endDateEnd",
            end_date_start="endDateStart",
            next_token="nextToken",
            page_size=1,
        )
        assert_matches_type(AsyncCursor[Balance], balance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncM3ter) -> None:
        response = await async_client.balances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(AsyncCursor[Balance], balance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncM3ter) -> None:
        async with async_client.balances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(AsyncCursor[Balance], balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncM3ter) -> None:
        balance = await async_client.balances.delete(
            id="id",
        )
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncM3ter) -> None:
        response = await async_client.balances.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = await response.parse()
        assert_matches_type(Balance, balance, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncM3ter) -> None:
        async with async_client.balances.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(Balance, balance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.balances.with_raw_response.delete(
                id="",
            )
