# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.usage import file_upload_generate_upload_url_params
from ...._base_client import make_request_options
from ....types.usage.file_upload_generate_upload_url_response import FileUploadGenerateUploadURLResponse

__all__ = ["FileUploadsResource", "AsyncFileUploadsResource"]


class FileUploadsResource(SyncAPIResource):
    """
    Endpoints for submitting usage data measurements to the m3ter platform:
    - **Directly:** You can use the **Submit Measurements** call to submit raw data measurements directly using the **Ingest API**.
    - **Indirectly:** You can use the platform's file upload service calls to prepare for and submit a file for data ingest using the **Config API**.

    To use the file upload service:
    - First, make a **Generate an upload URL** call to obtain a temporary upload URL and an upload job ID.
    - You can then upload your data measurements file using a `PUT` request using the upload URL as the endpoint.
    - Any errors are reported via the normal [Alerts](https://www.m3ter.com/docs/guides/viewing-and-managing-alerts) service in the Console UI.
    - If any issues occur with a file upload, you can use the upload job ID with other file upload service calls we provide to troubleshoot and resolve issues.

    **Note:** You can also perform a File Upload via a Meter's Details page in the m3ter Console using a `CSV` formatted file you've prepared for usage data measurements ingest for the Meter.

    In the m3ter documentation, see also:
    - [Optimizing Measurement Submissions](https://www.m3ter.com/docs/guides/m3ter-apis/ingest-api-limits).
    - [File Uploads for Data Ingest](https://www.m3ter.com/docs/guides/submitting-usage-data/file-uploads-for-data-ingest)
    """

    @cached_property
    def jobs(self) -> JobsResource:
        """
        Endpoints for submitting usage data measurements to the m3ter platform:
        - **Directly:** You can use the **Submit Measurements** call to submit raw data measurements directly using the **Ingest API**.
        - **Indirectly:** You can use the platform's file upload service calls to prepare for and submit a file for data ingest using the **Config API**.

        To use the file upload service:
        - First, make a **Generate an upload URL** call to obtain a temporary upload URL and an upload job ID.
        - You can then upload your data measurements file using a `PUT` request using the upload URL as the endpoint.
        - Any errors are reported via the normal [Alerts](https://www.m3ter.com/docs/guides/viewing-and-managing-alerts) service in the Console UI.
        - If any issues occur with a file upload, you can use the upload job ID with other file upload service calls we provide to troubleshoot and resolve issues.

        **Note:** You can also perform a File Upload via a Meter's Details page in the m3ter Console using a `CSV` formatted file you've prepared for usage data measurements ingest for the Meter.

        In the m3ter documentation, see also:
        - [Optimizing Measurement Submissions](https://www.m3ter.com/docs/guides/m3ter-apis/ingest-api-limits).
        - [File Uploads for Data Ingest](https://www.m3ter.com/docs/guides/submitting-usage-data/file-uploads-for-data-ingest)
        """
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FileUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FileUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#with_streaming_response
        """
        return FileUploadsResourceWithStreamingResponse(self)

    def generate_upload_url(
        self,
        *,
        org_id: str | None = None,
        content_length: int,
        content_type: Literal["application/json", "text/json"],
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUploadGenerateUploadURLResponse:
        """
        Generate a URL for uploading a file containing measurements to the platform in
        preparation for the measurements it contains to be ingested:

        - An upload URL is returned together with an upload job id:
        - You can then upload your data measurements file using a `PUT` request using
          the returned upload URL as the endpoint.
        - You can use the returned upload job id with other calls to the File Upload
          Service for any follow-up or troubleshooting.

        **Important:**

        - The `contentLength` request parameter is required.
        - The upload URL is time limited - it is valid for **_one_** minute.

        Part of the file upload service for submitting measurements data files.

        Args:
          content_length: The size of the body in bytes. For example: `"contentLength": 485`, where 485 is
              the size in bytes of the file to upload.

              **NOTE:** Required.

          content_type:
              The media type of the entity body sent, for example:
              `"contentType":"text/json"`.

              **NOTE:** Currently only a JSON formatted file type is supported by the File
              Upload Service.

          file_name: The name of the measurements file to be uploaded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._post(
            path_template("/organizations/{org_id}/fileuploads/measurements/generateUploadUrl", org_id=org_id),
            body=maybe_transform(
                {
                    "content_length": content_length,
                    "content_type": content_type,
                    "file_name": file_name,
                },
                file_upload_generate_upload_url_params.FileUploadGenerateUploadURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUploadGenerateUploadURLResponse,
        )


class AsyncFileUploadsResource(AsyncAPIResource):
    """
    Endpoints for submitting usage data measurements to the m3ter platform:
    - **Directly:** You can use the **Submit Measurements** call to submit raw data measurements directly using the **Ingest API**.
    - **Indirectly:** You can use the platform's file upload service calls to prepare for and submit a file for data ingest using the **Config API**.

    To use the file upload service:
    - First, make a **Generate an upload URL** call to obtain a temporary upload URL and an upload job ID.
    - You can then upload your data measurements file using a `PUT` request using the upload URL as the endpoint.
    - Any errors are reported via the normal [Alerts](https://www.m3ter.com/docs/guides/viewing-and-managing-alerts) service in the Console UI.
    - If any issues occur with a file upload, you can use the upload job ID with other file upload service calls we provide to troubleshoot and resolve issues.

    **Note:** You can also perform a File Upload via a Meter's Details page in the m3ter Console using a `CSV` formatted file you've prepared for usage data measurements ingest for the Meter.

    In the m3ter documentation, see also:
    - [Optimizing Measurement Submissions](https://www.m3ter.com/docs/guides/m3ter-apis/ingest-api-limits).
    - [File Uploads for Data Ingest](https://www.m3ter.com/docs/guides/submitting-usage-data/file-uploads-for-data-ingest)
    """

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        """
        Endpoints for submitting usage data measurements to the m3ter platform:
        - **Directly:** You can use the **Submit Measurements** call to submit raw data measurements directly using the **Ingest API**.
        - **Indirectly:** You can use the platform's file upload service calls to prepare for and submit a file for data ingest using the **Config API**.

        To use the file upload service:
        - First, make a **Generate an upload URL** call to obtain a temporary upload URL and an upload job ID.
        - You can then upload your data measurements file using a `PUT` request using the upload URL as the endpoint.
        - Any errors are reported via the normal [Alerts](https://www.m3ter.com/docs/guides/viewing-and-managing-alerts) service in the Console UI.
        - If any issues occur with a file upload, you can use the upload job ID with other file upload service calls we provide to troubleshoot and resolve issues.

        **Note:** You can also perform a File Upload via a Meter's Details page in the m3ter Console using a `CSV` formatted file you've prepared for usage data measurements ingest for the Meter.

        In the m3ter documentation, see also:
        - [Optimizing Measurement Submissions](https://www.m3ter.com/docs/guides/m3ter-apis/ingest-api-limits).
        - [File Uploads for Data Ingest](https://www.m3ter.com/docs/guides/submitting-usage-data/file-uploads-for-data-ingest)
        """
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFileUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFileUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/m3ter-com/m3ter-sdk-python#with_streaming_response
        """
        return AsyncFileUploadsResourceWithStreamingResponse(self)

    async def generate_upload_url(
        self,
        *,
        org_id: str | None = None,
        content_length: int,
        content_type: Literal["application/json", "text/json"],
        file_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUploadGenerateUploadURLResponse:
        """
        Generate a URL for uploading a file containing measurements to the platform in
        preparation for the measurements it contains to be ingested:

        - An upload URL is returned together with an upload job id:
        - You can then upload your data measurements file using a `PUT` request using
          the returned upload URL as the endpoint.
        - You can use the returned upload job id with other calls to the File Upload
          Service for any follow-up or troubleshooting.

        **Important:**

        - The `contentLength` request parameter is required.
        - The upload URL is time limited - it is valid for **_one_** minute.

        Part of the file upload service for submitting measurements data files.

        Args:
          content_length: The size of the body in bytes. For example: `"contentLength": 485`, where 485 is
              the size in bytes of the file to upload.

              **NOTE:** Required.

          content_type:
              The media type of the entity body sent, for example:
              `"contentType":"text/json"`.

              **NOTE:** Currently only a JSON formatted file type is supported by the File
              Upload Service.

          file_name: The name of the measurements file to be uploaded.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if org_id is None:
            org_id = self._client._get_org_id_path_param()
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._post(
            path_template("/organizations/{org_id}/fileuploads/measurements/generateUploadUrl", org_id=org_id),
            body=await async_maybe_transform(
                {
                    "content_length": content_length,
                    "content_type": content_type,
                    "file_name": file_name,
                },
                file_upload_generate_upload_url_params.FileUploadGenerateUploadURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUploadGenerateUploadURLResponse,
        )


class FileUploadsResourceWithRawResponse:
    def __init__(self, file_uploads: FileUploadsResource) -> None:
        self._file_uploads = file_uploads

        self.generate_upload_url = to_raw_response_wrapper(
            file_uploads.generate_upload_url,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        """
        Endpoints for submitting usage data measurements to the m3ter platform:
        - **Directly:** You can use the **Submit Measurements** call to submit raw data measurements directly using the **Ingest API**.
        - **Indirectly:** You can use the platform's file upload service calls to prepare for and submit a file for data ingest using the **Config API**.

        To use the file upload service:
        - First, make a **Generate an upload URL** call to obtain a temporary upload URL and an upload job ID.
        - You can then upload your data measurements file using a `PUT` request using the upload URL as the endpoint.
        - Any errors are reported via the normal [Alerts](https://www.m3ter.com/docs/guides/viewing-and-managing-alerts) service in the Console UI.
        - If any issues occur with a file upload, you can use the upload job ID with other file upload service calls we provide to troubleshoot and resolve issues.

        **Note:** You can also perform a File Upload via a Meter's Details page in the m3ter Console using a `CSV` formatted file you've prepared for usage data measurements ingest for the Meter.

        In the m3ter documentation, see also:
        - [Optimizing Measurement Submissions](https://www.m3ter.com/docs/guides/m3ter-apis/ingest-api-limits).
        - [File Uploads for Data Ingest](https://www.m3ter.com/docs/guides/submitting-usage-data/file-uploads-for-data-ingest)
        """
        return JobsResourceWithRawResponse(self._file_uploads.jobs)


class AsyncFileUploadsResourceWithRawResponse:
    def __init__(self, file_uploads: AsyncFileUploadsResource) -> None:
        self._file_uploads = file_uploads

        self.generate_upload_url = async_to_raw_response_wrapper(
            file_uploads.generate_upload_url,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        """
        Endpoints for submitting usage data measurements to the m3ter platform:
        - **Directly:** You can use the **Submit Measurements** call to submit raw data measurements directly using the **Ingest API**.
        - **Indirectly:** You can use the platform's file upload service calls to prepare for and submit a file for data ingest using the **Config API**.

        To use the file upload service:
        - First, make a **Generate an upload URL** call to obtain a temporary upload URL and an upload job ID.
        - You can then upload your data measurements file using a `PUT` request using the upload URL as the endpoint.
        - Any errors are reported via the normal [Alerts](https://www.m3ter.com/docs/guides/viewing-and-managing-alerts) service in the Console UI.
        - If any issues occur with a file upload, you can use the upload job ID with other file upload service calls we provide to troubleshoot and resolve issues.

        **Note:** You can also perform a File Upload via a Meter's Details page in the m3ter Console using a `CSV` formatted file you've prepared for usage data measurements ingest for the Meter.

        In the m3ter documentation, see also:
        - [Optimizing Measurement Submissions](https://www.m3ter.com/docs/guides/m3ter-apis/ingest-api-limits).
        - [File Uploads for Data Ingest](https://www.m3ter.com/docs/guides/submitting-usage-data/file-uploads-for-data-ingest)
        """
        return AsyncJobsResourceWithRawResponse(self._file_uploads.jobs)


class FileUploadsResourceWithStreamingResponse:
    def __init__(self, file_uploads: FileUploadsResource) -> None:
        self._file_uploads = file_uploads

        self.generate_upload_url = to_streamed_response_wrapper(
            file_uploads.generate_upload_url,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        """
        Endpoints for submitting usage data measurements to the m3ter platform:
        - **Directly:** You can use the **Submit Measurements** call to submit raw data measurements directly using the **Ingest API**.
        - **Indirectly:** You can use the platform's file upload service calls to prepare for and submit a file for data ingest using the **Config API**.

        To use the file upload service:
        - First, make a **Generate an upload URL** call to obtain a temporary upload URL and an upload job ID.
        - You can then upload your data measurements file using a `PUT` request using the upload URL as the endpoint.
        - Any errors are reported via the normal [Alerts](https://www.m3ter.com/docs/guides/viewing-and-managing-alerts) service in the Console UI.
        - If any issues occur with a file upload, you can use the upload job ID with other file upload service calls we provide to troubleshoot and resolve issues.

        **Note:** You can also perform a File Upload via a Meter's Details page in the m3ter Console using a `CSV` formatted file you've prepared for usage data measurements ingest for the Meter.

        In the m3ter documentation, see also:
        - [Optimizing Measurement Submissions](https://www.m3ter.com/docs/guides/m3ter-apis/ingest-api-limits).
        - [File Uploads for Data Ingest](https://www.m3ter.com/docs/guides/submitting-usage-data/file-uploads-for-data-ingest)
        """
        return JobsResourceWithStreamingResponse(self._file_uploads.jobs)


class AsyncFileUploadsResourceWithStreamingResponse:
    def __init__(self, file_uploads: AsyncFileUploadsResource) -> None:
        self._file_uploads = file_uploads

        self.generate_upload_url = async_to_streamed_response_wrapper(
            file_uploads.generate_upload_url,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        Endpoints for submitting usage data measurements to the m3ter platform:
        - **Directly:** You can use the **Submit Measurements** call to submit raw data measurements directly using the **Ingest API**.
        - **Indirectly:** You can use the platform's file upload service calls to prepare for and submit a file for data ingest using the **Config API**.

        To use the file upload service:
        - First, make a **Generate an upload URL** call to obtain a temporary upload URL and an upload job ID.
        - You can then upload your data measurements file using a `PUT` request using the upload URL as the endpoint.
        - Any errors are reported via the normal [Alerts](https://www.m3ter.com/docs/guides/viewing-and-managing-alerts) service in the Console UI.
        - If any issues occur with a file upload, you can use the upload job ID with other file upload service calls we provide to troubleshoot and resolve issues.

        **Note:** You can also perform a File Upload via a Meter's Details page in the m3ter Console using a `CSV` formatted file you've prepared for usage data measurements ingest for the Meter.

        In the m3ter documentation, see also:
        - [Optimizing Measurement Submissions](https://www.m3ter.com/docs/guides/m3ter-apis/ingest-api-limits).
        - [File Uploads for Data Ingest](https://www.m3ter.com/docs/guides/submitting-usage-data/file-uploads-for-data-ingest)
        """
        return AsyncJobsResourceWithStreamingResponse(self._file_uploads.jobs)
