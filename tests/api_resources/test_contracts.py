# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter_sdk import M3ter, AsyncM3ter
from tests.utils import assert_matches_type
from m3ter_sdk.types import (
    ContractResponse,
    ContractEndDateBillingEntitiesResponse,
)
from m3ter_sdk._utils import parse_date, parse_datetime
from m3ter_sdk.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContracts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: M3ter) -> None:
        contract = client.contracts.create(
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: M3ter) -> None:
        contract = client.contracts.create(
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
            code="JS!?Q0]r] ]$]",
            custom_fields={"foo": "string"},
            description="description",
            purchase_order_number="purchaseOrderNumber",
            version=0,
        )
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: M3ter) -> None:
        response = client.contracts.with_raw_response.create(
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: M3ter) -> None:
        with client.contracts.with_streaming_response.create(
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.contracts.with_raw_response.create(
                org_id="",
                account_id="x",
                end_date=parse_date("2019-12-27"),
                name="x",
                start_date=parse_date("2019-12-27"),
            )

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        contract = client.contracts.retrieve(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.contracts.with_raw_response.retrieve(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.contracts.with_streaming_response.retrieve(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.contracts.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contracts.with_raw_response.retrieve(
                id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_update(self, client: M3ter) -> None:
        contract = client.contracts.update(
            id="id",
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: M3ter) -> None:
        contract = client.contracts.update(
            id="id",
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
            code="JS!?Q0]r] ]$]",
            custom_fields={"foo": "string"},
            description="description",
            purchase_order_number="purchaseOrderNumber",
            version=0,
        )
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: M3ter) -> None:
        response = client.contracts.with_raw_response.update(
            id="id",
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: M3ter) -> None:
        with client.contracts.with_streaming_response.update(
            id="id",
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.contracts.with_raw_response.update(
                id="id",
                org_id="",
                account_id="x",
                end_date=parse_date("2019-12-27"),
                name="x",
                start_date=parse_date("2019-12-27"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contracts.with_raw_response.update(
                id="",
                org_id="orgId",
                account_id="x",
                end_date=parse_date("2019-12-27"),
                name="x",
                start_date=parse_date("2019-12-27"),
            )

    @parametrize
    def test_method_list(self, client: M3ter) -> None:
        contract = client.contracts.list(
            org_id="orgId",
        )
        assert_matches_type(SyncCursor[ContractResponse], contract, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: M3ter) -> None:
        contract = client.contracts.list(
            org_id="orgId",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            codes=["string"],
            ids=["string"],
            next_token="nextToken",
            page_size=1,
        )
        assert_matches_type(SyncCursor[ContractResponse], contract, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: M3ter) -> None:
        response = client.contracts.with_raw_response.list(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(SyncCursor[ContractResponse], contract, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: M3ter) -> None:
        with client.contracts.with_streaming_response.list(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(SyncCursor[ContractResponse], contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.contracts.with_raw_response.list(
                org_id="",
            )

    @parametrize
    def test_method_delete(self, client: M3ter) -> None:
        contract = client.contracts.delete(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: M3ter) -> None:
        response = client.contracts.with_raw_response.delete(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: M3ter) -> None:
        with client.contracts.with_streaming_response.delete(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.contracts.with_raw_response.delete(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contracts.with_raw_response.delete(
                id="",
                org_id="orgId",
            )

    @parametrize
    def test_method_end_date_billing_entities(self, client: M3ter) -> None:
        contract = client.contracts.end_date_billing_entities(
            id="id",
            org_id="orgId",
            billing_entities=["CONTRACT"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContractEndDateBillingEntitiesResponse, contract, path=["response"])

    @parametrize
    def test_method_end_date_billing_entities_with_all_params(self, client: M3ter) -> None:
        contract = client.contracts.end_date_billing_entities(
            id="id",
            org_id="orgId",
            billing_entities=["CONTRACT"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            apply_to_children=True,
        )
        assert_matches_type(ContractEndDateBillingEntitiesResponse, contract, path=["response"])

    @parametrize
    def test_raw_response_end_date_billing_entities(self, client: M3ter) -> None:
        response = client.contracts.with_raw_response.end_date_billing_entities(
            id="id",
            org_id="orgId",
            billing_entities=["CONTRACT"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert_matches_type(ContractEndDateBillingEntitiesResponse, contract, path=["response"])

    @parametrize
    def test_streaming_response_end_date_billing_entities(self, client: M3ter) -> None:
        with client.contracts.with_streaming_response.end_date_billing_entities(
            id="id",
            org_id="orgId",
            billing_entities=["CONTRACT"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert_matches_type(ContractEndDateBillingEntitiesResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_end_date_billing_entities(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.contracts.with_raw_response.end_date_billing_entities(
                id="id",
                org_id="",
                billing_entities=["CONTRACT"],
                end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contracts.with_raw_response.end_date_billing_entities(
                id="",
                org_id="orgId",
                billing_entities=["CONTRACT"],
                end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            )


class TestAsyncContracts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncM3ter) -> None:
        contract = await async_client.contracts.create(
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncM3ter) -> None:
        contract = await async_client.contracts.create(
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
            code="JS!?Q0]r] ]$]",
            custom_fields={"foo": "string"},
            description="description",
            purchase_order_number="purchaseOrderNumber",
            version=0,
        )
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncM3ter) -> None:
        response = await async_client.contracts.with_raw_response.create(
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncM3ter) -> None:
        async with async_client.contracts.with_streaming_response.create(
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.contracts.with_raw_response.create(
                org_id="",
                account_id="x",
                end_date=parse_date("2019-12-27"),
                name="x",
                start_date=parse_date("2019-12-27"),
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        contract = await async_client.contracts.retrieve(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.contracts.with_raw_response.retrieve(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.contracts.with_streaming_response.retrieve(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.contracts.with_raw_response.retrieve(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contracts.with_raw_response.retrieve(
                id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncM3ter) -> None:
        contract = await async_client.contracts.update(
            id="id",
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncM3ter) -> None:
        contract = await async_client.contracts.update(
            id="id",
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
            code="JS!?Q0]r] ]$]",
            custom_fields={"foo": "string"},
            description="description",
            purchase_order_number="purchaseOrderNumber",
            version=0,
        )
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncM3ter) -> None:
        response = await async_client.contracts.with_raw_response.update(
            id="id",
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncM3ter) -> None:
        async with async_client.contracts.with_streaming_response.update(
            id="id",
            org_id="orgId",
            account_id="x",
            end_date=parse_date("2019-12-27"),
            name="x",
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.contracts.with_raw_response.update(
                id="id",
                org_id="",
                account_id="x",
                end_date=parse_date("2019-12-27"),
                name="x",
                start_date=parse_date("2019-12-27"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contracts.with_raw_response.update(
                id="",
                org_id="orgId",
                account_id="x",
                end_date=parse_date("2019-12-27"),
                name="x",
                start_date=parse_date("2019-12-27"),
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncM3ter) -> None:
        contract = await async_client.contracts.list(
            org_id="orgId",
        )
        assert_matches_type(AsyncCursor[ContractResponse], contract, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncM3ter) -> None:
        contract = await async_client.contracts.list(
            org_id="orgId",
            account_id="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            codes=["string"],
            ids=["string"],
            next_token="nextToken",
            page_size=1,
        )
        assert_matches_type(AsyncCursor[ContractResponse], contract, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncM3ter) -> None:
        response = await async_client.contracts.with_raw_response.list(
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(AsyncCursor[ContractResponse], contract, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncM3ter) -> None:
        async with async_client.contracts.with_streaming_response.list(
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(AsyncCursor[ContractResponse], contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.contracts.with_raw_response.list(
                org_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncM3ter) -> None:
        contract = await async_client.contracts.delete(
            id="id",
            org_id="orgId",
        )
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncM3ter) -> None:
        response = await async_client.contracts.with_raw_response.delete(
            id="id",
            org_id="orgId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncM3ter) -> None:
        async with async_client.contracts.with_streaming_response.delete(
            id="id",
            org_id="orgId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.contracts.with_raw_response.delete(
                id="id",
                org_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contracts.with_raw_response.delete(
                id="",
                org_id="orgId",
            )

    @parametrize
    async def test_method_end_date_billing_entities(self, async_client: AsyncM3ter) -> None:
        contract = await async_client.contracts.end_date_billing_entities(
            id="id",
            org_id="orgId",
            billing_entities=["CONTRACT"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ContractEndDateBillingEntitiesResponse, contract, path=["response"])

    @parametrize
    async def test_method_end_date_billing_entities_with_all_params(self, async_client: AsyncM3ter) -> None:
        contract = await async_client.contracts.end_date_billing_entities(
            id="id",
            org_id="orgId",
            billing_entities=["CONTRACT"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            apply_to_children=True,
        )
        assert_matches_type(ContractEndDateBillingEntitiesResponse, contract, path=["response"])

    @parametrize
    async def test_raw_response_end_date_billing_entities(self, async_client: AsyncM3ter) -> None:
        response = await async_client.contracts.with_raw_response.end_date_billing_entities(
            id="id",
            org_id="orgId",
            billing_entities=["CONTRACT"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert_matches_type(ContractEndDateBillingEntitiesResponse, contract, path=["response"])

    @parametrize
    async def test_streaming_response_end_date_billing_entities(self, async_client: AsyncM3ter) -> None:
        async with async_client.contracts.with_streaming_response.end_date_billing_entities(
            id="id",
            org_id="orgId",
            billing_entities=["CONTRACT"],
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert_matches_type(ContractEndDateBillingEntitiesResponse, contract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_end_date_billing_entities(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.contracts.with_raw_response.end_date_billing_entities(
                id="id",
                org_id="",
                billing_entities=["CONTRACT"],
                end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contracts.with_raw_response.end_date_billing_entities(
                id="",
                org_id="orgId",
                billing_entities=["CONTRACT"],
                end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            )
