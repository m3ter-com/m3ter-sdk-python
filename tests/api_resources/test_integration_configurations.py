# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from m3ter import M3ter, AsyncM3ter
from m3ter.types import (
    IntegrationConfigurationResponse,
    IntegrationConfigurationListResponse,
    IntegrationConfigurationCreateResponse,
    IntegrationConfigurationDeleteResponse,
    IntegrationConfigurationEnableResponse,
    IntegrationConfigurationUpdateResponse,
)
from tests.utils import assert_matches_type
from m3ter.pagination import SyncCursor, AsyncCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrationConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: M3ter) -> None:
        integration_configuration = client.integration_configurations.create(
            config_data={"foo": "bar"},
            credentials={"type": "HTTP_BASIC"},
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
        )
        assert_matches_type(IntegrationConfigurationCreateResponse, integration_configuration, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: M3ter) -> None:
        integration_configuration = client.integration_configurations.create(
            config_data={"foo": "bar"},
            credentials={
                "type": "HTTP_BASIC",
                "destination": "WEBHOOK",
                "empty": True,
                "name": "name",
                "version": 0,
            },
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
            version=0,
        )
        assert_matches_type(IntegrationConfigurationCreateResponse, integration_configuration, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: M3ter) -> None:
        response = client.integration_configurations.with_raw_response.create(
            config_data={"foo": "bar"},
            credentials={"type": "HTTP_BASIC"},
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = response.parse()
        assert_matches_type(IntegrationConfigurationCreateResponse, integration_configuration, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: M3ter) -> None:
        with client.integration_configurations.with_streaming_response.create(
            config_data={"foo": "bar"},
            credentials={"type": "HTTP_BASIC"},
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = response.parse()
            assert_matches_type(IntegrationConfigurationCreateResponse, integration_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: M3ter) -> None:
        integration_configuration = client.integration_configurations.retrieve(
            id="id",
        )
        assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: M3ter) -> None:
        response = client.integration_configurations.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = response.parse()
        assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: M3ter) -> None:
        with client.integration_configurations.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = response.parse()
            assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.integration_configurations.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_update(self, client: M3ter) -> None:
        integration_configuration = client.integration_configurations.update(
            id="id",
            config_data={"foo": "bar"},
            credentials={"type": "HTTP_BASIC"},
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
        )
        assert_matches_type(IntegrationConfigurationUpdateResponse, integration_configuration, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: M3ter) -> None:
        integration_configuration = client.integration_configurations.update(
            id="id",
            config_data={"foo": "bar"},
            credentials={
                "type": "HTTP_BASIC",
                "destination": "WEBHOOK",
                "empty": True,
                "name": "name",
                "version": 0,
            },
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
            version=0,
        )
        assert_matches_type(IntegrationConfigurationUpdateResponse, integration_configuration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: M3ter) -> None:
        response = client.integration_configurations.with_raw_response.update(
            id="id",
            config_data={"foo": "bar"},
            credentials={"type": "HTTP_BASIC"},
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = response.parse()
        assert_matches_type(IntegrationConfigurationUpdateResponse, integration_configuration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: M3ter) -> None:
        with client.integration_configurations.with_streaming_response.update(
            id="id",
            config_data={"foo": "bar"},
            credentials={"type": "HTTP_BASIC"},
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = response.parse()
            assert_matches_type(IntegrationConfigurationUpdateResponse, integration_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.integration_configurations.with_raw_response.update(
                id="",
                config_data={"foo": "bar"},
                credentials={"type": "HTTP_BASIC"},
                destination="destination",
                destination_id="destinationId",
                entity_id="entityId",
                entity_type="entityType",
                integration_credentials_id="integrationCredentialsId",
                name="name",
            )

    @parametrize
    def test_method_list(self, client: M3ter) -> None:
        integration_configuration = client.integration_configurations.list()
        assert_matches_type(
            SyncCursor[IntegrationConfigurationListResponse], integration_configuration, path=["response"]
        )

    @parametrize
    def test_method_list_with_all_params(self, client: M3ter) -> None:
        integration_configuration = client.integration_configurations.list(
            next_token="nextToken",
            page_size=1,
        )
        assert_matches_type(
            SyncCursor[IntegrationConfigurationListResponse], integration_configuration, path=["response"]
        )

    @parametrize
    def test_raw_response_list(self, client: M3ter) -> None:
        response = client.integration_configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = response.parse()
        assert_matches_type(
            SyncCursor[IntegrationConfigurationListResponse], integration_configuration, path=["response"]
        )

    @parametrize
    def test_streaming_response_list(self, client: M3ter) -> None:
        with client.integration_configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = response.parse()
            assert_matches_type(
                SyncCursor[IntegrationConfigurationListResponse], integration_configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: M3ter) -> None:
        integration_configuration = client.integration_configurations.delete(
            id="id",
        )
        assert_matches_type(IntegrationConfigurationDeleteResponse, integration_configuration, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: M3ter) -> None:
        response = client.integration_configurations.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = response.parse()
        assert_matches_type(IntegrationConfigurationDeleteResponse, integration_configuration, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: M3ter) -> None:
        with client.integration_configurations.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = response.parse()
            assert_matches_type(IntegrationConfigurationDeleteResponse, integration_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.integration_configurations.with_raw_response.delete(
                id="",
            )

    @parametrize
    def test_method_enable(self, client: M3ter) -> None:
        integration_configuration = client.integration_configurations.enable(
            id="id",
        )
        assert_matches_type(IntegrationConfigurationEnableResponse, integration_configuration, path=["response"])

    @parametrize
    def test_raw_response_enable(self, client: M3ter) -> None:
        response = client.integration_configurations.with_raw_response.enable(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = response.parse()
        assert_matches_type(IntegrationConfigurationEnableResponse, integration_configuration, path=["response"])

    @parametrize
    def test_streaming_response_enable(self, client: M3ter) -> None:
        with client.integration_configurations.with_streaming_response.enable(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = response.parse()
            assert_matches_type(IntegrationConfigurationEnableResponse, integration_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enable(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.integration_configurations.with_raw_response.enable(
                id="",
            )

    @parametrize
    def test_method_get_by_entity(self, client: M3ter) -> None:
        integration_configuration = client.integration_configurations.get_by_entity(
            entity_type="entityType",
        )
        assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

    @parametrize
    def test_method_get_by_entity_with_all_params(self, client: M3ter) -> None:
        integration_configuration = client.integration_configurations.get_by_entity(
            entity_type="entityType",
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
        )
        assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

    @parametrize
    def test_raw_response_get_by_entity(self, client: M3ter) -> None:
        response = client.integration_configurations.with_raw_response.get_by_entity(
            entity_type="entityType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = response.parse()
        assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

    @parametrize
    def test_streaming_response_get_by_entity(self, client: M3ter) -> None:
        with client.integration_configurations.with_streaming_response.get_by_entity(
            entity_type="entityType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = response.parse()
            assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_by_entity(self, client: M3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_type` but received ''"):
            client.integration_configurations.with_raw_response.get_by_entity(
                entity_type="",
            )


class TestAsyncIntegrationConfigurations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncM3ter) -> None:
        integration_configuration = await async_client.integration_configurations.create(
            config_data={"foo": "bar"},
            credentials={"type": "HTTP_BASIC"},
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
        )
        assert_matches_type(IntegrationConfigurationCreateResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncM3ter) -> None:
        integration_configuration = await async_client.integration_configurations.create(
            config_data={"foo": "bar"},
            credentials={
                "type": "HTTP_BASIC",
                "destination": "WEBHOOK",
                "empty": True,
                "name": "name",
                "version": 0,
            },
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
            version=0,
        )
        assert_matches_type(IntegrationConfigurationCreateResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncM3ter) -> None:
        response = await async_client.integration_configurations.with_raw_response.create(
            config_data={"foo": "bar"},
            credentials={"type": "HTTP_BASIC"},
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = await response.parse()
        assert_matches_type(IntegrationConfigurationCreateResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncM3ter) -> None:
        async with async_client.integration_configurations.with_streaming_response.create(
            config_data={"foo": "bar"},
            credentials={"type": "HTTP_BASIC"},
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = await response.parse()
            assert_matches_type(IntegrationConfigurationCreateResponse, integration_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncM3ter) -> None:
        integration_configuration = await async_client.integration_configurations.retrieve(
            id="id",
        )
        assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncM3ter) -> None:
        response = await async_client.integration_configurations.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = await response.parse()
        assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncM3ter) -> None:
        async with async_client.integration_configurations.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = await response.parse()
            assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.integration_configurations.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncM3ter) -> None:
        integration_configuration = await async_client.integration_configurations.update(
            id="id",
            config_data={"foo": "bar"},
            credentials={"type": "HTTP_BASIC"},
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
        )
        assert_matches_type(IntegrationConfigurationUpdateResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncM3ter) -> None:
        integration_configuration = await async_client.integration_configurations.update(
            id="id",
            config_data={"foo": "bar"},
            credentials={
                "type": "HTTP_BASIC",
                "destination": "WEBHOOK",
                "empty": True,
                "name": "name",
                "version": 0,
            },
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
            version=0,
        )
        assert_matches_type(IntegrationConfigurationUpdateResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncM3ter) -> None:
        response = await async_client.integration_configurations.with_raw_response.update(
            id="id",
            config_data={"foo": "bar"},
            credentials={"type": "HTTP_BASIC"},
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = await response.parse()
        assert_matches_type(IntegrationConfigurationUpdateResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncM3ter) -> None:
        async with async_client.integration_configurations.with_streaming_response.update(
            id="id",
            config_data={"foo": "bar"},
            credentials={"type": "HTTP_BASIC"},
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
            entity_type="entityType",
            integration_credentials_id="integrationCredentialsId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = await response.parse()
            assert_matches_type(IntegrationConfigurationUpdateResponse, integration_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.integration_configurations.with_raw_response.update(
                id="",
                config_data={"foo": "bar"},
                credentials={"type": "HTTP_BASIC"},
                destination="destination",
                destination_id="destinationId",
                entity_id="entityId",
                entity_type="entityType",
                integration_credentials_id="integrationCredentialsId",
                name="name",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncM3ter) -> None:
        integration_configuration = await async_client.integration_configurations.list()
        assert_matches_type(
            AsyncCursor[IntegrationConfigurationListResponse], integration_configuration, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncM3ter) -> None:
        integration_configuration = await async_client.integration_configurations.list(
            next_token="nextToken",
            page_size=1,
        )
        assert_matches_type(
            AsyncCursor[IntegrationConfigurationListResponse], integration_configuration, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncM3ter) -> None:
        response = await async_client.integration_configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = await response.parse()
        assert_matches_type(
            AsyncCursor[IntegrationConfigurationListResponse], integration_configuration, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncM3ter) -> None:
        async with async_client.integration_configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = await response.parse()
            assert_matches_type(
                AsyncCursor[IntegrationConfigurationListResponse], integration_configuration, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncM3ter) -> None:
        integration_configuration = await async_client.integration_configurations.delete(
            id="id",
        )
        assert_matches_type(IntegrationConfigurationDeleteResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncM3ter) -> None:
        response = await async_client.integration_configurations.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = await response.parse()
        assert_matches_type(IntegrationConfigurationDeleteResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncM3ter) -> None:
        async with async_client.integration_configurations.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = await response.parse()
            assert_matches_type(IntegrationConfigurationDeleteResponse, integration_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.integration_configurations.with_raw_response.delete(
                id="",
            )

    @parametrize
    async def test_method_enable(self, async_client: AsyncM3ter) -> None:
        integration_configuration = await async_client.integration_configurations.enable(
            id="id",
        )
        assert_matches_type(IntegrationConfigurationEnableResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncM3ter) -> None:
        response = await async_client.integration_configurations.with_raw_response.enable(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = await response.parse()
        assert_matches_type(IntegrationConfigurationEnableResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncM3ter) -> None:
        async with async_client.integration_configurations.with_streaming_response.enable(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = await response.parse()
            assert_matches_type(IntegrationConfigurationEnableResponse, integration_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enable(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.integration_configurations.with_raw_response.enable(
                id="",
            )

    @parametrize
    async def test_method_get_by_entity(self, async_client: AsyncM3ter) -> None:
        integration_configuration = await async_client.integration_configurations.get_by_entity(
            entity_type="entityType",
        )
        assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_method_get_by_entity_with_all_params(self, async_client: AsyncM3ter) -> None:
        integration_configuration = await async_client.integration_configurations.get_by_entity(
            entity_type="entityType",
            destination="destination",
            destination_id="destinationId",
            entity_id="entityId",
        )
        assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_raw_response_get_by_entity(self, async_client: AsyncM3ter) -> None:
        response = await async_client.integration_configurations.with_raw_response.get_by_entity(
            entity_type="entityType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration_configuration = await response.parse()
        assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_get_by_entity(self, async_client: AsyncM3ter) -> None:
        async with async_client.integration_configurations.with_streaming_response.get_by_entity(
            entity_type="entityType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration_configuration = await response.parse()
            assert_matches_type(IntegrationConfigurationResponse, integration_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_by_entity(self, async_client: AsyncM3ter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_type` but received ''"):
            await async_client.integration_configurations.with_raw_response.get_by_entity(
                entity_type="",
            )
