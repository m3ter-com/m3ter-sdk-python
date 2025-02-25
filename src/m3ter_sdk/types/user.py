# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["User", "PermissionPolicy"]


class PermissionPolicy(BaseModel):
    action: List[
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

    effect: Literal["ALLOW", "DENY"]
    """
    Specifies whether or not the user is allowed to perform the action on the
    resource.

    **NOTE:** Use lower case, for example: `"allow"`. If you use upper case, you'll
    receive an error.
    """

    resource: List[str]
    """
    See
    [Statements - Available Resources](https://www.m3ter.com/docs/guides/managing-organization-and-users/creating-and-managing-permissions#statements---available-resources)
    for a listing of available resources for Permission Policy statements.
    """


class User(BaseModel):
    id: Optional[str] = None
    """The unique identifier (UUID) of this user."""

    contact_number: Optional[str] = FieldInfo(alias="contactNumber", default=None)
    """The user's contact telephone number."""

    created_by: Optional[str] = FieldInfo(alias="createdBy", default=None)
    """The user who created this user."""

    dt_created: Optional[datetime] = FieldInfo(alias="dtCreated", default=None)
    """The date and time _(in ISO-8601 format)_ when the user was created."""

    dt_end_access: Optional[datetime] = FieldInfo(alias="dtEndAccess", default=None)
    """The date and time _(in ISO 8601 format)_ when the user's access will end.

    Used to set or update the date and time a user's access expires.
    """

    dt_last_modified: Optional[datetime] = FieldInfo(alias="dtLastModified", default=None)
    """The date and time _(in ISO-8601 format)_ when the user was last modified."""

    email: Optional[str] = None
    """The email address for this user."""

    first_accepted_terms_and_conditions: Optional[datetime] = FieldInfo(
        alias="firstAcceptedTermsAndConditions", default=None
    )
    """
    The date and time _(in ISO 8601 format)_ when this user first accepted the the
    m3ter terms and conditions.
    """

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The first name of the user."""

    last_accepted_terms_and_conditions: Optional[datetime] = FieldInfo(
        alias="lastAcceptedTermsAndConditions", default=None
    )
    """
    The date and time _(in ISO 8601 format)_ when this user last accepted the the
    m3ter terms and conditions.
    """

    last_modified_by: Optional[str] = FieldInfo(alias="lastModifiedBy", default=None)
    """The unique identifier (UUID) of the user who last modified this user record."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The surname of the user."""

    organizations: Optional[List[str]] = None
    """An array listing the Organizations where this user has access."""

    permission_policy: Optional[List[PermissionPolicy]] = FieldInfo(alias="permissionPolicy", default=None)
    """An array of permission statements for the user.

    Each permission statement defines a specific permission for the user.
    """

    support_user: Optional[bool] = FieldInfo(alias="supportUser", default=None)
    """Indicates whether this is a m3ter Support user."""

    version: Optional[int] = None
    """The version number:

    - **Create:** On initial Create to insert a new entity, the version is set at 1
      in the response.
    - **Update:** On successful Update, the version is incremented by 1 in the
      response.
    """
