# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter_sdk import M3ter, AsyncM3ter
from tests.utils import assert_matches_type
from m3ter_sdk.types import (
    Bill,
    BillSearchResponse,
    BillApproveResponse,
)
from m3ter_sdk.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBills:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        bill = client.bills.retrieve(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.bills.with_raw_response.retrieve(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.bills.with_streaming_response.retrieve(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(Bill, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.bills.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.bills.with_raw_response.retrieve(
                id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_list(self, client: M3ter) -> None:
        bill = client.bills.list(
            org_id="orgId",
        )
        assert_matches_type(SyncCursor[Bill], bill, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: M3ter) -> None:
        bill = client.bills.list(
            org_id="orgId",
            account_id="accountId",
            bill_date="billDate",
            bill_date_end="billDateEnd",
            bill_date_start="billDateStart",
            billing_frequency="billingFrequency",
            exclude_line_items=True,
            external_invoice_date_end="externalInvoiceDateEnd",
            external_invoice_date_start="externalInvoiceDateStart",
            ids=["string"],
            include_bill_total=True,
            locked=True,
            next_token="nextToken",
            page_size=1,
            status="PENDING",
        )
        assert_matches_type(SyncCursor[Bill], bill, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: M3ter) -> None:
        response = client.bills.with_raw_response.list(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(SyncCursor[Bill], bill, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: M3ter) -> None:
        with client.bills.with_streaming_response.list(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(SyncCursor[Bill], bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.bills.with_raw_response.list(
                org_id="",
            )

    @parametrize
    def test_method_delete(self, client: M3ter) -> None:
        bill = client.bills.delete(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: M3ter) -> None:
        response = client.bills.with_raw_response.delete(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: M3ter) -> None:
        with client.bills.with_streaming_response.delete(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(Bill, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.bills.with_raw_response.delete(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.bills.with_raw_response.delete(
                id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_approve(self, client: M3ter) -> None:
        bill = client.bills.approve(
            org_id="orgId",
            bill_ids=["string"],
        )
        assert_matches_type(BillApproveResponse, bill, path=["response"])

    @parametrize
    def test_method_approve_with_all_params(self, client: M3ter) -> None:
        bill = client.bills.approve(
            org_id="orgId",
            bill_ids=["string"],
            account_ids="accountIds",
            external_invoice_date_end="externalInvoiceDateEnd",
            external_invoice_date_start="externalInvoiceDateStart",
        )
        assert_matches_type(BillApproveResponse, bill, path=["response"])

    @parametrize
    def test_raw_response_approve(self, client: M3ter) -> None:
        response = client.bills.with_raw_response.approve(
            org_id="orgId",
            bill_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(BillApproveResponse, bill, path=["response"])

    @parametrize
    def test_streaming_response_approve(self, client: M3ter) -> None:
        with client.bills.with_streaming_response.approve(
            org_id="orgId",
            bill_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(BillApproveResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_approve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.bills.with_raw_response.approve(
                org_id="",
                bill_ids=["string"],
            )

    @parametrize
    def test_method_latest_by_account(self, client: M3ter) -> None:
        bill = client.bills.latest_by_account(
            account_id="accountId",
            org_id="orgId",
        )
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    def test_raw_response_latest_by_account(self, client: M3ter) -> None:
        response = client.bills.with_raw_response.latest_by_account(
            account_id="accountId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    def test_streaming_response_latest_by_account(self, client: M3ter) -> None:
        with client.bills.with_streaming_response.latest_by_account(
            account_id="accountId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(Bill, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_latest_by_account(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.bills.with_raw_response.latest_by_account(
                account_id="accountId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.bills.with_raw_response.latest_by_account(
                account_id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_lock(self, client: M3ter) -> None:
        bill = client.bills.lock(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    def test_raw_response_lock(self, client: M3ter) -> None:
        response = client.bills.with_raw_response.lock(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    def test_streaming_response_lock(self, client: M3ter) -> None:
        with client.bills.with_streaming_response.lock(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(Bill, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_lock(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.bills.with_raw_response.lock(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.bills.with_raw_response.lock(
                id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_search(self, client: M3ter) -> None:
        bill = client.bills.search(
            org_id="orgId",
        )
        assert_matches_type(BillSearchResponse, bill, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: M3ter) -> None:
        bill = client.bills.search(
            org_id="orgId",
            from_document=0,
            operator="AND",
            page_size=1,
            search_query="searchQuery",
            sort_by="sortBy",
            sort_order="ASC",
        )
        assert_matches_type(BillSearchResponse, bill, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: M3ter) -> None:
        response = client.bills.with_raw_response.search(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(BillSearchResponse, bill, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: M3ter) -> None:
        with client.bills.with_streaming_response.search(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(BillSearchResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.bills.with_raw_response.search(
                org_id="",
            )

    @parametrize
    def test_method_update_status(self, client: M3ter) -> None:
        bill = client.bills.update_status(
            id="id",
            org_id="orgId",
            status="PENDING",
        )
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    def test_raw_response_update_status(self, client: M3ter) -> None:
        response = client.bills.with_raw_response.update_status(
            id="id",
            org_id="orgId",
            status="PENDING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = response.parse()
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    def test_streaming_response_update_status(self, client: M3ter) -> None:
        with client.bills.with_streaming_response.update_status(
            id="id",
            org_id="orgId",
            status="PENDING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = response.parse()
            assert_matches_type(Bill, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_status(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.bills.with_raw_response.update_status(
                id="id",
                org_id="",
                status="PENDING",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.bills.with_raw_response.update_status(
                id="",
                org_id="orgId",
                status="PENDING",
            )


class TestAsyncBills:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        bill = await async_client.bills.retrieve(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.bills.with_raw_response.retrieve(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.bills.with_streaming_response.retrieve(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(Bill, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.bills.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.bills.with_raw_response.retrieve(
                id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncM3ter) -> None:
        bill = await async_client.bills.list(
            org_id="orgId",
        )
        assert_matches_type(AsyncCursor[Bill], bill, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncM3ter) -> None:
        bill = await async_client.bills.list(
            org_id="orgId",
            account_id="accountId",
            bill_date="billDate",
            bill_date_end="billDateEnd",
            bill_date_start="billDateStart",
            billing_frequency="billingFrequency",
            exclude_line_items=True,
            external_invoice_date_end="externalInvoiceDateEnd",
            external_invoice_date_start="externalInvoiceDateStart",
            ids=["string"],
            include_bill_total=True,
            locked=True,
            next_token="nextToken",
            page_size=1,
            status="PENDING",
        )
        assert_matches_type(AsyncCursor[Bill], bill, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncM3ter) -> None:
        response = await async_client.bills.with_raw_response.list(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(AsyncCursor[Bill], bill, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncM3ter) -> None:
        async with async_client.bills.with_streaming_response.list(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(AsyncCursor[Bill], bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.bills.with_raw_response.list(
                org_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncM3ter) -> None:
        bill = await async_client.bills.delete(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncM3ter) -> None:
        response = await async_client.bills.with_raw_response.delete(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncM3ter) -> None:
        async with async_client.bills.with_streaming_response.delete(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(Bill, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.bills.with_raw_response.delete(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.bills.with_raw_response.delete(
                id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_approve(self, async_client: AsyncM3ter) -> None:
        bill = await async_client.bills.approve(
            org_id="orgId",
            bill_ids=["string"],
        )
        assert_matches_type(BillApproveResponse, bill, path=["response"])

    @parametrize
    async def test_method_approve_with_all_params(self, async_client: AsyncM3ter) -> None:
        bill = await async_client.bills.approve(
            org_id="orgId",
            bill_ids=["string"],
            account_ids="accountIds",
            external_invoice_date_end="externalInvoiceDateEnd",
            external_invoice_date_start="externalInvoiceDateStart",
        )
        assert_matches_type(BillApproveResponse, bill, path=["response"])

    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.bills.with_raw_response.approve(
            org_id="orgId",
            bill_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(BillApproveResponse, bill, path=["response"])

    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncM3ter) -> None:
        async with async_client.bills.with_streaming_response.approve(
            org_id="orgId",
            bill_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(BillApproveResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_approve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.bills.with_raw_response.approve(
                org_id="",
                bill_ids=["string"],
            )

    @parametrize
    async def test_method_latest_by_account(self, async_client: AsyncM3ter) -> None:
        bill = await async_client.bills.latest_by_account(
            account_id="accountId",
            org_id="orgId",
        )
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    async def test_raw_response_latest_by_account(self, async_client: AsyncM3ter) -> None:
        response = await async_client.bills.with_raw_response.latest_by_account(
            account_id="accountId",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    async def test_streaming_response_latest_by_account(self, async_client: AsyncM3ter) -> None:
        async with async_client.bills.with_streaming_response.latest_by_account(
            account_id="accountId",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(Bill, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_latest_by_account(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.bills.with_raw_response.latest_by_account(
                account_id="accountId",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.bills.with_raw_response.latest_by_account(
                account_id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_lock(self, async_client: AsyncM3ter) -> None:
        bill = await async_client.bills.lock(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    async def test_raw_response_lock(self, async_client: AsyncM3ter) -> None:
        response = await async_client.bills.with_raw_response.lock(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    async def test_streaming_response_lock(self, async_client: AsyncM3ter) -> None:
        async with async_client.bills.with_streaming_response.lock(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(Bill, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_lock(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.bills.with_raw_response.lock(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.bills.with_raw_response.lock(
                id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_search(self, async_client: AsyncM3ter) -> None:
        bill = await async_client.bills.search(
            org_id="orgId",
        )
        assert_matches_type(BillSearchResponse, bill, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncM3ter) -> None:
        bill = await async_client.bills.search(
            org_id="orgId",
            from_document=0,
            operator="AND",
            page_size=1,
            search_query="searchQuery",
            sort_by="sortBy",
            sort_order="ASC",
        )
        assert_matches_type(BillSearchResponse, bill, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncM3ter) -> None:
        response = await async_client.bills.with_raw_response.search(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(BillSearchResponse, bill, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncM3ter) -> None:
        async with async_client.bills.with_streaming_response.search(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(BillSearchResponse, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.bills.with_raw_response.search(
                org_id="",
            )

    @parametrize
    async def test_method_update_status(self, async_client: AsyncM3ter) -> None:
        bill = await async_client.bills.update_status(
            id="id",
            org_id="orgId",
            status="PENDING",
        )
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncM3ter) -> None:
        response = await async_client.bills.with_raw_response.update_status(
            id="id",
            org_id="orgId",
            status="PENDING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bill = await response.parse()
        assert_matches_type(Bill, bill, path=["response"])

    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncM3ter) -> None:
        async with async_client.bills.with_streaming_response.update_status(
            id="id",
            org_id="orgId",
            status="PENDING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bill = await response.parse()
            assert_matches_type(Bill, bill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.bills.with_raw_response.update_status(
                id="id",
                org_id="",
                status="PENDING",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.bills.with_raw_response.update_status(
                id="",
                org_id="orgId",
                status="PENDING",
            )
