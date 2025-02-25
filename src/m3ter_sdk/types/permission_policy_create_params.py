# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PermissionPolicyCreateParams", "PermissionPolicy"]


class PermissionPolicyCreateParams(TypedDict, total=False):
    org_id: Annotated[str, PropertyInfo(alias="orgId")]

    name: Required[str]

    permission_policy: Required[Annotated[Iterable[PermissionPolicy], PropertyInfo(alias="permissionPolicy")]]

    version: int
    """The version number of the entity:

    - **Create entity:** Not valid for initial insertion of new entity - do not use
      for Create. On initial Create, version is set at 1 and listed in the response.
    - **Update Entity:** On Update, version is required and must match the existing
      version because a check is performed to ensure sequential versioning is
      preserved. Version is incremented by 1 and listed in the response.
    """


class PermissionPolicy(TypedDict, total=False):
    action: Required[
        List[
            Literal[
                "ALL",
                "CONFIG_CREATE",
                "CONFIG_RETRIEVE",
                "CONFIG_UPDATE",
                "CONFIG_DELETE",
                "CONFIG_EXPORT",
                "ANALYTICS_QUERY",
                "MEASUREMENTS_UPLOAD",
                "MEASUREMENTS_FILEUPLOAD",
                "MEASUREMENTS_RETRIEVE",
                "MEASUREMENTS_EXPORT",
                "FORECAST_RETRIEVE",
                "HEALTHSCORES_RETRIEVE",
                "ANOMALIES_RETRIEVE",
                "EXPORTS_DOWNLOAD",
            ]
        ]
    ]
    """
    The actions available to users who are assigned the Permission Policy - what
    they can do or cannot do with respect to the specified resource.

    **NOTE:** Use lower case and a colon-separated format, for example, if you want
    to confer full CRUD, use:

    ```
    "config:create",
    "config:delete",
    "config:retrieve",
    "config:update"
    ```
    """

    effect: Required[Literal["ALLOW", "DENY"]]
    """
    Specifies whether or not the user is allowed to perform the action on the
    resource.

    **NOTE:** Use lower case, for example: `"allow"`. If you use upper case, you'll
    receive an error.
    """

    resource: Required[List[str]]
    """
    See
    [Statements - Available Resources](https://www.m3ter.com/docs/guides/managing-organization-and-users/creating-and-managing-permissions#statements---available-resources)
    for a listing of available resources for Permission Policy statements.
    """
