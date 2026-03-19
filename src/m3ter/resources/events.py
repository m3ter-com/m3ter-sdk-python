# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import event_list_params, event_get_fields_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursor, AsyncCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.event_response import EventResponse
from ..types.event_get_types_response import EventGetTypesResponse
from ..types.event_get_fields_response import EventGetFieldsResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    """
    This section provides Endpoints for operations that allow you to retrieve detailed information about individual Events, list all Events or specific Event Types, and explore dynamic fields available for each Event Type.

    Events encompass specific instances of state changes within the system, such as the creation of a new Prepayment/Commitment for an Account. Each Event is classified under an Event Type framework, providing context about what kind of change occurred to generate the Event.

    **Events for Configuration and Billing Entities**

    Many Event Types cover common configuration and billing objects, where the Event is generated for a state change of one of these objects - for when the configuration or billing object is **created**, **deleted**, or **updated**.

    For example:
    * configuration.commitment.created
    * configuration.commitment.deleted
    * configuration.commitment.updated
    * configuration.account.created
    * configuration.account.deleted
    * configuration.account.updated
    * billing.bill.created
    * billing.bill.deleted
    * billing.bill.created

    **Events for Errors or Failures**

    There are also Event Types for certain kinds of error that can occur:

    * For an Integration:
      * validation
      * authentication
      * perform
      * missing account mapping
      * disabled

    * For a Usage Data Ingest Submission:
      * validation failure

    * For Data Export Jobs:
      * data export job failure

    **Scheduled Events**

    In addition to system-generated Events that occur when a configuration entity undergoes a state change at creation, update, or deletion of the entity, you can use API calls to create and configure *Scheduled Event Configurations*. Scheduled Events are custom Event types, which you can set up by referencing Date/Time fields on configuration and billing entities. See the [ScheduledEventConfigurations](https://www.m3ter.com/docs/api#tag/ScheduledEventConfigurations) section of this API Reference for more details.

    **Notifications for Events**

    You can create Notification rules based on Events and these rules can reference and apply calculations to the Event's fields. This allows you to set up customized alerts to be sent out via webhooks when the Event occurs and any conditions you've built into the Notification rule's calculation are satisfied.

    See the [Notifications](https://www.m3ter.com/docs/api#tag/Notifications) section for more details.

    **Other Events**

    When Events occur, they can cause other Events, such as when a Notification is triggered by the Event it is based on. For these Events there are currently two categories:
    * Notification
    * IntegrationEvent

    Also see [Utilizing Events and Notifications](https://www.m3ter.com/docs/guides/utilizing-events-and-notifications) and [Object Definitions and API Calls](https://www.m3ter.com/docs/guides/utilizing-events-and-notifications/object-definitions-and-api-calls) in the m3ter documentation for more guidance.
    """

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        org_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventResponse:
        """
        Retrieve a specific Event.

        Retrieves detailed information about the specific Event with the given UUID. An
        Event corresponds to a unique instance of a state change within the system,
        classified under a specific Event Type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/organizations/{org_id}/events/{id}", org_id=org_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventResponse,
        )

    def list(
        self,
        *,
        org_id: str | None = None,
        account_id: str | Omit = omit,
        event_name: Optional[str] | Omit = omit,
        event_type: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_actioned: bool | Omit = omit,
        next_token: str | Omit = omit,
        notification_code: str | Omit = omit,
        notification_id: str | Omit = omit,
        page_size: int | Omit = omit,
        resource_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursor[EventResponse]:
        """
        List all Events.

        Retrieve a list of all Events, with options to filter the returned list based on
        various criteria. Each Event represents a unique instance of a state change
        within the system, classified under a specific kind of Event.

        **NOTES:** You can:

        - Use `eventName` as a valid Query parameter to filter the list of Events
          returned. For example:
          `.../organizations/{orgId}/events?eventName=configuration.commitment.created`
        - Use the
          [List Notification Events](https://www.m3ter.com/docs/api#tag/Events/operation/ListEventTypes)
          endpoint in this section. The response lists the valid Query parameters.

        Args:
          account_id: The Account ID associated with the Event to filter the results. Returns the
              Events that have been generated for the Account.

          event_type:
              The category of Events to filter the results by. Options:

              - Notification
              - IntegrationEvent
              - IngestValidationFailure
              - DataExportJobFailure

          ids: List of Event UUIDs to filter the results.

              **NOTE:** cannot be used with other filters.

          include_actioned: A Boolean flag indicating whether to return Events that have been actioned.

              - **TRUE** - include actioned Events.
              - **FALSE** - exclude actioned Events.

          next_token: The `nextToken` for multi-page retrievals. It is used to fetch the next page of
              Events in a paginated list.

          notification_code: Short code of the Notification to filter the results. Returns the Events that
              have triggered the Notification.

          notification_id: Notification UUID to filter the results. Returns the Events that have triggered
              the Notification.

          page_size: The maximum number of Events to retrieve per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get_api_list(
            path_template("/organizations/{org_id}/events", org_id=org_id),
            page=SyncCursor[EventResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "event_name": event_name,
                        "event_type": event_type,
                        "ids": ids,
                        "include_actioned": include_actioned,
                        "next_token": next_token,
                        "notification_code": notification_code,
                        "notification_id": notification_id,
                        "page_size": page_size,
                        "resource_id": resource_id,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=EventResponse,
        )

    def get_fields(
        self,
        *,
        org_id: str | None = None,
        event_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetFieldsResponse:
        """List Event Fields.

        Retrieves a list of Fields for a specific Event Type.

        These Fields are dynamic
        and forward compatibile, enabling calculation operations on the Event schema.

        **Notes:**

        - In many of the Response schema for this call, such as when you retrieve the
          Fields for a `configuration.commitment.created` Event Type, `new` represents
          the attributes the newly created object has. The Response to a call to
          retrieve the Fields for a `configuration.commitment.updated` Event Type will
          contain Field values for both the `old` and `new` objects. The Response to a
          call to retrieve the Fields for a `configuration.commitment.deleted` Event
          Type will only contain `old` Fields, for values at point of deletion. Having
          access to reference both `new` and `old` Field values for an object can be
          very useful if you want to base a Notification rule on an Event and include a
          calculation in the rule that, for example, compares `new` values with `old` -
          for example, trigger a Notification only when a Commitment has been updated
          and the `new` value for the `amount` is at least $1,000 greater than the `old`
          value.
        - Some Event types will show `customFields` even though the specific billing or
          configuration object the Event is for does not yet have the custom fields
          functionality implemented. For these Events, their `customFields` values will
          not be populated until such time as the custom fields functionality is
          implemented for them

        Args:
          event_name: The name of the specific Event Type to use as a list filter, for example
              `configuration.commitment.created`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/organizations/{org_id}/events/fields", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"event_name": event_name}, event_get_fields_params.EventGetFieldsParams),
            ),
            cast_to=EventGetFieldsResponse,
        )

    def get_types(
        self,
        *,
        org_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetTypesResponse:
        """
        Retrieve a list of Notification Event Types.

        This endpoint retrieves a list of Event Types that can have Notification rules
        configured.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/organizations/{org_id}/events/types", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventGetTypesResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    """
    This section provides Endpoints for operations that allow you to retrieve detailed information about individual Events, list all Events or specific Event Types, and explore dynamic fields available for each Event Type.

    Events encompass specific instances of state changes within the system, such as the creation of a new Prepayment/Commitment for an Account. Each Event is classified under an Event Type framework, providing context about what kind of change occurred to generate the Event.

    **Events for Configuration and Billing Entities**

    Many Event Types cover common configuration and billing objects, where the Event is generated for a state change of one of these objects - for when the configuration or billing object is **created**, **deleted**, or **updated**.

    For example:
    * configuration.commitment.created
    * configuration.commitment.deleted
    * configuration.commitment.updated
    * configuration.account.created
    * configuration.account.deleted
    * configuration.account.updated
    * billing.bill.created
    * billing.bill.deleted
    * billing.bill.created

    **Events for Errors or Failures**

    There are also Event Types for certain kinds of error that can occur:

    * For an Integration:
      * validation
      * authentication
      * perform
      * missing account mapping
      * disabled

    * For a Usage Data Ingest Submission:
      * validation failure

    * For Data Export Jobs:
      * data export job failure

    **Scheduled Events**

    In addition to system-generated Events that occur when a configuration entity undergoes a state change at creation, update, or deletion of the entity, you can use API calls to create and configure *Scheduled Event Configurations*. Scheduled Events are custom Event types, which you can set up by referencing Date/Time fields on configuration and billing entities. See the [ScheduledEventConfigurations](https://www.m3ter.com/docs/api#tag/ScheduledEventConfigurations) section of this API Reference for more details.

    **Notifications for Events**

    You can create Notification rules based on Events and these rules can reference and apply calculations to the Event's fields. This allows you to set up customized alerts to be sent out via webhooks when the Event occurs and any conditions you've built into the Notification rule's calculation are satisfied.

    See the [Notifications](https://www.m3ter.com/docs/api#tag/Notifications) section for more details.

    **Other Events**

    When Events occur, they can cause other Events, such as when a Notification is triggered by the Event it is based on. For these Events there are currently two categories:
    * Notification
    * IntegrationEvent

    Also see [Utilizing Events and Notifications](https://www.m3ter.com/docs/guides/utilizing-events-and-notifications) and [Object Definitions and API Calls](https://www.m3ter.com/docs/guides/utilizing-events-and-notifications/object-definitions-and-api-calls) in the m3ter documentation for more guidance.
    """

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        org_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventResponse:
        """
        Retrieve a specific Event.

        Retrieves detailed information about the specific Event with the given UUID. An
        Event corresponds to a unique instance of a state change within the system,
        classified under a specific Event Type.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/organizations/{org_id}/events/{id}", org_id=org_id, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventResponse,
        )

    def list(
        self,
        *,
        org_id: str | None = None,
        account_id: str | Omit = omit,
        event_name: Optional[str] | Omit = omit,
        event_type: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        include_actioned: bool | Omit = omit,
        next_token: str | Omit = omit,
        notification_code: str | Omit = omit,
        notification_id: str | Omit = omit,
        page_size: int | Omit = omit,
        resource_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EventResponse, AsyncCursor[EventResponse]]:
        """
        List all Events.

        Retrieve a list of all Events, with options to filter the returned list based on
        various criteria. Each Event represents a unique instance of a state change
        within the system, classified under a specific kind of Event.

        **NOTES:** You can:

        - Use `eventName` as a valid Query parameter to filter the list of Events
          returned. For example:
          `.../organizations/{orgId}/events?eventName=configuration.commitment.created`
        - Use the
          [List Notification Events](https://www.m3ter.com/docs/api#tag/Events/operation/ListEventTypes)
          endpoint in this section. The response lists the valid Query parameters.

        Args:
          account_id: The Account ID associated with the Event to filter the results. Returns the
              Events that have been generated for the Account.

          event_type:
              The category of Events to filter the results by. Options:

              - Notification
              - IntegrationEvent
              - IngestValidationFailure
              - DataExportJobFailure

          ids: List of Event UUIDs to filter the results.

              **NOTE:** cannot be used with other filters.

          include_actioned: A Boolean flag indicating whether to return Events that have been actioned.

              - **TRUE** - include actioned Events.
              - **FALSE** - exclude actioned Events.

          next_token: The `nextToken` for multi-page retrievals. It is used to fetch the next page of
              Events in a paginated list.

          notification_code: Short code of the Notification to filter the results. Returns the Events that
              have triggered the Notification.

          notification_id: Notification UUID to filter the results. Returns the Events that have triggered
              the Notification.

          page_size: The maximum number of Events to retrieve per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get_api_list(
            path_template("/organizations/{org_id}/events", org_id=org_id),
            page=AsyncCursor[EventResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "event_name": event_name,
                        "event_type": event_type,
                        "ids": ids,
                        "include_actioned": include_actioned,
                        "next_token": next_token,
                        "notification_code": notification_code,
                        "notification_id": notification_id,
                        "page_size": page_size,
                        "resource_id": resource_id,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=EventResponse,
        )

    async def get_fields(
        self,
        *,
        org_id: str | None = None,
        event_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetFieldsResponse:
        """List Event Fields.

        Retrieves a list of Fields for a specific Event Type.

        These Fields are dynamic
        and forward compatibile, enabling calculation operations on the Event schema.

        **Notes:**

        - In many of the Response schema for this call, such as when you retrieve the
          Fields for a `configuration.commitment.created` Event Type, `new` represents
          the attributes the newly created object has. The Response to a call to
          retrieve the Fields for a `configuration.commitment.updated` Event Type will
          contain Field values for both the `old` and `new` objects. The Response to a
          call to retrieve the Fields for a `configuration.commitment.deleted` Event
          Type will only contain `old` Fields, for values at point of deletion. Having
          access to reference both `new` and `old` Field values for an object can be
          very useful if you want to base a Notification rule on an Event and include a
          calculation in the rule that, for example, compares `new` values with `old` -
          for example, trigger a Notification only when a Commitment has been updated
          and the `new` value for the `amount` is at least $1,000 greater than the `old`
          value.
        - Some Event types will show `customFields` even though the specific billing or
          configuration object the Event is for does not yet have the custom fields
          functionality implemented. For these Events, their `customFields` values will
          not be populated until such time as the custom fields functionality is
          implemented for them

        Args:
          event_name: The name of the specific Event Type to use as a list filter, for example
              `configuration.commitment.created`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/organizations/{org_id}/events/fields", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"event_name": event_name}, event_get_fields_params.EventGetFieldsParams
                ),
            ),
            cast_to=EventGetFieldsResponse,
        )

    async def get_types(
        self,
        *,
        org_id: str | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventGetTypesResponse:
        """
        Retrieve a list of Notification Event Types.

        This endpoint retrieves a list of Event Types that can have Notification rules
        configured.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/organizations/{org_id}/events/types", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventGetTypesResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.retrieve = to_raw_response_wrapper(
            events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.get_fields = to_raw_response_wrapper(
            events.get_fields,
        )
        self.get_types = to_raw_response_wrapper(
            events.get_types,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.retrieve = async_to_raw_response_wrapper(
            events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.get_fields = async_to_raw_response_wrapper(
            events.get_fields,
        )
        self.get_types = async_to_raw_response_wrapper(
            events.get_types,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.retrieve = to_streamed_response_wrapper(
            events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.get_fields = to_streamed_response_wrapper(
            events.get_fields,
        )
        self.get_types = to_streamed_response_wrapper(
            events.get_types,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.retrieve = async_to_streamed_response_wrapper(
            events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.get_fields = async_to_streamed_response_wrapper(
            events.get_fields,
        )
        self.get_types = async_to_streamed_response_wrapper(
            events.get_types,
        )
