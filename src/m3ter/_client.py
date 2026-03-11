# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import TYPE_CHECKING, Any, Mapping
from datetime import datetime
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._models import FinalRequestOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import M3terError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        bills,
        plans,
        usage,
        users,
        events,
        meters,
        charges,
        accounts,
        balances,
        counters,
        pricings,
        products,
        webhooks,
        bill_jobs,
        contracts,
        currencies,
        statements,
        bill_config,
        commitments,
        plan_groups,
        aggregations,
        data_exports,
        account_plans,
        custom_fields,
        debit_reasons,
        lookup_tables,
        authentication,
        credit_reasons,
        plan_templates,
        resource_groups,
        counter_pricings,
        plan_group_links,
        external_mappings,
        transaction_types,
        counter_adjustments,
        organization_config,
        permission_policies,
        compound_aggregations,
        integration_configurations,
        notification_configurations,
        scheduled_event_configurations,
    )
    from .resources.plans import PlansResource, AsyncPlansResource
    from .resources.events import EventsResource, AsyncEventsResource
    from .resources.meters import MetersResource, AsyncMetersResource
    from .resources.charges import ChargesResource, AsyncChargesResource
    from .resources.accounts import AccountsResource, AsyncAccountsResource
    from .resources.counters import CountersResource, AsyncCountersResource
    from .resources.pricings import PricingsResource, AsyncPricingsResource
    from .resources.products import ProductsResource, AsyncProductsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.bill_jobs import BillJobsResource, AsyncBillJobsResource
    from .resources.contracts import ContractsResource, AsyncContractsResource
    from .resources.currencies import CurrenciesResource, AsyncCurrenciesResource
    from .resources.bill_config import BillConfigResource, AsyncBillConfigResource
    from .resources.bills.bills import BillsResource, AsyncBillsResource
    from .resources.commitments import CommitmentsResource, AsyncCommitmentsResource
    from .resources.plan_groups import PlanGroupsResource, AsyncPlanGroupsResource
    from .resources.usage.usage import UsageResource, AsyncUsageResource
    from .resources.users.users import UsersResource, AsyncUsersResource
    from .resources.aggregations import AggregationsResource, AsyncAggregationsResource
    from .resources.account_plans import AccountPlansResource, AsyncAccountPlansResource
    from .resources.custom_fields import CustomFieldsResource, AsyncCustomFieldsResource
    from .resources.debit_reasons import DebitReasonsResource, AsyncDebitReasonsResource
    from .resources.authentication import AuthenticationResource, AsyncAuthenticationResource
    from .resources.credit_reasons import CreditReasonsResource, AsyncCreditReasonsResource
    from .resources.plan_templates import PlanTemplatesResource, AsyncPlanTemplatesResource
    from .resources.resource_groups import ResourceGroupsResource, AsyncResourceGroupsResource
    from .resources.counter_pricings import CounterPricingsResource, AsyncCounterPricingsResource
    from .resources.plan_group_links import PlanGroupLinksResource, AsyncPlanGroupLinksResource
    from .resources.balances.balances import BalancesResource, AsyncBalancesResource
    from .resources.external_mappings import ExternalMappingsResource, AsyncExternalMappingsResource
    from .resources.transaction_types import TransactionTypesResource, AsyncTransactionTypesResource
    from .resources.counter_adjustments import CounterAdjustmentsResource, AsyncCounterAdjustmentsResource
    from .resources.organization_config import OrganizationConfigResource, AsyncOrganizationConfigResource
    from .resources.permission_policies import PermissionPoliciesResource, AsyncPermissionPoliciesResource
    from .resources.compound_aggregations import CompoundAggregationsResource, AsyncCompoundAggregationsResource
    from .resources.statements.statements import StatementsResource, AsyncStatementsResource
    from .resources.data_exports.data_exports import DataExportsResource, AsyncDataExportsResource
    from .resources.integration_configurations import (
        IntegrationConfigurationsResource,
        AsyncIntegrationConfigurationsResource,
    )
    from .resources.lookup_tables.lookup_tables import LookupTablesResource, AsyncLookupTablesResource
    from .resources.notification_configurations import (
        NotificationConfigurationsResource,
        AsyncNotificationConfigurationsResource,
    )
    from .resources.scheduled_event_configurations import (
        ScheduledEventConfigurationsResource,
        AsyncScheduledEventConfigurationsResource,
    )

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "M3ter", "AsyncM3ter", "Client", "AsyncClient"]

from .types import AuthenticationGetBearerTokenResponse


