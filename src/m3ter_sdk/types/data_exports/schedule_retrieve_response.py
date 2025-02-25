# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .usage_data_export_schedule import UsageDataExportSchedule
from .operational_data_export_schedule import OperationalDataExportSchedule

__all__ = ["ScheduleRetrieveResponse"]

ScheduleRetrieveResponse: TypeAlias = Union[OperationalDataExportSchedule, UsageDataExportSchedule]