class M3ter(SyncAPIClient):
    # client options
    api_key: str
    api_secret: str
    token: str | None
    token_expiry: datetime | None
    org_id: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_secret: str | None = None,
        token: str | None = None,
        token_expiry: datetime | None = None,
        org_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous M3ter client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `M3TER_API_KEY`
        - `api_secret` from `M3TER_API_SECRET`
        - `token` from `M3TER_API_TOKEN`
        - `org_id` from `M3TER_ORG_ID`
        """
        if api_key is None:
            api_key = os.environ.get("M3TER_API_KEY")
        if api_key is None:
            raise M3terError(
                "The api_key client option must be set either by passing api_key to the client or by setting the M3TER_API_KEY environment variable"
            )
        self.api_key = api_key

        if api_secret is None:
            api_secret = os.environ.get("M3TER_API_SECRET")
        if api_secret is None:
            raise M3terError(
                "The api_secret client option must be set either by passing api_secret to the client or by setting the M3TER_API_SECRET environment variable"
            )
        self.api_secret = api_secret

        if token is None:
            token = os.environ.get("M3TER_API_TOKEN")
        self.token = token
        self.token_expiry = token_expiry

        if org_id is None:
            org_id = os.environ.get("M3TER_ORG_ID")
        if org_id is None:
            raise M3terError(
                "The org_id client option must be set either by passing org_id to the client or by setting the M3TER_ORG_ID environment variable"
            )
        self.org_id = org_id

        if base_url is None:
            base_url = os.environ.get("M3TER_BASE_URL")
        self._base_url_overridden = base_url is not None
        if base_url is None:
            base_url = f"https://api.m3ter.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def authentication(self) -> AuthenticationResource:
        """
        Endpoint for retrieving a JSON Web Token (JWT) bearer token for a ServiceUser using the Client Credentials Grant flow.

        A ServiceUser represents the automated process you want to grant access to your Organization - that is, as an API user.
        """
        from .resources.authentication import AuthenticationResource

        return AuthenticationResource(self)

    @cached_property
    def accounts(self) -> AccountsResource:
        """
        Endpoints for Account related operations such as creation, update, list and delete.
        An Account represents one of your end-customer accounts.

        Accounts do not belong to a Product to allow for cases where an end customer takes more than one of your Products, and the charges for these Products differ.

        You typically attach a priced Plan or Plan Template to an Account before you can generate bills for the Account:
        - If a customer consumes several of your Products, you can attach a priced Plan or Plan Template to the Account for charging against each Product.
        - If an Account is charged solely on the basis of an agreed Prepayment/Commitment amount but not all of the Prepayment is prepaid, you can use a customized billing schedule for outstanding fees without having to attach a Plan to the Account to generate Bills.

        You can create Child Accounts for end customers who hold multiple Accounts with you. You can then set up billing for the Parent/Child Account usage to have the end-customer billed once for the Parent Account, instead of having separate bills issued for usage against each of their multiple Accounts.

        **IMPORTANT! - use of PII:** The use of any of your end-customers' Personally Identifiable Information (PII) in m3ter is restricted to a few fields on the **Account** entity. Please ensure that only the ``name``, ``address``, or ``emailAddress`` fields contain any end-customer PII data on any Accounts you create. See the [Introduction section](https://www.m3ter.com/docs/api#section/Introduction) above for more details.
        """
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def account_plans(self) -> AccountPlansResource:
        """
        Endpoints for AccountPlan and AccountPlanGroup related operations such as creation, update, list and delete.

        **AccountPlans**
        An Account represents one of your end-customer accounts. To create an AccountPlan, you attach a Product Plan to an Account. The AccountPlan then determines the charges incurred at billing by your end customer for consuming the Product the Plan is for:
        * **AccountPlan Active/Inactive**. Set start and end dates to define the period the AccountPlan is active for the Account.
        * **AccountPlan per Product**. If an end customer consumes multiple Products, create separate AccountPlans to charge for each Product.

        **AccountPlan Constraints:**
        * Only one AccountPlan per Product can be active at any one time for an Account.
        * If you create a Plan as a custom Plan for a specific Account, you can only use it to create an AccountPlan for that Account.

        **AccountPlanGroups**
        Plan Groups are used when you want to apply a minimum spend amount at billing across several of your Products each of which are priced separately - when you create the Plan Group, you define an overall minimum spend and then add any priced Plans you want to include in the Group. To create an AccounPlanGroup, you can attach a Plan Group to an Account that consumes the separate Products which are priced using the included Plans. At billing, the minimum spend you've defined for the Plan Group is applied:
        * **Active AccountPlanGroup**. Set the start and end dates to define the period for which the Plan Group will be active for the Account.

        **Plan Group Notes:**
        * You can only add *one Plan for the same Product* to a Plan Group. See the [Plan Group](https://www.m3ter.com/docs/api#tag/PlanGroup) in this API Reference for more details on creating Plan Groups.
        * You can create a *custom Plan Group* for an Account, which means the Plan Group can only be attached to that Account to create an AccountPlanGroup.

        **AcountPlanGroup - Notes and Constraints:**
        * **AccountPlanGroup is type of AccountPlan** When you attach a Plan Group to an Account, this creates an AccountPlanGroup. However, the m3ter data model *does not support a separate AccountPlanGroup entity*, and an AccountPlanGroup is a type of AccountPlan where a `planGroupId` is used instead of a `planId` when it's created. See the [Create AccountPlan](https://www.m3ter.com/docs/api#tag/AccountPlan/operation/PostAccountPlan) call in this section and [Attaching Plan Groups to an Account](https://www.m3ter.com/docs/guides/end-customer-accounts/attaching-plan-groups-to-an-account) in our main User Documentation.
        * **Multiple AccountPlan Groups:** You can attach more than one Plan Group to an Account to create multiple AccountPlanGroups, but the rule that *only one attached Plan per Product can be active at any one time for an Account* is preserved:
                * Multiple attached Plan Groups on an Account can have overlapping dates only if none of the Plan Groups contain a Plan belonging to the same Product. If you try to attach a Plan Group to an Account with Plan Groups already attached and:
                        * The new Plan Group contains a Product Plan that also belongs to a Plan Group already attached to the Account.
                        * The dates for these "matched Plan" Plan Groups being active for the Account would overlap.
                        * Then you'll receive an error and the attachment will be blocked.
        """
        from .resources.account_plans import AccountPlansResource

        return AccountPlansResource(self)

    @cached_property
    def aggregations(self) -> AggregationsResource:
        """Endpoints for listing, creating, updating, retrieving, or deleting Aggregations.

        An Aggregation links to a Meter and targets a Data Field or Derived Field on the Meter. You define the method of aggregation used to convert the usage data collected by the targeted Meter field into a numerical unit of measurement.

        You can then use the unit of measurement an Aggregation yields as a metric for pricing Product Plans and apply usage-based pricing to your products and services. You might also want to aggregate raw data measures for other purposes, such as to feed into analytical or business performance tools.

        **Notes:**
        * **Contrast with Compound Aggregations**. Standard or simple Aggregations of this type, which apply an aggregation method directly to Meter usage data fields, are contrasted with [Compound Aggregations](https://www.m3ter.com/docs/api#tag/CompoundAggregation). A Compound Aggregation typically references one or more simple Aggregations and applies a calculation to them to derive pricing metrics needed to serve more complex usage-based pricing scenarios.
        * **Segmented Aggregations**. Segmented Aggregations allow you to segment the usage data collected by a single Meter. This capability is very useful for implementing some pricing and billing use cases. See [Segmented Aggregations](https://www.m3ter.com/docs/guides/usage-data-aggregations/segmented-aggregations) in our main documentation for more details.
        """
        from .resources.aggregations import AggregationsResource

        return AggregationsResource(self)

    @cached_property
    def balances(self) -> BalancesResource:
        """Endpoints for creating/retrieving/updating/deleting Balances on Accounts.

        When you have created a Balance for an Account, you can create a positive or negative Transaction amounts for the Balance. To do this, you must first define Transaction Types for your Organization, and then use one of these Transaction Types when you add a specific Transaction to a Balance - see the [Create TransactionType](https://www.m3ter.com/docs/api#tag/TransactionType/operation/CreateTransactionType) call in the Transaction Type section in this API Reference for more details.

        Balances are typically used when a customer prepays an amount to add a credit to their Account, which can then be draw-down against charges due for product or service consumption. You can include options to top-up the original Balance.

        Examples of how Balances for end customer Accounts can be used:

        * Onboarding Balance/Free Trials. Offering an onboarding incentive to new customers as an initial free credit Balance on their Account.

        * Balance as initial commitment. Add a Balance amount to a new customer Account. This acts as an initial commitment, which allows them to use the service and gain an accurate insight into their usage level.

        * Managing Customer Satisfaction. Use Balance as credits that will be applied to subsequent Bills as compensation for acknowledged service delivery issues.

        * Facilitating Balance Adjustments:
                * Apply negative amounts to immediately write-off outstanding Balances.

        #### What is the difference between Balances and Commitments/Prepayments?

        To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

        Commitments - also referred to as Prepayments - are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the commitment or prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

        In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

        You can use Commitments/Prepayments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Commitment credit on an Account is drawn-down - Balance amounts first or Commitment/Prepayment amounts first.
        """
        from .resources.balances import BalancesResource

        return BalancesResource(self)

    @cached_property
    def bills(self) -> BillsResource:
        """
        Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills.

        Bills are generated for an Account, and are calculated in accordance with the usage-based pricing Plans applied for the Products the Account consumes. These endpoints enable interaction with the billing system, allowing you to obtain billing details and insights into the consumption patterns and charges of your end-customer Accounts.
        """
        from .resources.bills import BillsResource

        return BillsResource(self)

    @cached_property
    def bill_config(self) -> BillConfigResource:
        """Endpoints for updating and retreiving the Bill Configuration for an Organization.

        The Organization represents your company as a direct customer of the m3ter service.

        You can use the **Update BillConfig** endpoint to set a global lock date for **all** Bills - any Bill with a service period end date on or before the set date will be locked and cannot be updated.

        **Warning: Ensure all Bills are Approved!** If you try to set a global lock date when there remains Bills in a *Pending* state whose service period end date is on or before the specified lock date, then you'll receive an error.
        """
        from .resources.bill_config import BillConfigResource

        return BillConfigResource(self)

    @cached_property
    def commitments(self) -> CommitmentsResource:
        """
        Endpoints that manage Commitments *(also known as Prepayments)* in the context of usage-based pricing and billing. A Commitment represents an agreement where the end-customer has agreed to pay a fixed minimum amount throughout the contract period. ***The commitment amount is payable regardless of the actual usage by the customer of your service or product.***

        These endpoints enable the creation, updating, retrieval, and deletion of Commitments. Use them to manage your customer's Commitments and ensure optimal revenue recognition:
        * Specify which type of charges can draw-down against a Commitment amount on an Account at billing: usage, minimum spend, standing charges, or recurring charges.
        * Define overage surcharge percentages, which are applied when the usage charges exceed the agreed Commitment amount within the contract duration.

        #### What is the difference between Balances and Commitments/Prepayments?

        To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

        Commitments/Prepayments are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

        In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

        You can use Prepayments/Commitments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Prepayment credit on an Account is drawn-down - Balance amounts first or Prepayment amounts first.

        #### Billing for Commitments

        If not all of an agreed Commitment amount is paid at the start of an end-customer contract period, you can choose one of two options for billing the outstanding fees due on the customer Account:
        - Select a Product *Plan to bill with*.
        - Define a *schedule of billing dates*.
        """
        from .resources.commitments import CommitmentsResource

        return CommitmentsResource(self)

    @cached_property
    def bill_jobs(self) -> BillJobsResource:
        """Endpoints for creating, retrieving, listing, and cancelling Bill Jobs.

        Bill Jobs are critical components in billing management, providing asynchronous mechanisms to calculate and handle bills.

        Bill Jobs give you the flexibiity to run Bills manually for Accounts to suit different billing management purposes. For example, some historical usage data has come in for an Account and you want to run a Bill for a specific date on that Account to check that the Bill is showing correctly for the charges due on the new usage data.
        """
        from .resources.bill_jobs import BillJobsResource

        return BillJobsResource(self)

    @cached_property
    def charges(self) -> ChargesResource:
        """Endpoints for creating/updating/deleting Charges.

        Create Charges for your end-customer Accounts to create ad-hoc line items for Account billing. Charges are:
        * Created for either debit or credit amounts.
        * Linked to a Product for accounting purposes.
        * Optionally linked to a Contract.
        * Given a specific date for billing. When a bill job has run for the specified Charge bill date, a Charge appears as an Ad-hoc line item on the Bill.
        * Assigned a service period.
        * Available in any currency defined for your Organization.
        See [Creating Charges for Accounts](https://www.m3ter.com/docs/guides/end-customer-accounts/creating-charges-for-accounts) in our main user documentation for more details.

        Alternatively, you can create a Charge for a Balance on an end-customer Account to create balance fee line items for Account billing. See [Creating Charges for Balances](https://www.m3ter.com/docs/guides/end-customer-accounts/creating-balances-for-accounts/creating-charges-for-balances) in our main user documentation for more details.
        """
        from .resources.charges import ChargesResource

        return ChargesResource(self)

    @cached_property
    def compound_aggregations(self) -> CompoundAggregationsResource:
        """
        Endpoints for Compound Aggregation related operations such as creation, update, list and delete.

        Use Compound Aggregations to create numerical measures from usage data by applying a calculation to one or more simple Aggregations or Custom Fields. These numerical measures can then be used as pricing metrics to price your Product Plans, enabling you to implement a wide range of usage-based pricing use cases.

        You can create two types of Compound Aggregation:

        **Global**
        - Pricing: Not tied to any specific product and can be used to price Plans belonging to any Product.
        - Calculation: can reference all simple Aggregations - both Global simple Aggregations and any product-specific simple Aggregations.

        **Product-specific**
        - Pricing: belong to a specific Product and can only be used to price Plans belonging to the same Product.
        - Calculation: can reference any simple Aggregations belonging to the same Product and any Global simple Aggregations.

        **IMPORTANT!** If a simple Aggregation referenced by a Compound Aggregation has a **Quantity per unit** defined or a **Rounding** defined, these will not be factored into the value used by the calculation. For example, if the simple Aggregation referenced has a base value of 100 and has **Quantity per unit** set at 10, the Compound Aggregation calculation *will use the base value of 100 not 10*.

        To better understand and use Compound Aggregations, refer to the example [Compound Aggregation Use Case](https://www.m3ter.com/docs/guides/setting-up-usage-data-meters-and-aggregations/compound-aggregations#example-use-case) in the m3ter documentation.
        """
        from .resources.compound_aggregations import CompoundAggregationsResource

        return CompoundAggregationsResource(self)

    @cached_property
    def contracts(self) -> ContractsResource:
        """
        Endpoints for Contract related operations such as creation, update, list and delete.

        Contracts are created for Accounts, which are your end-user customers. Contracts can be used for:
        * **Accounts Reporting**. To serve your general accounting operations and processes, you can report on total Contract values for an Account.
        * **Contract Billing**. Various billing entities associated with an Account can  be linked to Contracts on the Account to meet your specific Contract billing use cases.
        """
        from .resources.contracts import ContractsResource

        return ContractsResource(self)

    @cached_property
    def counters(self) -> CountersResource:
        """Endpoints for listing, creating, retrieving, updating, or deleting Counters.

        You can create Counters for your m3ter Organization, which can then be used as pricing metrics to apply a unit-based [CounterPricing](https://www.m3ter.com/docs/api#tag/CounterPricing) to Product Plans or Plan Templates for recurring subscription charges on Accounts.

        Counters can then be used to post [CounterAdjustments](https://www.m3ter.com/docs/api#tag/CounterAdjustments) on your end-customer Accounts.

        Accounts are then billed in accordance with the CounterPricing on Plans attached to the Accounts and for the actual Counter quantities Accounts subscribe to. See [Recurring Charges: Counters](https://www.m3ter.com/docs/guides/recurring-charges-counters) in our main user documentation for more details.
        """
        from .resources.counters import CountersResource

        return CountersResource(self)

    @cached_property
    def counter_adjustments(self) -> CounterAdjustmentsResource:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting CounterAdjustments.

        If you attach a Plan to an Account which is priced using a Counter to apply unit-based pricing, you can then create CounterAdjustments for the Account using that Counter to ensure the Account is billed according to the number of Counter units the Account subscribes to in a given billing period.

        See [Understanding and Creating Counter Adjustments for Accounts](https://www.m3ter.com/docs/guides/recurring-charges-counters/creating-counter-adjustments-for-accounts) for more information.
        """
        from .resources.counter_adjustments import CounterAdjustmentsResource

        return CounterAdjustmentsResource(self)

    @cached_property
    def counter_pricings(self) -> CounterPricingsResource:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting CounterPricing.

        Create the CounterPricing for a Plan/PlanTemplate using a Counter, and define a unit-based pricing structure for charging end customer Accounts put on the Plan.

        See [Creating Counters and Pricing Plans](https://www.m3ter.com/docs/guides/recurring-charges-counters/creating-counters) for more information.
        """
        from .resources.counter_pricings import CounterPricingsResource

        return CounterPricingsResource(self)

    @cached_property
    def credit_reasons(self) -> CreditReasonsResource:
        """Endpoints for CreditReason operations such as creation, update, list, and delete.

        You can create CreditReasons for your Organization, and then use them when creating a credit line item on a bill, or applying a product credit to a bill. CreditReasons provide contextual information as to why a credit was applied.
        """
        from .resources.credit_reasons import CreditReasonsResource

        return CreditReasonsResource(self)

    @cached_property
    def currencies(self) -> CurrenciesResource:
        """Endpoints for Currency operations such as creation, update, list, and delete.

        Currencies are stored for your Organization, and can then be used to specify currencies on various entities such as plan groups and plan templates.

        **IMPORTANT!**
        The Currencies you want to use in your Organization must be created first.

        The currency you select for your Organization determines the billing currency and overrides any currency settings in your pricing Plans.
        For example, if the Organization currency is set to USD and a pricing Plan used for an Account is set to GBP, the bill for an Account using that Plan is calculated in GBP, and then each bill line item converted to USD amounts.

        Currency conversion rates are setup in the *OrganizationConfig*. For more details, see [Creating and Managing Currencies](https://www.m3ter.com/docs/guides/organization-and-access-management/viewing-and-editing-organization#creating-and-managing-currencies) in the m3ter Documentation.
        """
        from .resources.currencies import CurrenciesResource

        return CurrenciesResource(self)

    @cached_property
    def custom_fields(self) -> CustomFieldsResource:
        """
        Endpoints for retrieving and updating Custom Fields at the Organization level for all entities that support them.

        Custom Fields in m3ter allow you to store custom data in the form of number or string values against m3ter entities in a way that does not directly affect the normal working operation of the m3ter platform. Having this capability to store data in a free-hand fashion can prove very useful in helping you to meet specific usage-based pricing and other operational business use cases.

        However, you can exploit the values stored on Custom Fields in a more direct way by referencing them in Derived Field and Compound Aggregation calculations. Given the key role these calculations can play when implementing usage-based pricing schema, any Custom Fields you reference will then affect how the platform behaves. Referencing Custom Field values in your calculations offers a much wider scope of options when it comes to resolving complex usage-based pricing use cases.

        Custom Fields can be added to the following entities at Organizational level:
        * Organization
        * Account
        * AccountPlan
        * Aggregation
        * Compound Aggregation
        * Meter
        * Product
        * Plan
        * PlanTemplate
        * Contract

        These all follow the same pattern - a new *(optional)* field is available on the entity request and response bodies called "customFields" which is a object in this format:
        ```
        "customFields": {
                        "exampleCustomField1": 7.1,
                        "exampleCustomField2": "stringValue"
        }
        ```
        The value for a Custom Field can be a string or a number.

        **Using Custom Field values in calculations:**
        - You can add Custom Fields at two levels - the Organization level and the individual entity level.
        - The Organizational level field provides a default value and *must be added* if you want to also add a Custom Field of the same name at the corresponding individual entity level. If you reference the Custom Field in a calculation, the value for the individual entity level field is used. If no field is defined at individual entity level, then the Organization level field value is used.

        **Important: Constraints and Exceptions!**

        **Custom Fields at Organization Level**. Currently, you cannot create Custom Fields at the Organization-level for the following enitites:
        * Plan Group
        * Balance
        * Balance Transaction Schedule
        * Balance Charge Schedule

        Therefore you cannot reference the Custom Fields values created at the individual entity level for these entities in your Derived Field or Compound Aggregation calculations.

        **Derived Field Calculations**. You can *only reference Custom Fields* for the following entities:
        * Organization
        * Meter
        * Account

        However, if you are using Meters belonging to *a specific Product*, that is, not *Global Meters*, you can also reference Custom Fields added to a Product in Derived Field calculations.

        **Compound Aggregation Calculations - Meter Custom Fields**. The value of the *Organization level Meter Custom Field will always be used*, even if you have defined a corresponding field at the individual Meter level.

        See [Working with Custom Fields](https://www.m3ter.com/docs/guides/creating-and-managing-products/working-with-custom-fields) in the m3ter documentation for more information.
        """
        from .resources.custom_fields import CustomFieldsResource

        return CustomFieldsResource(self)

    @cached_property
    def data_exports(self) -> DataExportsResource:
        """Endpoints for triggering one-off, ad-hoc Data Exports.

        You can set up and run ad-hoc Exports to export two kinds of data from your m3ter Organization:
        * Usage data.
        * Operational data for entities.

        **Ad-Hoc Export Destinations** When setting up and running an ad-hoc Export:
        * You can define one or more Export Destinations - see the [ExportDestination](https://www.m3ter.com/docs/api#tag/ExportDestination) section of this API Reference. When the export runs, the data is sent through to the sepecified Destination. However, the export file is also made available for you to download it locally.
        * You can set up and run Data Exports without defining a Destination. The data is not exported but the compiled export file is made available for downloading locally.
        * For details on downloading an export file, see the [Get Data Export File Download URL](https://www.m3ter.com/docs/api#tag/ExportDestination/operation/GenerateDataExportFileDownloadUrl) endpoint in this API Reference.

        **Preview Version!** The Data Export feature is currently available only in Preview release version. See [Feature Release Stages](https://www.m3ter.com/docs/guides/getting-started/feature-release-stages) for Preview release definition. ExportAdHoc endpoints will only be available if Data Export has been enabled for your Organization. For more details see [Data Export(Preview)](https://www.m3ter.com/docs/guides/data-exports) in our main User documentation. If you're interested in previewing the Data Export feature, please get in touch with m3ter Support or your m3ter contact.
        """
        from .resources.data_exports import DataExportsResource

        return DataExportsResource(self)

    @cached_property
    def debit_reasons(self) -> DebitReasonsResource:
        """Endpoints for DebitReason operations such as creation, update, list, and delete.

        You can create DebitReasons for your Organization, and then use them when creating a debit line item on a bill, or applying a product debit to a bill. DebitReasons provide contextual information as to why a debit was applied.
        """
        from .resources.debit_reasons import DebitReasonsResource

        return DebitReasonsResource(self)

    @cached_property
    def events(self) -> EventsResource:
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
        from .resources.events import EventsResource

        return EventsResource(self)

    @cached_property
    def external_mappings(self) -> ExternalMappingsResource:
        """
        Endpoints for managing External Mapping related operations such as creation, update, list and delete.

        When you integrate your 3rd-party systems with the m3ter platform, a mapping between entities in the local system *(m3ter)* and external systems is constructed. This *External Mapping* is crucial in scenarios where data from external systems is consumed or where data from the local system is to be synchronized with external systems.

        When you are working to set up your Integrations and want to test or troubleshoot your implementation before going live, you might need to create External Mappings manually and, at a later date, edit or delete them.
        """
        from .resources.external_mappings import ExternalMappingsResource

        return ExternalMappingsResource(self)

    @cached_property
    def integration_configurations(self) -> IntegrationConfigurationsResource:
        """
        A suite of endpoints for configuring and managing third party integrations within the m3ter platform. The integration endpoints in this section facilitate various operations such as creating, updating, listing, and deletion of integrations.

        m3ter integrations enable seamless data synchronization and mapping with external systems required in core business processes. These processes often include sales, pricing, billing and invoicing, and general finance.

        With m3ter integrations, you can establish robust connections with popular business platforms, enhancing your operational capabilities. For example:
        * Chargebee
        * Salesforce
        * Stripe
        * Netsuite
        * Paddle
        * Xero
        * QuickBooks
        """
        from .resources.integration_configurations import IntegrationConfigurationsResource

        return IntegrationConfigurationsResource(self)

    @cached_property
    def lookup_tables(self) -> LookupTablesResource:
        """Endpoints for creating/updating/deleting Lookup Tables.

        Lookup Tables enable you to manage dynamic data mappings that your calculations reference. Use them for currency conversion, pricing tiers, discount rates, and similar scenarios where you require values to change operationally but for calculation logic to remain constant.

        **Beta Version!** The Lookup Table feature is currently available in Beta release version. See [Feature Release Stages](https://www.m3ter.com/docs/guides/getting-started/feature-release-stages) for Beta release definition. Lookup Table endpoints will only be available if Lookup Tables have been enabled for your Organization. For more details see [Lookup Tables (Beta)](https://www.m3ter.com/docs/guides/lookup-tables) in our main User documentation.
        """
        from .resources.lookup_tables import LookupTablesResource

        return LookupTablesResource(self)

    @cached_property
    def meters(self) -> MetersResource:
        """Endpoints for listing, creating, updating, retrieving, or deleting Meters.

        Use Meters to submit usage data for the consumption of your products and services by end customers. This usage data then becomes the basis for setting up usage-based pricing for your products and services.

        Examples of usage data collected in Meters:
        * Number of logins.
        * Duration of session.
        * Amount of data downloaded.

        To collect usage data and ingest it into the platform, you can define two types of fields for Meters:
        - `dataFields` Used to collect raw usage data measures - numeric quantitative data values or non-numeric point data values.
        - `derivedFields` Used to derive usage data measures that are the result of applying a calculation to `dataFields`, `customFields`, or system `Timestamp` fields.

        You can also:
        - Create `customFields` for a Meter, which allows you to attach custom data to the Meter as name/value pairs.
        - Create Global Meters, which are not tied to a specific Product and allow you to collect usage data that will form the basis of usage-based pricing across multiple Products.

        **IMPORTANT! - use of PII:** The use of any of your end-customers' Personally Identifiable Information (PII) in m3ter is restricted to a few fields on the **Account** entity. Please ensure that any fields you configure for Meters, such as Data Fields or Derived Fields, do not contain any end-customer PII data. See the [Introduction section](https://www.m3ter.com/docs/api#section/Introduction) above for more details.

        See also:
        - [Reviewing Meter Options](https://www.m3ter.com/docs/guides/setting-up-usage-data-meters-and-aggregations/reviewing-meter-options).
        """
        from .resources.meters import MetersResource

        return MetersResource(self)

    @cached_property
    def notification_configurations(self) -> NotificationConfigurationsResource:
        """This section provides endpoints for managing Event Notifications.

        You can create Notifications based on system Events generated by the platform. When you base a Notification on a specific Event type, you can include a calculation that references the fields available on that Event type to define precise conditions that must be met for the Notification to be triggered when an Event of that type occurs. In this way, you can set up highly customized Notifications that act as timely alerts to inform you about significant occurrences within your Organization. For instance, if you provide a sign-up bonus to new end-customer Accounts, you can set up a Notification to alert you when an end-customer Account has used up a certain percentage of their bonus credit.

        You can also set up Notifications based on Scheduled Event types you've created for your Organization. See the [ScheduledEventConfigurations](https://www.m3ter.com/docs/api#tag/ScheduledEventConfigurations) section of this API Reference and [Working with Scheduled Events](https://www.m3ter.com/docs/guides/alerts-events-and-notifications/utilizing-events-and-notifications/working-with-scheduled-events) in our user documentation.

        For more details on Event types and their fields, see the [Events](https://www.m3ter.com/docs/api#tag/Events) section.

        For detailed guidance on working with Events and Notifications, refer to the [Utilizing Events and Notifications](https://www.m3ter.com/docs/guides/utilizing-events-and-notifications) section of the m3ter user documentation.
        """
        from .resources.notification_configurations import NotificationConfigurationsResource

        return NotificationConfigurationsResource(self)

    @cached_property
    def organization_config(self) -> OrganizationConfigResource:
        """Endpoints for retrieving or updating the Organization Config.

        Organization represents your company as a direct customer of m3ter. Use Organization configuration to define *Organization-wide* settings. For example:
        - Timezone.
        - Currencies and currency conversions.
        - Billing operations settings, such as:
                - Epoch dates to control first billing dates.
                - Whether to bill customer accounts in advance/in arrears for standing charge amounts, minimum spend amounts, and commitment fees.

        For other aspects of your Organization setup and configuration, see the following sections in this API Reference:
        * [Custom Fields](https://www.m3ter.com/docs/api#tag/CustomField)
        * [Currencies](https://www.m3ter.com/docs/api#tag/Currency)
        * [Credit Reasons](https://www.m3ter.com/docs/api#tag/CreditReason)
        * [Debit Reason](https://www.m3ter.com/docs/api#tag/DebitReason)
        * [Transaction Types](https://www.m3ter.com/docs/api#tag/TransactionType)

        See also:
        - [Managing your Organization](https://www.m3ter.com/docs/guides/managing-organization-and-users/viewing-and-editing-organization).
        """
        from .resources.organization_config import OrganizationConfigResource

        return OrganizationConfigResource(self)

    @cached_property
    def permission_policies(self) -> PermissionPoliciesResource:
        """
        Endpoints for Permission Policy related operations such as creation, update, add and retrieve.

        Permission Policies can restrict or grant access to specific resources for both Users *(people)* and Service Users *(automated processes with direct API access)*. This enables you to control precisely what a User can do in your m3ter Organization.

        For more details, see [Understanding, Creating, and Managing Permission Policies](https://www.m3ter.com/docs/guides/organization-and-access-management/creating-and-managing-permissions#permission-policy-statements---available-actions-and-resources) in our main Documentation.
        """
        from .resources.permission_policies import PermissionPoliciesResource

        return PermissionPoliciesResource(self)

    @cached_property
    def plans(self) -> PlansResource:
        """Endpoints for listing, creating, updating, retrieving, or deleting Plans.

        A Plan is based on a PlanTemplate and represents a specific pricing plan for one of your products or services. Each Plan inherits general billing attributes or pricing structure from its parent Plan Template. Some attributes can be overriden for the specific Plan.

        When you've created the Plan Templates and Plans you need for your Products, you can configure the exact pricing structures for Plans to charge customers that consume one or more of your Products.

        You can then attach the appropriately priced Plans to customer Accounts to create [Account Plans](https://www.m3ter.com/docs/api#tag/AccountPlan) and enable charges to be calculated correctly for billing against those Accounts.

        See also:
        - [Reviewing Options for Plans and Plan Templates](https://www.m3ter.com/docs/guides/working-with-plan-templates-and-plans/reviewing-configuration-options-for-plans-and-plan-templates).
        """
        from .resources.plans import PlansResource

        return PlansResource(self)

    @cached_property
    def plan_groups(self) -> PlanGroupsResource:
        """
        Endpoints for PlanGroup related operations such as creation, update, retrieve, list and delete.

        PlanGroups are constructs that group multiple plans together. This enables a unified approach to efficiently handle various uses cases across different plans. For example applying a minimum spend amount at billing, across several of your products or features that are each priced separately.
        """
        from .resources.plan_groups import PlanGroupsResource

        return PlanGroupsResource(self)

    @cached_property
    def plan_group_links(self) -> PlanGroupLinksResource:
        """
        Endpoints for PlanGroupLink related operations such as creation, update, list and delete.

        PlanGroupLinks are the intersection table between a PlanGroup and its associated Plans. A PlanGroupLink is only created when at least 1 Plan is linked to a PlanGroup.
        """
        from .resources.plan_group_links import PlanGroupLinksResource

        return PlanGroupLinksResource(self)

    @cached_property
    def plan_templates(self) -> PlanTemplatesResource:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting PlanTemplates.

        Use PlanTemplates to define default values for Plans. These default values control the billing operations you want applied to your products. PlanTemplates avoid repetition in configuration work - many Plans will share settings for billing operations and differ only in the details of their pricing structures.

        A PlanTemplate is linked to a Product, and each Plan is a child of a PlanTemplate.
        """
        from .resources.plan_templates import PlanTemplatesResource

        return PlanTemplatesResource(self)

    @cached_property
    def pricings(self) -> PricingsResource:
        """Endpoints for listing, creating, updating, retrieving, or deleting Pricing.

        Create the Pricing for a Plan/PlanTemplate with usage data Aggregations, and define a usage-based pricing structure for charging end customer Accounts put on the Plan.

        See [Reviewing Pricing Options for Plans and Plan Templates](https://www.m3ter.com/docs/guides/pricing-plans/reviewing-pricing-options-and-pricing-plans) for more information.
        """
        from .resources.pricings import PricingsResource

        return PricingsResource(self)

    @cached_property
    def products(self) -> ProductsResource:
        """Endpoints for listing, creating, updating, retrieving, or deleting Products.

        A Product represents the products and services you offer to your end customers. Products act as a container for the Meters, Aggregations, Pricing, and Plans required to implement usage-based and other pricing models for your Organization.
        """
        from .resources.products import ProductsResource

        return ProductsResource(self)

    @cached_property
    def resource_groups(self) -> ResourceGroupsResource:
        """
        Endpoints for ResourceGroup related operations such as creation, update, list and delete.

        ResourceGroups are used in the context of Permission Policies, which controls what a User who has been given access to your Organization can and cannot do. For example, you might want to create a Permissions Policy that denies Users the ability to retrieve Meters.

        Resources are defined as m3ter Resource Identifiers *(MRIs)* in the format:

        ```
        service: resource - type / item - type / id
        ```

        Where:

        * service is a distinct part of the overall m3ter system, and which forms a natural functional grouping, such as "config" or "billing".

        * resource-type is the resource type item accessed - for example: "Plan", "Meter", "Bill"

        * item-type is one of:

                * "item" - to specify an individual item.

                * "group" - to specify a resource group.

        * id is the resource group id or the resource item id

        Resources can be assigned to one or more ResourceGroups. For example, a Plan can be assigned to Plan ResourceGroups, a Meter can be assigned to Meter ResourceGroups, and so on. This is useful for cases where you want to create Permission Policies which allow or deny access to a specific subset of resources. For example, grant a user access to only some of the Plans in your Organization.

        This concept of grouping resources applies to every resource in m3ter, including ResourceGroups themselves. This allows you to nest ResourceGroups to support hierarchies of groups.

        See [Understanding, Creating, and Managing Permission Policies](https://www.m3ter.com/docs/guides/managing-organization-and-users/creating-and-managing-permissions) in the m3ter documentation for more information.

        **Note: User Resource Groups** You can create a User Resource Group to group resources of type = `user`. You can then retrieve a list of the User Resource Groups a user belongs to. For more details, see the [Retrieve OrgUser Groups](https://www.m3ter.com/docs/api#tag/OrgUsers/operation/GetOrgUserGroups) call in the OrgUsers section.
        """
        from .resources.resource_groups import ResourceGroupsResource

        return ResourceGroupsResource(self)

    @cached_property
    def scheduled_event_configurations(self) -> ScheduledEventConfigurationsResource:
        """Endpoints for retrieving and managing scheduled Events' configurations.

        Scheduled Event Configurations define custom Event types that reference Date/Time fields belonging to configuration and billing entities. They therefore provide you with an extra degree of flexibility over and above system-generated Events for setting up Notifications based on Events.

        For more details, see the [Working with Scheduled Events](https://www.m3ter.com/docs/guides/alerts-events-and-notifications/utilizing-events-and-notifications/working-with-scheduled-events) in our Documenation.
        """
        from .resources.scheduled_event_configurations import ScheduledEventConfigurationsResource

        return ScheduledEventConfigurationsResource(self)

    @cached_property
    def statements(self) -> StatementsResource:
        """
        Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills.

        Bills are generated for an Account, and are calculated in accordance with the usage-based pricing Plans applied for the Products the Account consumes. These endpoints enable interaction with the billing system, allowing you to obtain billing details and insights into the consumption patterns and charges of your end-customer Accounts.
        """
        from .resources.statements import StatementsResource

        return StatementsResource(self)

    @cached_property
    def transaction_types(self) -> TransactionTypesResource:
        """
        Endpoints for TransactionType operations such as creation, update, list, retrieve, and delete.

        You can create TransactionTypes for your Organization, which can then be used when creating and updating Balances. Example TransactionTypes: "Balance Amount" or "Add Funds".

        For details on creating a Transaction amount for a Balance using a TransactionType you've created for your Organization, see the [Create Balance Transaction](https://www.m3ter.com/docs/api#tag/Balances/operation/PostBalanceTransaction) call in the [Balances](https://www.m3ter.com/docs/api#tag/Balances) section of this API Reference.
        """
        from .resources.transaction_types import TransactionTypesResource

        return TransactionTypesResource(self)

    @cached_property
    def usage(self) -> UsageResource:
        from .resources.usage import UsageResource

        return UsageResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        """
        A suite of endpoints for configuring and managing third party integrations within the m3ter platform. The integration endpoints in this section facilitate various operations such as creating, updating, listing, and deletion of integrations.

        m3ter integrations enable seamless data synchronization and mapping with external systems required in core business processes. These processes often include sales, pricing, billing and invoicing, and general finance.

        With m3ter integrations, you can establish robust connections with popular business platforms, enhancing your operational capabilities. For example:
        * Chargebee
        * Salesforce
        * Stripe
        * Netsuite
        * Paddle
        * Xero
        * QuickBooks
        """
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> M3terWithRawResponse:
        return M3terWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> M3terWithStreamedResponse:
        return M3terWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        token = self.token
        if token is None:
            return {}
        return {"Authorization": f"Bearer {token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.token or headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    @override
    def _prepare_options(
        self,
        options: FinalRequestOptions,  # noqa: ARG002
    ) -> FinalRequestOptions:
        token_valid: bool = self.token is not None and (self.token_expiry is None or self.token_expiry > datetime.now())
        if not options.url.endswith("/oauth/token"):
            if not token_valid:
                auth: str = base64.b64encode(f"{self.api_key}:{self.api_secret}".encode("utf8")).decode("utf8")
                token: AuthenticationGetBearerTokenResponse = self.authentication.get_bearer_token(
                    grant_type="client_credentials", extra_headers={"Authorization": f"Basic {auth}"}
                )
                self.token = token.access_token
                # expiry minus 5 minutes from effective refreshing
                self.token_expiry = datetime.fromtimestamp(token.expires_in - 300)
        return options

    def copy(
        self,
        *,
        api_key: str | None = None,
        api_secret: str | None = None,
        token: str | None = None,
        token_expiry: datetime | None = None,
        org_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        client = self.__class__(
            api_key=api_key or self.api_key,
            api_secret=api_secret or self.api_secret,
            token=token or self.token,
            token_expiry=token_expiry or self.token_expiry,
            org_id=org_id or self.org_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def _get_org_id_path_param(self) -> str:
        return self.org_id

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncM3ter(AsyncAPIClient):
    # client options
    api_key: str
    api_secret: str
    token: str | None
    org_id: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        api_secret: str | None = None,
        token: str | None = None,
        org_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncM3ter client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `M3TER_API_KEY`
        - `api_secret` from `M3TER_API_SECRET`
        - `token` from `M3TER_API_TOKEN`
        - `org_id` from `M3TER_ORG_ID`
        """
        if api_key is None:
            api_key = os.environ.get("M3TER_API_KEY")
        if api_key is None:
            raise M3terError(
                "The api_key client option must be set either by passing api_key to the client or by setting the M3TER_API_KEY environment variable"
            )
        self.api_key = api_key

        if api_secret is None:
            api_secret = os.environ.get("M3TER_API_SECRET")
        if api_secret is None:
            raise M3terError(
                "The api_secret client option must be set either by passing api_secret to the client or by setting the M3TER_API_SECRET environment variable"
            )
        self.api_secret = api_secret

        if token is None:
            token = os.environ.get("M3TER_API_TOKEN")
        self.token = token

        if org_id is None:
            org_id = os.environ.get("M3TER_ORG_ID")
        if org_id is None:
            raise M3terError(
                "The org_id client option must be set either by passing org_id to the client or by setting the M3TER_ORG_ID environment variable"
            )
        self.org_id = org_id

        if base_url is None:
            base_url = os.environ.get("M3TER_BASE_URL")
        self._base_url_overridden = base_url is not None
        if base_url is None:
            base_url = f"https://api.m3ter.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def authentication(self) -> AsyncAuthenticationResource:
        """
        Endpoint for retrieving a JSON Web Token (JWT) bearer token for a ServiceUser using the Client Credentials Grant flow.

        A ServiceUser represents the automated process you want to grant access to your Organization - that is, as an API user.
        """
        from .resources.authentication import AsyncAuthenticationResource

        return AsyncAuthenticationResource(self)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """
        Endpoints for Account related operations such as creation, update, list and delete.
        An Account represents one of your end-customer accounts.

        Accounts do not belong to a Product to allow for cases where an end customer takes more than one of your Products, and the charges for these Products differ.

        You typically attach a priced Plan or Plan Template to an Account before you can generate bills for the Account:
        - If a customer consumes several of your Products, you can attach a priced Plan or Plan Template to the Account for charging against each Product.
        - If an Account is charged solely on the basis of an agreed Prepayment/Commitment amount but not all of the Prepayment is prepaid, you can use a customized billing schedule for outstanding fees without having to attach a Plan to the Account to generate Bills.

        You can create Child Accounts for end customers who hold multiple Accounts with you. You can then set up billing for the Parent/Child Account usage to have the end-customer billed once for the Parent Account, instead of having separate bills issued for usage against each of their multiple Accounts.

        **IMPORTANT! - use of PII:** The use of any of your end-customers' Personally Identifiable Information (PII) in m3ter is restricted to a few fields on the **Account** entity. Please ensure that only the ``name``, ``address``, or ``emailAddress`` fields contain any end-customer PII data on any Accounts you create. See the [Introduction section](https://www.m3ter.com/docs/api#section/Introduction) above for more details.
        """
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def account_plans(self) -> AsyncAccountPlansResource:
        """
        Endpoints for AccountPlan and AccountPlanGroup related operations such as creation, update, list and delete.

        **AccountPlans**
        An Account represents one of your end-customer accounts. To create an AccountPlan, you attach a Product Plan to an Account. The AccountPlan then determines the charges incurred at billing by your end customer for consuming the Product the Plan is for:
        * **AccountPlan Active/Inactive**. Set start and end dates to define the period the AccountPlan is active for the Account.
        * **AccountPlan per Product**. If an end customer consumes multiple Products, create separate AccountPlans to charge for each Product.

        **AccountPlan Constraints:**
        * Only one AccountPlan per Product can be active at any one time for an Account.
        * If you create a Plan as a custom Plan for a specific Account, you can only use it to create an AccountPlan for that Account.

        **AccountPlanGroups**
        Plan Groups are used when you want to apply a minimum spend amount at billing across several of your Products each of which are priced separately - when you create the Plan Group, you define an overall minimum spend and then add any priced Plans you want to include in the Group. To create an AccounPlanGroup, you can attach a Plan Group to an Account that consumes the separate Products which are priced using the included Plans. At billing, the minimum spend you've defined for the Plan Group is applied:
        * **Active AccountPlanGroup**. Set the start and end dates to define the period for which the Plan Group will be active for the Account.

        **Plan Group Notes:**
        * You can only add *one Plan for the same Product* to a Plan Group. See the [Plan Group](https://www.m3ter.com/docs/api#tag/PlanGroup) in this API Reference for more details on creating Plan Groups.
        * You can create a *custom Plan Group* for an Account, which means the Plan Group can only be attached to that Account to create an AccountPlanGroup.

        **AcountPlanGroup - Notes and Constraints:**
        * **AccountPlanGroup is type of AccountPlan** When you attach a Plan Group to an Account, this creates an AccountPlanGroup. However, the m3ter data model *does not support a separate AccountPlanGroup entity*, and an AccountPlanGroup is a type of AccountPlan where a `planGroupId` is used instead of a `planId` when it's created. See the [Create AccountPlan](https://www.m3ter.com/docs/api#tag/AccountPlan/operation/PostAccountPlan) call in this section and [Attaching Plan Groups to an Account](https://www.m3ter.com/docs/guides/end-customer-accounts/attaching-plan-groups-to-an-account) in our main User Documentation.
        * **Multiple AccountPlan Groups:** You can attach more than one Plan Group to an Account to create multiple AccountPlanGroups, but the rule that *only one attached Plan per Product can be active at any one time for an Account* is preserved:
                * Multiple attached Plan Groups on an Account can have overlapping dates only if none of the Plan Groups contain a Plan belonging to the same Product. If you try to attach a Plan Group to an Account with Plan Groups already attached and:
                        * The new Plan Group contains a Product Plan that also belongs to a Plan Group already attached to the Account.
                        * The dates for these "matched Plan" Plan Groups being active for the Account would overlap.
                        * Then you'll receive an error and the attachment will be blocked.
        """
        from .resources.account_plans import AsyncAccountPlansResource

        return AsyncAccountPlansResource(self)

    @cached_property
    def aggregations(self) -> AsyncAggregationsResource:
        """Endpoints for listing, creating, updating, retrieving, or deleting Aggregations.

        An Aggregation links to a Meter and targets a Data Field or Derived Field on the Meter. You define the method of aggregation used to convert the usage data collected by the targeted Meter field into a numerical unit of measurement.

        You can then use the unit of measurement an Aggregation yields as a metric for pricing Product Plans and apply usage-based pricing to your products and services. You might also want to aggregate raw data measures for other purposes, such as to feed into analytical or business performance tools.

        **Notes:**
        * **Contrast with Compound Aggregations**. Standard or simple Aggregations of this type, which apply an aggregation method directly to Meter usage data fields, are contrasted with [Compound Aggregations](https://www.m3ter.com/docs/api#tag/CompoundAggregation). A Compound Aggregation typically references one or more simple Aggregations and applies a calculation to them to derive pricing metrics needed to serve more complex usage-based pricing scenarios.
        * **Segmented Aggregations**. Segmented Aggregations allow you to segment the usage data collected by a single Meter. This capability is very useful for implementing some pricing and billing use cases. See [Segmented Aggregations](https://www.m3ter.com/docs/guides/usage-data-aggregations/segmented-aggregations) in our main documentation for more details.
        """
        from .resources.aggregations import AsyncAggregationsResource

        return AsyncAggregationsResource(self)

    @cached_property
    def balances(self) -> AsyncBalancesResource:
        """Endpoints for creating/retrieving/updating/deleting Balances on Accounts.

        When you have created a Balance for an Account, you can create a positive or negative Transaction amounts for the Balance. To do this, you must first define Transaction Types for your Organization, and then use one of these Transaction Types when you add a specific Transaction to a Balance - see the [Create TransactionType](https://www.m3ter.com/docs/api#tag/TransactionType/operation/CreateTransactionType) call in the Transaction Type section in this API Reference for more details.

        Balances are typically used when a customer prepays an amount to add a credit to their Account, which can then be draw-down against charges due for product or service consumption. You can include options to top-up the original Balance.

        Examples of how Balances for end customer Accounts can be used:

        * Onboarding Balance/Free Trials. Offering an onboarding incentive to new customers as an initial free credit Balance on their Account.

        * Balance as initial commitment. Add a Balance amount to a new customer Account. This acts as an initial commitment, which allows them to use the service and gain an accurate insight into their usage level.

        * Managing Customer Satisfaction. Use Balance as credits that will be applied to subsequent Bills as compensation for acknowledged service delivery issues.

        * Facilitating Balance Adjustments:
                * Apply negative amounts to immediately write-off outstanding Balances.

        #### What is the difference between Balances and Commitments/Prepayments?

        To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

        Commitments - also referred to as Prepayments - are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the commitment or prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

        In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

        You can use Commitments/Prepayments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Commitment credit on an Account is drawn-down - Balance amounts first or Commitment/Prepayment amounts first.
        """
        from .resources.balances import AsyncBalancesResource

        return AsyncBalancesResource(self)

    @cached_property
    def bills(self) -> AsyncBillsResource:
        """
        Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills.

        Bills are generated for an Account, and are calculated in accordance with the usage-based pricing Plans applied for the Products the Account consumes. These endpoints enable interaction with the billing system, allowing you to obtain billing details and insights into the consumption patterns and charges of your end-customer Accounts.
        """
        from .resources.bills import AsyncBillsResource

        return AsyncBillsResource(self)

    @cached_property
    def bill_config(self) -> AsyncBillConfigResource:
        """Endpoints for updating and retreiving the Bill Configuration for an Organization.

        The Organization represents your company as a direct customer of the m3ter service.

        You can use the **Update BillConfig** endpoint to set a global lock date for **all** Bills - any Bill with a service period end date on or before the set date will be locked and cannot be updated.

        **Warning: Ensure all Bills are Approved!** If you try to set a global lock date when there remains Bills in a *Pending* state whose service period end date is on or before the specified lock date, then you'll receive an error.
        """
        from .resources.bill_config import AsyncBillConfigResource

        return AsyncBillConfigResource(self)

    @cached_property
    def commitments(self) -> AsyncCommitmentsResource:
        """
        Endpoints that manage Commitments *(also known as Prepayments)* in the context of usage-based pricing and billing. A Commitment represents an agreement where the end-customer has agreed to pay a fixed minimum amount throughout the contract period. ***The commitment amount is payable regardless of the actual usage by the customer of your service or product.***

        These endpoints enable the creation, updating, retrieval, and deletion of Commitments. Use them to manage your customer's Commitments and ensure optimal revenue recognition:
        * Specify which type of charges can draw-down against a Commitment amount on an Account at billing: usage, minimum spend, standing charges, or recurring charges.
        * Define overage surcharge percentages, which are applied when the usage charges exceed the agreed Commitment amount within the contract duration.

        #### What is the difference between Balances and Commitments/Prepayments?

        To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

        Commitments/Prepayments are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

        In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

        You can use Prepayments/Commitments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Prepayment credit on an Account is drawn-down - Balance amounts first or Prepayment amounts first.

        #### Billing for Commitments

        If not all of an agreed Commitment amount is paid at the start of an end-customer contract period, you can choose one of two options for billing the outstanding fees due on the customer Account:
        - Select a Product *Plan to bill with*.
        - Define a *schedule of billing dates*.
        """
        from .resources.commitments import AsyncCommitmentsResource

        return AsyncCommitmentsResource(self)

    @cached_property
    def bill_jobs(self) -> AsyncBillJobsResource:
        """Endpoints for creating, retrieving, listing, and cancelling Bill Jobs.

        Bill Jobs are critical components in billing management, providing asynchronous mechanisms to calculate and handle bills.

        Bill Jobs give you the flexibiity to run Bills manually for Accounts to suit different billing management purposes. For example, some historical usage data has come in for an Account and you want to run a Bill for a specific date on that Account to check that the Bill is showing correctly for the charges due on the new usage data.
        """
        from .resources.bill_jobs import AsyncBillJobsResource

        return AsyncBillJobsResource(self)

    @cached_property
    def charges(self) -> AsyncChargesResource:
        """Endpoints for creating/updating/deleting Charges.

        Create Charges for your end-customer Accounts to create ad-hoc line items for Account billing. Charges are:
        * Created for either debit or credit amounts.
        * Linked to a Product for accounting purposes.
        * Optionally linked to a Contract.
        * Given a specific date for billing. When a bill job has run for the specified Charge bill date, a Charge appears as an Ad-hoc line item on the Bill.
        * Assigned a service period.
        * Available in any currency defined for your Organization.
        See [Creating Charges for Accounts](https://www.m3ter.com/docs/guides/end-customer-accounts/creating-charges-for-accounts) in our main user documentation for more details.

        Alternatively, you can create a Charge for a Balance on an end-customer Account to create balance fee line items for Account billing. See [Creating Charges for Balances](https://www.m3ter.com/docs/guides/end-customer-accounts/creating-balances-for-accounts/creating-charges-for-balances) in our main user documentation for more details.
        """
        from .resources.charges import AsyncChargesResource

        return AsyncChargesResource(self)

    @cached_property
    def compound_aggregations(self) -> AsyncCompoundAggregationsResource:
        """
        Endpoints for Compound Aggregation related operations such as creation, update, list and delete.

        Use Compound Aggregations to create numerical measures from usage data by applying a calculation to one or more simple Aggregations or Custom Fields. These numerical measures can then be used as pricing metrics to price your Product Plans, enabling you to implement a wide range of usage-based pricing use cases.

        You can create two types of Compound Aggregation:

        **Global**
        - Pricing: Not tied to any specific product and can be used to price Plans belonging to any Product.
        - Calculation: can reference all simple Aggregations - both Global simple Aggregations and any product-specific simple Aggregations.

        **Product-specific**
        - Pricing: belong to a specific Product and can only be used to price Plans belonging to the same Product.
        - Calculation: can reference any simple Aggregations belonging to the same Product and any Global simple Aggregations.

        **IMPORTANT!** If a simple Aggregation referenced by a Compound Aggregation has a **Quantity per unit** defined or a **Rounding** defined, these will not be factored into the value used by the calculation. For example, if the simple Aggregation referenced has a base value of 100 and has **Quantity per unit** set at 10, the Compound Aggregation calculation *will use the base value of 100 not 10*.

        To better understand and use Compound Aggregations, refer to the example [Compound Aggregation Use Case](https://www.m3ter.com/docs/guides/setting-up-usage-data-meters-and-aggregations/compound-aggregations#example-use-case) in the m3ter documentation.
        """
        from .resources.compound_aggregations import AsyncCompoundAggregationsResource

        return AsyncCompoundAggregationsResource(self)

    @cached_property
    def contracts(self) -> AsyncContractsResource:
        """
        Endpoints for Contract related operations such as creation, update, list and delete.

        Contracts are created for Accounts, which are your end-user customers. Contracts can be used for:
        * **Accounts Reporting**. To serve your general accounting operations and processes, you can report on total Contract values for an Account.
        * **Contract Billing**. Various billing entities associated with an Account can  be linked to Contracts on the Account to meet your specific Contract billing use cases.
        """
        from .resources.contracts import AsyncContractsResource

        return AsyncContractsResource(self)

    @cached_property
    def counters(self) -> AsyncCountersResource:
        """Endpoints for listing, creating, retrieving, updating, or deleting Counters.

        You can create Counters for your m3ter Organization, which can then be used as pricing metrics to apply a unit-based [CounterPricing](https://www.m3ter.com/docs/api#tag/CounterPricing) to Product Plans or Plan Templates for recurring subscription charges on Accounts.

        Counters can then be used to post [CounterAdjustments](https://www.m3ter.com/docs/api#tag/CounterAdjustments) on your end-customer Accounts.

        Accounts are then billed in accordance with the CounterPricing on Plans attached to the Accounts and for the actual Counter quantities Accounts subscribe to. See [Recurring Charges: Counters](https://www.m3ter.com/docs/guides/recurring-charges-counters) in our main user documentation for more details.
        """
        from .resources.counters import AsyncCountersResource

        return AsyncCountersResource(self)

    @cached_property
    def counter_adjustments(self) -> AsyncCounterAdjustmentsResource:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting CounterAdjustments.

        If you attach a Plan to an Account which is priced using a Counter to apply unit-based pricing, you can then create CounterAdjustments for the Account using that Counter to ensure the Account is billed according to the number of Counter units the Account subscribes to in a given billing period.

        See [Understanding and Creating Counter Adjustments for Accounts](https://www.m3ter.com/docs/guides/recurring-charges-counters/creating-counter-adjustments-for-accounts) for more information.
        """
        from .resources.counter_adjustments import AsyncCounterAdjustmentsResource

        return AsyncCounterAdjustmentsResource(self)

    @cached_property
    def counter_pricings(self) -> AsyncCounterPricingsResource:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting CounterPricing.

        Create the CounterPricing for a Plan/PlanTemplate using a Counter, and define a unit-based pricing structure for charging end customer Accounts put on the Plan.

        See [Creating Counters and Pricing Plans](https://www.m3ter.com/docs/guides/recurring-charges-counters/creating-counters) for more information.
        """
        from .resources.counter_pricings import AsyncCounterPricingsResource

        return AsyncCounterPricingsResource(self)

    @cached_property
    def credit_reasons(self) -> AsyncCreditReasonsResource:
        """Endpoints for CreditReason operations such as creation, update, list, and delete.

        You can create CreditReasons for your Organization, and then use them when creating a credit line item on a bill, or applying a product credit to a bill. CreditReasons provide contextual information as to why a credit was applied.
        """
        from .resources.credit_reasons import AsyncCreditReasonsResource

        return AsyncCreditReasonsResource(self)

    @cached_property
    def currencies(self) -> AsyncCurrenciesResource:
        """Endpoints for Currency operations such as creation, update, list, and delete.

        Currencies are stored for your Organization, and can then be used to specify currencies on various entities such as plan groups and plan templates.

        **IMPORTANT!**
        The Currencies you want to use in your Organization must be created first.

        The currency you select for your Organization determines the billing currency and overrides any currency settings in your pricing Plans.
        For example, if the Organization currency is set to USD and a pricing Plan used for an Account is set to GBP, the bill for an Account using that Plan is calculated in GBP, and then each bill line item converted to USD amounts.

        Currency conversion rates are setup in the *OrganizationConfig*. For more details, see [Creating and Managing Currencies](https://www.m3ter.com/docs/guides/organization-and-access-management/viewing-and-editing-organization#creating-and-managing-currencies) in the m3ter Documentation.
        """
        from .resources.currencies import AsyncCurrenciesResource

        return AsyncCurrenciesResource(self)

    @cached_property
    def custom_fields(self) -> AsyncCustomFieldsResource:
        """
        Endpoints for retrieving and updating Custom Fields at the Organization level for all entities that support them.

        Custom Fields in m3ter allow you to store custom data in the form of number or string values against m3ter entities in a way that does not directly affect the normal working operation of the m3ter platform. Having this capability to store data in a free-hand fashion can prove very useful in helping you to meet specific usage-based pricing and other operational business use cases.

        However, you can exploit the values stored on Custom Fields in a more direct way by referencing them in Derived Field and Compound Aggregation calculations. Given the key role these calculations can play when implementing usage-based pricing schema, any Custom Fields you reference will then affect how the platform behaves. Referencing Custom Field values in your calculations offers a much wider scope of options when it comes to resolving complex usage-based pricing use cases.

        Custom Fields can be added to the following entities at Organizational level:
        * Organization
        * Account
        * AccountPlan
        * Aggregation
        * Compound Aggregation
        * Meter
        * Product
        * Plan
        * PlanTemplate
        * Contract

        These all follow the same pattern - a new *(optional)* field is available on the entity request and response bodies called "customFields" which is a object in this format:
        ```
        "customFields": {
                        "exampleCustomField1": 7.1,
                        "exampleCustomField2": "stringValue"
        }
        ```
        The value for a Custom Field can be a string or a number.

        **Using Custom Field values in calculations:**
        - You can add Custom Fields at two levels - the Organization level and the individual entity level.
        - The Organizational level field provides a default value and *must be added* if you want to also add a Custom Field of the same name at the corresponding individual entity level. If you reference the Custom Field in a calculation, the value for the individual entity level field is used. If no field is defined at individual entity level, then the Organization level field value is used.

        **Important: Constraints and Exceptions!**

        **Custom Fields at Organization Level**. Currently, you cannot create Custom Fields at the Organization-level for the following enitites:
        * Plan Group
        * Balance
        * Balance Transaction Schedule
        * Balance Charge Schedule

        Therefore you cannot reference the Custom Fields values created at the individual entity level for these entities in your Derived Field or Compound Aggregation calculations.

        **Derived Field Calculations**. You can *only reference Custom Fields* for the following entities:
        * Organization
        * Meter
        * Account

        However, if you are using Meters belonging to *a specific Product*, that is, not *Global Meters*, you can also reference Custom Fields added to a Product in Derived Field calculations.

        **Compound Aggregation Calculations - Meter Custom Fields**. The value of the *Organization level Meter Custom Field will always be used*, even if you have defined a corresponding field at the individual Meter level.

        See [Working with Custom Fields](https://www.m3ter.com/docs/guides/creating-and-managing-products/working-with-custom-fields) in the m3ter documentation for more information.
        """
        from .resources.custom_fields import AsyncCustomFieldsResource

        return AsyncCustomFieldsResource(self)

    @cached_property
    def data_exports(self) -> AsyncDataExportsResource:
        """Endpoints for triggering one-off, ad-hoc Data Exports.

        You can set up and run ad-hoc Exports to export two kinds of data from your m3ter Organization:
        * Usage data.
        * Operational data for entities.

        **Ad-Hoc Export Destinations** When setting up and running an ad-hoc Export:
        * You can define one or more Export Destinations - see the [ExportDestination](https://www.m3ter.com/docs/api#tag/ExportDestination) section of this API Reference. When the export runs, the data is sent through to the sepecified Destination. However, the export file is also made available for you to download it locally.
        * You can set up and run Data Exports without defining a Destination. The data is not exported but the compiled export file is made available for downloading locally.
        * For details on downloading an export file, see the [Get Data Export File Download URL](https://www.m3ter.com/docs/api#tag/ExportDestination/operation/GenerateDataExportFileDownloadUrl) endpoint in this API Reference.

        **Preview Version!** The Data Export feature is currently available only in Preview release version. See [Feature Release Stages](https://www.m3ter.com/docs/guides/getting-started/feature-release-stages) for Preview release definition. ExportAdHoc endpoints will only be available if Data Export has been enabled for your Organization. For more details see [Data Export(Preview)](https://www.m3ter.com/docs/guides/data-exports) in our main User documentation. If you're interested in previewing the Data Export feature, please get in touch with m3ter Support or your m3ter contact.
        """
        from .resources.data_exports import AsyncDataExportsResource

        return AsyncDataExportsResource(self)

    @cached_property
    def debit_reasons(self) -> AsyncDebitReasonsResource:
        """Endpoints for DebitReason operations such as creation, update, list, and delete.

        You can create DebitReasons for your Organization, and then use them when creating a debit line item on a bill, or applying a product debit to a bill. DebitReasons provide contextual information as to why a debit was applied.
        """
        from .resources.debit_reasons import AsyncDebitReasonsResource

        return AsyncDebitReasonsResource(self)

    @cached_property
    def events(self) -> AsyncEventsResource:
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
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

    @cached_property
    def external_mappings(self) -> AsyncExternalMappingsResource:
        """
        Endpoints for managing External Mapping related operations such as creation, update, list and delete.

        When you integrate your 3rd-party systems with the m3ter platform, a mapping between entities in the local system *(m3ter)* and external systems is constructed. This *External Mapping* is crucial in scenarios where data from external systems is consumed or where data from the local system is to be synchronized with external systems.

        When you are working to set up your Integrations and want to test or troubleshoot your implementation before going live, you might need to create External Mappings manually and, at a later date, edit or delete them.
        """
        from .resources.external_mappings import AsyncExternalMappingsResource

        return AsyncExternalMappingsResource(self)

    @cached_property
    def integration_configurations(self) -> AsyncIntegrationConfigurationsResource:
        """
        A suite of endpoints for configuring and managing third party integrations within the m3ter platform. The integration endpoints in this section facilitate various operations such as creating, updating, listing, and deletion of integrations.

        m3ter integrations enable seamless data synchronization and mapping with external systems required in core business processes. These processes often include sales, pricing, billing and invoicing, and general finance.

        With m3ter integrations, you can establish robust connections with popular business platforms, enhancing your operational capabilities. For example:
        * Chargebee
        * Salesforce
        * Stripe
        * Netsuite
        * Paddle
        * Xero
        * QuickBooks
        """
        from .resources.integration_configurations import AsyncIntegrationConfigurationsResource

        return AsyncIntegrationConfigurationsResource(self)

    @cached_property
    def lookup_tables(self) -> AsyncLookupTablesResource:
        """Endpoints for creating/updating/deleting Lookup Tables.

        Lookup Tables enable you to manage dynamic data mappings that your calculations reference. Use them for currency conversion, pricing tiers, discount rates, and similar scenarios where you require values to change operationally but for calculation logic to remain constant.

        **Beta Version!** The Lookup Table feature is currently available in Beta release version. See [Feature Release Stages](https://www.m3ter.com/docs/guides/getting-started/feature-release-stages) for Beta release definition. Lookup Table endpoints will only be available if Lookup Tables have been enabled for your Organization. For more details see [Lookup Tables (Beta)](https://www.m3ter.com/docs/guides/lookup-tables) in our main User documentation.
        """
        from .resources.lookup_tables import AsyncLookupTablesResource

        return AsyncLookupTablesResource(self)

    @cached_property
    def meters(self) -> AsyncMetersResource:
        """Endpoints for listing, creating, updating, retrieving, or deleting Meters.

        Use Meters to submit usage data for the consumption of your products and services by end customers. This usage data then becomes the basis for setting up usage-based pricing for your products and services.

        Examples of usage data collected in Meters:
        * Number of logins.
        * Duration of session.
        * Amount of data downloaded.

        To collect usage data and ingest it into the platform, you can define two types of fields for Meters:
        - `dataFields` Used to collect raw usage data measures - numeric quantitative data values or non-numeric point data values.
        - `derivedFields` Used to derive usage data measures that are the result of applying a calculation to `dataFields`, `customFields`, or system `Timestamp` fields.

        You can also:
        - Create `customFields` for a Meter, which allows you to attach custom data to the Meter as name/value pairs.
        - Create Global Meters, which are not tied to a specific Product and allow you to collect usage data that will form the basis of usage-based pricing across multiple Products.

        **IMPORTANT! - use of PII:** The use of any of your end-customers' Personally Identifiable Information (PII) in m3ter is restricted to a few fields on the **Account** entity. Please ensure that any fields you configure for Meters, such as Data Fields or Derived Fields, do not contain any end-customer PII data. See the [Introduction section](https://www.m3ter.com/docs/api#section/Introduction) above for more details.

        See also:
        - [Reviewing Meter Options](https://www.m3ter.com/docs/guides/setting-up-usage-data-meters-and-aggregations/reviewing-meter-options).
        """
        from .resources.meters import AsyncMetersResource

        return AsyncMetersResource(self)

    @cached_property
    def notification_configurations(self) -> AsyncNotificationConfigurationsResource:
        """This section provides endpoints for managing Event Notifications.

        You can create Notifications based on system Events generated by the platform. When you base a Notification on a specific Event type, you can include a calculation that references the fields available on that Event type to define precise conditions that must be met for the Notification to be triggered when an Event of that type occurs. In this way, you can set up highly customized Notifications that act as timely alerts to inform you about significant occurrences within your Organization. For instance, if you provide a sign-up bonus to new end-customer Accounts, you can set up a Notification to alert you when an end-customer Account has used up a certain percentage of their bonus credit.

        You can also set up Notifications based on Scheduled Event types you've created for your Organization. See the [ScheduledEventConfigurations](https://www.m3ter.com/docs/api#tag/ScheduledEventConfigurations) section of this API Reference and [Working with Scheduled Events](https://www.m3ter.com/docs/guides/alerts-events-and-notifications/utilizing-events-and-notifications/working-with-scheduled-events) in our user documentation.

        For more details on Event types and their fields, see the [Events](https://www.m3ter.com/docs/api#tag/Events) section.

        For detailed guidance on working with Events and Notifications, refer to the [Utilizing Events and Notifications](https://www.m3ter.com/docs/guides/utilizing-events-and-notifications) section of the m3ter user documentation.
        """
        from .resources.notification_configurations import AsyncNotificationConfigurationsResource

        return AsyncNotificationConfigurationsResource(self)

    @cached_property
    def organization_config(self) -> AsyncOrganizationConfigResource:
        """Endpoints for retrieving or updating the Organization Config.

        Organization represents your company as a direct customer of m3ter. Use Organization configuration to define *Organization-wide* settings. For example:
        - Timezone.
        - Currencies and currency conversions.
        - Billing operations settings, such as:
                - Epoch dates to control first billing dates.
                - Whether to bill customer accounts in advance/in arrears for standing charge amounts, minimum spend amounts, and commitment fees.

        For other aspects of your Organization setup and configuration, see the following sections in this API Reference:
        * [Custom Fields](https://www.m3ter.com/docs/api#tag/CustomField)
        * [Currencies](https://www.m3ter.com/docs/api#tag/Currency)
        * [Credit Reasons](https://www.m3ter.com/docs/api#tag/CreditReason)
        * [Debit Reason](https://www.m3ter.com/docs/api#tag/DebitReason)
        * [Transaction Types](https://www.m3ter.com/docs/api#tag/TransactionType)

        See also:
        - [Managing your Organization](https://www.m3ter.com/docs/guides/managing-organization-and-users/viewing-and-editing-organization).
        """
        from .resources.organization_config import AsyncOrganizationConfigResource

        return AsyncOrganizationConfigResource(self)

    @cached_property
    def permission_policies(self) -> AsyncPermissionPoliciesResource:
        """
        Endpoints for Permission Policy related operations such as creation, update, add and retrieve.

        Permission Policies can restrict or grant access to specific resources for both Users *(people)* and Service Users *(automated processes with direct API access)*. This enables you to control precisely what a User can do in your m3ter Organization.

        For more details, see [Understanding, Creating, and Managing Permission Policies](https://www.m3ter.com/docs/guides/organization-and-access-management/creating-and-managing-permissions#permission-policy-statements---available-actions-and-resources) in our main Documentation.
        """
        from .resources.permission_policies import AsyncPermissionPoliciesResource

        return AsyncPermissionPoliciesResource(self)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        """Endpoints for listing, creating, updating, retrieving, or deleting Plans.

        A Plan is based on a PlanTemplate and represents a specific pricing plan for one of your products or services. Each Plan inherits general billing attributes or pricing structure from its parent Plan Template. Some attributes can be overriden for the specific Plan.

        When you've created the Plan Templates and Plans you need for your Products, you can configure the exact pricing structures for Plans to charge customers that consume one or more of your Products.

        You can then attach the appropriately priced Plans to customer Accounts to create [Account Plans](https://www.m3ter.com/docs/api#tag/AccountPlan) and enable charges to be calculated correctly for billing against those Accounts.

        See also:
        - [Reviewing Options for Plans and Plan Templates](https://www.m3ter.com/docs/guides/working-with-plan-templates-and-plans/reviewing-configuration-options-for-plans-and-plan-templates).
        """
        from .resources.plans import AsyncPlansResource

        return AsyncPlansResource(self)

    @cached_property
    def plan_groups(self) -> AsyncPlanGroupsResource:
        """
        Endpoints for PlanGroup related operations such as creation, update, retrieve, list and delete.

        PlanGroups are constructs that group multiple plans together. This enables a unified approach to efficiently handle various uses cases across different plans. For example applying a minimum spend amount at billing, across several of your products or features that are each priced separately.
        """
        from .resources.plan_groups import AsyncPlanGroupsResource

        return AsyncPlanGroupsResource(self)

    @cached_property
    def plan_group_links(self) -> AsyncPlanGroupLinksResource:
        """
        Endpoints for PlanGroupLink related operations such as creation, update, list and delete.

        PlanGroupLinks are the intersection table between a PlanGroup and its associated Plans. A PlanGroupLink is only created when at least 1 Plan is linked to a PlanGroup.
        """
        from .resources.plan_group_links import AsyncPlanGroupLinksResource

        return AsyncPlanGroupLinksResource(self)

    @cached_property
    def plan_templates(self) -> AsyncPlanTemplatesResource:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting PlanTemplates.

        Use PlanTemplates to define default values for Plans. These default values control the billing operations you want applied to your products. PlanTemplates avoid repetition in configuration work - many Plans will share settings for billing operations and differ only in the details of their pricing structures.

        A PlanTemplate is linked to a Product, and each Plan is a child of a PlanTemplate.
        """
        from .resources.plan_templates import AsyncPlanTemplatesResource

        return AsyncPlanTemplatesResource(self)

    @cached_property
    def pricings(self) -> AsyncPricingsResource:
        """Endpoints for listing, creating, updating, retrieving, or deleting Pricing.

        Create the Pricing for a Plan/PlanTemplate with usage data Aggregations, and define a usage-based pricing structure for charging end customer Accounts put on the Plan.

        See [Reviewing Pricing Options for Plans and Plan Templates](https://www.m3ter.com/docs/guides/pricing-plans/reviewing-pricing-options-and-pricing-plans) for more information.
        """
        from .resources.pricings import AsyncPricingsResource

        return AsyncPricingsResource(self)

    @cached_property
    def products(self) -> AsyncProductsResource:
        """Endpoints for listing, creating, updating, retrieving, or deleting Products.

        A Product represents the products and services you offer to your end customers. Products act as a container for the Meters, Aggregations, Pricing, and Plans required to implement usage-based and other pricing models for your Organization.
        """
        from .resources.products import AsyncProductsResource

        return AsyncProductsResource(self)

    @cached_property
    def resource_groups(self) -> AsyncResourceGroupsResource:
        """
        Endpoints for ResourceGroup related operations such as creation, update, list and delete.

        ResourceGroups are used in the context of Permission Policies, which controls what a User who has been given access to your Organization can and cannot do. For example, you might want to create a Permissions Policy that denies Users the ability to retrieve Meters.

        Resources are defined as m3ter Resource Identifiers *(MRIs)* in the format:

        ```
        service: resource - type / item - type / id
        ```

        Where:

        * service is a distinct part of the overall m3ter system, and which forms a natural functional grouping, such as "config" or "billing".

        * resource-type is the resource type item accessed - for example: "Plan", "Meter", "Bill"

        * item-type is one of:

                * "item" - to specify an individual item.

                * "group" - to specify a resource group.

        * id is the resource group id or the resource item id

        Resources can be assigned to one or more ResourceGroups. For example, a Plan can be assigned to Plan ResourceGroups, a Meter can be assigned to Meter ResourceGroups, and so on. This is useful for cases where you want to create Permission Policies which allow or deny access to a specific subset of resources. For example, grant a user access to only some of the Plans in your Organization.

        This concept of grouping resources applies to every resource in m3ter, including ResourceGroups themselves. This allows you to nest ResourceGroups to support hierarchies of groups.

        See [Understanding, Creating, and Managing Permission Policies](https://www.m3ter.com/docs/guides/managing-organization-and-users/creating-and-managing-permissions) in the m3ter documentation for more information.

        **Note: User Resource Groups** You can create a User Resource Group to group resources of type = `user`. You can then retrieve a list of the User Resource Groups a user belongs to. For more details, see the [Retrieve OrgUser Groups](https://www.m3ter.com/docs/api#tag/OrgUsers/operation/GetOrgUserGroups) call in the OrgUsers section.
        """
        from .resources.resource_groups import AsyncResourceGroupsResource

        return AsyncResourceGroupsResource(self)

    @cached_property
    def scheduled_event_configurations(self) -> AsyncScheduledEventConfigurationsResource:
        """Endpoints for retrieving and managing scheduled Events' configurations.

        Scheduled Event Configurations define custom Event types that reference Date/Time fields belonging to configuration and billing entities. They therefore provide you with an extra degree of flexibility over and above system-generated Events for setting up Notifications based on Events.

        For more details, see the [Working with Scheduled Events](https://www.m3ter.com/docs/guides/alerts-events-and-notifications/utilizing-events-and-notifications/working-with-scheduled-events) in our Documenation.
        """
        from .resources.scheduled_event_configurations import AsyncScheduledEventConfigurationsResource

        return AsyncScheduledEventConfigurationsResource(self)

    @cached_property
    def statements(self) -> AsyncStatementsResource:
        """
        Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills.

        Bills are generated for an Account, and are calculated in accordance with the usage-based pricing Plans applied for the Products the Account consumes. These endpoints enable interaction with the billing system, allowing you to obtain billing details and insights into the consumption patterns and charges of your end-customer Accounts.
        """
        from .resources.statements import AsyncStatementsResource

        return AsyncStatementsResource(self)

    @cached_property
    def transaction_types(self) -> AsyncTransactionTypesResource:
        """
        Endpoints for TransactionType operations such as creation, update, list, retrieve, and delete.

        You can create TransactionTypes for your Organization, which can then be used when creating and updating Balances. Example TransactionTypes: "Balance Amount" or "Add Funds".

        For details on creating a Transaction amount for a Balance using a TransactionType you've created for your Organization, see the [Create Balance Transaction](https://www.m3ter.com/docs/api#tag/Balances/operation/PostBalanceTransaction) call in the [Balances](https://www.m3ter.com/docs/api#tag/Balances) section of this API Reference.
        """
        from .resources.transaction_types import AsyncTransactionTypesResource

        return AsyncTransactionTypesResource(self)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        from .resources.usage import AsyncUsageResource

        return AsyncUsageResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        """
        A suite of endpoints for configuring and managing third party integrations within the m3ter platform. The integration endpoints in this section facilitate various operations such as creating, updating, listing, and deletion of integrations.

        m3ter integrations enable seamless data synchronization and mapping with external systems required in core business processes. These processes often include sales, pricing, billing and invoicing, and general finance.

        With m3ter integrations, you can establish robust connections with popular business platforms, enhancing your operational capabilities. For example:
        * Chargebee
        * Salesforce
        * Stripe
        * Netsuite
        * Paddle
        * Xero
        * QuickBooks
        """
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncM3terWithRawResponse:
        return AsyncM3terWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncM3terWithStreamedResponse:
        return AsyncM3terWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        token = self.token
        if token is None:
            return {}
        return {"Authorization": f"Bearer {token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the token to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        api_secret: str | None = None,
        token: str | None = None,
        org_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        client = self.__class__(
            api_key=api_key or self.api_key,
            api_secret=api_secret or self.api_secret,
            token=token or self.token,
            org_id=org_id or self.org_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def _get_org_id_path_param(self) -> str:
        return self.org_id

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class M3terWithRawResponse:
    _client: M3ter

    def __init__(self, client: M3ter) -> None:
        self._client = client

    @cached_property
    def authentication(self) -> authentication.AuthenticationResourceWithRawResponse:
        """
        Endpoint for retrieving a JSON Web Token (JWT) bearer token for a ServiceUser using the Client Credentials Grant flow.

        A ServiceUser represents the automated process you want to grant access to your Organization - that is, as an API user.
        """
        from .resources.authentication import AuthenticationResourceWithRawResponse

        return AuthenticationResourceWithRawResponse(self._client.authentication)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        """
        Endpoints for Account related operations such as creation, update, list and delete.
        An Account represents one of your end-customer accounts.

        Accounts do not belong to a Product to allow for cases where an end customer takes more than one of your Products, and the charges for these Products differ.

        You typically attach a priced Plan or Plan Template to an Account before you can generate bills for the Account:
        - If a customer consumes several of your Products, you can attach a priced Plan or Plan Template to the Account for charging against each Product.
        - If an Account is charged solely on the basis of an agreed Prepayment/Commitment amount but not all of the Prepayment is prepaid, you can use a customized billing schedule for outstanding fees without having to attach a Plan to the Account to generate Bills.

        You can create Child Accounts for end customers who hold multiple Accounts with you. You can then set up billing for the Parent/Child Account usage to have the end-customer billed once for the Parent Account, instead of having separate bills issued for usage against each of their multiple Accounts.

        **IMPORTANT! - use of PII:** The use of any of your end-customers' Personally Identifiable Information (PII) in m3ter is restricted to a few fields on the **Account** entity. Please ensure that only the ``name``, ``address``, or ``emailAddress`` fields contain any end-customer PII data on any Accounts you create. See the [Introduction section](https://www.m3ter.com/docs/api#section/Introduction) above for more details.
        """
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def account_plans(self) -> account_plans.AccountPlansResourceWithRawResponse:
        """
        Endpoints for AccountPlan and AccountPlanGroup related operations such as creation, update, list and delete.

        **AccountPlans**
        An Account represents one of your end-customer accounts. To create an AccountPlan, you attach a Product Plan to an Account. The AccountPlan then determines the charges incurred at billing by your end customer for consuming the Product the Plan is for:
        * **AccountPlan Active/Inactive**. Set start and end dates to define the period the AccountPlan is active for the Account.
        * **AccountPlan per Product**. If an end customer consumes multiple Products, create separate AccountPlans to charge for each Product.

        **AccountPlan Constraints:**
        * Only one AccountPlan per Product can be active at any one time for an Account.
        * If you create a Plan as a custom Plan for a specific Account, you can only use it to create an AccountPlan for that Account.

        **AccountPlanGroups**
        Plan Groups are used when you want to apply a minimum spend amount at billing across several of your Products each of which are priced separately - when you create the Plan Group, you define an overall minimum spend and then add any priced Plans you want to include in the Group. To create an AccounPlanGroup, you can attach a Plan Group to an Account that consumes the separate Products which are priced using the included Plans. At billing, the minimum spend you've defined for the Plan Group is applied:
        * **Active AccountPlanGroup**. Set the start and end dates to define the period for which the Plan Group will be active for the Account.

        **Plan Group Notes:**
        * You can only add *one Plan for the same Product* to a Plan Group. See the [Plan Group](https://www.m3ter.com/docs/api#tag/PlanGroup) in this API Reference for more details on creating Plan Groups.
        * You can create a *custom Plan Group* for an Account, which means the Plan Group can only be attached to that Account to create an AccountPlanGroup.

        **AcountPlanGroup - Notes and Constraints:**
        * **AccountPlanGroup is type of AccountPlan** When you attach a Plan Group to an Account, this creates an AccountPlanGroup. However, the m3ter data model *does not support a separate AccountPlanGroup entity*, and an AccountPlanGroup is a type of AccountPlan where a `planGroupId` is used instead of a `planId` when it's created. See the [Create AccountPlan](https://www.m3ter.com/docs/api#tag/AccountPlan/operation/PostAccountPlan) call in this section and [Attaching Plan Groups to an Account](https://www.m3ter.com/docs/guides/end-customer-accounts/attaching-plan-groups-to-an-account) in our main User Documentation.
        * **Multiple AccountPlan Groups:** You can attach more than one Plan Group to an Account to create multiple AccountPlanGroups, but the rule that *only one attached Plan per Product can be active at any one time for an Account* is preserved:
                * Multiple attached Plan Groups on an Account can have overlapping dates only if none of the Plan Groups contain a Plan belonging to the same Product. If you try to attach a Plan Group to an Account with Plan Groups already attached and:
                        * The new Plan Group contains a Product Plan that also belongs to a Plan Group already attached to the Account.
                        * The dates for these "matched Plan" Plan Groups being active for the Account would overlap.
                        * Then you'll receive an error and the attachment will be blocked.
        """
        from .resources.account_plans import AccountPlansResourceWithRawResponse

        return AccountPlansResourceWithRawResponse(self._client.account_plans)

    @cached_property
    def aggregations(self) -> aggregations.AggregationsResourceWithRawResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Aggregations.

        An Aggregation links to a Meter and targets a Data Field or Derived Field on the Meter. You define the method of aggregation used to convert the usage data collected by the targeted Meter field into a numerical unit of measurement.

        You can then use the unit of measurement an Aggregation yields as a metric for pricing Product Plans and apply usage-based pricing to your products and services. You might also want to aggregate raw data measures for other purposes, such as to feed into analytical or business performance tools.

        **Notes:**
        * **Contrast with Compound Aggregations**. Standard or simple Aggregations of this type, which apply an aggregation method directly to Meter usage data fields, are contrasted with [Compound Aggregations](https://www.m3ter.com/docs/api#tag/CompoundAggregation). A Compound Aggregation typically references one or more simple Aggregations and applies a calculation to them to derive pricing metrics needed to serve more complex usage-based pricing scenarios.
        * **Segmented Aggregations**. Segmented Aggregations allow you to segment the usage data collected by a single Meter. This capability is very useful for implementing some pricing and billing use cases. See [Segmented Aggregations](https://www.m3ter.com/docs/guides/usage-data-aggregations/segmented-aggregations) in our main documentation for more details.
        """
        from .resources.aggregations import AggregationsResourceWithRawResponse

        return AggregationsResourceWithRawResponse(self._client.aggregations)

    @cached_property
    def balances(self) -> balances.BalancesResourceWithRawResponse:
        """Endpoints for creating/retrieving/updating/deleting Balances on Accounts.

        When you have created a Balance for an Account, you can create a positive or negative Transaction amounts for the Balance. To do this, you must first define Transaction Types for your Organization, and then use one of these Transaction Types when you add a specific Transaction to a Balance - see the [Create TransactionType](https://www.m3ter.com/docs/api#tag/TransactionType/operation/CreateTransactionType) call in the Transaction Type section in this API Reference for more details.

        Balances are typically used when a customer prepays an amount to add a credit to their Account, which can then be draw-down against charges due for product or service consumption. You can include options to top-up the original Balance.

        Examples of how Balances for end customer Accounts can be used:

        * Onboarding Balance/Free Trials. Offering an onboarding incentive to new customers as an initial free credit Balance on their Account.

        * Balance as initial commitment. Add a Balance amount to a new customer Account. This acts as an initial commitment, which allows them to use the service and gain an accurate insight into their usage level.

        * Managing Customer Satisfaction. Use Balance as credits that will be applied to subsequent Bills as compensation for acknowledged service delivery issues.

        * Facilitating Balance Adjustments:
                * Apply negative amounts to immediately write-off outstanding Balances.

        #### What is the difference between Balances and Commitments/Prepayments?

        To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

        Commitments - also referred to as Prepayments - are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the commitment or prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

        In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

        You can use Commitments/Prepayments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Commitment credit on an Account is drawn-down - Balance amounts first or Commitment/Prepayment amounts first.
        """
        from .resources.balances import BalancesResourceWithRawResponse

        return BalancesResourceWithRawResponse(self._client.balances)

    @cached_property
    def bills(self) -> bills.BillsResourceWithRawResponse:
        """
        Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills.

        Bills are generated for an Account, and are calculated in accordance with the usage-based pricing Plans applied for the Products the Account consumes. These endpoints enable interaction with the billing system, allowing you to obtain billing details and insights into the consumption patterns and charges of your end-customer Accounts.
        """
        from .resources.bills import BillsResourceWithRawResponse

        return BillsResourceWithRawResponse(self._client.bills)

    @cached_property
    def bill_config(self) -> bill_config.BillConfigResourceWithRawResponse:
        """Endpoints for updating and retreiving the Bill Configuration for an Organization.

        The Organization represents your company as a direct customer of the m3ter service.

        You can use the **Update BillConfig** endpoint to set a global lock date for **all** Bills - any Bill with a service period end date on or before the set date will be locked and cannot be updated.

        **Warning: Ensure all Bills are Approved!** If you try to set a global lock date when there remains Bills in a *Pending* state whose service period end date is on or before the specified lock date, then you'll receive an error.
        """
        from .resources.bill_config import BillConfigResourceWithRawResponse

        return BillConfigResourceWithRawResponse(self._client.bill_config)

    @cached_property
    def commitments(self) -> commitments.CommitmentsResourceWithRawResponse:
        """
        Endpoints that manage Commitments *(also known as Prepayments)* in the context of usage-based pricing and billing. A Commitment represents an agreement where the end-customer has agreed to pay a fixed minimum amount throughout the contract period. ***The commitment amount is payable regardless of the actual usage by the customer of your service or product.***

        These endpoints enable the creation, updating, retrieval, and deletion of Commitments. Use them to manage your customer's Commitments and ensure optimal revenue recognition:
        * Specify which type of charges can draw-down against a Commitment amount on an Account at billing: usage, minimum spend, standing charges, or recurring charges.
        * Define overage surcharge percentages, which are applied when the usage charges exceed the agreed Commitment amount within the contract duration.

        #### What is the difference between Balances and Commitments/Prepayments?

        To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

        Commitments/Prepayments are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

        In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

        You can use Prepayments/Commitments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Prepayment credit on an Account is drawn-down - Balance amounts first or Prepayment amounts first.

        #### Billing for Commitments

        If not all of an agreed Commitment amount is paid at the start of an end-customer contract period, you can choose one of two options for billing the outstanding fees due on the customer Account:
        - Select a Product *Plan to bill with*.
        - Define a *schedule of billing dates*.
        """
        from .resources.commitments import CommitmentsResourceWithRawResponse

        return CommitmentsResourceWithRawResponse(self._client.commitments)

    @cached_property
    def bill_jobs(self) -> bill_jobs.BillJobsResourceWithRawResponse:
        """Endpoints for creating, retrieving, listing, and cancelling Bill Jobs.

        Bill Jobs are critical components in billing management, providing asynchronous mechanisms to calculate and handle bills.

        Bill Jobs give you the flexibiity to run Bills manually for Accounts to suit different billing management purposes. For example, some historical usage data has come in for an Account and you want to run a Bill for a specific date on that Account to check that the Bill is showing correctly for the charges due on the new usage data.
        """
        from .resources.bill_jobs import BillJobsResourceWithRawResponse

        return BillJobsResourceWithRawResponse(self._client.bill_jobs)

    @cached_property
    def charges(self) -> charges.ChargesResourceWithRawResponse:
        """Endpoints for creating/updating/deleting Charges.

        Create Charges for your end-customer Accounts to create ad-hoc line items for Account billing. Charges are:
        * Created for either debit or credit amounts.
        * Linked to a Product for accounting purposes.
        * Optionally linked to a Contract.
        * Given a specific date for billing. When a bill job has run for the specified Charge bill date, a Charge appears as an Ad-hoc line item on the Bill.
        * Assigned a service period.
        * Available in any currency defined for your Organization.
        See [Creating Charges for Accounts](https://www.m3ter.com/docs/guides/end-customer-accounts/creating-charges-for-accounts) in our main user documentation for more details.

        Alternatively, you can create a Charge for a Balance on an end-customer Account to create balance fee line items for Account billing. See [Creating Charges for Balances](https://www.m3ter.com/docs/guides/end-customer-accounts/creating-balances-for-accounts/creating-charges-for-balances) in our main user documentation for more details.
        """
        from .resources.charges import ChargesResourceWithRawResponse

        return ChargesResourceWithRawResponse(self._client.charges)

    @cached_property
    def compound_aggregations(self) -> compound_aggregations.CompoundAggregationsResourceWithRawResponse:
        """
        Endpoints for Compound Aggregation related operations such as creation, update, list and delete.

        Use Compound Aggregations to create numerical measures from usage data by applying a calculation to one or more simple Aggregations or Custom Fields. These numerical measures can then be used as pricing metrics to price your Product Plans, enabling you to implement a wide range of usage-based pricing use cases.

        You can create two types of Compound Aggregation:

        **Global**
        - Pricing: Not tied to any specific product and can be used to price Plans belonging to any Product.
        - Calculation: can reference all simple Aggregations - both Global simple Aggregations and any product-specific simple Aggregations.

        **Product-specific**
        - Pricing: belong to a specific Product and can only be used to price Plans belonging to the same Product.
        - Calculation: can reference any simple Aggregations belonging to the same Product and any Global simple Aggregations.

        **IMPORTANT!** If a simple Aggregation referenced by a Compound Aggregation has a **Quantity per unit** defined or a **Rounding** defined, these will not be factored into the value used by the calculation. For example, if the simple Aggregation referenced has a base value of 100 and has **Quantity per unit** set at 10, the Compound Aggregation calculation *will use the base value of 100 not 10*.

        To better understand and use Compound Aggregations, refer to the example [Compound Aggregation Use Case](https://www.m3ter.com/docs/guides/setting-up-usage-data-meters-and-aggregations/compound-aggregations#example-use-case) in the m3ter documentation.
        """
        from .resources.compound_aggregations import CompoundAggregationsResourceWithRawResponse

        return CompoundAggregationsResourceWithRawResponse(self._client.compound_aggregations)

    @cached_property
    def contracts(self) -> contracts.ContractsResourceWithRawResponse:
        """
        Endpoints for Contract related operations such as creation, update, list and delete.

        Contracts are created for Accounts, which are your end-user customers. Contracts can be used for:
        * **Accounts Reporting**. To serve your general accounting operations and processes, you can report on total Contract values for an Account.
        * **Contract Billing**. Various billing entities associated with an Account can  be linked to Contracts on the Account to meet your specific Contract billing use cases.
        """
        from .resources.contracts import ContractsResourceWithRawResponse

        return ContractsResourceWithRawResponse(self._client.contracts)

    @cached_property
    def counters(self) -> counters.CountersResourceWithRawResponse:
        """Endpoints for listing, creating, retrieving, updating, or deleting Counters.

        You can create Counters for your m3ter Organization, which can then be used as pricing metrics to apply a unit-based [CounterPricing](https://www.m3ter.com/docs/api#tag/CounterPricing) to Product Plans or Plan Templates for recurring subscription charges on Accounts.

        Counters can then be used to post [CounterAdjustments](https://www.m3ter.com/docs/api#tag/CounterAdjustments) on your end-customer Accounts.

        Accounts are then billed in accordance with the CounterPricing on Plans attached to the Accounts and for the actual Counter quantities Accounts subscribe to. See [Recurring Charges: Counters](https://www.m3ter.com/docs/guides/recurring-charges-counters) in our main user documentation for more details.
        """
        from .resources.counters import CountersResourceWithRawResponse

        return CountersResourceWithRawResponse(self._client.counters)

    @cached_property
    def counter_adjustments(self) -> counter_adjustments.CounterAdjustmentsResourceWithRawResponse:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting CounterAdjustments.

        If you attach a Plan to an Account which is priced using a Counter to apply unit-based pricing, you can then create CounterAdjustments for the Account using that Counter to ensure the Account is billed according to the number of Counter units the Account subscribes to in a given billing period.

        See [Understanding and Creating Counter Adjustments for Accounts](https://www.m3ter.com/docs/guides/recurring-charges-counters/creating-counter-adjustments-for-accounts) for more information.
        """
        from .resources.counter_adjustments import CounterAdjustmentsResourceWithRawResponse

        return CounterAdjustmentsResourceWithRawResponse(self._client.counter_adjustments)

    @cached_property
    def counter_pricings(self) -> counter_pricings.CounterPricingsResourceWithRawResponse:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting CounterPricing.

        Create the CounterPricing for a Plan/PlanTemplate using a Counter, and define a unit-based pricing structure for charging end customer Accounts put on the Plan.

        See [Creating Counters and Pricing Plans](https://www.m3ter.com/docs/guides/recurring-charges-counters/creating-counters) for more information.
        """
        from .resources.counter_pricings import CounterPricingsResourceWithRawResponse

        return CounterPricingsResourceWithRawResponse(self._client.counter_pricings)

    @cached_property
    def credit_reasons(self) -> credit_reasons.CreditReasonsResourceWithRawResponse:
        """Endpoints for CreditReason operations such as creation, update, list, and delete.

        You can create CreditReasons for your Organization, and then use them when creating a credit line item on a bill, or applying a product credit to a bill. CreditReasons provide contextual information as to why a credit was applied.
        """
        from .resources.credit_reasons import CreditReasonsResourceWithRawResponse

        return CreditReasonsResourceWithRawResponse(self._client.credit_reasons)

    @cached_property
    def currencies(self) -> currencies.CurrenciesResourceWithRawResponse:
        """Endpoints for Currency operations such as creation, update, list, and delete.

        Currencies are stored for your Organization, and can then be used to specify currencies on various entities such as plan groups and plan templates.

        **IMPORTANT!**
        The Currencies you want to use in your Organization must be created first.

        The currency you select for your Organization determines the billing currency and overrides any currency settings in your pricing Plans.
        For example, if the Organization currency is set to USD and a pricing Plan used for an Account is set to GBP, the bill for an Account using that Plan is calculated in GBP, and then each bill line item converted to USD amounts.

        Currency conversion rates are setup in the *OrganizationConfig*. For more details, see [Creating and Managing Currencies](https://www.m3ter.com/docs/guides/organization-and-access-management/viewing-and-editing-organization#creating-and-managing-currencies) in the m3ter Documentation.
        """
        from .resources.currencies import CurrenciesResourceWithRawResponse

        return CurrenciesResourceWithRawResponse(self._client.currencies)

    @cached_property
    def custom_fields(self) -> custom_fields.CustomFieldsResourceWithRawResponse:
        """
        Endpoints for retrieving and updating Custom Fields at the Organization level for all entities that support them.

        Custom Fields in m3ter allow you to store custom data in the form of number or string values against m3ter entities in a way that does not directly affect the normal working operation of the m3ter platform. Having this capability to store data in a free-hand fashion can prove very useful in helping you to meet specific usage-based pricing and other operational business use cases.

        However, you can exploit the values stored on Custom Fields in a more direct way by referencing them in Derived Field and Compound Aggregation calculations. Given the key role these calculations can play when implementing usage-based pricing schema, any Custom Fields you reference will then affect how the platform behaves. Referencing Custom Field values in your calculations offers a much wider scope of options when it comes to resolving complex usage-based pricing use cases.

        Custom Fields can be added to the following entities at Organizational level:
        * Organization
        * Account
        * AccountPlan
        * Aggregation
        * Compound Aggregation
        * Meter
        * Product
        * Plan
        * PlanTemplate
        * Contract

        These all follow the same pattern - a new *(optional)* field is available on the entity request and response bodies called "customFields" which is a object in this format:
        ```
        "customFields": {
                        "exampleCustomField1": 7.1,
                        "exampleCustomField2": "stringValue"
        }
        ```
        The value for a Custom Field can be a string or a number.

        **Using Custom Field values in calculations:**
        - You can add Custom Fields at two levels - the Organization level and the individual entity level.
        - The Organizational level field provides a default value and *must be added* if you want to also add a Custom Field of the same name at the corresponding individual entity level. If you reference the Custom Field in a calculation, the value for the individual entity level field is used. If no field is defined at individual entity level, then the Organization level field value is used.

        **Important: Constraints and Exceptions!**

        **Custom Fields at Organization Level**. Currently, you cannot create Custom Fields at the Organization-level for the following enitites:
        * Plan Group
        * Balance
        * Balance Transaction Schedule
        * Balance Charge Schedule

        Therefore you cannot reference the Custom Fields values created at the individual entity level for these entities in your Derived Field or Compound Aggregation calculations.

        **Derived Field Calculations**. You can *only reference Custom Fields* for the following entities:
        * Organization
        * Meter
        * Account

        However, if you are using Meters belonging to *a specific Product*, that is, not *Global Meters*, you can also reference Custom Fields added to a Product in Derived Field calculations.

        **Compound Aggregation Calculations - Meter Custom Fields**. The value of the *Organization level Meter Custom Field will always be used*, even if you have defined a corresponding field at the individual Meter level.

        See [Working with Custom Fields](https://www.m3ter.com/docs/guides/creating-and-managing-products/working-with-custom-fields) in the m3ter documentation for more information.
        """
        from .resources.custom_fields import CustomFieldsResourceWithRawResponse

        return CustomFieldsResourceWithRawResponse(self._client.custom_fields)

    @cached_property
    def data_exports(self) -> data_exports.DataExportsResourceWithRawResponse:
        """Endpoints for triggering one-off, ad-hoc Data Exports.

        You can set up and run ad-hoc Exports to export two kinds of data from your m3ter Organization:
        * Usage data.
        * Operational data for entities.

        **Ad-Hoc Export Destinations** When setting up and running an ad-hoc Export:
        * You can define one or more Export Destinations - see the [ExportDestination](https://www.m3ter.com/docs/api#tag/ExportDestination) section of this API Reference. When the export runs, the data is sent through to the sepecified Destination. However, the export file is also made available for you to download it locally.
        * You can set up and run Data Exports without defining a Destination. The data is not exported but the compiled export file is made available for downloading locally.
        * For details on downloading an export file, see the [Get Data Export File Download URL](https://www.m3ter.com/docs/api#tag/ExportDestination/operation/GenerateDataExportFileDownloadUrl) endpoint in this API Reference.

        **Preview Version!** The Data Export feature is currently available only in Preview release version. See [Feature Release Stages](https://www.m3ter.com/docs/guides/getting-started/feature-release-stages) for Preview release definition. ExportAdHoc endpoints will only be available if Data Export has been enabled for your Organization. For more details see [Data Export(Preview)](https://www.m3ter.com/docs/guides/data-exports) in our main User documentation. If you're interested in previewing the Data Export feature, please get in touch with m3ter Support or your m3ter contact.
        """
        from .resources.data_exports import DataExportsResourceWithRawResponse

        return DataExportsResourceWithRawResponse(self._client.data_exports)

    @cached_property
    def debit_reasons(self) -> debit_reasons.DebitReasonsResourceWithRawResponse:
        """Endpoints for DebitReason operations such as creation, update, list, and delete.

        You can create DebitReasons for your Organization, and then use them when creating a debit line item on a bill, or applying a product debit to a bill. DebitReasons provide contextual information as to why a debit was applied.
        """
        from .resources.debit_reasons import DebitReasonsResourceWithRawResponse

        return DebitReasonsResourceWithRawResponse(self._client.debit_reasons)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
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
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def external_mappings(self) -> external_mappings.ExternalMappingsResourceWithRawResponse:
        """
        Endpoints for managing External Mapping related operations such as creation, update, list and delete.

        When you integrate your 3rd-party systems with the m3ter platform, a mapping between entities in the local system *(m3ter)* and external systems is constructed. This *External Mapping* is crucial in scenarios where data from external systems is consumed or where data from the local system is to be synchronized with external systems.

        When you are working to set up your Integrations and want to test or troubleshoot your implementation before going live, you might need to create External Mappings manually and, at a later date, edit or delete them.
        """
        from .resources.external_mappings import ExternalMappingsResourceWithRawResponse

        return ExternalMappingsResourceWithRawResponse(self._client.external_mappings)

    @cached_property
    def integration_configurations(self) -> integration_configurations.IntegrationConfigurationsResourceWithRawResponse:
        """
        A suite of endpoints for configuring and managing third party integrations within the m3ter platform. The integration endpoints in this section facilitate various operations such as creating, updating, listing, and deletion of integrations.

        m3ter integrations enable seamless data synchronization and mapping with external systems required in core business processes. These processes often include sales, pricing, billing and invoicing, and general finance.

        With m3ter integrations, you can establish robust connections with popular business platforms, enhancing your operational capabilities. For example:
        * Chargebee
        * Salesforce
        * Stripe
        * Netsuite
        * Paddle
        * Xero
        * QuickBooks
        """
        from .resources.integration_configurations import IntegrationConfigurationsResourceWithRawResponse

        return IntegrationConfigurationsResourceWithRawResponse(self._client.integration_configurations)

    @cached_property
    def lookup_tables(self) -> lookup_tables.LookupTablesResourceWithRawResponse:
        """Endpoints for creating/updating/deleting Lookup Tables.

        Lookup Tables enable you to manage dynamic data mappings that your calculations reference. Use them for currency conversion, pricing tiers, discount rates, and similar scenarios where you require values to change operationally but for calculation logic to remain constant.

        **Beta Version!** The Lookup Table feature is currently available in Beta release version. See [Feature Release Stages](https://www.m3ter.com/docs/guides/getting-started/feature-release-stages) for Beta release definition. Lookup Table endpoints will only be available if Lookup Tables have been enabled for your Organization. For more details see [Lookup Tables (Beta)](https://www.m3ter.com/docs/guides/lookup-tables) in our main User documentation.
        """
        from .resources.lookup_tables import LookupTablesResourceWithRawResponse

        return LookupTablesResourceWithRawResponse(self._client.lookup_tables)

    @cached_property
    def meters(self) -> meters.MetersResourceWithRawResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Meters.

        Use Meters to submit usage data for the consumption of your products and services by end customers. This usage data then becomes the basis for setting up usage-based pricing for your products and services.

        Examples of usage data collected in Meters:
        * Number of logins.
        * Duration of session.
        * Amount of data downloaded.

        To collect usage data and ingest it into the platform, you can define two types of fields for Meters:
        - `dataFields` Used to collect raw usage data measures - numeric quantitative data values or non-numeric point data values.
        - `derivedFields` Used to derive usage data measures that are the result of applying a calculation to `dataFields`, `customFields`, or system `Timestamp` fields.

        You can also:
        - Create `customFields` for a Meter, which allows you to attach custom data to the Meter as name/value pairs.
        - Create Global Meters, which are not tied to a specific Product and allow you to collect usage data that will form the basis of usage-based pricing across multiple Products.

        **IMPORTANT! - use of PII:** The use of any of your end-customers' Personally Identifiable Information (PII) in m3ter is restricted to a few fields on the **Account** entity. Please ensure that any fields you configure for Meters, such as Data Fields or Derived Fields, do not contain any end-customer PII data. See the [Introduction section](https://www.m3ter.com/docs/api#section/Introduction) above for more details.

        See also:
        - [Reviewing Meter Options](https://www.m3ter.com/docs/guides/setting-up-usage-data-meters-and-aggregations/reviewing-meter-options).
        """
        from .resources.meters import MetersResourceWithRawResponse

        return MetersResourceWithRawResponse(self._client.meters)

    @cached_property
    def notification_configurations(
        self,
    ) -> notification_configurations.NotificationConfigurationsResourceWithRawResponse:
        """This section provides endpoints for managing Event Notifications.

        You can create Notifications based on system Events generated by the platform. When you base a Notification on a specific Event type, you can include a calculation that references the fields available on that Event type to define precise conditions that must be met for the Notification to be triggered when an Event of that type occurs. In this way, you can set up highly customized Notifications that act as timely alerts to inform you about significant occurrences within your Organization. For instance, if you provide a sign-up bonus to new end-customer Accounts, you can set up a Notification to alert you when an end-customer Account has used up a certain percentage of their bonus credit.

        You can also set up Notifications based on Scheduled Event types you've created for your Organization. See the [ScheduledEventConfigurations](https://www.m3ter.com/docs/api#tag/ScheduledEventConfigurations) section of this API Reference and [Working with Scheduled Events](https://www.m3ter.com/docs/guides/alerts-events-and-notifications/utilizing-events-and-notifications/working-with-scheduled-events) in our user documentation.

        For more details on Event types and their fields, see the [Events](https://www.m3ter.com/docs/api#tag/Events) section.

        For detailed guidance on working with Events and Notifications, refer to the [Utilizing Events and Notifications](https://www.m3ter.com/docs/guides/utilizing-events-and-notifications) section of the m3ter user documentation.
        """
        from .resources.notification_configurations import NotificationConfigurationsResourceWithRawResponse

        return NotificationConfigurationsResourceWithRawResponse(self._client.notification_configurations)

    @cached_property
    def organization_config(self) -> organization_config.OrganizationConfigResourceWithRawResponse:
        """Endpoints for retrieving or updating the Organization Config.

        Organization represents your company as a direct customer of m3ter. Use Organization configuration to define *Organization-wide* settings. For example:
        - Timezone.
        - Currencies and currency conversions.
        - Billing operations settings, such as:
                - Epoch dates to control first billing dates.
                - Whether to bill customer accounts in advance/in arrears for standing charge amounts, minimum spend amounts, and commitment fees.

        For other aspects of your Organization setup and configuration, see the following sections in this API Reference:
        * [Custom Fields](https://www.m3ter.com/docs/api#tag/CustomField)
        * [Currencies](https://www.m3ter.com/docs/api#tag/Currency)
        * [Credit Reasons](https://www.m3ter.com/docs/api#tag/CreditReason)
        * [Debit Reason](https://www.m3ter.com/docs/api#tag/DebitReason)
        * [Transaction Types](https://www.m3ter.com/docs/api#tag/TransactionType)

        See also:
        - [Managing your Organization](https://www.m3ter.com/docs/guides/managing-organization-and-users/viewing-and-editing-organization).
        """
        from .resources.organization_config import OrganizationConfigResourceWithRawResponse

        return OrganizationConfigResourceWithRawResponse(self._client.organization_config)

    @cached_property
    def permission_policies(self) -> permission_policies.PermissionPoliciesResourceWithRawResponse:
        """
        Endpoints for Permission Policy related operations such as creation, update, add and retrieve.

        Permission Policies can restrict or grant access to specific resources for both Users *(people)* and Service Users *(automated processes with direct API access)*. This enables you to control precisely what a User can do in your m3ter Organization.

        For more details, see [Understanding, Creating, and Managing Permission Policies](https://www.m3ter.com/docs/guides/organization-and-access-management/creating-and-managing-permissions#permission-policy-statements---available-actions-and-resources) in our main Documentation.
        """
        from .resources.permission_policies import PermissionPoliciesResourceWithRawResponse

        return PermissionPoliciesResourceWithRawResponse(self._client.permission_policies)

    @cached_property
    def plans(self) -> plans.PlansResourceWithRawResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Plans.

        A Plan is based on a PlanTemplate and represents a specific pricing plan for one of your products or services. Each Plan inherits general billing attributes or pricing structure from its parent Plan Template. Some attributes can be overriden for the specific Plan.

        When you've created the Plan Templates and Plans you need for your Products, you can configure the exact pricing structures for Plans to charge customers that consume one or more of your Products.

        You can then attach the appropriately priced Plans to customer Accounts to create [Account Plans](https://www.m3ter.com/docs/api#tag/AccountPlan) and enable charges to be calculated correctly for billing against those Accounts.

        See also:
        - [Reviewing Options for Plans and Plan Templates](https://www.m3ter.com/docs/guides/working-with-plan-templates-and-plans/reviewing-configuration-options-for-plans-and-plan-templates).
        """
        from .resources.plans import PlansResourceWithRawResponse

        return PlansResourceWithRawResponse(self._client.plans)

    @cached_property
    def plan_groups(self) -> plan_groups.PlanGroupsResourceWithRawResponse:
        """
        Endpoints for PlanGroup related operations such as creation, update, retrieve, list and delete.

        PlanGroups are constructs that group multiple plans together. This enables a unified approach to efficiently handle various uses cases across different plans. For example applying a minimum spend amount at billing, across several of your products or features that are each priced separately.
        """
        from .resources.plan_groups import PlanGroupsResourceWithRawResponse

        return PlanGroupsResourceWithRawResponse(self._client.plan_groups)

    @cached_property
    def plan_group_links(self) -> plan_group_links.PlanGroupLinksResourceWithRawResponse:
        """
        Endpoints for PlanGroupLink related operations such as creation, update, list and delete.

        PlanGroupLinks are the intersection table between a PlanGroup and its associated Plans. A PlanGroupLink is only created when at least 1 Plan is linked to a PlanGroup.
        """
        from .resources.plan_group_links import PlanGroupLinksResourceWithRawResponse

        return PlanGroupLinksResourceWithRawResponse(self._client.plan_group_links)

    @cached_property
    def plan_templates(self) -> plan_templates.PlanTemplatesResourceWithRawResponse:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting PlanTemplates.

        Use PlanTemplates to define default values for Plans. These default values control the billing operations you want applied to your products. PlanTemplates avoid repetition in configuration work - many Plans will share settings for billing operations and differ only in the details of their pricing structures.

        A PlanTemplate is linked to a Product, and each Plan is a child of a PlanTemplate.
        """
        from .resources.plan_templates import PlanTemplatesResourceWithRawResponse

        return PlanTemplatesResourceWithRawResponse(self._client.plan_templates)

    @cached_property
    def pricings(self) -> pricings.PricingsResourceWithRawResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Pricing.

        Create the Pricing for a Plan/PlanTemplate with usage data Aggregations, and define a usage-based pricing structure for charging end customer Accounts put on the Plan.

        See [Reviewing Pricing Options for Plans and Plan Templates](https://www.m3ter.com/docs/guides/pricing-plans/reviewing-pricing-options-and-pricing-plans) for more information.
        """
        from .resources.pricings import PricingsResourceWithRawResponse

        return PricingsResourceWithRawResponse(self._client.pricings)

    @cached_property
    def products(self) -> products.ProductsResourceWithRawResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Products.

        A Product represents the products and services you offer to your end customers. Products act as a container for the Meters, Aggregations, Pricing, and Plans required to implement usage-based and other pricing models for your Organization.
        """
        from .resources.products import ProductsResourceWithRawResponse

        return ProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def resource_groups(self) -> resource_groups.ResourceGroupsResourceWithRawResponse:
        """
        Endpoints for ResourceGroup related operations such as creation, update, list and delete.

        ResourceGroups are used in the context of Permission Policies, which controls what a User who has been given access to your Organization can and cannot do. For example, you might want to create a Permissions Policy that denies Users the ability to retrieve Meters.

        Resources are defined as m3ter Resource Identifiers *(MRIs)* in the format:

        ```
        service: resource - type / item - type / id
        ```

        Where:

        * service is a distinct part of the overall m3ter system, and which forms a natural functional grouping, such as "config" or "billing".

        * resource-type is the resource type item accessed - for example: "Plan", "Meter", "Bill"

        * item-type is one of:

                * "item" - to specify an individual item.

                * "group" - to specify a resource group.

        * id is the resource group id or the resource item id

        Resources can be assigned to one or more ResourceGroups. For example, a Plan can be assigned to Plan ResourceGroups, a Meter can be assigned to Meter ResourceGroups, and so on. This is useful for cases where you want to create Permission Policies which allow or deny access to a specific subset of resources. For example, grant a user access to only some of the Plans in your Organization.

        This concept of grouping resources applies to every resource in m3ter, including ResourceGroups themselves. This allows you to nest ResourceGroups to support hierarchies of groups.

        See [Understanding, Creating, and Managing Permission Policies](https://www.m3ter.com/docs/guides/managing-organization-and-users/creating-and-managing-permissions) in the m3ter documentation for more information.

        **Note: User Resource Groups** You can create a User Resource Group to group resources of type = `user`. You can then retrieve a list of the User Resource Groups a user belongs to. For more details, see the [Retrieve OrgUser Groups](https://www.m3ter.com/docs/api#tag/OrgUsers/operation/GetOrgUserGroups) call in the OrgUsers section.
        """
        from .resources.resource_groups import ResourceGroupsResourceWithRawResponse

        return ResourceGroupsResourceWithRawResponse(self._client.resource_groups)

    @cached_property
    def scheduled_event_configurations(
        self,
    ) -> scheduled_event_configurations.ScheduledEventConfigurationsResourceWithRawResponse:
        """Endpoints for retrieving and managing scheduled Events' configurations.

        Scheduled Event Configurations define custom Event types that reference Date/Time fields belonging to configuration and billing entities. They therefore provide you with an extra degree of flexibility over and above system-generated Events for setting up Notifications based on Events.

        For more details, see the [Working with Scheduled Events](https://www.m3ter.com/docs/guides/alerts-events-and-notifications/utilizing-events-and-notifications/working-with-scheduled-events) in our Documenation.
        """
        from .resources.scheduled_event_configurations import ScheduledEventConfigurationsResourceWithRawResponse

        return ScheduledEventConfigurationsResourceWithRawResponse(self._client.scheduled_event_configurations)

    @cached_property
    def statements(self) -> statements.StatementsResourceWithRawResponse:
        """
        Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills.

        Bills are generated for an Account, and are calculated in accordance with the usage-based pricing Plans applied for the Products the Account consumes. These endpoints enable interaction with the billing system, allowing you to obtain billing details and insights into the consumption patterns and charges of your end-customer Accounts.
        """
        from .resources.statements import StatementsResourceWithRawResponse

        return StatementsResourceWithRawResponse(self._client.statements)

    @cached_property
    def transaction_types(self) -> transaction_types.TransactionTypesResourceWithRawResponse:
        """
        Endpoints for TransactionType operations such as creation, update, list, retrieve, and delete.

        You can create TransactionTypes for your Organization, which can then be used when creating and updating Balances. Example TransactionTypes: "Balance Amount" or "Add Funds".

        For details on creating a Transaction amount for a Balance using a TransactionType you've created for your Organization, see the [Create Balance Transaction](https://www.m3ter.com/docs/api#tag/Balances/operation/PostBalanceTransaction) call in the [Balances](https://www.m3ter.com/docs/api#tag/Balances) section of this API Reference.
        """
        from .resources.transaction_types import TransactionTypesResourceWithRawResponse

        return TransactionTypesResourceWithRawResponse(self._client.transaction_types)

    @cached_property
    def usage(self) -> usage.UsageResourceWithRawResponse:
        from .resources.usage import UsageResourceWithRawResponse

        return UsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        """
        A suite of endpoints for configuring and managing third party integrations within the m3ter platform. The integration endpoints in this section facilitate various operations such as creating, updating, listing, and deletion of integrations.

        m3ter integrations enable seamless data synchronization and mapping with external systems required in core business processes. These processes often include sales, pricing, billing and invoicing, and general finance.

        With m3ter integrations, you can establish robust connections with popular business platforms, enhancing your operational capabilities. For example:
        * Chargebee
        * Salesforce
        * Stripe
        * Netsuite
        * Paddle
        * Xero
        * QuickBooks
        """
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)


class AsyncM3terWithRawResponse:
    _client: AsyncM3ter

    def __init__(self, client: AsyncM3ter) -> None:
        self._client = client

    @cached_property
    def authentication(self) -> authentication.AsyncAuthenticationResourceWithRawResponse:
        """
        Endpoint for retrieving a JSON Web Token (JWT) bearer token for a ServiceUser using the Client Credentials Grant flow.

        A ServiceUser represents the automated process you want to grant access to your Organization - that is, as an API user.
        """
        from .resources.authentication import AsyncAuthenticationResourceWithRawResponse

        return AsyncAuthenticationResourceWithRawResponse(self._client.authentication)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        """
        Endpoints for Account related operations such as creation, update, list and delete.
        An Account represents one of your end-customer accounts.

        Accounts do not belong to a Product to allow for cases where an end customer takes more than one of your Products, and the charges for these Products differ.

        You typically attach a priced Plan or Plan Template to an Account before you can generate bills for the Account:
        - If a customer consumes several of your Products, you can attach a priced Plan or Plan Template to the Account for charging against each Product.
        - If an Account is charged solely on the basis of an agreed Prepayment/Commitment amount but not all of the Prepayment is prepaid, you can use a customized billing schedule for outstanding fees without having to attach a Plan to the Account to generate Bills.

        You can create Child Accounts for end customers who hold multiple Accounts with you. You can then set up billing for the Parent/Child Account usage to have the end-customer billed once for the Parent Account, instead of having separate bills issued for usage against each of their multiple Accounts.

        **IMPORTANT! - use of PII:** The use of any of your end-customers' Personally Identifiable Information (PII) in m3ter is restricted to a few fields on the **Account** entity. Please ensure that only the ``name``, ``address``, or ``emailAddress`` fields contain any end-customer PII data on any Accounts you create. See the [Introduction section](https://www.m3ter.com/docs/api#section/Introduction) above for more details.
        """
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def account_plans(self) -> account_plans.AsyncAccountPlansResourceWithRawResponse:
        """
        Endpoints for AccountPlan and AccountPlanGroup related operations such as creation, update, list and delete.

        **AccountPlans**
        An Account represents one of your end-customer accounts. To create an AccountPlan, you attach a Product Plan to an Account. The AccountPlan then determines the charges incurred at billing by your end customer for consuming the Product the Plan is for:
        * **AccountPlan Active/Inactive**. Set start and end dates to define the period the AccountPlan is active for the Account.
        * **AccountPlan per Product**. If an end customer consumes multiple Products, create separate AccountPlans to charge for each Product.

        **AccountPlan Constraints:**
        * Only one AccountPlan per Product can be active at any one time for an Account.
        * If you create a Plan as a custom Plan for a specific Account, you can only use it to create an AccountPlan for that Account.

        **AccountPlanGroups**
        Plan Groups are used when you want to apply a minimum spend amount at billing across several of your Products each of which are priced separately - when you create the Plan Group, you define an overall minimum spend and then add any priced Plans you want to include in the Group. To create an AccounPlanGroup, you can attach a Plan Group to an Account that consumes the separate Products which are priced using the included Plans. At billing, the minimum spend you've defined for the Plan Group is applied:
        * **Active AccountPlanGroup**. Set the start and end dates to define the period for which the Plan Group will be active for the Account.

        **Plan Group Notes:**
        * You can only add *one Plan for the same Product* to a Plan Group. See the [Plan Group](https://www.m3ter.com/docs/api#tag/PlanGroup) in this API Reference for more details on creating Plan Groups.
        * You can create a *custom Plan Group* for an Account, which means the Plan Group can only be attached to that Account to create an AccountPlanGroup.

        **AcountPlanGroup - Notes and Constraints:**
        * **AccountPlanGroup is type of AccountPlan** When you attach a Plan Group to an Account, this creates an AccountPlanGroup. However, the m3ter data model *does not support a separate AccountPlanGroup entity*, and an AccountPlanGroup is a type of AccountPlan where a `planGroupId` is used instead of a `planId` when it's created. See the [Create AccountPlan](https://www.m3ter.com/docs/api#tag/AccountPlan/operation/PostAccountPlan) call in this section and [Attaching Plan Groups to an Account](https://www.m3ter.com/docs/guides/end-customer-accounts/attaching-plan-groups-to-an-account) in our main User Documentation.
        * **Multiple AccountPlan Groups:** You can attach more than one Plan Group to an Account to create multiple AccountPlanGroups, but the rule that *only one attached Plan per Product can be active at any one time for an Account* is preserved:
                * Multiple attached Plan Groups on an Account can have overlapping dates only if none of the Plan Groups contain a Plan belonging to the same Product. If you try to attach a Plan Group to an Account with Plan Groups already attached and:
                        * The new Plan Group contains a Product Plan that also belongs to a Plan Group already attached to the Account.
                        * The dates for these "matched Plan" Plan Groups being active for the Account would overlap.
                        * Then you'll receive an error and the attachment will be blocked.
        """
        from .resources.account_plans import AsyncAccountPlansResourceWithRawResponse

        return AsyncAccountPlansResourceWithRawResponse(self._client.account_plans)

    @cached_property
    def aggregations(self) -> aggregations.AsyncAggregationsResourceWithRawResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Aggregations.

        An Aggregation links to a Meter and targets a Data Field or Derived Field on the Meter. You define the method of aggregation used to convert the usage data collected by the targeted Meter field into a numerical unit of measurement.

        You can then use the unit of measurement an Aggregation yields as a metric for pricing Product Plans and apply usage-based pricing to your products and services. You might also want to aggregate raw data measures for other purposes, such as to feed into analytical or business performance tools.

        **Notes:**
        * **Contrast with Compound Aggregations**. Standard or simple Aggregations of this type, which apply an aggregation method directly to Meter usage data fields, are contrasted with [Compound Aggregations](https://www.m3ter.com/docs/api#tag/CompoundAggregation). A Compound Aggregation typically references one or more simple Aggregations and applies a calculation to them to derive pricing metrics needed to serve more complex usage-based pricing scenarios.
        * **Segmented Aggregations**. Segmented Aggregations allow you to segment the usage data collected by a single Meter. This capability is very useful for implementing some pricing and billing use cases. See [Segmented Aggregations](https://www.m3ter.com/docs/guides/usage-data-aggregations/segmented-aggregations) in our main documentation for more details.
        """
        from .resources.aggregations import AsyncAggregationsResourceWithRawResponse

        return AsyncAggregationsResourceWithRawResponse(self._client.aggregations)

    @cached_property
    def balances(self) -> balances.AsyncBalancesResourceWithRawResponse:
        """Endpoints for creating/retrieving/updating/deleting Balances on Accounts.

        When you have created a Balance for an Account, you can create a positive or negative Transaction amounts for the Balance. To do this, you must first define Transaction Types for your Organization, and then use one of these Transaction Types when you add a specific Transaction to a Balance - see the [Create TransactionType](https://www.m3ter.com/docs/api#tag/TransactionType/operation/CreateTransactionType) call in the Transaction Type section in this API Reference for more details.

        Balances are typically used when a customer prepays an amount to add a credit to their Account, which can then be draw-down against charges due for product or service consumption. You can include options to top-up the original Balance.

        Examples of how Balances for end customer Accounts can be used:

        * Onboarding Balance/Free Trials. Offering an onboarding incentive to new customers as an initial free credit Balance on their Account.

        * Balance as initial commitment. Add a Balance amount to a new customer Account. This acts as an initial commitment, which allows them to use the service and gain an accurate insight into their usage level.

        * Managing Customer Satisfaction. Use Balance as credits that will be applied to subsequent Bills as compensation for acknowledged service delivery issues.

        * Facilitating Balance Adjustments:
                * Apply negative amounts to immediately write-off outstanding Balances.

        #### What is the difference between Balances and Commitments/Prepayments?

        To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

        Commitments - also referred to as Prepayments - are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the commitment or prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

        In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

        You can use Commitments/Prepayments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Commitment credit on an Account is drawn-down - Balance amounts first or Commitment/Prepayment amounts first.
        """
        from .resources.balances import AsyncBalancesResourceWithRawResponse

        return AsyncBalancesResourceWithRawResponse(self._client.balances)

    @cached_property
    def bills(self) -> bills.AsyncBillsResourceWithRawResponse:
        """
        Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills.

        Bills are generated for an Account, and are calculated in accordance with the usage-based pricing Plans applied for the Products the Account consumes. These endpoints enable interaction with the billing system, allowing you to obtain billing details and insights into the consumption patterns and charges of your end-customer Accounts.
        """
        from .resources.bills import AsyncBillsResourceWithRawResponse

        return AsyncBillsResourceWithRawResponse(self._client.bills)

    @cached_property
    def bill_config(self) -> bill_config.AsyncBillConfigResourceWithRawResponse:
        """Endpoints for updating and retreiving the Bill Configuration for an Organization.

        The Organization represents your company as a direct customer of the m3ter service.

        You can use the **Update BillConfig** endpoint to set a global lock date for **all** Bills - any Bill with a service period end date on or before the set date will be locked and cannot be updated.

        **Warning: Ensure all Bills are Approved!** If you try to set a global lock date when there remains Bills in a *Pending* state whose service period end date is on or before the specified lock date, then you'll receive an error.
        """
        from .resources.bill_config import AsyncBillConfigResourceWithRawResponse

        return AsyncBillConfigResourceWithRawResponse(self._client.bill_config)

    @cached_property
    def commitments(self) -> commitments.AsyncCommitmentsResourceWithRawResponse:
        """
        Endpoints that manage Commitments *(also known as Prepayments)* in the context of usage-based pricing and billing. A Commitment represents an agreement where the end-customer has agreed to pay a fixed minimum amount throughout the contract period. ***The commitment amount is payable regardless of the actual usage by the customer of your service or product.***

        These endpoints enable the creation, updating, retrieval, and deletion of Commitments. Use them to manage your customer's Commitments and ensure optimal revenue recognition:
        * Specify which type of charges can draw-down against a Commitment amount on an Account at billing: usage, minimum spend, standing charges, or recurring charges.
        * Define overage surcharge percentages, which are applied when the usage charges exceed the agreed Commitment amount within the contract duration.

        #### What is the difference between Balances and Commitments/Prepayments?

        To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

        Commitments/Prepayments are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

        In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

        You can use Prepayments/Commitments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Prepayment credit on an Account is drawn-down - Balance amounts first or Prepayment amounts first.

        #### Billing for Commitments

        If not all of an agreed Commitment amount is paid at the start of an end-customer contract period, you can choose one of two options for billing the outstanding fees due on the customer Account:
        - Select a Product *Plan to bill with*.
        - Define a *schedule of billing dates*.
        """
        from .resources.commitments import AsyncCommitmentsResourceWithRawResponse

        return AsyncCommitmentsResourceWithRawResponse(self._client.commitments)

    @cached_property
    def bill_jobs(self) -> bill_jobs.AsyncBillJobsResourceWithRawResponse:
        """Endpoints for creating, retrieving, listing, and cancelling Bill Jobs.

        Bill Jobs are critical components in billing management, providing asynchronous mechanisms to calculate and handle bills.

        Bill Jobs give you the flexibiity to run Bills manually for Accounts to suit different billing management purposes. For example, some historical usage data has come in for an Account and you want to run a Bill for a specific date on that Account to check that the Bill is showing correctly for the charges due on the new usage data.
        """
        from .resources.bill_jobs import AsyncBillJobsResourceWithRawResponse

        return AsyncBillJobsResourceWithRawResponse(self._client.bill_jobs)

    @cached_property
    def charges(self) -> charges.AsyncChargesResourceWithRawResponse:
        """Endpoints for creating/updating/deleting Charges.

        Create Charges for your end-customer Accounts to create ad-hoc line items for Account billing. Charges are:
        * Created for either debit or credit amounts.
        * Linked to a Product for accounting purposes.
        * Optionally linked to a Contract.
        * Given a specific date for billing. When a bill job has run for the specified Charge bill date, a Charge appears as an Ad-hoc line item on the Bill.
        * Assigned a service period.
        * Available in any currency defined for your Organization.
        See [Creating Charges for Accounts](https://www.m3ter.com/docs/guides/end-customer-accounts/creating-charges-for-accounts) in our main user documentation for more details.

        Alternatively, you can create a Charge for a Balance on an end-customer Account to create balance fee line items for Account billing. See [Creating Charges for Balances](https://www.m3ter.com/docs/guides/end-customer-accounts/creating-balances-for-accounts/creating-charges-for-balances) in our main user documentation for more details.
        """
        from .resources.charges import AsyncChargesResourceWithRawResponse

        return AsyncChargesResourceWithRawResponse(self._client.charges)

    @cached_property
    def compound_aggregations(self) -> compound_aggregations.AsyncCompoundAggregationsResourceWithRawResponse:
        """
        Endpoints for Compound Aggregation related operations such as creation, update, list and delete.

        Use Compound Aggregations to create numerical measures from usage data by applying a calculation to one or more simple Aggregations or Custom Fields. These numerical measures can then be used as pricing metrics to price your Product Plans, enabling you to implement a wide range of usage-based pricing use cases.

        You can create two types of Compound Aggregation:

        **Global**
        - Pricing: Not tied to any specific product and can be used to price Plans belonging to any Product.
        - Calculation: can reference all simple Aggregations - both Global simple Aggregations and any product-specific simple Aggregations.

        **Product-specific**
        - Pricing: belong to a specific Product and can only be used to price Plans belonging to the same Product.
        - Calculation: can reference any simple Aggregations belonging to the same Product and any Global simple Aggregations.

        **IMPORTANT!** If a simple Aggregation referenced by a Compound Aggregation has a **Quantity per unit** defined or a **Rounding** defined, these will not be factored into the value used by the calculation. For example, if the simple Aggregation referenced has a base value of 100 and has **Quantity per unit** set at 10, the Compound Aggregation calculation *will use the base value of 100 not 10*.

        To better understand and use Compound Aggregations, refer to the example [Compound Aggregation Use Case](https://www.m3ter.com/docs/guides/setting-up-usage-data-meters-and-aggregations/compound-aggregations#example-use-case) in the m3ter documentation.
        """
        from .resources.compound_aggregations import AsyncCompoundAggregationsResourceWithRawResponse

        return AsyncCompoundAggregationsResourceWithRawResponse(self._client.compound_aggregations)

    @cached_property
    def contracts(self) -> contracts.AsyncContractsResourceWithRawResponse:
        """
        Endpoints for Contract related operations such as creation, update, list and delete.

        Contracts are created for Accounts, which are your end-user customers. Contracts can be used for:
        * **Accounts Reporting**. To serve your general accounting operations and processes, you can report on total Contract values for an Account.
        * **Contract Billing**. Various billing entities associated with an Account can  be linked to Contracts on the Account to meet your specific Contract billing use cases.
        """
        from .resources.contracts import AsyncContractsResourceWithRawResponse

        return AsyncContractsResourceWithRawResponse(self._client.contracts)

    @cached_property
    def counters(self) -> counters.AsyncCountersResourceWithRawResponse:
        """Endpoints for listing, creating, retrieving, updating, or deleting Counters.

        You can create Counters for your m3ter Organization, which can then be used as pricing metrics to apply a unit-based [CounterPricing](https://www.m3ter.com/docs/api#tag/CounterPricing) to Product Plans or Plan Templates for recurring subscription charges on Accounts.

        Counters can then be used to post [CounterAdjustments](https://www.m3ter.com/docs/api#tag/CounterAdjustments) on your end-customer Accounts.

        Accounts are then billed in accordance with the CounterPricing on Plans attached to the Accounts and for the actual Counter quantities Accounts subscribe to. See [Recurring Charges: Counters](https://www.m3ter.com/docs/guides/recurring-charges-counters) in our main user documentation for more details.
        """
        from .resources.counters import AsyncCountersResourceWithRawResponse

        return AsyncCountersResourceWithRawResponse(self._client.counters)

    @cached_property
    def counter_adjustments(self) -> counter_adjustments.AsyncCounterAdjustmentsResourceWithRawResponse:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting CounterAdjustments.

        If you attach a Plan to an Account which is priced using a Counter to apply unit-based pricing, you can then create CounterAdjustments for the Account using that Counter to ensure the Account is billed according to the number of Counter units the Account subscribes to in a given billing period.

        See [Understanding and Creating Counter Adjustments for Accounts](https://www.m3ter.com/docs/guides/recurring-charges-counters/creating-counter-adjustments-for-accounts) for more information.
        """
        from .resources.counter_adjustments import AsyncCounterAdjustmentsResourceWithRawResponse

        return AsyncCounterAdjustmentsResourceWithRawResponse(self._client.counter_adjustments)

    @cached_property
    def counter_pricings(self) -> counter_pricings.AsyncCounterPricingsResourceWithRawResponse:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting CounterPricing.

        Create the CounterPricing for a Plan/PlanTemplate using a Counter, and define a unit-based pricing structure for charging end customer Accounts put on the Plan.

        See [Creating Counters and Pricing Plans](https://www.m3ter.com/docs/guides/recurring-charges-counters/creating-counters) for more information.
        """
        from .resources.counter_pricings import AsyncCounterPricingsResourceWithRawResponse

        return AsyncCounterPricingsResourceWithRawResponse(self._client.counter_pricings)

    @cached_property
    def credit_reasons(self) -> credit_reasons.AsyncCreditReasonsResourceWithRawResponse:
        """Endpoints for CreditReason operations such as creation, update, list, and delete.

        You can create CreditReasons for your Organization, and then use them when creating a credit line item on a bill, or applying a product credit to a bill. CreditReasons provide contextual information as to why a credit was applied.
        """
        from .resources.credit_reasons import AsyncCreditReasonsResourceWithRawResponse

        return AsyncCreditReasonsResourceWithRawResponse(self._client.credit_reasons)

    @cached_property
    def currencies(self) -> currencies.AsyncCurrenciesResourceWithRawResponse:
        """Endpoints for Currency operations such as creation, update, list, and delete.

        Currencies are stored for your Organization, and can then be used to specify currencies on various entities such as plan groups and plan templates.

        **IMPORTANT!**
        The Currencies you want to use in your Organization must be created first.

        The currency you select for your Organization determines the billing currency and overrides any currency settings in your pricing Plans.
        For example, if the Organization currency is set to USD and a pricing Plan used for an Account is set to GBP, the bill for an Account using that Plan is calculated in GBP, and then each bill line item converted to USD amounts.

        Currency conversion rates are setup in the *OrganizationConfig*. For more details, see [Creating and Managing Currencies](https://www.m3ter.com/docs/guides/organization-and-access-management/viewing-and-editing-organization#creating-and-managing-currencies) in the m3ter Documentation.
        """
        from .resources.currencies import AsyncCurrenciesResourceWithRawResponse

        return AsyncCurrenciesResourceWithRawResponse(self._client.currencies)

    @cached_property
    def custom_fields(self) -> custom_fields.AsyncCustomFieldsResourceWithRawResponse:
        """
        Endpoints for retrieving and updating Custom Fields at the Organization level for all entities that support them.

        Custom Fields in m3ter allow you to store custom data in the form of number or string values against m3ter entities in a way that does not directly affect the normal working operation of the m3ter platform. Having this capability to store data in a free-hand fashion can prove very useful in helping you to meet specific usage-based pricing and other operational business use cases.

        However, you can exploit the values stored on Custom Fields in a more direct way by referencing them in Derived Field and Compound Aggregation calculations. Given the key role these calculations can play when implementing usage-based pricing schema, any Custom Fields you reference will then affect how the platform behaves. Referencing Custom Field values in your calculations offers a much wider scope of options when it comes to resolving complex usage-based pricing use cases.

        Custom Fields can be added to the following entities at Organizational level:
        * Organization
        * Account
        * AccountPlan
        * Aggregation
        * Compound Aggregation
        * Meter
        * Product
        * Plan
        * PlanTemplate
        * Contract

        These all follow the same pattern - a new *(optional)* field is available on the entity request and response bodies called "customFields" which is a object in this format:
        ```
        "customFields": {
                        "exampleCustomField1": 7.1,
                        "exampleCustomField2": "stringValue"
        }
        ```
        The value for a Custom Field can be a string or a number.

        **Using Custom Field values in calculations:**
        - You can add Custom Fields at two levels - the Organization level and the individual entity level.
        - The Organizational level field provides a default value and *must be added* if you want to also add a Custom Field of the same name at the corresponding individual entity level. If you reference the Custom Field in a calculation, the value for the individual entity level field is used. If no field is defined at individual entity level, then the Organization level field value is used.

        **Important: Constraints and Exceptions!**

        **Custom Fields at Organization Level**. Currently, you cannot create Custom Fields at the Organization-level for the following enitites:
        * Plan Group
        * Balance
        * Balance Transaction Schedule
        * Balance Charge Schedule

        Therefore you cannot reference the Custom Fields values created at the individual entity level for these entities in your Derived Field or Compound Aggregation calculations.

        **Derived Field Calculations**. You can *only reference Custom Fields* for the following entities:
        * Organization
        * Meter
        * Account

        However, if you are using Meters belonging to *a specific Product*, that is, not *Global Meters*, you can also reference Custom Fields added to a Product in Derived Field calculations.

        **Compound Aggregation Calculations - Meter Custom Fields**. The value of the *Organization level Meter Custom Field will always be used*, even if you have defined a corresponding field at the individual Meter level.

        See [Working with Custom Fields](https://www.m3ter.com/docs/guides/creating-and-managing-products/working-with-custom-fields) in the m3ter documentation for more information.
        """
        from .resources.custom_fields import AsyncCustomFieldsResourceWithRawResponse

        return AsyncCustomFieldsResourceWithRawResponse(self._client.custom_fields)

    @cached_property
    def data_exports(self) -> data_exports.AsyncDataExportsResourceWithRawResponse:
        """Endpoints for triggering one-off, ad-hoc Data Exports.

        You can set up and run ad-hoc Exports to export two kinds of data from your m3ter Organization:
        * Usage data.
        * Operational data for entities.

        **Ad-Hoc Export Destinations** When setting up and running an ad-hoc Export:
        * You can define one or more Export Destinations - see the [ExportDestination](https://www.m3ter.com/docs/api#tag/ExportDestination) section of this API Reference. When the export runs, the data is sent through to the sepecified Destination. However, the export file is also made available for you to download it locally.
        * You can set up and run Data Exports without defining a Destination. The data is not exported but the compiled export file is made available for downloading locally.
        * For details on downloading an export file, see the [Get Data Export File Download URL](https://www.m3ter.com/docs/api#tag/ExportDestination/operation/GenerateDataExportFileDownloadUrl) endpoint in this API Reference.

        **Preview Version!** The Data Export feature is currently available only in Preview release version. See [Feature Release Stages](https://www.m3ter.com/docs/guides/getting-started/feature-release-stages) for Preview release definition. ExportAdHoc endpoints will only be available if Data Export has been enabled for your Organization. For more details see [Data Export(Preview)](https://www.m3ter.com/docs/guides/data-exports) in our main User documentation. If you're interested in previewing the Data Export feature, please get in touch with m3ter Support or your m3ter contact.
        """
        from .resources.data_exports import AsyncDataExportsResourceWithRawResponse

        return AsyncDataExportsResourceWithRawResponse(self._client.data_exports)

    @cached_property
    def debit_reasons(self) -> debit_reasons.AsyncDebitReasonsResourceWithRawResponse:
        """Endpoints for DebitReason operations such as creation, update, list, and delete.

        You can create DebitReasons for your Organization, and then use them when creating a debit line item on a bill, or applying a product debit to a bill. DebitReasons provide contextual information as to why a debit was applied.
        """
        from .resources.debit_reasons import AsyncDebitReasonsResourceWithRawResponse

        return AsyncDebitReasonsResourceWithRawResponse(self._client.debit_reasons)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
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
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def external_mappings(self) -> external_mappings.AsyncExternalMappingsResourceWithRawResponse:
        """
        Endpoints for managing External Mapping related operations such as creation, update, list and delete.

        When you integrate your 3rd-party systems with the m3ter platform, a mapping between entities in the local system *(m3ter)* and external systems is constructed. This *External Mapping* is crucial in scenarios where data from external systems is consumed or where data from the local system is to be synchronized with external systems.

        When you are working to set up your Integrations and want to test or troubleshoot your implementation before going live, you might need to create External Mappings manually and, at a later date, edit or delete them.
        """
        from .resources.external_mappings import AsyncExternalMappingsResourceWithRawResponse

        return AsyncExternalMappingsResourceWithRawResponse(self._client.external_mappings)

    @cached_property
    def integration_configurations(
        self,
    ) -> integration_configurations.AsyncIntegrationConfigurationsResourceWithRawResponse:
        """
        A suite of endpoints for configuring and managing third party integrations within the m3ter platform. The integration endpoints in this section facilitate various operations such as creating, updating, listing, and deletion of integrations.

        m3ter integrations enable seamless data synchronization and mapping with external systems required in core business processes. These processes often include sales, pricing, billing and invoicing, and general finance.

        With m3ter integrations, you can establish robust connections with popular business platforms, enhancing your operational capabilities. For example:
        * Chargebee
        * Salesforce
        * Stripe
        * Netsuite
        * Paddle
        * Xero
        * QuickBooks
        """
        from .resources.integration_configurations import AsyncIntegrationConfigurationsResourceWithRawResponse

        return AsyncIntegrationConfigurationsResourceWithRawResponse(self._client.integration_configurations)

    @cached_property
    def lookup_tables(self) -> lookup_tables.AsyncLookupTablesResourceWithRawResponse:
        """Endpoints for creating/updating/deleting Lookup Tables.

        Lookup Tables enable you to manage dynamic data mappings that your calculations reference. Use them for currency conversion, pricing tiers, discount rates, and similar scenarios where you require values to change operationally but for calculation logic to remain constant.

        **Beta Version!** The Lookup Table feature is currently available in Beta release version. See [Feature Release Stages](https://www.m3ter.com/docs/guides/getting-started/feature-release-stages) for Beta release definition. Lookup Table endpoints will only be available if Lookup Tables have been enabled for your Organization. For more details see [Lookup Tables (Beta)](https://www.m3ter.com/docs/guides/lookup-tables) in our main User documentation.
        """
        from .resources.lookup_tables import AsyncLookupTablesResourceWithRawResponse

        return AsyncLookupTablesResourceWithRawResponse(self._client.lookup_tables)

    @cached_property
    def meters(self) -> meters.AsyncMetersResourceWithRawResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Meters.

        Use Meters to submit usage data for the consumption of your products and services by end customers. This usage data then becomes the basis for setting up usage-based pricing for your products and services.

        Examples of usage data collected in Meters:
        * Number of logins.
        * Duration of session.
        * Amount of data downloaded.

        To collect usage data and ingest it into the platform, you can define two types of fields for Meters:
        - `dataFields` Used to collect raw usage data measures - numeric quantitative data values or non-numeric point data values.
        - `derivedFields` Used to derive usage data measures that are the result of applying a calculation to `dataFields`, `customFields`, or system `Timestamp` fields.

        You can also:
        - Create `customFields` for a Meter, which allows you to attach custom data to the Meter as name/value pairs.
        - Create Global Meters, which are not tied to a specific Product and allow you to collect usage data that will form the basis of usage-based pricing across multiple Products.

        **IMPORTANT! - use of PII:** The use of any of your end-customers' Personally Identifiable Information (PII) in m3ter is restricted to a few fields on the **Account** entity. Please ensure that any fields you configure for Meters, such as Data Fields or Derived Fields, do not contain any end-customer PII data. See the [Introduction section](https://www.m3ter.com/docs/api#section/Introduction) above for more details.

        See also:
        - [Reviewing Meter Options](https://www.m3ter.com/docs/guides/setting-up-usage-data-meters-and-aggregations/reviewing-meter-options).
        """
        from .resources.meters import AsyncMetersResourceWithRawResponse

        return AsyncMetersResourceWithRawResponse(self._client.meters)

    @cached_property
    def notification_configurations(
        self,
    ) -> notification_configurations.AsyncNotificationConfigurationsResourceWithRawResponse:
        """This section provides endpoints for managing Event Notifications.

        You can create Notifications based on system Events generated by the platform. When you base a Notification on a specific Event type, you can include a calculation that references the fields available on that Event type to define precise conditions that must be met for the Notification to be triggered when an Event of that type occurs. In this way, you can set up highly customized Notifications that act as timely alerts to inform you about significant occurrences within your Organization. For instance, if you provide a sign-up bonus to new end-customer Accounts, you can set up a Notification to alert you when an end-customer Account has used up a certain percentage of their bonus credit.

        You can also set up Notifications based on Scheduled Event types you've created for your Organization. See the [ScheduledEventConfigurations](https://www.m3ter.com/docs/api#tag/ScheduledEventConfigurations) section of this API Reference and [Working with Scheduled Events](https://www.m3ter.com/docs/guides/alerts-events-and-notifications/utilizing-events-and-notifications/working-with-scheduled-events) in our user documentation.

        For more details on Event types and their fields, see the [Events](https://www.m3ter.com/docs/api#tag/Events) section.

        For detailed guidance on working with Events and Notifications, refer to the [Utilizing Events and Notifications](https://www.m3ter.com/docs/guides/utilizing-events-and-notifications) section of the m3ter user documentation.
        """
        from .resources.notification_configurations import AsyncNotificationConfigurationsResourceWithRawResponse

        return AsyncNotificationConfigurationsResourceWithRawResponse(self._client.notification_configurations)

    @cached_property
    def organization_config(self) -> organization_config.AsyncOrganizationConfigResourceWithRawResponse:
        """Endpoints for retrieving or updating the Organization Config.

        Organization represents your company as a direct customer of m3ter. Use Organization configuration to define *Organization-wide* settings. For example:
        - Timezone.
        - Currencies and currency conversions.
        - Billing operations settings, such as:
                - Epoch dates to control first billing dates.
                - Whether to bill customer accounts in advance/in arrears for standing charge amounts, minimum spend amounts, and commitment fees.

        For other aspects of your Organization setup and configuration, see the following sections in this API Reference:
        * [Custom Fields](https://www.m3ter.com/docs/api#tag/CustomField)
        * [Currencies](https://www.m3ter.com/docs/api#tag/Currency)
        * [Credit Reasons](https://www.m3ter.com/docs/api#tag/CreditReason)
        * [Debit Reason](https://www.m3ter.com/docs/api#tag/DebitReason)
        * [Transaction Types](https://www.m3ter.com/docs/api#tag/TransactionType)

        See also:
        - [Managing your Organization](https://www.m3ter.com/docs/guides/managing-organization-and-users/viewing-and-editing-organization).
        """
        from .resources.organization_config import AsyncOrganizationConfigResourceWithRawResponse

        return AsyncOrganizationConfigResourceWithRawResponse(self._client.organization_config)

    @cached_property
    def permission_policies(self) -> permission_policies.AsyncPermissionPoliciesResourceWithRawResponse:
        """
        Endpoints for Permission Policy related operations such as creation, update, add and retrieve.

        Permission Policies can restrict or grant access to specific resources for both Users *(people)* and Service Users *(automated processes with direct API access)*. This enables you to control precisely what a User can do in your m3ter Organization.

        For more details, see [Understanding, Creating, and Managing Permission Policies](https://www.m3ter.com/docs/guides/organization-and-access-management/creating-and-managing-permissions#permission-policy-statements---available-actions-and-resources) in our main Documentation.
        """
        from .resources.permission_policies import AsyncPermissionPoliciesResourceWithRawResponse

        return AsyncPermissionPoliciesResourceWithRawResponse(self._client.permission_policies)

    @cached_property
    def plans(self) -> plans.AsyncPlansResourceWithRawResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Plans.

        A Plan is based on a PlanTemplate and represents a specific pricing plan for one of your products or services. Each Plan inherits general billing attributes or pricing structure from its parent Plan Template. Some attributes can be overriden for the specific Plan.

        When you've created the Plan Templates and Plans you need for your Products, you can configure the exact pricing structures for Plans to charge customers that consume one or more of your Products.

        You can then attach the appropriately priced Plans to customer Accounts to create [Account Plans](https://www.m3ter.com/docs/api#tag/AccountPlan) and enable charges to be calculated correctly for billing against those Accounts.

        See also:
        - [Reviewing Options for Plans and Plan Templates](https://www.m3ter.com/docs/guides/working-with-plan-templates-and-plans/reviewing-configuration-options-for-plans-and-plan-templates).
        """
        from .resources.plans import AsyncPlansResourceWithRawResponse

        return AsyncPlansResourceWithRawResponse(self._client.plans)

    @cached_property
    def plan_groups(self) -> plan_groups.AsyncPlanGroupsResourceWithRawResponse:
        """
        Endpoints for PlanGroup related operations such as creation, update, retrieve, list and delete.

        PlanGroups are constructs that group multiple plans together. This enables a unified approach to efficiently handle various uses cases across different plans. For example applying a minimum spend amount at billing, across several of your products or features that are each priced separately.
        """
        from .resources.plan_groups import AsyncPlanGroupsResourceWithRawResponse

        return AsyncPlanGroupsResourceWithRawResponse(self._client.plan_groups)

    @cached_property
    def plan_group_links(self) -> plan_group_links.AsyncPlanGroupLinksResourceWithRawResponse:
        """
        Endpoints for PlanGroupLink related operations such as creation, update, list and delete.

        PlanGroupLinks are the intersection table between a PlanGroup and its associated Plans. A PlanGroupLink is only created when at least 1 Plan is linked to a PlanGroup.
        """
        from .resources.plan_group_links import AsyncPlanGroupLinksResourceWithRawResponse

        return AsyncPlanGroupLinksResourceWithRawResponse(self._client.plan_group_links)

    @cached_property
    def plan_templates(self) -> plan_templates.AsyncPlanTemplatesResourceWithRawResponse:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting PlanTemplates.

        Use PlanTemplates to define default values for Plans. These default values control the billing operations you want applied to your products. PlanTemplates avoid repetition in configuration work - many Plans will share settings for billing operations and differ only in the details of their pricing structures.

        A PlanTemplate is linked to a Product, and each Plan is a child of a PlanTemplate.
        """
        from .resources.plan_templates import AsyncPlanTemplatesResourceWithRawResponse

        return AsyncPlanTemplatesResourceWithRawResponse(self._client.plan_templates)

    @cached_property
    def pricings(self) -> pricings.AsyncPricingsResourceWithRawResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Pricing.

        Create the Pricing for a Plan/PlanTemplate with usage data Aggregations, and define a usage-based pricing structure for charging end customer Accounts put on the Plan.

        See [Reviewing Pricing Options for Plans and Plan Templates](https://www.m3ter.com/docs/guides/pricing-plans/reviewing-pricing-options-and-pricing-plans) for more information.
        """
        from .resources.pricings import AsyncPricingsResourceWithRawResponse

        return AsyncPricingsResourceWithRawResponse(self._client.pricings)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithRawResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Products.

        A Product represents the products and services you offer to your end customers. Products act as a container for the Meters, Aggregations, Pricing, and Plans required to implement usage-based and other pricing models for your Organization.
        """
        from .resources.products import AsyncProductsResourceWithRawResponse

        return AsyncProductsResourceWithRawResponse(self._client.products)

    @cached_property
    def resource_groups(self) -> resource_groups.AsyncResourceGroupsResourceWithRawResponse:
        """
        Endpoints for ResourceGroup related operations such as creation, update, list and delete.

        ResourceGroups are used in the context of Permission Policies, which controls what a User who has been given access to your Organization can and cannot do. For example, you might want to create a Permissions Policy that denies Users the ability to retrieve Meters.

        Resources are defined as m3ter Resource Identifiers *(MRIs)* in the format:

        ```
        service: resource - type / item - type / id
        ```

        Where:

        * service is a distinct part of the overall m3ter system, and which forms a natural functional grouping, such as "config" or "billing".

        * resource-type is the resource type item accessed - for example: "Plan", "Meter", "Bill"

        * item-type is one of:

                * "item" - to specify an individual item.

                * "group" - to specify a resource group.

        * id is the resource group id or the resource item id

        Resources can be assigned to one or more ResourceGroups. For example, a Plan can be assigned to Plan ResourceGroups, a Meter can be assigned to Meter ResourceGroups, and so on. This is useful for cases where you want to create Permission Policies which allow or deny access to a specific subset of resources. For example, grant a user access to only some of the Plans in your Organization.

        This concept of grouping resources applies to every resource in m3ter, including ResourceGroups themselves. This allows you to nest ResourceGroups to support hierarchies of groups.

        See [Understanding, Creating, and Managing Permission Policies](https://www.m3ter.com/docs/guides/managing-organization-and-users/creating-and-managing-permissions) in the m3ter documentation for more information.

        **Note: User Resource Groups** You can create a User Resource Group to group resources of type = `user`. You can then retrieve a list of the User Resource Groups a user belongs to. For more details, see the [Retrieve OrgUser Groups](https://www.m3ter.com/docs/api#tag/OrgUsers/operation/GetOrgUserGroups) call in the OrgUsers section.
        """
        from .resources.resource_groups import AsyncResourceGroupsResourceWithRawResponse

        return AsyncResourceGroupsResourceWithRawResponse(self._client.resource_groups)

    @cached_property
    def scheduled_event_configurations(
        self,
    ) -> scheduled_event_configurations.AsyncScheduledEventConfigurationsResourceWithRawResponse:
        """Endpoints for retrieving and managing scheduled Events' configurations.

        Scheduled Event Configurations define custom Event types that reference Date/Time fields belonging to configuration and billing entities. They therefore provide you with an extra degree of flexibility over and above system-generated Events for setting up Notifications based on Events.

        For more details, see the [Working with Scheduled Events](https://www.m3ter.com/docs/guides/alerts-events-and-notifications/utilizing-events-and-notifications/working-with-scheduled-events) in our Documenation.
        """
        from .resources.scheduled_event_configurations import AsyncScheduledEventConfigurationsResourceWithRawResponse

        return AsyncScheduledEventConfigurationsResourceWithRawResponse(self._client.scheduled_event_configurations)

    @cached_property
    def statements(self) -> statements.AsyncStatementsResourceWithRawResponse:
        """
        Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills.

        Bills are generated for an Account, and are calculated in accordance with the usage-based pricing Plans applied for the Products the Account consumes. These endpoints enable interaction with the billing system, allowing you to obtain billing details and insights into the consumption patterns and charges of your end-customer Accounts.
        """
        from .resources.statements import AsyncStatementsResourceWithRawResponse

        return AsyncStatementsResourceWithRawResponse(self._client.statements)

    @cached_property
    def transaction_types(self) -> transaction_types.AsyncTransactionTypesResourceWithRawResponse:
        """
        Endpoints for TransactionType operations such as creation, update, list, retrieve, and delete.

        You can create TransactionTypes for your Organization, which can then be used when creating and updating Balances. Example TransactionTypes: "Balance Amount" or "Add Funds".

        For details on creating a Transaction amount for a Balance using a TransactionType you've created for your Organization, see the [Create Balance Transaction](https://www.m3ter.com/docs/api#tag/Balances/operation/PostBalanceTransaction) call in the [Balances](https://www.m3ter.com/docs/api#tag/Balances) section of this API Reference.
        """
        from .resources.transaction_types import AsyncTransactionTypesResourceWithRawResponse

        return AsyncTransactionTypesResourceWithRawResponse(self._client.transaction_types)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithRawResponse:
        from .resources.usage import AsyncUsageResourceWithRawResponse

        return AsyncUsageResourceWithRawResponse(self._client.usage)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        """
        A suite of endpoints for configuring and managing third party integrations within the m3ter platform. The integration endpoints in this section facilitate various operations such as creating, updating, listing, and deletion of integrations.

        m3ter integrations enable seamless data synchronization and mapping with external systems required in core business processes. These processes often include sales, pricing, billing and invoicing, and general finance.

        With m3ter integrations, you can establish robust connections with popular business platforms, enhancing your operational capabilities. For example:
        * Chargebee
        * Salesforce
        * Stripe
        * Netsuite
        * Paddle
        * Xero
        * QuickBooks
        """
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)


class M3terWithStreamedResponse:
    _client: M3ter

    def __init__(self, client: M3ter) -> None:
        self._client = client

    @cached_property
    def authentication(self) -> authentication.AuthenticationResourceWithStreamingResponse:
        """
        Endpoint for retrieving a JSON Web Token (JWT) bearer token for a ServiceUser using the Client Credentials Grant flow.

        A ServiceUser represents the automated process you want to grant access to your Organization - that is, as an API user.
        """
        from .resources.authentication import AuthenticationResourceWithStreamingResponse

        return AuthenticationResourceWithStreamingResponse(self._client.authentication)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        """
        Endpoints for Account related operations such as creation, update, list and delete.
        An Account represents one of your end-customer accounts.

        Accounts do not belong to a Product to allow for cases where an end customer takes more than one of your Products, and the charges for these Products differ.

        You typically attach a priced Plan or Plan Template to an Account before you can generate bills for the Account:
        - If a customer consumes several of your Products, you can attach a priced Plan or Plan Template to the Account for charging against each Product.
        - If an Account is charged solely on the basis of an agreed Prepayment/Commitment amount but not all of the Prepayment is prepaid, you can use a customized billing schedule for outstanding fees without having to attach a Plan to the Account to generate Bills.

        You can create Child Accounts for end customers who hold multiple Accounts with you. You can then set up billing for the Parent/Child Account usage to have the end-customer billed once for the Parent Account, instead of having separate bills issued for usage against each of their multiple Accounts.

        **IMPORTANT! - use of PII:** The use of any of your end-customers' Personally Identifiable Information (PII) in m3ter is restricted to a few fields on the **Account** entity. Please ensure that only the ``name``, ``address``, or ``emailAddress`` fields contain any end-customer PII data on any Accounts you create. See the [Introduction section](https://www.m3ter.com/docs/api#section/Introduction) above for more details.
        """
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def account_plans(self) -> account_plans.AccountPlansResourceWithStreamingResponse:
        """
        Endpoints for AccountPlan and AccountPlanGroup related operations such as creation, update, list and delete.

        **AccountPlans**
        An Account represents one of your end-customer accounts. To create an AccountPlan, you attach a Product Plan to an Account. The AccountPlan then determines the charges incurred at billing by your end customer for consuming the Product the Plan is for:
        * **AccountPlan Active/Inactive**. Set start and end dates to define the period the AccountPlan is active for the Account.
        * **AccountPlan per Product**. If an end customer consumes multiple Products, create separate AccountPlans to charge for each Product.

        **AccountPlan Constraints:**
        * Only one AccountPlan per Product can be active at any one time for an Account.
        * If you create a Plan as a custom Plan for a specific Account, you can only use it to create an AccountPlan for that Account.

        **AccountPlanGroups**
        Plan Groups are used when you want to apply a minimum spend amount at billing across several of your Products each of which are priced separately - when you create the Plan Group, you define an overall minimum spend and then add any priced Plans you want to include in the Group. To create an AccounPlanGroup, you can attach a Plan Group to an Account that consumes the separate Products which are priced using the included Plans. At billing, the minimum spend you've defined for the Plan Group is applied:
        * **Active AccountPlanGroup**. Set the start and end dates to define the period for which the Plan Group will be active for the Account.

        **Plan Group Notes:**
        * You can only add *one Plan for the same Product* to a Plan Group. See the [Plan Group](https://www.m3ter.com/docs/api#tag/PlanGroup) in this API Reference for more details on creating Plan Groups.
        * You can create a *custom Plan Group* for an Account, which means the Plan Group can only be attached to that Account to create an AccountPlanGroup.

        **AcountPlanGroup - Notes and Constraints:**
        * **AccountPlanGroup is type of AccountPlan** When you attach a Plan Group to an Account, this creates an AccountPlanGroup. However, the m3ter data model *does not support a separate AccountPlanGroup entity*, and an AccountPlanGroup is a type of AccountPlan where a `planGroupId` is used instead of a `planId` when it's created. See the [Create AccountPlan](https://www.m3ter.com/docs/api#tag/AccountPlan/operation/PostAccountPlan) call in this section and [Attaching Plan Groups to an Account](https://www.m3ter.com/docs/guides/end-customer-accounts/attaching-plan-groups-to-an-account) in our main User Documentation.
        * **Multiple AccountPlan Groups:** You can attach more than one Plan Group to an Account to create multiple AccountPlanGroups, but the rule that *only one attached Plan per Product can be active at any one time for an Account* is preserved:
                * Multiple attached Plan Groups on an Account can have overlapping dates only if none of the Plan Groups contain a Plan belonging to the same Product. If you try to attach a Plan Group to an Account with Plan Groups already attached and:
                        * The new Plan Group contains a Product Plan that also belongs to a Plan Group already attached to the Account.
                        * The dates for these "matched Plan" Plan Groups being active for the Account would overlap.
                        * Then you'll receive an error and the attachment will be blocked.
        """
        from .resources.account_plans import AccountPlansResourceWithStreamingResponse

        return AccountPlansResourceWithStreamingResponse(self._client.account_plans)

    @cached_property
    def aggregations(self) -> aggregations.AggregationsResourceWithStreamingResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Aggregations.

        An Aggregation links to a Meter and targets a Data Field or Derived Field on the Meter. You define the method of aggregation used to convert the usage data collected by the targeted Meter field into a numerical unit of measurement.

        You can then use the unit of measurement an Aggregation yields as a metric for pricing Product Plans and apply usage-based pricing to your products and services. You might also want to aggregate raw data measures for other purposes, such as to feed into analytical or business performance tools.

        **Notes:**
        * **Contrast with Compound Aggregations**. Standard or simple Aggregations of this type, which apply an aggregation method directly to Meter usage data fields, are contrasted with [Compound Aggregations](https://www.m3ter.com/docs/api#tag/CompoundAggregation). A Compound Aggregation typically references one or more simple Aggregations and applies a calculation to them to derive pricing metrics needed to serve more complex usage-based pricing scenarios.
        * **Segmented Aggregations**. Segmented Aggregations allow you to segment the usage data collected by a single Meter. This capability is very useful for implementing some pricing and billing use cases. See [Segmented Aggregations](https://www.m3ter.com/docs/guides/usage-data-aggregations/segmented-aggregations) in our main documentation for more details.
        """
        from .resources.aggregations import AggregationsResourceWithStreamingResponse

        return AggregationsResourceWithStreamingResponse(self._client.aggregations)

    @cached_property
    def balances(self) -> balances.BalancesResourceWithStreamingResponse:
        """Endpoints for creating/retrieving/updating/deleting Balances on Accounts.

        When you have created a Balance for an Account, you can create a positive or negative Transaction amounts for the Balance. To do this, you must first define Transaction Types for your Organization, and then use one of these Transaction Types when you add a specific Transaction to a Balance - see the [Create TransactionType](https://www.m3ter.com/docs/api#tag/TransactionType/operation/CreateTransactionType) call in the Transaction Type section in this API Reference for more details.

        Balances are typically used when a customer prepays an amount to add a credit to their Account, which can then be draw-down against charges due for product or service consumption. You can include options to top-up the original Balance.

        Examples of how Balances for end customer Accounts can be used:

        * Onboarding Balance/Free Trials. Offering an onboarding incentive to new customers as an initial free credit Balance on their Account.

        * Balance as initial commitment. Add a Balance amount to a new customer Account. This acts as an initial commitment, which allows them to use the service and gain an accurate insight into their usage level.

        * Managing Customer Satisfaction. Use Balance as credits that will be applied to subsequent Bills as compensation for acknowledged service delivery issues.

        * Facilitating Balance Adjustments:
                * Apply negative amounts to immediately write-off outstanding Balances.

        #### What is the difference between Balances and Commitments/Prepayments?

        To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

        Commitments - also referred to as Prepayments - are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the commitment or prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

        In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

        You can use Commitments/Prepayments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Commitment credit on an Account is drawn-down - Balance amounts first or Commitment/Prepayment amounts first.
        """
        from .resources.balances import BalancesResourceWithStreamingResponse

        return BalancesResourceWithStreamingResponse(self._client.balances)

    @cached_property
    def bills(self) -> bills.BillsResourceWithStreamingResponse:
        """
        Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills.

        Bills are generated for an Account, and are calculated in accordance with the usage-based pricing Plans applied for the Products the Account consumes. These endpoints enable interaction with the billing system, allowing you to obtain billing details and insights into the consumption patterns and charges of your end-customer Accounts.
        """
        from .resources.bills import BillsResourceWithStreamingResponse

        return BillsResourceWithStreamingResponse(self._client.bills)

    @cached_property
    def bill_config(self) -> bill_config.BillConfigResourceWithStreamingResponse:
        """Endpoints for updating and retreiving the Bill Configuration for an Organization.

        The Organization represents your company as a direct customer of the m3ter service.

        You can use the **Update BillConfig** endpoint to set a global lock date for **all** Bills - any Bill with a service period end date on or before the set date will be locked and cannot be updated.

        **Warning: Ensure all Bills are Approved!** If you try to set a global lock date when there remains Bills in a *Pending* state whose service period end date is on or before the specified lock date, then you'll receive an error.
        """
        from .resources.bill_config import BillConfigResourceWithStreamingResponse

        return BillConfigResourceWithStreamingResponse(self._client.bill_config)

    @cached_property
    def commitments(self) -> commitments.CommitmentsResourceWithStreamingResponse:
        """
        Endpoints that manage Commitments *(also known as Prepayments)* in the context of usage-based pricing and billing. A Commitment represents an agreement where the end-customer has agreed to pay a fixed minimum amount throughout the contract period. ***The commitment amount is payable regardless of the actual usage by the customer of your service or product.***

        These endpoints enable the creation, updating, retrieval, and deletion of Commitments. Use them to manage your customer's Commitments and ensure optimal revenue recognition:
        * Specify which type of charges can draw-down against a Commitment amount on an Account at billing: usage, minimum spend, standing charges, or recurring charges.
        * Define overage surcharge percentages, which are applied when the usage charges exceed the agreed Commitment amount within the contract duration.

        #### What is the difference between Balances and Commitments/Prepayments?

        To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

        Commitments/Prepayments are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

        In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

        You can use Prepayments/Commitments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Prepayment credit on an Account is drawn-down - Balance amounts first or Prepayment amounts first.

        #### Billing for Commitments

        If not all of an agreed Commitment amount is paid at the start of an end-customer contract period, you can choose one of two options for billing the outstanding fees due on the customer Account:
        - Select a Product *Plan to bill with*.
        - Define a *schedule of billing dates*.
        """
        from .resources.commitments import CommitmentsResourceWithStreamingResponse

        return CommitmentsResourceWithStreamingResponse(self._client.commitments)

    @cached_property
    def bill_jobs(self) -> bill_jobs.BillJobsResourceWithStreamingResponse:
        """Endpoints for creating, retrieving, listing, and cancelling Bill Jobs.

        Bill Jobs are critical components in billing management, providing asynchronous mechanisms to calculate and handle bills.

        Bill Jobs give you the flexibiity to run Bills manually for Accounts to suit different billing management purposes. For example, some historical usage data has come in for an Account and you want to run a Bill for a specific date on that Account to check that the Bill is showing correctly for the charges due on the new usage data.
        """
        from .resources.bill_jobs import BillJobsResourceWithStreamingResponse

        return BillJobsResourceWithStreamingResponse(self._client.bill_jobs)

    @cached_property
    def charges(self) -> charges.ChargesResourceWithStreamingResponse:
        """Endpoints for creating/updating/deleting Charges.

        Create Charges for your end-customer Accounts to create ad-hoc line items for Account billing. Charges are:
        * Created for either debit or credit amounts.
        * Linked to a Product for accounting purposes.
        * Optionally linked to a Contract.
        * Given a specific date for billing. When a bill job has run for the specified Charge bill date, a Charge appears as an Ad-hoc line item on the Bill.
        * Assigned a service period.
        * Available in any currency defined for your Organization.
        See [Creating Charges for Accounts](https://www.m3ter.com/docs/guides/end-customer-accounts/creating-charges-for-accounts) in our main user documentation for more details.

        Alternatively, you can create a Charge for a Balance on an end-customer Account to create balance fee line items for Account billing. See [Creating Charges for Balances](https://www.m3ter.com/docs/guides/end-customer-accounts/creating-balances-for-accounts/creating-charges-for-balances) in our main user documentation for more details.
        """
        from .resources.charges import ChargesResourceWithStreamingResponse

        return ChargesResourceWithStreamingResponse(self._client.charges)

    @cached_property
    def compound_aggregations(self) -> compound_aggregations.CompoundAggregationsResourceWithStreamingResponse:
        """
        Endpoints for Compound Aggregation related operations such as creation, update, list and delete.

        Use Compound Aggregations to create numerical measures from usage data by applying a calculation to one or more simple Aggregations or Custom Fields. These numerical measures can then be used as pricing metrics to price your Product Plans, enabling you to implement a wide range of usage-based pricing use cases.

        You can create two types of Compound Aggregation:

        **Global**
        - Pricing: Not tied to any specific product and can be used to price Plans belonging to any Product.
        - Calculation: can reference all simple Aggregations - both Global simple Aggregations and any product-specific simple Aggregations.

        **Product-specific**
        - Pricing: belong to a specific Product and can only be used to price Plans belonging to the same Product.
        - Calculation: can reference any simple Aggregations belonging to the same Product and any Global simple Aggregations.

        **IMPORTANT!** If a simple Aggregation referenced by a Compound Aggregation has a **Quantity per unit** defined or a **Rounding** defined, these will not be factored into the value used by the calculation. For example, if the simple Aggregation referenced has a base value of 100 and has **Quantity per unit** set at 10, the Compound Aggregation calculation *will use the base value of 100 not 10*.

        To better understand and use Compound Aggregations, refer to the example [Compound Aggregation Use Case](https://www.m3ter.com/docs/guides/setting-up-usage-data-meters-and-aggregations/compound-aggregations#example-use-case) in the m3ter documentation.
        """
        from .resources.compound_aggregations import CompoundAggregationsResourceWithStreamingResponse

        return CompoundAggregationsResourceWithStreamingResponse(self._client.compound_aggregations)

    @cached_property
    def contracts(self) -> contracts.ContractsResourceWithStreamingResponse:
        """
        Endpoints for Contract related operations such as creation, update, list and delete.

        Contracts are created for Accounts, which are your end-user customers. Contracts can be used for:
        * **Accounts Reporting**. To serve your general accounting operations and processes, you can report on total Contract values for an Account.
        * **Contract Billing**. Various billing entities associated with an Account can  be linked to Contracts on the Account to meet your specific Contract billing use cases.
        """
        from .resources.contracts import ContractsResourceWithStreamingResponse

        return ContractsResourceWithStreamingResponse(self._client.contracts)

    @cached_property
    def counters(self) -> counters.CountersResourceWithStreamingResponse:
        """Endpoints for listing, creating, retrieving, updating, or deleting Counters.

        You can create Counters for your m3ter Organization, which can then be used as pricing metrics to apply a unit-based [CounterPricing](https://www.m3ter.com/docs/api#tag/CounterPricing) to Product Plans or Plan Templates for recurring subscription charges on Accounts.

        Counters can then be used to post [CounterAdjustments](https://www.m3ter.com/docs/api#tag/CounterAdjustments) on your end-customer Accounts.

        Accounts are then billed in accordance with the CounterPricing on Plans attached to the Accounts and for the actual Counter quantities Accounts subscribe to. See [Recurring Charges: Counters](https://www.m3ter.com/docs/guides/recurring-charges-counters) in our main user documentation for more details.
        """
        from .resources.counters import CountersResourceWithStreamingResponse

        return CountersResourceWithStreamingResponse(self._client.counters)

    @cached_property
    def counter_adjustments(self) -> counter_adjustments.CounterAdjustmentsResourceWithStreamingResponse:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting CounterAdjustments.

        If you attach a Plan to an Account which is priced using a Counter to apply unit-based pricing, you can then create CounterAdjustments for the Account using that Counter to ensure the Account is billed according to the number of Counter units the Account subscribes to in a given billing period.

        See [Understanding and Creating Counter Adjustments for Accounts](https://www.m3ter.com/docs/guides/recurring-charges-counters/creating-counter-adjustments-for-accounts) for more information.
        """
        from .resources.counter_adjustments import CounterAdjustmentsResourceWithStreamingResponse

        return CounterAdjustmentsResourceWithStreamingResponse(self._client.counter_adjustments)

    @cached_property
    def counter_pricings(self) -> counter_pricings.CounterPricingsResourceWithStreamingResponse:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting CounterPricing.

        Create the CounterPricing for a Plan/PlanTemplate using a Counter, and define a unit-based pricing structure for charging end customer Accounts put on the Plan.

        See [Creating Counters and Pricing Plans](https://www.m3ter.com/docs/guides/recurring-charges-counters/creating-counters) for more information.
        """
        from .resources.counter_pricings import CounterPricingsResourceWithStreamingResponse

        return CounterPricingsResourceWithStreamingResponse(self._client.counter_pricings)

    @cached_property
    def credit_reasons(self) -> credit_reasons.CreditReasonsResourceWithStreamingResponse:
        """Endpoints for CreditReason operations such as creation, update, list, and delete.

        You can create CreditReasons for your Organization, and then use them when creating a credit line item on a bill, or applying a product credit to a bill. CreditReasons provide contextual information as to why a credit was applied.
        """
        from .resources.credit_reasons import CreditReasonsResourceWithStreamingResponse

        return CreditReasonsResourceWithStreamingResponse(self._client.credit_reasons)

    @cached_property
    def currencies(self) -> currencies.CurrenciesResourceWithStreamingResponse:
        """Endpoints for Currency operations such as creation, update, list, and delete.

        Currencies are stored for your Organization, and can then be used to specify currencies on various entities such as plan groups and plan templates.

        **IMPORTANT!**
        The Currencies you want to use in your Organization must be created first.

        The currency you select for your Organization determines the billing currency and overrides any currency settings in your pricing Plans.
        For example, if the Organization currency is set to USD and a pricing Plan used for an Account is set to GBP, the bill for an Account using that Plan is calculated in GBP, and then each bill line item converted to USD amounts.

        Currency conversion rates are setup in the *OrganizationConfig*. For more details, see [Creating and Managing Currencies](https://www.m3ter.com/docs/guides/organization-and-access-management/viewing-and-editing-organization#creating-and-managing-currencies) in the m3ter Documentation.
        """
        from .resources.currencies import CurrenciesResourceWithStreamingResponse

        return CurrenciesResourceWithStreamingResponse(self._client.currencies)

    @cached_property
    def custom_fields(self) -> custom_fields.CustomFieldsResourceWithStreamingResponse:
        """
        Endpoints for retrieving and updating Custom Fields at the Organization level for all entities that support them.

        Custom Fields in m3ter allow you to store custom data in the form of number or string values against m3ter entities in a way that does not directly affect the normal working operation of the m3ter platform. Having this capability to store data in a free-hand fashion can prove very useful in helping you to meet specific usage-based pricing and other operational business use cases.

        However, you can exploit the values stored on Custom Fields in a more direct way by referencing them in Derived Field and Compound Aggregation calculations. Given the key role these calculations can play when implementing usage-based pricing schema, any Custom Fields you reference will then affect how the platform behaves. Referencing Custom Field values in your calculations offers a much wider scope of options when it comes to resolving complex usage-based pricing use cases.

        Custom Fields can be added to the following entities at Organizational level:
        * Organization
        * Account
        * AccountPlan
        * Aggregation
        * Compound Aggregation
        * Meter
        * Product
        * Plan
        * PlanTemplate
        * Contract

        These all follow the same pattern - a new *(optional)* field is available on the entity request and response bodies called "customFields" which is a object in this format:
        ```
        "customFields": {
                        "exampleCustomField1": 7.1,
                        "exampleCustomField2": "stringValue"
        }
        ```
        The value for a Custom Field can be a string or a number.

        **Using Custom Field values in calculations:**
        - You can add Custom Fields at two levels - the Organization level and the individual entity level.
        - The Organizational level field provides a default value and *must be added* if you want to also add a Custom Field of the same name at the corresponding individual entity level. If you reference the Custom Field in a calculation, the value for the individual entity level field is used. If no field is defined at individual entity level, then the Organization level field value is used.

        **Important: Constraints and Exceptions!**

        **Custom Fields at Organization Level**. Currently, you cannot create Custom Fields at the Organization-level for the following enitites:
        * Plan Group
        * Balance
        * Balance Transaction Schedule
        * Balance Charge Schedule

        Therefore you cannot reference the Custom Fields values created at the individual entity level for these entities in your Derived Field or Compound Aggregation calculations.

        **Derived Field Calculations**. You can *only reference Custom Fields* for the following entities:
        * Organization
        * Meter
        * Account

        However, if you are using Meters belonging to *a specific Product*, that is, not *Global Meters*, you can also reference Custom Fields added to a Product in Derived Field calculations.

        **Compound Aggregation Calculations - Meter Custom Fields**. The value of the *Organization level Meter Custom Field will always be used*, even if you have defined a corresponding field at the individual Meter level.

        See [Working with Custom Fields](https://www.m3ter.com/docs/guides/creating-and-managing-products/working-with-custom-fields) in the m3ter documentation for more information.
        """
        from .resources.custom_fields import CustomFieldsResourceWithStreamingResponse

        return CustomFieldsResourceWithStreamingResponse(self._client.custom_fields)

    @cached_property
    def data_exports(self) -> data_exports.DataExportsResourceWithStreamingResponse:
        """Endpoints for triggering one-off, ad-hoc Data Exports.

        You can set up and run ad-hoc Exports to export two kinds of data from your m3ter Organization:
        * Usage data.
        * Operational data for entities.

        **Ad-Hoc Export Destinations** When setting up and running an ad-hoc Export:
        * You can define one or more Export Destinations - see the [ExportDestination](https://www.m3ter.com/docs/api#tag/ExportDestination) section of this API Reference. When the export runs, the data is sent through to the sepecified Destination. However, the export file is also made available for you to download it locally.
        * You can set up and run Data Exports without defining a Destination. The data is not exported but the compiled export file is made available for downloading locally.
        * For details on downloading an export file, see the [Get Data Export File Download URL](https://www.m3ter.com/docs/api#tag/ExportDestination/operation/GenerateDataExportFileDownloadUrl) endpoint in this API Reference.

        **Preview Version!** The Data Export feature is currently available only in Preview release version. See [Feature Release Stages](https://www.m3ter.com/docs/guides/getting-started/feature-release-stages) for Preview release definition. ExportAdHoc endpoints will only be available if Data Export has been enabled for your Organization. For more details see [Data Export(Preview)](https://www.m3ter.com/docs/guides/data-exports) in our main User documentation. If you're interested in previewing the Data Export feature, please get in touch with m3ter Support or your m3ter contact.
        """
        from .resources.data_exports import DataExportsResourceWithStreamingResponse

        return DataExportsResourceWithStreamingResponse(self._client.data_exports)

    @cached_property
    def debit_reasons(self) -> debit_reasons.DebitReasonsResourceWithStreamingResponse:
        """Endpoints for DebitReason operations such as creation, update, list, and delete.

        You can create DebitReasons for your Organization, and then use them when creating a debit line item on a bill, or applying a product debit to a bill. DebitReasons provide contextual information as to why a debit was applied.
        """
        from .resources.debit_reasons import DebitReasonsResourceWithStreamingResponse

        return DebitReasonsResourceWithStreamingResponse(self._client.debit_reasons)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
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
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def external_mappings(self) -> external_mappings.ExternalMappingsResourceWithStreamingResponse:
        """
        Endpoints for managing External Mapping related operations such as creation, update, list and delete.

        When you integrate your 3rd-party systems with the m3ter platform, a mapping between entities in the local system *(m3ter)* and external systems is constructed. This *External Mapping* is crucial in scenarios where data from external systems is consumed or where data from the local system is to be synchronized with external systems.

        When you are working to set up your Integrations and want to test or troubleshoot your implementation before going live, you might need to create External Mappings manually and, at a later date, edit or delete them.
        """
        from .resources.external_mappings import ExternalMappingsResourceWithStreamingResponse

        return ExternalMappingsResourceWithStreamingResponse(self._client.external_mappings)

    @cached_property
    def integration_configurations(
        self,
    ) -> integration_configurations.IntegrationConfigurationsResourceWithStreamingResponse:
        """
        A suite of endpoints for configuring and managing third party integrations within the m3ter platform. The integration endpoints in this section facilitate various operations such as creating, updating, listing, and deletion of integrations.

        m3ter integrations enable seamless data synchronization and mapping with external systems required in core business processes. These processes often include sales, pricing, billing and invoicing, and general finance.

        With m3ter integrations, you can establish robust connections with popular business platforms, enhancing your operational capabilities. For example:
        * Chargebee
        * Salesforce
        * Stripe
        * Netsuite
        * Paddle
        * Xero
        * QuickBooks
        """
        from .resources.integration_configurations import IntegrationConfigurationsResourceWithStreamingResponse

        return IntegrationConfigurationsResourceWithStreamingResponse(self._client.integration_configurations)

    @cached_property
    def lookup_tables(self) -> lookup_tables.LookupTablesResourceWithStreamingResponse:
        """Endpoints for creating/updating/deleting Lookup Tables.

        Lookup Tables enable you to manage dynamic data mappings that your calculations reference. Use them for currency conversion, pricing tiers, discount rates, and similar scenarios where you require values to change operationally but for calculation logic to remain constant.

        **Beta Version!** The Lookup Table feature is currently available in Beta release version. See [Feature Release Stages](https://www.m3ter.com/docs/guides/getting-started/feature-release-stages) for Beta release definition. Lookup Table endpoints will only be available if Lookup Tables have been enabled for your Organization. For more details see [Lookup Tables (Beta)](https://www.m3ter.com/docs/guides/lookup-tables) in our main User documentation.
        """
        from .resources.lookup_tables import LookupTablesResourceWithStreamingResponse

        return LookupTablesResourceWithStreamingResponse(self._client.lookup_tables)

    @cached_property
    def meters(self) -> meters.MetersResourceWithStreamingResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Meters.

        Use Meters to submit usage data for the consumption of your products and services by end customers. This usage data then becomes the basis for setting up usage-based pricing for your products and services.

        Examples of usage data collected in Meters:
        * Number of logins.
        * Duration of session.
        * Amount of data downloaded.

        To collect usage data and ingest it into the platform, you can define two types of fields for Meters:
        - `dataFields` Used to collect raw usage data measures - numeric quantitative data values or non-numeric point data values.
        - `derivedFields` Used to derive usage data measures that are the result of applying a calculation to `dataFields`, `customFields`, or system `Timestamp` fields.

        You can also:
        - Create `customFields` for a Meter, which allows you to attach custom data to the Meter as name/value pairs.
        - Create Global Meters, which are not tied to a specific Product and allow you to collect usage data that will form the basis of usage-based pricing across multiple Products.

        **IMPORTANT! - use of PII:** The use of any of your end-customers' Personally Identifiable Information (PII) in m3ter is restricted to a few fields on the **Account** entity. Please ensure that any fields you configure for Meters, such as Data Fields or Derived Fields, do not contain any end-customer PII data. See the [Introduction section](https://www.m3ter.com/docs/api#section/Introduction) above for more details.

        See also:
        - [Reviewing Meter Options](https://www.m3ter.com/docs/guides/setting-up-usage-data-meters-and-aggregations/reviewing-meter-options).
        """
        from .resources.meters import MetersResourceWithStreamingResponse

        return MetersResourceWithStreamingResponse(self._client.meters)

    @cached_property
    def notification_configurations(
        self,
    ) -> notification_configurations.NotificationConfigurationsResourceWithStreamingResponse:
        """This section provides endpoints for managing Event Notifications.

        You can create Notifications based on system Events generated by the platform. When you base a Notification on a specific Event type, you can include a calculation that references the fields available on that Event type to define precise conditions that must be met for the Notification to be triggered when an Event of that type occurs. In this way, you can set up highly customized Notifications that act as timely alerts to inform you about significant occurrences within your Organization. For instance, if you provide a sign-up bonus to new end-customer Accounts, you can set up a Notification to alert you when an end-customer Account has used up a certain percentage of their bonus credit.

        You can also set up Notifications based on Scheduled Event types you've created for your Organization. See the [ScheduledEventConfigurations](https://www.m3ter.com/docs/api#tag/ScheduledEventConfigurations) section of this API Reference and [Working with Scheduled Events](https://www.m3ter.com/docs/guides/alerts-events-and-notifications/utilizing-events-and-notifications/working-with-scheduled-events) in our user documentation.

        For more details on Event types and their fields, see the [Events](https://www.m3ter.com/docs/api#tag/Events) section.

        For detailed guidance on working with Events and Notifications, refer to the [Utilizing Events and Notifications](https://www.m3ter.com/docs/guides/utilizing-events-and-notifications) section of the m3ter user documentation.
        """
        from .resources.notification_configurations import NotificationConfigurationsResourceWithStreamingResponse

        return NotificationConfigurationsResourceWithStreamingResponse(self._client.notification_configurations)

    @cached_property
    def organization_config(self) -> organization_config.OrganizationConfigResourceWithStreamingResponse:
        """Endpoints for retrieving or updating the Organization Config.

        Organization represents your company as a direct customer of m3ter. Use Organization configuration to define *Organization-wide* settings. For example:
        - Timezone.
        - Currencies and currency conversions.
        - Billing operations settings, such as:
                - Epoch dates to control first billing dates.
                - Whether to bill customer accounts in advance/in arrears for standing charge amounts, minimum spend amounts, and commitment fees.

        For other aspects of your Organization setup and configuration, see the following sections in this API Reference:
        * [Custom Fields](https://www.m3ter.com/docs/api#tag/CustomField)
        * [Currencies](https://www.m3ter.com/docs/api#tag/Currency)
        * [Credit Reasons](https://www.m3ter.com/docs/api#tag/CreditReason)
        * [Debit Reason](https://www.m3ter.com/docs/api#tag/DebitReason)
        * [Transaction Types](https://www.m3ter.com/docs/api#tag/TransactionType)

        See also:
        - [Managing your Organization](https://www.m3ter.com/docs/guides/managing-organization-and-users/viewing-and-editing-organization).
        """
        from .resources.organization_config import OrganizationConfigResourceWithStreamingResponse

        return OrganizationConfigResourceWithStreamingResponse(self._client.organization_config)

    @cached_property
    def permission_policies(self) -> permission_policies.PermissionPoliciesResourceWithStreamingResponse:
        """
        Endpoints for Permission Policy related operations such as creation, update, add and retrieve.

        Permission Policies can restrict or grant access to specific resources for both Users *(people)* and Service Users *(automated processes with direct API access)*. This enables you to control precisely what a User can do in your m3ter Organization.

        For more details, see [Understanding, Creating, and Managing Permission Policies](https://www.m3ter.com/docs/guides/organization-and-access-management/creating-and-managing-permissions#permission-policy-statements---available-actions-and-resources) in our main Documentation.
        """
        from .resources.permission_policies import PermissionPoliciesResourceWithStreamingResponse

        return PermissionPoliciesResourceWithStreamingResponse(self._client.permission_policies)

    @cached_property
    def plans(self) -> plans.PlansResourceWithStreamingResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Plans.

        A Plan is based on a PlanTemplate and represents a specific pricing plan for one of your products or services. Each Plan inherits general billing attributes or pricing structure from its parent Plan Template. Some attributes can be overriden for the specific Plan.

        When you've created the Plan Templates and Plans you need for your Products, you can configure the exact pricing structures for Plans to charge customers that consume one or more of your Products.

        You can then attach the appropriately priced Plans to customer Accounts to create [Account Plans](https://www.m3ter.com/docs/api#tag/AccountPlan) and enable charges to be calculated correctly for billing against those Accounts.

        See also:
        - [Reviewing Options for Plans and Plan Templates](https://www.m3ter.com/docs/guides/working-with-plan-templates-and-plans/reviewing-configuration-options-for-plans-and-plan-templates).
        """
        from .resources.plans import PlansResourceWithStreamingResponse

        return PlansResourceWithStreamingResponse(self._client.plans)

    @cached_property
    def plan_groups(self) -> plan_groups.PlanGroupsResourceWithStreamingResponse:
        """
        Endpoints for PlanGroup related operations such as creation, update, retrieve, list and delete.

        PlanGroups are constructs that group multiple plans together. This enables a unified approach to efficiently handle various uses cases across different plans. For example applying a minimum spend amount at billing, across several of your products or features that are each priced separately.
        """
        from .resources.plan_groups import PlanGroupsResourceWithStreamingResponse

        return PlanGroupsResourceWithStreamingResponse(self._client.plan_groups)

    @cached_property
    def plan_group_links(self) -> plan_group_links.PlanGroupLinksResourceWithStreamingResponse:
        """
        Endpoints for PlanGroupLink related operations such as creation, update, list and delete.

        PlanGroupLinks are the intersection table between a PlanGroup and its associated Plans. A PlanGroupLink is only created when at least 1 Plan is linked to a PlanGroup.
        """
        from .resources.plan_group_links import PlanGroupLinksResourceWithStreamingResponse

        return PlanGroupLinksResourceWithStreamingResponse(self._client.plan_group_links)

    @cached_property
    def plan_templates(self) -> plan_templates.PlanTemplatesResourceWithStreamingResponse:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting PlanTemplates.

        Use PlanTemplates to define default values for Plans. These default values control the billing operations you want applied to your products. PlanTemplates avoid repetition in configuration work - many Plans will share settings for billing operations and differ only in the details of their pricing structures.

        A PlanTemplate is linked to a Product, and each Plan is a child of a PlanTemplate.
        """
        from .resources.plan_templates import PlanTemplatesResourceWithStreamingResponse

        return PlanTemplatesResourceWithStreamingResponse(self._client.plan_templates)

    @cached_property
    def pricings(self) -> pricings.PricingsResourceWithStreamingResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Pricing.

        Create the Pricing for a Plan/PlanTemplate with usage data Aggregations, and define a usage-based pricing structure for charging end customer Accounts put on the Plan.

        See [Reviewing Pricing Options for Plans and Plan Templates](https://www.m3ter.com/docs/guides/pricing-plans/reviewing-pricing-options-and-pricing-plans) for more information.
        """
        from .resources.pricings import PricingsResourceWithStreamingResponse

        return PricingsResourceWithStreamingResponse(self._client.pricings)

    @cached_property
    def products(self) -> products.ProductsResourceWithStreamingResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Products.

        A Product represents the products and services you offer to your end customers. Products act as a container for the Meters, Aggregations, Pricing, and Plans required to implement usage-based and other pricing models for your Organization.
        """
        from .resources.products import ProductsResourceWithStreamingResponse

        return ProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def resource_groups(self) -> resource_groups.ResourceGroupsResourceWithStreamingResponse:
        """
        Endpoints for ResourceGroup related operations such as creation, update, list and delete.

        ResourceGroups are used in the context of Permission Policies, which controls what a User who has been given access to your Organization can and cannot do. For example, you might want to create a Permissions Policy that denies Users the ability to retrieve Meters.

        Resources are defined as m3ter Resource Identifiers *(MRIs)* in the format:

        ```
        service: resource - type / item - type / id
        ```

        Where:

        * service is a distinct part of the overall m3ter system, and which forms a natural functional grouping, such as "config" or "billing".

        * resource-type is the resource type item accessed - for example: "Plan", "Meter", "Bill"

        * item-type is one of:

                * "item" - to specify an individual item.

                * "group" - to specify a resource group.

        * id is the resource group id or the resource item id

        Resources can be assigned to one or more ResourceGroups. For example, a Plan can be assigned to Plan ResourceGroups, a Meter can be assigned to Meter ResourceGroups, and so on. This is useful for cases where you want to create Permission Policies which allow or deny access to a specific subset of resources. For example, grant a user access to only some of the Plans in your Organization.

        This concept of grouping resources applies to every resource in m3ter, including ResourceGroups themselves. This allows you to nest ResourceGroups to support hierarchies of groups.

        See [Understanding, Creating, and Managing Permission Policies](https://www.m3ter.com/docs/guides/managing-organization-and-users/creating-and-managing-permissions) in the m3ter documentation for more information.

        **Note: User Resource Groups** You can create a User Resource Group to group resources of type = `user`. You can then retrieve a list of the User Resource Groups a user belongs to. For more details, see the [Retrieve OrgUser Groups](https://www.m3ter.com/docs/api#tag/OrgUsers/operation/GetOrgUserGroups) call in the OrgUsers section.
        """
        from .resources.resource_groups import ResourceGroupsResourceWithStreamingResponse

        return ResourceGroupsResourceWithStreamingResponse(self._client.resource_groups)

    @cached_property
    def scheduled_event_configurations(
        self,
    ) -> scheduled_event_configurations.ScheduledEventConfigurationsResourceWithStreamingResponse:
        """Endpoints for retrieving and managing scheduled Events' configurations.

        Scheduled Event Configurations define custom Event types that reference Date/Time fields belonging to configuration and billing entities. They therefore provide you with an extra degree of flexibility over and above system-generated Events for setting up Notifications based on Events.

        For more details, see the [Working with Scheduled Events](https://www.m3ter.com/docs/guides/alerts-events-and-notifications/utilizing-events-and-notifications/working-with-scheduled-events) in our Documenation.
        """
        from .resources.scheduled_event_configurations import ScheduledEventConfigurationsResourceWithStreamingResponse

        return ScheduledEventConfigurationsResourceWithStreamingResponse(self._client.scheduled_event_configurations)

    @cached_property
    def statements(self) -> statements.StatementsResourceWithStreamingResponse:
        """
        Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills.

        Bills are generated for an Account, and are calculated in accordance with the usage-based pricing Plans applied for the Products the Account consumes. These endpoints enable interaction with the billing system, allowing you to obtain billing details and insights into the consumption patterns and charges of your end-customer Accounts.
        """
        from .resources.statements import StatementsResourceWithStreamingResponse

        return StatementsResourceWithStreamingResponse(self._client.statements)

    @cached_property
    def transaction_types(self) -> transaction_types.TransactionTypesResourceWithStreamingResponse:
        """
        Endpoints for TransactionType operations such as creation, update, list, retrieve, and delete.

        You can create TransactionTypes for your Organization, which can then be used when creating and updating Balances. Example TransactionTypes: "Balance Amount" or "Add Funds".

        For details on creating a Transaction amount for a Balance using a TransactionType you've created for your Organization, see the [Create Balance Transaction](https://www.m3ter.com/docs/api#tag/Balances/operation/PostBalanceTransaction) call in the [Balances](https://www.m3ter.com/docs/api#tag/Balances) section of this API Reference.
        """
        from .resources.transaction_types import TransactionTypesResourceWithStreamingResponse

        return TransactionTypesResourceWithStreamingResponse(self._client.transaction_types)

    @cached_property
    def usage(self) -> usage.UsageResourceWithStreamingResponse:
        from .resources.usage import UsageResourceWithStreamingResponse

        return UsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        """
        A suite of endpoints for configuring and managing third party integrations within the m3ter platform. The integration endpoints in this section facilitate various operations such as creating, updating, listing, and deletion of integrations.

        m3ter integrations enable seamless data synchronization and mapping with external systems required in core business processes. These processes often include sales, pricing, billing and invoicing, and general finance.

        With m3ter integrations, you can establish robust connections with popular business platforms, enhancing your operational capabilities. For example:
        * Chargebee
        * Salesforce
        * Stripe
        * Netsuite
        * Paddle
        * Xero
        * QuickBooks
        """
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)


class AsyncM3terWithStreamedResponse:
    _client: AsyncM3ter

    def __init__(self, client: AsyncM3ter) -> None:
        self._client = client

    @cached_property
    def authentication(self) -> authentication.AsyncAuthenticationResourceWithStreamingResponse:
        """
        Endpoint for retrieving a JSON Web Token (JWT) bearer token for a ServiceUser using the Client Credentials Grant flow.

        A ServiceUser represents the automated process you want to grant access to your Organization - that is, as an API user.
        """
        from .resources.authentication import AsyncAuthenticationResourceWithStreamingResponse

        return AsyncAuthenticationResourceWithStreamingResponse(self._client.authentication)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        """
        Endpoints for Account related operations such as creation, update, list and delete.
        An Account represents one of your end-customer accounts.

        Accounts do not belong to a Product to allow for cases where an end customer takes more than one of your Products, and the charges for these Products differ.

        You typically attach a priced Plan or Plan Template to an Account before you can generate bills for the Account:
        - If a customer consumes several of your Products, you can attach a priced Plan or Plan Template to the Account for charging against each Product.
        - If an Account is charged solely on the basis of an agreed Prepayment/Commitment amount but not all of the Prepayment is prepaid, you can use a customized billing schedule for outstanding fees without having to attach a Plan to the Account to generate Bills.

        You can create Child Accounts for end customers who hold multiple Accounts with you. You can then set up billing for the Parent/Child Account usage to have the end-customer billed once for the Parent Account, instead of having separate bills issued for usage against each of their multiple Accounts.

        **IMPORTANT! - use of PII:** The use of any of your end-customers' Personally Identifiable Information (PII) in m3ter is restricted to a few fields on the **Account** entity. Please ensure that only the ``name``, ``address``, or ``emailAddress`` fields contain any end-customer PII data on any Accounts you create. See the [Introduction section](https://www.m3ter.com/docs/api#section/Introduction) above for more details.
        """
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def account_plans(self) -> account_plans.AsyncAccountPlansResourceWithStreamingResponse:
        """
        Endpoints for AccountPlan and AccountPlanGroup related operations such as creation, update, list and delete.

        **AccountPlans**
        An Account represents one of your end-customer accounts. To create an AccountPlan, you attach a Product Plan to an Account. The AccountPlan then determines the charges incurred at billing by your end customer for consuming the Product the Plan is for:
        * **AccountPlan Active/Inactive**. Set start and end dates to define the period the AccountPlan is active for the Account.
        * **AccountPlan per Product**. If an end customer consumes multiple Products, create separate AccountPlans to charge for each Product.

        **AccountPlan Constraints:**
        * Only one AccountPlan per Product can be active at any one time for an Account.
        * If you create a Plan as a custom Plan for a specific Account, you can only use it to create an AccountPlan for that Account.

        **AccountPlanGroups**
        Plan Groups are used when you want to apply a minimum spend amount at billing across several of your Products each of which are priced separately - when you create the Plan Group, you define an overall minimum spend and then add any priced Plans you want to include in the Group. To create an AccounPlanGroup, you can attach a Plan Group to an Account that consumes the separate Products which are priced using the included Plans. At billing, the minimum spend you've defined for the Plan Group is applied:
        * **Active AccountPlanGroup**. Set the start and end dates to define the period for which the Plan Group will be active for the Account.

        **Plan Group Notes:**
        * You can only add *one Plan for the same Product* to a Plan Group. See the [Plan Group](https://www.m3ter.com/docs/api#tag/PlanGroup) in this API Reference for more details on creating Plan Groups.
        * You can create a *custom Plan Group* for an Account, which means the Plan Group can only be attached to that Account to create an AccountPlanGroup.

        **AcountPlanGroup - Notes and Constraints:**
        * **AccountPlanGroup is type of AccountPlan** When you attach a Plan Group to an Account, this creates an AccountPlanGroup. However, the m3ter data model *does not support a separate AccountPlanGroup entity*, and an AccountPlanGroup is a type of AccountPlan where a `planGroupId` is used instead of a `planId` when it's created. See the [Create AccountPlan](https://www.m3ter.com/docs/api#tag/AccountPlan/operation/PostAccountPlan) call in this section and [Attaching Plan Groups to an Account](https://www.m3ter.com/docs/guides/end-customer-accounts/attaching-plan-groups-to-an-account) in our main User Documentation.
        * **Multiple AccountPlan Groups:** You can attach more than one Plan Group to an Account to create multiple AccountPlanGroups, but the rule that *only one attached Plan per Product can be active at any one time for an Account* is preserved:
                * Multiple attached Plan Groups on an Account can have overlapping dates only if none of the Plan Groups contain a Plan belonging to the same Product. If you try to attach a Plan Group to an Account with Plan Groups already attached and:
                        * The new Plan Group contains a Product Plan that also belongs to a Plan Group already attached to the Account.
                        * The dates for these "matched Plan" Plan Groups being active for the Account would overlap.
                        * Then you'll receive an error and the attachment will be blocked.
        """
        from .resources.account_plans import AsyncAccountPlansResourceWithStreamingResponse

        return AsyncAccountPlansResourceWithStreamingResponse(self._client.account_plans)

    @cached_property
    def aggregations(self) -> aggregations.AsyncAggregationsResourceWithStreamingResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Aggregations.

        An Aggregation links to a Meter and targets a Data Field or Derived Field on the Meter. You define the method of aggregation used to convert the usage data collected by the targeted Meter field into a numerical unit of measurement.

        You can then use the unit of measurement an Aggregation yields as a metric for pricing Product Plans and apply usage-based pricing to your products and services. You might also want to aggregate raw data measures for other purposes, such as to feed into analytical or business performance tools.

        **Notes:**
        * **Contrast with Compound Aggregations**. Standard or simple Aggregations of this type, which apply an aggregation method directly to Meter usage data fields, are contrasted with [Compound Aggregations](https://www.m3ter.com/docs/api#tag/CompoundAggregation). A Compound Aggregation typically references one or more simple Aggregations and applies a calculation to them to derive pricing metrics needed to serve more complex usage-based pricing scenarios.
        * **Segmented Aggregations**. Segmented Aggregations allow you to segment the usage data collected by a single Meter. This capability is very useful for implementing some pricing and billing use cases. See [Segmented Aggregations](https://www.m3ter.com/docs/guides/usage-data-aggregations/segmented-aggregations) in our main documentation for more details.
        """
        from .resources.aggregations import AsyncAggregationsResourceWithStreamingResponse

        return AsyncAggregationsResourceWithStreamingResponse(self._client.aggregations)

    @cached_property
    def balances(self) -> balances.AsyncBalancesResourceWithStreamingResponse:
        """Endpoints for creating/retrieving/updating/deleting Balances on Accounts.

        When you have created a Balance for an Account, you can create a positive or negative Transaction amounts for the Balance. To do this, you must first define Transaction Types for your Organization, and then use one of these Transaction Types when you add a specific Transaction to a Balance - see the [Create TransactionType](https://www.m3ter.com/docs/api#tag/TransactionType/operation/CreateTransactionType) call in the Transaction Type section in this API Reference for more details.

        Balances are typically used when a customer prepays an amount to add a credit to their Account, which can then be draw-down against charges due for product or service consumption. You can include options to top-up the original Balance.

        Examples of how Balances for end customer Accounts can be used:

        * Onboarding Balance/Free Trials. Offering an onboarding incentive to new customers as an initial free credit Balance on their Account.

        * Balance as initial commitment. Add a Balance amount to a new customer Account. This acts as an initial commitment, which allows them to use the service and gain an accurate insight into their usage level.

        * Managing Customer Satisfaction. Use Balance as credits that will be applied to subsequent Bills as compensation for acknowledged service delivery issues.

        * Facilitating Balance Adjustments:
                * Apply negative amounts to immediately write-off outstanding Balances.

        #### What is the difference between Balances and Commitments/Prepayments?

        To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

        Commitments - also referred to as Prepayments - are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the commitment or prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

        In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

        You can use Commitments/Prepayments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Commitment credit on an Account is drawn-down - Balance amounts first or Commitment/Prepayment amounts first.
        """
        from .resources.balances import AsyncBalancesResourceWithStreamingResponse

        return AsyncBalancesResourceWithStreamingResponse(self._client.balances)

    @cached_property
    def bills(self) -> bills.AsyncBillsResourceWithStreamingResponse:
        """
        Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills.

        Bills are generated for an Account, and are calculated in accordance with the usage-based pricing Plans applied for the Products the Account consumes. These endpoints enable interaction with the billing system, allowing you to obtain billing details and insights into the consumption patterns and charges of your end-customer Accounts.
        """
        from .resources.bills import AsyncBillsResourceWithStreamingResponse

        return AsyncBillsResourceWithStreamingResponse(self._client.bills)

    @cached_property
    def bill_config(self) -> bill_config.AsyncBillConfigResourceWithStreamingResponse:
        """Endpoints for updating and retreiving the Bill Configuration for an Organization.

        The Organization represents your company as a direct customer of the m3ter service.

        You can use the **Update BillConfig** endpoint to set a global lock date for **all** Bills - any Bill with a service period end date on or before the set date will be locked and cannot be updated.

        **Warning: Ensure all Bills are Approved!** If you try to set a global lock date when there remains Bills in a *Pending* state whose service period end date is on or before the specified lock date, then you'll receive an error.
        """
        from .resources.bill_config import AsyncBillConfigResourceWithStreamingResponse

        return AsyncBillConfigResourceWithStreamingResponse(self._client.bill_config)

    @cached_property
    def commitments(self) -> commitments.AsyncCommitmentsResourceWithStreamingResponse:
        """
        Endpoints that manage Commitments *(also known as Prepayments)* in the context of usage-based pricing and billing. A Commitment represents an agreement where the end-customer has agreed to pay a fixed minimum amount throughout the contract period. ***The commitment amount is payable regardless of the actual usage by the customer of your service or product.***

        These endpoints enable the creation, updating, retrieval, and deletion of Commitments. Use them to manage your customer's Commitments and ensure optimal revenue recognition:
        * Specify which type of charges can draw-down against a Commitment amount on an Account at billing: usage, minimum spend, standing charges, or recurring charges.
        * Define overage surcharge percentages, which are applied when the usage charges exceed the agreed Commitment amount within the contract duration.

        #### What is the difference between Balances and Commitments/Prepayments?

        To manage credit amounts for your end-customer Accounts, you can use Balances or Commitments/Prepayments. However, these two kinds of credits for Accounts serve different purposes.

        Commitments/Prepayments are used for amounts end-customers have agreed to pay for consuming your product or services across a full contract term. A customer might pay the entire or only part of the agreed amount upfront, but ***the prepayment amount is payable regardless of the actual usage by the customer of your service or product.***

        In contrast, a Balance - often referred to as a Top-Up or Prepaid draw-down - is used when a customer wants to add a credit amount to their Account at any time during the service period or when you as service provider want to add a credit to a customer Account. This Balance credit can then be drawn-down against for billing the Account for usage, minimum spend, standing charges, or recurring charges due. Balances therefore serve payment use cases in a more flexible way, for example to be used for a "Free Credit" sign-up scheme you offer to encourage sales or to enhance customer satisfaction by adding credit to an Account to compensate for service delivery issues.

        You can use Prepayments/Commitments and Balances together on Account, and define at Organization or individual Account level the order in which any Balance/Prepayment credit on an Account is drawn-down - Balance amounts first or Prepayment amounts first.

        #### Billing for Commitments

        If not all of an agreed Commitment amount is paid at the start of an end-customer contract period, you can choose one of two options for billing the outstanding fees due on the customer Account:
        - Select a Product *Plan to bill with*.
        - Define a *schedule of billing dates*.
        """
        from .resources.commitments import AsyncCommitmentsResourceWithStreamingResponse

        return AsyncCommitmentsResourceWithStreamingResponse(self._client.commitments)

    @cached_property
    def bill_jobs(self) -> bill_jobs.AsyncBillJobsResourceWithStreamingResponse:
        """Endpoints for creating, retrieving, listing, and cancelling Bill Jobs.

        Bill Jobs are critical components in billing management, providing asynchronous mechanisms to calculate and handle bills.

        Bill Jobs give you the flexibiity to run Bills manually for Accounts to suit different billing management purposes. For example, some historical usage data has come in for an Account and you want to run a Bill for a specific date on that Account to check that the Bill is showing correctly for the charges due on the new usage data.
        """
        from .resources.bill_jobs import AsyncBillJobsResourceWithStreamingResponse

        return AsyncBillJobsResourceWithStreamingResponse(self._client.bill_jobs)

    @cached_property
    def charges(self) -> charges.AsyncChargesResourceWithStreamingResponse:
        """Endpoints for creating/updating/deleting Charges.

        Create Charges for your end-customer Accounts to create ad-hoc line items for Account billing. Charges are:
        * Created for either debit or credit amounts.
        * Linked to a Product for accounting purposes.
        * Optionally linked to a Contract.
        * Given a specific date for billing. When a bill job has run for the specified Charge bill date, a Charge appears as an Ad-hoc line item on the Bill.
        * Assigned a service period.
        * Available in any currency defined for your Organization.
        See [Creating Charges for Accounts](https://www.m3ter.com/docs/guides/end-customer-accounts/creating-charges-for-accounts) in our main user documentation for more details.

        Alternatively, you can create a Charge for a Balance on an end-customer Account to create balance fee line items for Account billing. See [Creating Charges for Balances](https://www.m3ter.com/docs/guides/end-customer-accounts/creating-balances-for-accounts/creating-charges-for-balances) in our main user documentation for more details.
        """
        from .resources.charges import AsyncChargesResourceWithStreamingResponse

        return AsyncChargesResourceWithStreamingResponse(self._client.charges)

    @cached_property
    def compound_aggregations(self) -> compound_aggregations.AsyncCompoundAggregationsResourceWithStreamingResponse:
        """
        Endpoints for Compound Aggregation related operations such as creation, update, list and delete.

        Use Compound Aggregations to create numerical measures from usage data by applying a calculation to one or more simple Aggregations or Custom Fields. These numerical measures can then be used as pricing metrics to price your Product Plans, enabling you to implement a wide range of usage-based pricing use cases.

        You can create two types of Compound Aggregation:

        **Global**
        - Pricing: Not tied to any specific product and can be used to price Plans belonging to any Product.
        - Calculation: can reference all simple Aggregations - both Global simple Aggregations and any product-specific simple Aggregations.

        **Product-specific**
        - Pricing: belong to a specific Product and can only be used to price Plans belonging to the same Product.
        - Calculation: can reference any simple Aggregations belonging to the same Product and any Global simple Aggregations.

        **IMPORTANT!** If a simple Aggregation referenced by a Compound Aggregation has a **Quantity per unit** defined or a **Rounding** defined, these will not be factored into the value used by the calculation. For example, if the simple Aggregation referenced has a base value of 100 and has **Quantity per unit** set at 10, the Compound Aggregation calculation *will use the base value of 100 not 10*.

        To better understand and use Compound Aggregations, refer to the example [Compound Aggregation Use Case](https://www.m3ter.com/docs/guides/setting-up-usage-data-meters-and-aggregations/compound-aggregations#example-use-case) in the m3ter documentation.
        """
        from .resources.compound_aggregations import AsyncCompoundAggregationsResourceWithStreamingResponse

        return AsyncCompoundAggregationsResourceWithStreamingResponse(self._client.compound_aggregations)

    @cached_property
    def contracts(self) -> contracts.AsyncContractsResourceWithStreamingResponse:
        """
        Endpoints for Contract related operations such as creation, update, list and delete.

        Contracts are created for Accounts, which are your end-user customers. Contracts can be used for:
        * **Accounts Reporting**. To serve your general accounting operations and processes, you can report on total Contract values for an Account.
        * **Contract Billing**. Various billing entities associated with an Account can  be linked to Contracts on the Account to meet your specific Contract billing use cases.
        """
        from .resources.contracts import AsyncContractsResourceWithStreamingResponse

        return AsyncContractsResourceWithStreamingResponse(self._client.contracts)

    @cached_property
    def counters(self) -> counters.AsyncCountersResourceWithStreamingResponse:
        """Endpoints for listing, creating, retrieving, updating, or deleting Counters.

        You can create Counters for your m3ter Organization, which can then be used as pricing metrics to apply a unit-based [CounterPricing](https://www.m3ter.com/docs/api#tag/CounterPricing) to Product Plans or Plan Templates for recurring subscription charges on Accounts.

        Counters can then be used to post [CounterAdjustments](https://www.m3ter.com/docs/api#tag/CounterAdjustments) on your end-customer Accounts.

        Accounts are then billed in accordance with the CounterPricing on Plans attached to the Accounts and for the actual Counter quantities Accounts subscribe to. See [Recurring Charges: Counters](https://www.m3ter.com/docs/guides/recurring-charges-counters) in our main user documentation for more details.
        """
        from .resources.counters import AsyncCountersResourceWithStreamingResponse

        return AsyncCountersResourceWithStreamingResponse(self._client.counters)

    @cached_property
    def counter_adjustments(self) -> counter_adjustments.AsyncCounterAdjustmentsResourceWithStreamingResponse:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting CounterAdjustments.

        If you attach a Plan to an Account which is priced using a Counter to apply unit-based pricing, you can then create CounterAdjustments for the Account using that Counter to ensure the Account is billed according to the number of Counter units the Account subscribes to in a given billing period.

        See [Understanding and Creating Counter Adjustments for Accounts](https://www.m3ter.com/docs/guides/recurring-charges-counters/creating-counter-adjustments-for-accounts) for more information.
        """
        from .resources.counter_adjustments import AsyncCounterAdjustmentsResourceWithStreamingResponse

        return AsyncCounterAdjustmentsResourceWithStreamingResponse(self._client.counter_adjustments)

    @cached_property
    def counter_pricings(self) -> counter_pricings.AsyncCounterPricingsResourceWithStreamingResponse:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting CounterPricing.

        Create the CounterPricing for a Plan/PlanTemplate using a Counter, and define a unit-based pricing structure for charging end customer Accounts put on the Plan.

        See [Creating Counters and Pricing Plans](https://www.m3ter.com/docs/guides/recurring-charges-counters/creating-counters) for more information.
        """
        from .resources.counter_pricings import AsyncCounterPricingsResourceWithStreamingResponse

        return AsyncCounterPricingsResourceWithStreamingResponse(self._client.counter_pricings)

    @cached_property
    def credit_reasons(self) -> credit_reasons.AsyncCreditReasonsResourceWithStreamingResponse:
        """Endpoints for CreditReason operations such as creation, update, list, and delete.

        You can create CreditReasons for your Organization, and then use them when creating a credit line item on a bill, or applying a product credit to a bill. CreditReasons provide contextual information as to why a credit was applied.
        """
        from .resources.credit_reasons import AsyncCreditReasonsResourceWithStreamingResponse

        return AsyncCreditReasonsResourceWithStreamingResponse(self._client.credit_reasons)

    @cached_property
    def currencies(self) -> currencies.AsyncCurrenciesResourceWithStreamingResponse:
        """Endpoints for Currency operations such as creation, update, list, and delete.

        Currencies are stored for your Organization, and can then be used to specify currencies on various entities such as plan groups and plan templates.

        **IMPORTANT!**
        The Currencies you want to use in your Organization must be created first.

        The currency you select for your Organization determines the billing currency and overrides any currency settings in your pricing Plans.
        For example, if the Organization currency is set to USD and a pricing Plan used for an Account is set to GBP, the bill for an Account using that Plan is calculated in GBP, and then each bill line item converted to USD amounts.

        Currency conversion rates are setup in the *OrganizationConfig*. For more details, see [Creating and Managing Currencies](https://www.m3ter.com/docs/guides/organization-and-access-management/viewing-and-editing-organization#creating-and-managing-currencies) in the m3ter Documentation.
        """
        from .resources.currencies import AsyncCurrenciesResourceWithStreamingResponse

        return AsyncCurrenciesResourceWithStreamingResponse(self._client.currencies)

    @cached_property
    def custom_fields(self) -> custom_fields.AsyncCustomFieldsResourceWithStreamingResponse:
        """
        Endpoints for retrieving and updating Custom Fields at the Organization level for all entities that support them.

        Custom Fields in m3ter allow you to store custom data in the form of number or string values against m3ter entities in a way that does not directly affect the normal working operation of the m3ter platform. Having this capability to store data in a free-hand fashion can prove very useful in helping you to meet specific usage-based pricing and other operational business use cases.

        However, you can exploit the values stored on Custom Fields in a more direct way by referencing them in Derived Field and Compound Aggregation calculations. Given the key role these calculations can play when implementing usage-based pricing schema, any Custom Fields you reference will then affect how the platform behaves. Referencing Custom Field values in your calculations offers a much wider scope of options when it comes to resolving complex usage-based pricing use cases.

        Custom Fields can be added to the following entities at Organizational level:
        * Organization
        * Account
        * AccountPlan
        * Aggregation
        * Compound Aggregation
        * Meter
        * Product
        * Plan
        * PlanTemplate
        * Contract

        These all follow the same pattern - a new *(optional)* field is available on the entity request and response bodies called "customFields" which is a object in this format:
        ```
        "customFields": {
                        "exampleCustomField1": 7.1,
                        "exampleCustomField2": "stringValue"
        }
        ```
        The value for a Custom Field can be a string or a number.

        **Using Custom Field values in calculations:**
        - You can add Custom Fields at two levels - the Organization level and the individual entity level.
        - The Organizational level field provides a default value and *must be added* if you want to also add a Custom Field of the same name at the corresponding individual entity level. If you reference the Custom Field in a calculation, the value for the individual entity level field is used. If no field is defined at individual entity level, then the Organization level field value is used.

        **Important: Constraints and Exceptions!**

        **Custom Fields at Organization Level**. Currently, you cannot create Custom Fields at the Organization-level for the following enitites:
        * Plan Group
        * Balance
        * Balance Transaction Schedule
        * Balance Charge Schedule

        Therefore you cannot reference the Custom Fields values created at the individual entity level for these entities in your Derived Field or Compound Aggregation calculations.

        **Derived Field Calculations**. You can *only reference Custom Fields* for the following entities:
        * Organization
        * Meter
        * Account

        However, if you are using Meters belonging to *a specific Product*, that is, not *Global Meters*, you can also reference Custom Fields added to a Product in Derived Field calculations.

        **Compound Aggregation Calculations - Meter Custom Fields**. The value of the *Organization level Meter Custom Field will always be used*, even if you have defined a corresponding field at the individual Meter level.

        See [Working with Custom Fields](https://www.m3ter.com/docs/guides/creating-and-managing-products/working-with-custom-fields) in the m3ter documentation for more information.
        """
        from .resources.custom_fields import AsyncCustomFieldsResourceWithStreamingResponse

        return AsyncCustomFieldsResourceWithStreamingResponse(self._client.custom_fields)

    @cached_property
    def data_exports(self) -> data_exports.AsyncDataExportsResourceWithStreamingResponse:
        """Endpoints for triggering one-off, ad-hoc Data Exports.

        You can set up and run ad-hoc Exports to export two kinds of data from your m3ter Organization:
        * Usage data.
        * Operational data for entities.

        **Ad-Hoc Export Destinations** When setting up and running an ad-hoc Export:
        * You can define one or more Export Destinations - see the [ExportDestination](https://www.m3ter.com/docs/api#tag/ExportDestination) section of this API Reference. When the export runs, the data is sent through to the sepecified Destination. However, the export file is also made available for you to download it locally.
        * You can set up and run Data Exports without defining a Destination. The data is not exported but the compiled export file is made available for downloading locally.
        * For details on downloading an export file, see the [Get Data Export File Download URL](https://www.m3ter.com/docs/api#tag/ExportDestination/operation/GenerateDataExportFileDownloadUrl) endpoint in this API Reference.

        **Preview Version!** The Data Export feature is currently available only in Preview release version. See [Feature Release Stages](https://www.m3ter.com/docs/guides/getting-started/feature-release-stages) for Preview release definition. ExportAdHoc endpoints will only be available if Data Export has been enabled for your Organization. For more details see [Data Export(Preview)](https://www.m3ter.com/docs/guides/data-exports) in our main User documentation. If you're interested in previewing the Data Export feature, please get in touch with m3ter Support or your m3ter contact.
        """
        from .resources.data_exports import AsyncDataExportsResourceWithStreamingResponse

        return AsyncDataExportsResourceWithStreamingResponse(self._client.data_exports)

    @cached_property
    def debit_reasons(self) -> debit_reasons.AsyncDebitReasonsResourceWithStreamingResponse:
        """Endpoints for DebitReason operations such as creation, update, list, and delete.

        You can create DebitReasons for your Organization, and then use them when creating a debit line item on a bill, or applying a product debit to a bill. DebitReasons provide contextual information as to why a debit was applied.
        """
        from .resources.debit_reasons import AsyncDebitReasonsResourceWithStreamingResponse

        return AsyncDebitReasonsResourceWithStreamingResponse(self._client.debit_reasons)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
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
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def external_mappings(self) -> external_mappings.AsyncExternalMappingsResourceWithStreamingResponse:
        """
        Endpoints for managing External Mapping related operations such as creation, update, list and delete.

        When you integrate your 3rd-party systems with the m3ter platform, a mapping between entities in the local system *(m3ter)* and external systems is constructed. This *External Mapping* is crucial in scenarios where data from external systems is consumed or where data from the local system is to be synchronized with external systems.

        When you are working to set up your Integrations and want to test or troubleshoot your implementation before going live, you might need to create External Mappings manually and, at a later date, edit or delete them.
        """
        from .resources.external_mappings import AsyncExternalMappingsResourceWithStreamingResponse

        return AsyncExternalMappingsResourceWithStreamingResponse(self._client.external_mappings)

    @cached_property
    def integration_configurations(
        self,
    ) -> integration_configurations.AsyncIntegrationConfigurationsResourceWithStreamingResponse:
        """
        A suite of endpoints for configuring and managing third party integrations within the m3ter platform. The integration endpoints in this section facilitate various operations such as creating, updating, listing, and deletion of integrations.

        m3ter integrations enable seamless data synchronization and mapping with external systems required in core business processes. These processes often include sales, pricing, billing and invoicing, and general finance.

        With m3ter integrations, you can establish robust connections with popular business platforms, enhancing your operational capabilities. For example:
        * Chargebee
        * Salesforce
        * Stripe
        * Netsuite
        * Paddle
        * Xero
        * QuickBooks
        """
        from .resources.integration_configurations import AsyncIntegrationConfigurationsResourceWithStreamingResponse

        return AsyncIntegrationConfigurationsResourceWithStreamingResponse(self._client.integration_configurations)

    @cached_property
    def lookup_tables(self) -> lookup_tables.AsyncLookupTablesResourceWithStreamingResponse:
        """Endpoints for creating/updating/deleting Lookup Tables.

        Lookup Tables enable you to manage dynamic data mappings that your calculations reference. Use them for currency conversion, pricing tiers, discount rates, and similar scenarios where you require values to change operationally but for calculation logic to remain constant.

        **Beta Version!** The Lookup Table feature is currently available in Beta release version. See [Feature Release Stages](https://www.m3ter.com/docs/guides/getting-started/feature-release-stages) for Beta release definition. Lookup Table endpoints will only be available if Lookup Tables have been enabled for your Organization. For more details see [Lookup Tables (Beta)](https://www.m3ter.com/docs/guides/lookup-tables) in our main User documentation.
        """
        from .resources.lookup_tables import AsyncLookupTablesResourceWithStreamingResponse

        return AsyncLookupTablesResourceWithStreamingResponse(self._client.lookup_tables)

    @cached_property
    def meters(self) -> meters.AsyncMetersResourceWithStreamingResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Meters.

        Use Meters to submit usage data for the consumption of your products and services by end customers. This usage data then becomes the basis for setting up usage-based pricing for your products and services.

        Examples of usage data collected in Meters:
        * Number of logins.
        * Duration of session.
        * Amount of data downloaded.

        To collect usage data and ingest it into the platform, you can define two types of fields for Meters:
        - `dataFields` Used to collect raw usage data measures - numeric quantitative data values or non-numeric point data values.
        - `derivedFields` Used to derive usage data measures that are the result of applying a calculation to `dataFields`, `customFields`, or system `Timestamp` fields.

        You can also:
        - Create `customFields` for a Meter, which allows you to attach custom data to the Meter as name/value pairs.
        - Create Global Meters, which are not tied to a specific Product and allow you to collect usage data that will form the basis of usage-based pricing across multiple Products.

        **IMPORTANT! - use of PII:** The use of any of your end-customers' Personally Identifiable Information (PII) in m3ter is restricted to a few fields on the **Account** entity. Please ensure that any fields you configure for Meters, such as Data Fields or Derived Fields, do not contain any end-customer PII data. See the [Introduction section](https://www.m3ter.com/docs/api#section/Introduction) above for more details.

        See also:
        - [Reviewing Meter Options](https://www.m3ter.com/docs/guides/setting-up-usage-data-meters-and-aggregations/reviewing-meter-options).
        """
        from .resources.meters import AsyncMetersResourceWithStreamingResponse

        return AsyncMetersResourceWithStreamingResponse(self._client.meters)

    @cached_property
    def notification_configurations(
        self,
    ) -> notification_configurations.AsyncNotificationConfigurationsResourceWithStreamingResponse:
        """This section provides endpoints for managing Event Notifications.

        You can create Notifications based on system Events generated by the platform. When you base a Notification on a specific Event type, you can include a calculation that references the fields available on that Event type to define precise conditions that must be met for the Notification to be triggered when an Event of that type occurs. In this way, you can set up highly customized Notifications that act as timely alerts to inform you about significant occurrences within your Organization. For instance, if you provide a sign-up bonus to new end-customer Accounts, you can set up a Notification to alert you when an end-customer Account has used up a certain percentage of their bonus credit.

        You can also set up Notifications based on Scheduled Event types you've created for your Organization. See the [ScheduledEventConfigurations](https://www.m3ter.com/docs/api#tag/ScheduledEventConfigurations) section of this API Reference and [Working with Scheduled Events](https://www.m3ter.com/docs/guides/alerts-events-and-notifications/utilizing-events-and-notifications/working-with-scheduled-events) in our user documentation.

        For more details on Event types and their fields, see the [Events](https://www.m3ter.com/docs/api#tag/Events) section.

        For detailed guidance on working with Events and Notifications, refer to the [Utilizing Events and Notifications](https://www.m3ter.com/docs/guides/utilizing-events-and-notifications) section of the m3ter user documentation.
        """
        from .resources.notification_configurations import AsyncNotificationConfigurationsResourceWithStreamingResponse

        return AsyncNotificationConfigurationsResourceWithStreamingResponse(self._client.notification_configurations)

    @cached_property
    def organization_config(self) -> organization_config.AsyncOrganizationConfigResourceWithStreamingResponse:
        """Endpoints for retrieving or updating the Organization Config.

        Organization represents your company as a direct customer of m3ter. Use Organization configuration to define *Organization-wide* settings. For example:
        - Timezone.
        - Currencies and currency conversions.
        - Billing operations settings, such as:
                - Epoch dates to control first billing dates.
                - Whether to bill customer accounts in advance/in arrears for standing charge amounts, minimum spend amounts, and commitment fees.

        For other aspects of your Organization setup and configuration, see the following sections in this API Reference:
        * [Custom Fields](https://www.m3ter.com/docs/api#tag/CustomField)
        * [Currencies](https://www.m3ter.com/docs/api#tag/Currency)
        * [Credit Reasons](https://www.m3ter.com/docs/api#tag/CreditReason)
        * [Debit Reason](https://www.m3ter.com/docs/api#tag/DebitReason)
        * [Transaction Types](https://www.m3ter.com/docs/api#tag/TransactionType)

        See also:
        - [Managing your Organization](https://www.m3ter.com/docs/guides/managing-organization-and-users/viewing-and-editing-organization).
        """
        from .resources.organization_config import AsyncOrganizationConfigResourceWithStreamingResponse

        return AsyncOrganizationConfigResourceWithStreamingResponse(self._client.organization_config)

    @cached_property
    def permission_policies(self) -> permission_policies.AsyncPermissionPoliciesResourceWithStreamingResponse:
        """
        Endpoints for Permission Policy related operations such as creation, update, add and retrieve.

        Permission Policies can restrict or grant access to specific resources for both Users *(people)* and Service Users *(automated processes with direct API access)*. This enables you to control precisely what a User can do in your m3ter Organization.

        For more details, see [Understanding, Creating, and Managing Permission Policies](https://www.m3ter.com/docs/guides/organization-and-access-management/creating-and-managing-permissions#permission-policy-statements---available-actions-and-resources) in our main Documentation.
        """
        from .resources.permission_policies import AsyncPermissionPoliciesResourceWithStreamingResponse

        return AsyncPermissionPoliciesResourceWithStreamingResponse(self._client.permission_policies)

    @cached_property
    def plans(self) -> plans.AsyncPlansResourceWithStreamingResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Plans.

        A Plan is based on a PlanTemplate and represents a specific pricing plan for one of your products or services. Each Plan inherits general billing attributes or pricing structure from its parent Plan Template. Some attributes can be overriden for the specific Plan.

        When you've created the Plan Templates and Plans you need for your Products, you can configure the exact pricing structures for Plans to charge customers that consume one or more of your Products.

        You can then attach the appropriately priced Plans to customer Accounts to create [Account Plans](https://www.m3ter.com/docs/api#tag/AccountPlan) and enable charges to be calculated correctly for billing against those Accounts.

        See also:
        - [Reviewing Options for Plans and Plan Templates](https://www.m3ter.com/docs/guides/working-with-plan-templates-and-plans/reviewing-configuration-options-for-plans-and-plan-templates).
        """
        from .resources.plans import AsyncPlansResourceWithStreamingResponse

        return AsyncPlansResourceWithStreamingResponse(self._client.plans)

    @cached_property
    def plan_groups(self) -> plan_groups.AsyncPlanGroupsResourceWithStreamingResponse:
        """
        Endpoints for PlanGroup related operations such as creation, update, retrieve, list and delete.

        PlanGroups are constructs that group multiple plans together. This enables a unified approach to efficiently handle various uses cases across different plans. For example applying a minimum spend amount at billing, across several of your products or features that are each priced separately.
        """
        from .resources.plan_groups import AsyncPlanGroupsResourceWithStreamingResponse

        return AsyncPlanGroupsResourceWithStreamingResponse(self._client.plan_groups)

    @cached_property
    def plan_group_links(self) -> plan_group_links.AsyncPlanGroupLinksResourceWithStreamingResponse:
        """
        Endpoints for PlanGroupLink related operations such as creation, update, list and delete.

        PlanGroupLinks are the intersection table between a PlanGroup and its associated Plans. A PlanGroupLink is only created when at least 1 Plan is linked to a PlanGroup.
        """
        from .resources.plan_group_links import AsyncPlanGroupLinksResourceWithStreamingResponse

        return AsyncPlanGroupLinksResourceWithStreamingResponse(self._client.plan_group_links)

    @cached_property
    def plan_templates(self) -> plan_templates.AsyncPlanTemplatesResourceWithStreamingResponse:
        """
        Endpoints for listing, creating, updating, retrieving, or deleting PlanTemplates.

        Use PlanTemplates to define default values for Plans. These default values control the billing operations you want applied to your products. PlanTemplates avoid repetition in configuration work - many Plans will share settings for billing operations and differ only in the details of their pricing structures.

        A PlanTemplate is linked to a Product, and each Plan is a child of a PlanTemplate.
        """
        from .resources.plan_templates import AsyncPlanTemplatesResourceWithStreamingResponse

        return AsyncPlanTemplatesResourceWithStreamingResponse(self._client.plan_templates)

    @cached_property
    def pricings(self) -> pricings.AsyncPricingsResourceWithStreamingResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Pricing.

        Create the Pricing for a Plan/PlanTemplate with usage data Aggregations, and define a usage-based pricing structure for charging end customer Accounts put on the Plan.

        See [Reviewing Pricing Options for Plans and Plan Templates](https://www.m3ter.com/docs/guides/pricing-plans/reviewing-pricing-options-and-pricing-plans) for more information.
        """
        from .resources.pricings import AsyncPricingsResourceWithStreamingResponse

        return AsyncPricingsResourceWithStreamingResponse(self._client.pricings)

    @cached_property
    def products(self) -> products.AsyncProductsResourceWithStreamingResponse:
        """Endpoints for listing, creating, updating, retrieving, or deleting Products.

        A Product represents the products and services you offer to your end customers. Products act as a container for the Meters, Aggregations, Pricing, and Plans required to implement usage-based and other pricing models for your Organization.
        """
        from .resources.products import AsyncProductsResourceWithStreamingResponse

        return AsyncProductsResourceWithStreamingResponse(self._client.products)

    @cached_property
    def resource_groups(self) -> resource_groups.AsyncResourceGroupsResourceWithStreamingResponse:
        """
        Endpoints for ResourceGroup related operations such as creation, update, list and delete.

        ResourceGroups are used in the context of Permission Policies, which controls what a User who has been given access to your Organization can and cannot do. For example, you might want to create a Permissions Policy that denies Users the ability to retrieve Meters.

        Resources are defined as m3ter Resource Identifiers *(MRIs)* in the format:

        ```
        service: resource - type / item - type / id
        ```

        Where:

        * service is a distinct part of the overall m3ter system, and which forms a natural functional grouping, such as "config" or "billing".

        * resource-type is the resource type item accessed - for example: "Plan", "Meter", "Bill"

        * item-type is one of:

                * "item" - to specify an individual item.

                * "group" - to specify a resource group.

        * id is the resource group id or the resource item id

        Resources can be assigned to one or more ResourceGroups. For example, a Plan can be assigned to Plan ResourceGroups, a Meter can be assigned to Meter ResourceGroups, and so on. This is useful for cases where you want to create Permission Policies which allow or deny access to a specific subset of resources. For example, grant a user access to only some of the Plans in your Organization.

        This concept of grouping resources applies to every resource in m3ter, including ResourceGroups themselves. This allows you to nest ResourceGroups to support hierarchies of groups.

        See [Understanding, Creating, and Managing Permission Policies](https://www.m3ter.com/docs/guides/managing-organization-and-users/creating-and-managing-permissions) in the m3ter documentation for more information.

        **Note: User Resource Groups** You can create a User Resource Group to group resources of type = `user`. You can then retrieve a list of the User Resource Groups a user belongs to. For more details, see the [Retrieve OrgUser Groups](https://www.m3ter.com/docs/api#tag/OrgUsers/operation/GetOrgUserGroups) call in the OrgUsers section.
        """
        from .resources.resource_groups import AsyncResourceGroupsResourceWithStreamingResponse

        return AsyncResourceGroupsResourceWithStreamingResponse(self._client.resource_groups)

    @cached_property
    def scheduled_event_configurations(
        self,
    ) -> scheduled_event_configurations.AsyncScheduledEventConfigurationsResourceWithStreamingResponse:
        """Endpoints for retrieving and managing scheduled Events' configurations.

        Scheduled Event Configurations define custom Event types that reference Date/Time fields belonging to configuration and billing entities. They therefore provide you with an extra degree of flexibility over and above system-generated Events for setting up Notifications based on Events.

        For more details, see the [Working with Scheduled Events](https://www.m3ter.com/docs/guides/alerts-events-and-notifications/utilizing-events-and-notifications/working-with-scheduled-events) in our Documenation.
        """
        from .resources.scheduled_event_configurations import (
            AsyncScheduledEventConfigurationsResourceWithStreamingResponse,
        )

        return AsyncScheduledEventConfigurationsResourceWithStreamingResponse(
            self._client.scheduled_event_configurations
        )

    @cached_property
    def statements(self) -> statements.AsyncStatementsResourceWithStreamingResponse:
        """
        Endpoints for billing operations such as creating, updating, listing,downloading, and deleting Bills.

        Bills are generated for an Account, and are calculated in accordance with the usage-based pricing Plans applied for the Products the Account consumes. These endpoints enable interaction with the billing system, allowing you to obtain billing details and insights into the consumption patterns and charges of your end-customer Accounts.
        """
        from .resources.statements import AsyncStatementsResourceWithStreamingResponse

        return AsyncStatementsResourceWithStreamingResponse(self._client.statements)

    @cached_property
    def transaction_types(self) -> transaction_types.AsyncTransactionTypesResourceWithStreamingResponse:
        """
        Endpoints for TransactionType operations such as creation, update, list, retrieve, and delete.

        You can create TransactionTypes for your Organization, which can then be used when creating and updating Balances. Example TransactionTypes: "Balance Amount" or "Add Funds".

        For details on creating a Transaction amount for a Balance using a TransactionType you've created for your Organization, see the [Create Balance Transaction](https://www.m3ter.com/docs/api#tag/Balances/operation/PostBalanceTransaction) call in the [Balances](https://www.m3ter.com/docs/api#tag/Balances) section of this API Reference.
        """
        from .resources.transaction_types import AsyncTransactionTypesResourceWithStreamingResponse

        return AsyncTransactionTypesResourceWithStreamingResponse(self._client.transaction_types)

    @cached_property
    def usage(self) -> usage.AsyncUsageResourceWithStreamingResponse:
        from .resources.usage import AsyncUsageResourceWithStreamingResponse

        return AsyncUsageResourceWithStreamingResponse(self._client.usage)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        """
        A suite of endpoints for configuring and managing third party integrations within the m3ter platform. The integration endpoints in this section facilitate various operations such as creating, updating, listing, and deletion of integrations.

        m3ter integrations enable seamless data synchronization and mapping with external systems required in core business processes. These processes often include sales, pricing, billing and invoicing, and general finance.

        With m3ter integrations, you can establish robust connections with popular business platforms, enhancing your operational capabilities. For example:
        * Chargebee
        * Salesforce
        * Stripe
        * Netsuite
        * Paddle
        * Xero
        * QuickBooks
        """
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)


Client = M3ter

AsyncClient = AsyncM3ter
