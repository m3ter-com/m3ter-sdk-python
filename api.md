# Shared Types

```python
from m3ter_sdk.types import CurrencyConversion, PricingBand, SetString
```

# Authentication

Types:

```python
from m3ter_sdk.types import AuthenticationGetBearerTokenResponse
```

Methods:

- <code title="post /oauth/token">client.authentication.<a href="./src/m3ter_sdk/resources/authentication.py">get_bearer_token</a>(\*\*<a href="src/m3ter_sdk/types/authentication_get_bearer_token_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/authentication_get_bearer_token_response.py">AuthenticationGetBearerTokenResponse</a></code>

# Accounts

Types:

```python
from m3ter_sdk.types import (
    Account,
    Address,
    AccountEndDateBillingEntitiesResponse,
    AccountSearchResponse,
)
```

Methods:

- <code title="post /organizations/{orgId}/accounts">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/account_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account.py">Account</a></code>
- <code title="get /organizations/{orgId}/accounts/{id}">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/account.py">Account</a></code>
- <code title="put /organizations/{orgId}/accounts/{id}">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/account_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account.py">Account</a></code>
- <code title="get /organizations/{orgId}/accounts">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/account_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account.py">SyncCursor[Account]</a></code>
- <code title="delete /organizations/{orgId}/accounts/{id}">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/account.py">Account</a></code>
- <code title="put /organizations/{orgId}/accounts/{id}/enddatebillingentities">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">end_date_billing_entities</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/account_end_date_billing_entities_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account_end_date_billing_entities_response.py">AccountEndDateBillingEntitiesResponse</a></code>
- <code title="get /organizations/{orgId}/accounts/{id}/children">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">get_children</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/account_get_children_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account.py">Account</a></code>
- <code title="get /organizations/{orgId}/accounts/search">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">search</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/account_search_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account_search_response.py">AccountSearchResponse</a></code>

# AccountPlans

Types:

```python
from m3ter_sdk.types import AccountPlan
```

Methods:

- <code title="post /organizations/{orgId}/accountplans">client.account_plans.<a href="./src/m3ter_sdk/resources/account_plans.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/account_plan_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account_plan.py">AccountPlan</a></code>
- <code title="get /organizations/{orgId}/accountplans/{id}">client.account_plans.<a href="./src/m3ter_sdk/resources/account_plans.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/account_plan.py">AccountPlan</a></code>
- <code title="put /organizations/{orgId}/accountplans/{id}">client.account_plans.<a href="./src/m3ter_sdk/resources/account_plans.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/account_plan_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account_plan.py">AccountPlan</a></code>
- <code title="get /organizations/{orgId}/accountplans">client.account_plans.<a href="./src/m3ter_sdk/resources/account_plans.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/account_plan_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account_plan.py">SyncCursor[AccountPlan]</a></code>
- <code title="delete /organizations/{orgId}/accountplans/{id}">client.account_plans.<a href="./src/m3ter_sdk/resources/account_plans.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/account_plan.py">AccountPlan</a></code>

# Aggregations

Types:

```python
from m3ter_sdk.types import AggregationResponse
```

Methods:

- <code title="post /organizations/{orgId}/aggregations">client.aggregations.<a href="./src/m3ter_sdk/resources/aggregations.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/aggregation_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/aggregation_response.py">AggregationResponse</a></code>
- <code title="get /organizations/{orgId}/aggregations/{id}">client.aggregations.<a href="./src/m3ter_sdk/resources/aggregations.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/aggregation_response.py">AggregationResponse</a></code>
- <code title="put /organizations/{orgId}/aggregations/{id}">client.aggregations.<a href="./src/m3ter_sdk/resources/aggregations.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/aggregation_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/aggregation_response.py">AggregationResponse</a></code>
- <code title="get /organizations/{orgId}/aggregations">client.aggregations.<a href="./src/m3ter_sdk/resources/aggregations.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/aggregation_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/aggregation_response.py">SyncCursor[AggregationResponse]</a></code>
- <code title="delete /organizations/{orgId}/aggregations/{id}">client.aggregations.<a href="./src/m3ter_sdk/resources/aggregations.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/aggregation_response.py">AggregationResponse</a></code>

# Balances

Types:

```python
from m3ter_sdk.types import Balance
```

Methods:

- <code title="post /organizations/{orgId}/balances">client.balances.<a href="./src/m3ter_sdk/resources/balances/balances.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/balance_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/balance.py">Balance</a></code>
- <code title="get /organizations/{orgId}/balances/{id}">client.balances.<a href="./src/m3ter_sdk/resources/balances/balances.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/balance.py">Balance</a></code>
- <code title="put /organizations/{orgId}/balances/{id}">client.balances.<a href="./src/m3ter_sdk/resources/balances/balances.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/balance_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/balance.py">Balance</a></code>
- <code title="get /organizations/{orgId}/balances">client.balances.<a href="./src/m3ter_sdk/resources/balances/balances.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/balance_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/balance.py">SyncCursor[Balance]</a></code>
- <code title="delete /organizations/{orgId}/balances/{id}">client.balances.<a href="./src/m3ter_sdk/resources/balances/balances.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/balance.py">Balance</a></code>

## Transactions

Types:

```python
from m3ter_sdk.types.balances import Transaction, TransactionSummaryResponse
```

Methods:

- <code title="post /organizations/{orgId}/balances/{balanceId}/transactions">client.balances.transactions.<a href="./src/m3ter_sdk/resources/balances/transactions.py">create</a>(balance_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/balances/transaction_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/balances/transaction.py">Transaction</a></code>
- <code title="get /organizations/{orgId}/balances/{balanceId}/transactions">client.balances.transactions.<a href="./src/m3ter_sdk/resources/balances/transactions.py">list</a>(balance_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/balances/transaction_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/balances/transaction.py">SyncCursor[Transaction]</a></code>
- <code title="get /organizations/{orgId}/balances/{balanceId}/transactions/summary">client.balances.transactions.<a href="./src/m3ter_sdk/resources/balances/transactions.py">summary</a>(balance_id, \*, org_id) -> <a href="./src/m3ter_sdk/types/balances/transaction_summary_response.py">TransactionSummaryResponse</a></code>

# Bills

Types:

```python
from m3ter_sdk.types import Bill, BillApproveResponse, BillSearchResponse
```

Methods:

- <code title="get /organizations/{orgId}/bills/{id}">client.bills.<a href="./src/m3ter_sdk/resources/bills/bills.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/bill.py">Bill</a></code>
- <code title="get /organizations/{orgId}/bills">client.bills.<a href="./src/m3ter_sdk/resources/bills/bills.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/bill_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bill.py">SyncCursor[Bill]</a></code>
- <code title="delete /organizations/{orgId}/bills/{id}">client.bills.<a href="./src/m3ter_sdk/resources/bills/bills.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/bill.py">Bill</a></code>
- <code title="post /organizations/{orgId}/bills/approve">client.bills.<a href="./src/m3ter_sdk/resources/bills/bills.py">approve</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/bill_approve_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bill_approve_response.py">BillApproveResponse</a></code>
- <code title="get /organizations/{orgId}/bills/latest/{accountId}">client.bills.<a href="./src/m3ter_sdk/resources/bills/bills.py">latest_by_account</a>(account_id, \*, org_id) -> <a href="./src/m3ter_sdk/types/bill.py">Bill</a></code>
- <code title="put /organizations/{orgId}/bills/{id}/lock">client.bills.<a href="./src/m3ter_sdk/resources/bills/bills.py">lock</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/bill.py">Bill</a></code>
- <code title="get /organizations/{orgId}/bills/search">client.bills.<a href="./src/m3ter_sdk/resources/bills/bills.py">search</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/bill_search_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bill_search_response.py">BillSearchResponse</a></code>
- <code title="put /organizations/{orgId}/bills/{id}/status">client.bills.<a href="./src/m3ter_sdk/resources/bills/bills.py">update_status</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/bill_update_status_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bill.py">Bill</a></code>

## CreditLineItems

Types:

```python
from m3ter_sdk.types.bills import CreditLineItem
```

Methods:

- <code title="post /organizations/{orgId}/bills/{billId}/creditlineitems">client.bills.credit_line_items.<a href="./src/m3ter_sdk/resources/bills/credit_line_items.py">create</a>(bill_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/bills/credit_line_item_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bills/credit_line_item.py">CreditLineItem</a></code>
- <code title="get /organizations/{orgId}/bills/{billId}/creditlineitems/{id}">client.bills.credit_line_items.<a href="./src/m3ter_sdk/resources/bills/credit_line_items.py">retrieve</a>(id, \*, org_id, bill_id) -> <a href="./src/m3ter_sdk/types/bills/credit_line_item.py">CreditLineItem</a></code>
- <code title="put /organizations/{orgId}/bills/{billId}/creditlineitems/{id}">client.bills.credit_line_items.<a href="./src/m3ter_sdk/resources/bills/credit_line_items.py">update</a>(id, \*, org_id, bill_id, \*\*<a href="src/m3ter_sdk/types/bills/credit_line_item_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bills/credit_line_item.py">CreditLineItem</a></code>
- <code title="get /organizations/{orgId}/bills/{billId}/creditlineitems">client.bills.credit_line_items.<a href="./src/m3ter_sdk/resources/bills/credit_line_items.py">list</a>(bill_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/bills/credit_line_item_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bills/credit_line_item.py">SyncCursor[CreditLineItem]</a></code>
- <code title="delete /organizations/{orgId}/bills/{billId}/creditlineitems/{id}">client.bills.credit_line_items.<a href="./src/m3ter_sdk/resources/bills/credit_line_items.py">delete</a>(id, \*, org_id, bill_id) -> <a href="./src/m3ter_sdk/types/bills/credit_line_item.py">CreditLineItem</a></code>

## DebitLineItems

Types:

```python
from m3ter_sdk.types.bills import DebitLineItem
```

Methods:

- <code title="post /organizations/{orgId}/bills/{billId}/debitlineitems">client.bills.debit_line_items.<a href="./src/m3ter_sdk/resources/bills/debit_line_items.py">create</a>(bill_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/bills/debit_line_item_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bills/debit_line_item.py">DebitLineItem</a></code>
- <code title="get /organizations/{orgId}/bills/{billId}/debitlineitems/{id}">client.bills.debit_line_items.<a href="./src/m3ter_sdk/resources/bills/debit_line_items.py">retrieve</a>(id, \*, org_id, bill_id) -> <a href="./src/m3ter_sdk/types/bills/debit_line_item.py">DebitLineItem</a></code>
- <code title="put /organizations/{orgId}/bills/{billId}/debitlineitems/{id}">client.bills.debit_line_items.<a href="./src/m3ter_sdk/resources/bills/debit_line_items.py">update</a>(id, \*, org_id, bill_id, \*\*<a href="src/m3ter_sdk/types/bills/debit_line_item_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bills/debit_line_item.py">DebitLineItem</a></code>
- <code title="get /organizations/{orgId}/bills/{billId}/debitlineitems">client.bills.debit_line_items.<a href="./src/m3ter_sdk/resources/bills/debit_line_items.py">list</a>(bill_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/bills/debit_line_item_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bills/debit_line_item.py">SyncCursor[DebitLineItem]</a></code>
- <code title="delete /organizations/{orgId}/bills/{billId}/debitlineitems/{id}">client.bills.debit_line_items.<a href="./src/m3ter_sdk/resources/bills/debit_line_items.py">delete</a>(id, \*, org_id, bill_id) -> <a href="./src/m3ter_sdk/types/bills/debit_line_item.py">DebitLineItem</a></code>

## LineItems

Types:

```python
from m3ter_sdk.types.bills import LineItem
```

Methods:

- <code title="get /organizations/{orgId}/bills/{billId}/lineitems/{id}">client.bills.line_items.<a href="./src/m3ter_sdk/resources/bills/line_items.py">retrieve</a>(id, \*, org_id, bill_id) -> <a href="./src/m3ter_sdk/types/bills/line_item.py">LineItem</a></code>
- <code title="get /organizations/{orgId}/bills/{billId}/lineitems">client.bills.line_items.<a href="./src/m3ter_sdk/resources/bills/line_items.py">list</a>(bill_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/bills/line_item_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bills/line_item.py">SyncCursor[LineItem]</a></code>

# BillConfig

Types:

```python
from m3ter_sdk.types import BillConfig
```

Methods:

- <code title="get /organizations/{orgId}/billconfig">client.bill_config.<a href="./src/m3ter_sdk/resources/bill_config.py">retrieve</a>(\*, org_id) -> <a href="./src/m3ter_sdk/types/bill_config.py">BillConfig</a></code>
- <code title="put /organizations/{orgId}/billconfig">client.bill_config.<a href="./src/m3ter_sdk/resources/bill_config.py">update</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/bill_config_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bill_config.py">BillConfig</a></code>

# Commitments

Types:

```python
from m3ter_sdk.types import Commitment, CommitmentFee, CommitmentSearchResponse
```

Methods:

- <code title="post /organizations/{orgId}/commitments">client.commitments.<a href="./src/m3ter_sdk/resources/commitments.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/commitment_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/commitment.py">Commitment</a></code>
- <code title="get /organizations/{orgId}/commitments/{id}">client.commitments.<a href="./src/m3ter_sdk/resources/commitments.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/commitment.py">Commitment</a></code>
- <code title="put /organizations/{orgId}/commitments/{id}">client.commitments.<a href="./src/m3ter_sdk/resources/commitments.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/commitment_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/commitment.py">Commitment</a></code>
- <code title="get /organizations/{orgId}/commitments">client.commitments.<a href="./src/m3ter_sdk/resources/commitments.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/commitment_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/commitment.py">SyncCursor[Commitment]</a></code>
- <code title="delete /organizations/{orgId}/commitments/{id}">client.commitments.<a href="./src/m3ter_sdk/resources/commitments.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/commitment.py">Commitment</a></code>
- <code title="get /organizations/{orgId}/commitments/search">client.commitments.<a href="./src/m3ter_sdk/resources/commitments.py">search</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/commitment_search_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/commitment_search_response.py">CommitmentSearchResponse</a></code>

# BillJobs

Types:

```python
from m3ter_sdk.types import BillJob
```

Methods:

- <code title="post /organizations/{orgId}/billjobs">client.bill_jobs.<a href="./src/m3ter_sdk/resources/bill_jobs.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/bill_job_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bill_job.py">BillJob</a></code>
- <code title="get /organizations/{orgId}/billjobs/{id}">client.bill_jobs.<a href="./src/m3ter_sdk/resources/bill_jobs.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/bill_job.py">BillJob</a></code>
- <code title="get /organizations/{orgId}/billjobs">client.bill_jobs.<a href="./src/m3ter_sdk/resources/bill_jobs.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/bill_job_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bill_job.py">SyncCursor[BillJob]</a></code>
- <code title="post /organizations/{orgId}/billjobs/{id}/cancel">client.bill_jobs.<a href="./src/m3ter_sdk/resources/bill_jobs.py">cancel</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/bill_job.py">BillJob</a></code>
- <code title="post /organizations/{orgId}/billjobs/recalculate">client.bill_jobs.<a href="./src/m3ter_sdk/resources/bill_jobs.py">recalculate</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/bill_job_recalculate_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bill_job.py">BillJob</a></code>

# CompoundAggregations

Types:

```python
from m3ter_sdk.types import CompoundAggregation
```

Methods:

- <code title="post /organizations/{orgId}/compoundaggregations">client.compound_aggregations.<a href="./src/m3ter_sdk/resources/compound_aggregations.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/compound_aggregation_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/aggregation_response.py">AggregationResponse</a></code>
- <code title="get /organizations/{orgId}/compoundaggregations/{id}">client.compound_aggregations.<a href="./src/m3ter_sdk/resources/compound_aggregations.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/compound_aggregation.py">CompoundAggregation</a></code>
- <code title="put /organizations/{orgId}/compoundaggregations/{id}">client.compound_aggregations.<a href="./src/m3ter_sdk/resources/compound_aggregations.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/compound_aggregation_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/aggregation_response.py">AggregationResponse</a></code>
- <code title="get /organizations/{orgId}/compoundaggregations">client.compound_aggregations.<a href="./src/m3ter_sdk/resources/compound_aggregations.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/compound_aggregation_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/compound_aggregation.py">SyncCursor[CompoundAggregation]</a></code>
- <code title="delete /organizations/{orgId}/compoundaggregations/{id}">client.compound_aggregations.<a href="./src/m3ter_sdk/resources/compound_aggregations.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/compound_aggregation.py">CompoundAggregation</a></code>

# Contracts

Types:

```python
from m3ter_sdk.types import Contract, ContractEndDateBillingEntitiesResponse
```

Methods:

- <code title="post /organizations/{orgId}/contracts">client.contracts.<a href="./src/m3ter_sdk/resources/contracts.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/contract_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/contract.py">Contract</a></code>
- <code title="get /organizations/{orgId}/contracts/{id}">client.contracts.<a href="./src/m3ter_sdk/resources/contracts.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/contract.py">Contract</a></code>
- <code title="put /organizations/{orgId}/contracts/{id}">client.contracts.<a href="./src/m3ter_sdk/resources/contracts.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/contract_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/contract.py">Contract</a></code>
- <code title="get /organizations/{orgId}/contracts">client.contracts.<a href="./src/m3ter_sdk/resources/contracts.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/contract_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/contract.py">SyncCursor[Contract]</a></code>
- <code title="delete /organizations/{orgId}/contracts/{id}">client.contracts.<a href="./src/m3ter_sdk/resources/contracts.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/contract.py">Contract</a></code>
- <code title="put /organizations/{orgId}/contracts/{id}/enddatebillingentities">client.contracts.<a href="./src/m3ter_sdk/resources/contracts.py">end_date_billing_entities</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/contract_end_date_billing_entities_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/contract_end_date_billing_entities_response.py">ContractEndDateBillingEntitiesResponse</a></code>

# Counters

Types:

```python
from m3ter_sdk.types import Counter
```

Methods:

- <code title="post /organizations/{orgId}/counters">client.counters.<a href="./src/m3ter_sdk/resources/counters.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/counter_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter.py">Counter</a></code>
- <code title="get /organizations/{orgId}/counters/{id}">client.counters.<a href="./src/m3ter_sdk/resources/counters.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/counter.py">Counter</a></code>
- <code title="put /organizations/{orgId}/counters/{id}">client.counters.<a href="./src/m3ter_sdk/resources/counters.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/counter_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter.py">Counter</a></code>
- <code title="get /organizations/{orgId}/counters">client.counters.<a href="./src/m3ter_sdk/resources/counters.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/counter_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter.py">SyncCursor[Counter]</a></code>
- <code title="delete /organizations/{orgId}/counters/{id}">client.counters.<a href="./src/m3ter_sdk/resources/counters.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/counter.py">Counter</a></code>

# CounterAdjustments

Types:

```python
from m3ter_sdk.types import CounterAdjustment
```

Methods:

- <code title="post /organizations/{orgId}/counteradjustments">client.counter_adjustments.<a href="./src/m3ter_sdk/resources/counter_adjustments.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/counter_adjustment_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter_adjustment.py">CounterAdjustment</a></code>
- <code title="get /organizations/{orgId}/counteradjustments/{id}">client.counter_adjustments.<a href="./src/m3ter_sdk/resources/counter_adjustments.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/counter_adjustment.py">CounterAdjustment</a></code>
- <code title="put /organizations/{orgId}/counteradjustments/{id}">client.counter_adjustments.<a href="./src/m3ter_sdk/resources/counter_adjustments.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/counter_adjustment_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter_adjustment.py">CounterAdjustment</a></code>
- <code title="get /organizations/{orgId}/counteradjustments">client.counter_adjustments.<a href="./src/m3ter_sdk/resources/counter_adjustments.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/counter_adjustment_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter_adjustment.py">SyncCursor[CounterAdjustment]</a></code>
- <code title="delete /organizations/{orgId}/counteradjustments/{id}">client.counter_adjustments.<a href="./src/m3ter_sdk/resources/counter_adjustments.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/counter_adjustment.py">CounterAdjustment</a></code>

# CounterPricings

Types:

```python
from m3ter_sdk.types import CounterPricing
```

Methods:

- <code title="post /organizations/{orgId}/counterpricings">client.counter_pricings.<a href="./src/m3ter_sdk/resources/counter_pricings.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/counter_pricing_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter_pricing.py">CounterPricing</a></code>
- <code title="get /organizations/{orgId}/counterpricings/{id}">client.counter_pricings.<a href="./src/m3ter_sdk/resources/counter_pricings.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/counter_pricing.py">CounterPricing</a></code>
- <code title="put /organizations/{orgId}/counterpricings/{id}">client.counter_pricings.<a href="./src/m3ter_sdk/resources/counter_pricings.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/counter_pricing_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter_pricing.py">CounterPricing</a></code>
- <code title="get /organizations/{orgId}/counterpricings">client.counter_pricings.<a href="./src/m3ter_sdk/resources/counter_pricings.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/counter_pricing_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter_pricing.py">SyncCursor[CounterPricing]</a></code>
- <code title="delete /organizations/{orgId}/counterpricings/{id}">client.counter_pricings.<a href="./src/m3ter_sdk/resources/counter_pricings.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/counter_pricing.py">CounterPricing</a></code>

# CreditReasons

Types:

```python
from m3ter_sdk.types import CreditReason
```

Methods:

- <code title="post /organizations/{orgId}/picklists/creditreasons">client.credit_reasons.<a href="./src/m3ter_sdk/resources/credit_reasons.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/credit_reason_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/credit_reason.py">CreditReason</a></code>
- <code title="get /organizations/{orgId}/picklists/creditreasons/{id}">client.credit_reasons.<a href="./src/m3ter_sdk/resources/credit_reasons.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/credit_reason.py">CreditReason</a></code>
- <code title="put /organizations/{orgId}/picklists/creditreasons/{id}">client.credit_reasons.<a href="./src/m3ter_sdk/resources/credit_reasons.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/credit_reason_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/credit_reason.py">CreditReason</a></code>
- <code title="get /organizations/{orgId}/picklists/creditreasons">client.credit_reasons.<a href="./src/m3ter_sdk/resources/credit_reasons.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/credit_reason_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/credit_reason.py">SyncCursor[CreditReason]</a></code>
- <code title="delete /organizations/{orgId}/picklists/creditreasons/{id}">client.credit_reasons.<a href="./src/m3ter_sdk/resources/credit_reasons.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/credit_reason.py">CreditReason</a></code>

# Currencies

Types:

```python
from m3ter_sdk.types import Currency
```

Methods:

- <code title="post /organizations/{orgId}/picklists/currency">client.currencies.<a href="./src/m3ter_sdk/resources/currencies.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/currency_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/currency.py">Currency</a></code>
- <code title="get /organizations/{orgId}/picklists/currency/{id}">client.currencies.<a href="./src/m3ter_sdk/resources/currencies.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/currency.py">Currency</a></code>
- <code title="put /organizations/{orgId}/picklists/currency/{id}">client.currencies.<a href="./src/m3ter_sdk/resources/currencies.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/currency_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/currency.py">Currency</a></code>
- <code title="get /organizations/{orgId}/picklists/currency">client.currencies.<a href="./src/m3ter_sdk/resources/currencies.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/currency_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/currency.py">SyncCursor[Currency]</a></code>
- <code title="delete /organizations/{orgId}/picklists/currency/{id}">client.currencies.<a href="./src/m3ter_sdk/resources/currencies.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/currency.py">Currency</a></code>

# CustomFields

Types:

```python
from m3ter_sdk.types import CustomFields
```

Methods:

- <code title="get /organizations/{orgId}/customfields">client.custom_fields.<a href="./src/m3ter_sdk/resources/custom_fields.py">retrieve</a>(\*, org_id) -> <a href="./src/m3ter_sdk/types/custom_fields.py">CustomFields</a></code>
- <code title="put /organizations/{orgId}/customfields">client.custom_fields.<a href="./src/m3ter_sdk/resources/custom_fields.py">update</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/custom_field_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/custom_fields.py">CustomFields</a></code>

# DataExports

Types:

```python
from m3ter_sdk.types import AdhocExport, AdHocOperationalDataRequest, AdHocUsageDataRequest
```

Methods:

- <code title="post /organizations/{orgId}/dataexports/adhoc">client.data_exports.<a href="./src/m3ter_sdk/resources/data_exports/data_exports.py">create_adhoc</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/data_export_create_adhoc_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/adhoc_export.py">AdhocExport</a></code>

## Destinations

Types:

```python
from m3ter_sdk.types.data_exports import (
    DataExportDestination,
    DestinationCreateResponse,
    DestinationRetrieveResponse,
    DestinationUpdateResponse,
    DestinationDeleteResponse,
)
```

Methods:

- <code title="post /organizations/{orgId}/dataexports/destinations">client.data_exports.destinations.<a href="./src/m3ter_sdk/resources/data_exports/destinations.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/data_exports/destination_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/data_exports/destination_create_response.py">DestinationCreateResponse</a></code>
- <code title="get /organizations/{orgId}/dataexports/destinations/{id}">client.data_exports.destinations.<a href="./src/m3ter_sdk/resources/data_exports/destinations.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/data_exports/destination_retrieve_response.py">DestinationRetrieveResponse</a></code>
- <code title="put /organizations/{orgId}/dataexports/destinations/{id}">client.data_exports.destinations.<a href="./src/m3ter_sdk/resources/data_exports/destinations.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/data_exports/destination_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/data_exports/destination_update_response.py">DestinationUpdateResponse</a></code>
- <code title="get /organizations/{orgId}/dataexports/destinations">client.data_exports.destinations.<a href="./src/m3ter_sdk/resources/data_exports/destinations.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/data_exports/destination_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/data_exports/data_export_destination.py">SyncCursor[DataExportDestination]</a></code>
- <code title="delete /organizations/{orgId}/dataexports/destinations/{id}">client.data_exports.destinations.<a href="./src/m3ter_sdk/resources/data_exports/destinations.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/data_exports/destination_delete_response.py">DestinationDeleteResponse</a></code>

## Jobs

Types:

```python
from m3ter_sdk.types.data_exports import DataExportJob, JobGetDownloadURLResponse
```

Methods:

- <code title="get /organizations/{orgId}/dataexports/jobs/{id}">client.data_exports.jobs.<a href="./src/m3ter_sdk/resources/data_exports/jobs.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/data_exports/data_export_job.py">DataExportJob</a></code>
- <code title="get /organizations/{orgId}/dataexports/jobs">client.data_exports.jobs.<a href="./src/m3ter_sdk/resources/data_exports/jobs.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/data_exports/job_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/data_exports/data_export_job.py">SyncCursor[DataExportJob]</a></code>
- <code title="get /organizations/{orgId}/dataexports/jobs/{jobId}/getdownloadurl">client.data_exports.jobs.<a href="./src/m3ter_sdk/resources/data_exports/jobs.py">get_download_url</a>(job_id, \*, org_id) -> <a href="./src/m3ter_sdk/types/data_exports/job_get_download_url_response.py">JobGetDownloadURLResponse</a></code>

## Schedules

Types:

```python
from m3ter_sdk.types.data_exports import (
    OperationalDataExportScheduleRequest,
    OperationalDataExportScheduleResponse,
    UsageDataExportScheduleRequest,
    UsageDataExportScheduleResponse,
    ScheduleCreateResponse,
    ScheduleRetrieveResponse,
    ScheduleUpdateResponse,
    ScheduleListResponse,
    ScheduleDeleteResponse,
)
```

Methods:

- <code title="post /organizations/{orgId}/dataexports/schedules">client.data_exports.schedules.<a href="./src/m3ter_sdk/resources/data_exports/schedules.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/data_exports/schedule_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/data_exports/schedule_create_response.py">ScheduleCreateResponse</a></code>
- <code title="get /organizations/{orgId}/dataexports/schedules/{id}">client.data_exports.schedules.<a href="./src/m3ter_sdk/resources/data_exports/schedules.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/data_exports/schedule_retrieve_response.py">ScheduleRetrieveResponse</a></code>
- <code title="put /organizations/{orgId}/dataexports/schedules/{id}">client.data_exports.schedules.<a href="./src/m3ter_sdk/resources/data_exports/schedules.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/data_exports/schedule_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/data_exports/schedule_update_response.py">ScheduleUpdateResponse</a></code>
- <code title="get /organizations/{orgId}/dataexports/schedules">client.data_exports.schedules.<a href="./src/m3ter_sdk/resources/data_exports/schedules.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/data_exports/schedule_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/data_exports/schedule_list_response.py">SyncCursor[ScheduleListResponse]</a></code>
- <code title="delete /organizations/{orgId}/dataexports/schedules/{id}">client.data_exports.schedules.<a href="./src/m3ter_sdk/resources/data_exports/schedules.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/data_exports/schedule_delete_response.py">ScheduleDeleteResponse</a></code>

# DebitReasons

Types:

```python
from m3ter_sdk.types import DebitReason
```

Methods:

- <code title="post /organizations/{orgId}/picklists/debitreasons">client.debit_reasons.<a href="./src/m3ter_sdk/resources/debit_reasons.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/debit_reason_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/debit_reason.py">DebitReason</a></code>
- <code title="get /organizations/{orgId}/picklists/debitreasons/{id}">client.debit_reasons.<a href="./src/m3ter_sdk/resources/debit_reasons.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/debit_reason.py">DebitReason</a></code>
- <code title="put /organizations/{orgId}/picklists/debitreasons/{id}">client.debit_reasons.<a href="./src/m3ter_sdk/resources/debit_reasons.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/debit_reason_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/debit_reason.py">DebitReason</a></code>
- <code title="get /organizations/{orgId}/picklists/debitreasons">client.debit_reasons.<a href="./src/m3ter_sdk/resources/debit_reasons.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/debit_reason_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/debit_reason.py">SyncCursor[DebitReason]</a></code>
- <code title="delete /organizations/{orgId}/picklists/debitreasons/{id}">client.debit_reasons.<a href="./src/m3ter_sdk/resources/debit_reasons.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/debit_reason.py">DebitReason</a></code>

# Events

Types:

```python
from m3ter_sdk.types import Event, EventGetFieldsResponse, EventGetTypesResponse
```

Methods:

- <code title="get /organizations/{orgId}/events/{id}">client.events.<a href="./src/m3ter_sdk/resources/events.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/event.py">Event</a></code>
- <code title="get /organizations/{orgId}/events">client.events.<a href="./src/m3ter_sdk/resources/events.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/event_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/event.py">SyncCursor[Event]</a></code>
- <code title="get /organizations/{orgId}/events/fields">client.events.<a href="./src/m3ter_sdk/resources/events.py">get_fields</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/event_get_fields_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/event_get_fields_response.py">EventGetFieldsResponse</a></code>
- <code title="get /organizations/{orgId}/events/types">client.events.<a href="./src/m3ter_sdk/resources/events.py">get_types</a>(\*, org_id) -> <a href="./src/m3ter_sdk/types/event_get_types_response.py">EventGetTypesResponse</a></code>

# ExternalMappings

Types:

```python
from m3ter_sdk.types import ExternalMapping
```

Methods:

- <code title="post /organizations/{orgId}/externalmappings">client.external_mappings.<a href="./src/m3ter_sdk/resources/external_mappings.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/external_mapping_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/external_mapping.py">ExternalMapping</a></code>
- <code title="get /organizations/{orgId}/externalmappings/{id}">client.external_mappings.<a href="./src/m3ter_sdk/resources/external_mappings.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/external_mapping.py">ExternalMapping</a></code>
- <code title="put /organizations/{orgId}/externalmappings/{id}">client.external_mappings.<a href="./src/m3ter_sdk/resources/external_mappings.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/external_mapping_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/external_mapping.py">ExternalMapping</a></code>
- <code title="get /organizations/{orgId}/externalmappings">client.external_mappings.<a href="./src/m3ter_sdk/resources/external_mappings.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/external_mapping_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/external_mapping.py">SyncCursor[ExternalMapping]</a></code>
- <code title="delete /organizations/{orgId}/externalmappings/{id}">client.external_mappings.<a href="./src/m3ter_sdk/resources/external_mappings.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/external_mapping.py">ExternalMapping</a></code>
- <code title="get /organizations/{orgId}/externalmappings/externalid/{system}/{externalTable}/{externalId}">client.external_mappings.<a href="./src/m3ter_sdk/resources/external_mappings.py">list_by_external_entity</a>(external_id, \*, org_id, system, external_table, \*\*<a href="src/m3ter_sdk/types/external_mapping_list_by_external_entity_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/external_mapping.py">SyncCursor[ExternalMapping]</a></code>
- <code title="get /organizations/{orgId}/externalmappings/external/{entity}/{m3terId}">client.external_mappings.<a href="./src/m3ter_sdk/resources/external_mappings.py">list_by_m3ter_entity</a>(m3ter_id, \*, org_id, entity, \*\*<a href="src/m3ter_sdk/types/external_mapping_list_by_m3ter_entity_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/external_mapping.py">SyncCursor[ExternalMapping]</a></code>

# IntegrationConfigurations

Types:

```python
from m3ter_sdk.types import (
    IntegrationConfiguration,
    IntegrationConfigurationCreateResponse,
    IntegrationConfigurationUpdateResponse,
    IntegrationConfigurationListResponse,
    IntegrationConfigurationDeleteResponse,
    IntegrationConfigurationEnableResponse,
)
```

Methods:

- <code title="post /organizations/{orgId}/integrationconfigs">client.integration_configurations.<a href="./src/m3ter_sdk/resources/integration_configurations.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/integration_configuration_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/integration_configuration_create_response.py">IntegrationConfigurationCreateResponse</a></code>
- <code title="get /organizations/{orgId}/integrationconfigs/{id}">client.integration_configurations.<a href="./src/m3ter_sdk/resources/integration_configurations.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/integration_configuration.py">IntegrationConfiguration</a></code>
- <code title="put /organizations/{orgId}/integrationconfigs/{id}">client.integration_configurations.<a href="./src/m3ter_sdk/resources/integration_configurations.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/integration_configuration_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/integration_configuration_update_response.py">IntegrationConfigurationUpdateResponse</a></code>
- <code title="get /organizations/{orgId}/integrationconfigs">client.integration_configurations.<a href="./src/m3ter_sdk/resources/integration_configurations.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/integration_configuration_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/integration_configuration_list_response.py">SyncCursor[IntegrationConfigurationListResponse]</a></code>
- <code title="delete /organizations/{orgId}/integrationconfigs/{id}">client.integration_configurations.<a href="./src/m3ter_sdk/resources/integration_configurations.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/integration_configuration_delete_response.py">IntegrationConfigurationDeleteResponse</a></code>
- <code title="post /organizations/{orgId}/integrationconfigs/{id}/enable">client.integration_configurations.<a href="./src/m3ter_sdk/resources/integration_configurations.py">enable</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/integration_configuration_enable_response.py">IntegrationConfigurationEnableResponse</a></code>
- <code title="get /organizations/{orgId}/integrationconfigs/entity/{entityType}">client.integration_configurations.<a href="./src/m3ter_sdk/resources/integration_configurations.py">get_by_entity</a>(entity_type, \*, org_id, \*\*<a href="src/m3ter_sdk/types/integration_configuration_get_by_entity_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/integration_configuration.py">IntegrationConfiguration</a></code>

# Meters

Types:

```python
from m3ter_sdk.types import DataField, Meter
```

Methods:

- <code title="post /organizations/{orgId}/meters">client.meters.<a href="./src/m3ter_sdk/resources/meters.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/meter_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/meter.py">Meter</a></code>
- <code title="get /organizations/{orgId}/meters/{id}">client.meters.<a href="./src/m3ter_sdk/resources/meters.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/meter.py">Meter</a></code>
- <code title="put /organizations/{orgId}/meters/{id}">client.meters.<a href="./src/m3ter_sdk/resources/meters.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/meter_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/meter.py">Meter</a></code>
- <code title="get /organizations/{orgId}/meters">client.meters.<a href="./src/m3ter_sdk/resources/meters.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/meter_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/meter.py">SyncCursor[Meter]</a></code>
- <code title="delete /organizations/{orgId}/meters/{id}">client.meters.<a href="./src/m3ter_sdk/resources/meters.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/meter.py">Meter</a></code>

# NotificationConfigurations

Types:

```python
from m3ter_sdk.types import NotificationConfiguration
```

Methods:

- <code title="post /organizations/{orgId}/notifications/configurations">client.notification_configurations.<a href="./src/m3ter_sdk/resources/notification_configurations.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/notification_configuration_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/notification_configuration.py">NotificationConfiguration</a></code>
- <code title="get /organizations/{orgId}/notifications/configurations/{id}">client.notification_configurations.<a href="./src/m3ter_sdk/resources/notification_configurations.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/notification_configuration.py">NotificationConfiguration</a></code>
- <code title="put /organizations/{orgId}/notifications/configurations/{id}">client.notification_configurations.<a href="./src/m3ter_sdk/resources/notification_configurations.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/notification_configuration_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/notification_configuration.py">NotificationConfiguration</a></code>
- <code title="get /organizations/{orgId}/notifications/configurations">client.notification_configurations.<a href="./src/m3ter_sdk/resources/notification_configurations.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/notification_configuration_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/notification_configuration.py">SyncCursor[NotificationConfiguration]</a></code>
- <code title="delete /organizations/{orgId}/notifications/configurations/{id}">client.notification_configurations.<a href="./src/m3ter_sdk/resources/notification_configurations.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/notification_configuration.py">NotificationConfiguration</a></code>

# OrganizationConfig

Types:

```python
from m3ter_sdk.types import OrganizationConfig
```

Methods:

- <code title="get /organizations/{orgId}/organizationconfig">client.organization_config.<a href="./src/m3ter_sdk/resources/organization_config.py">retrieve</a>(\*, org_id) -> <a href="./src/m3ter_sdk/types/organization_config.py">OrganizationConfig</a></code>
- <code title="put /organizations/{orgId}/organizationconfig">client.organization_config.<a href="./src/m3ter_sdk/resources/organization_config.py">update</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/organization_config_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/organization_config.py">OrganizationConfig</a></code>

# PermissionPolicies

Types:

```python
from m3ter_sdk.types import (
    PermissionPolicy,
    PermissionStatement,
    PrincipalPermissionRequest,
    PermissionPolicyAddToServiceUserResponse,
    PermissionPolicyAddToSupportUserResponse,
    PermissionPolicyAddToUserResponse,
    PermissionPolicyAddToUserGroupResponse,
    PermissionPolicyRemoveFromServiceUserResponse,
    PermissionPolicyRemoveFromSupportUserResponse,
    PermissionPolicyRemoveFromUserResponse,
    PermissionPolicyRemoveFromUserGroupResponse,
)
```

Methods:

- <code title="post /organizations/{orgId}/permissionpolicies">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/permission_policy_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/permission_policy.py">PermissionPolicy</a></code>
- <code title="get /organizations/{orgId}/permissionpolicies/{id}">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/permission_policy.py">PermissionPolicy</a></code>
- <code title="put /organizations/{orgId}/permissionpolicies/{id}">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/permission_policy_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/permission_policy.py">PermissionPolicy</a></code>
- <code title="get /organizations/{orgId}/permissionpolicies">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/permission_policy_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/permission_policy.py">SyncCursor[PermissionPolicy]</a></code>
- <code title="delete /organizations/{orgId}/permissionpolicies/{id}">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/permission_policy.py">PermissionPolicy</a></code>
- <code title="post /organizations/{orgId}/permissionpolicies/{permissionPolicyId}/addtoserviceuser">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">add_to_service_user</a>(permission_policy_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/permission_policy_add_to_service_user_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/permission_policy_add_to_service_user_response.py">PermissionPolicyAddToServiceUserResponse</a></code>
- <code title="post /organizations/{orgId}/permissionpolicies/{permissionPolicyId}/addtosupportusers">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">add_to_support_user</a>(permission_policy_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/permission_policy_add_to_support_user_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/permission_policy_add_to_support_user_response.py">PermissionPolicyAddToSupportUserResponse</a></code>
- <code title="post /organizations/{orgId}/permissionpolicies/{permissionPolicyId}/addtouser">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">add_to_user</a>(permission_policy_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/permission_policy_add_to_user_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/permission_policy_add_to_user_response.py">PermissionPolicyAddToUserResponse</a></code>
- <code title="post /organizations/{orgId}/permissionpolicies/{permissionPolicyId}/addtousergroup">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">add_to_user_group</a>(permission_policy_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/permission_policy_add_to_user_group_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/permission_policy_add_to_user_group_response.py">PermissionPolicyAddToUserGroupResponse</a></code>
- <code title="post /organizations/{orgId}/permissionpolicies/{permissionPolicyId}/removefromserviceuser">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">remove_from_service_user</a>(permission_policy_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/permission_policy_remove_from_service_user_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/permission_policy_remove_from_service_user_response.py">PermissionPolicyRemoveFromServiceUserResponse</a></code>
- <code title="post /organizations/{orgId}/permissionpolicies/{permissionPolicyId}/removefromsupportusers">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">remove_from_support_user</a>(permission_policy_id, \*, org_id) -> <a href="./src/m3ter_sdk/types/permission_policy_remove_from_support_user_response.py">PermissionPolicyRemoveFromSupportUserResponse</a></code>
- <code title="post /organizations/{orgId}/permissionpolicies/{permissionPolicyId}/removefromuser">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">remove_from_user</a>(permission_policy_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/permission_policy_remove_from_user_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/permission_policy_remove_from_user_response.py">PermissionPolicyRemoveFromUserResponse</a></code>
- <code title="post /organizations/{orgId}/permissionpolicies/{permissionPolicyId}/removefromusergroup">client.permission_policies.<a href="./src/m3ter_sdk/resources/permission_policies.py">remove_from_user_group</a>(permission_policy_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/permission_policy_remove_from_user_group_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/permission_policy_remove_from_user_group_response.py">PermissionPolicyRemoveFromUserGroupResponse</a></code>

# Plans

Types:

```python
from m3ter_sdk.types import Plan
```

Methods:

- <code title="post /organizations/{orgId}/plans">client.plans.<a href="./src/m3ter_sdk/resources/plans.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan.py">Plan</a></code>
- <code title="get /organizations/{orgId}/plans/{id}">client.plans.<a href="./src/m3ter_sdk/resources/plans.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan.py">Plan</a></code>
- <code title="put /organizations/{orgId}/plans/{id}">client.plans.<a href="./src/m3ter_sdk/resources/plans.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan.py">Plan</a></code>
- <code title="get /organizations/{orgId}/plans">client.plans.<a href="./src/m3ter_sdk/resources/plans.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan.py">SyncCursor[Plan]</a></code>
- <code title="delete /organizations/{orgId}/plans/{id}">client.plans.<a href="./src/m3ter_sdk/resources/plans.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan.py">Plan</a></code>

# PlanGroups

Types:

```python
from m3ter_sdk.types import PlanGroup
```

Methods:

- <code title="post /organizations/{orgId}/plangroups">client.plan_groups.<a href="./src/m3ter_sdk/resources/plan_groups.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_group_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_group.py">PlanGroup</a></code>
- <code title="get /organizations/{orgId}/plangroups/{id}">client.plan_groups.<a href="./src/m3ter_sdk/resources/plan_groups.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan_group.py">PlanGroup</a></code>
- <code title="put /organizations/{orgId}/plangroups/{id}">client.plan_groups.<a href="./src/m3ter_sdk/resources/plan_groups.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_group_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_group.py">PlanGroup</a></code>
- <code title="get /organizations/{orgId}/plangroups">client.plan_groups.<a href="./src/m3ter_sdk/resources/plan_groups.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_group_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_group.py">SyncCursor[PlanGroup]</a></code>
- <code title="delete /organizations/{orgId}/plangroups/{id}">client.plan_groups.<a href="./src/m3ter_sdk/resources/plan_groups.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan_group.py">PlanGroup</a></code>

# PlanGroupLinks

Types:

```python
from m3ter_sdk.types import PlanGroupLink
```

Methods:

- <code title="post /organizations/{orgId}/plangrouplinks">client.plan_group_links.<a href="./src/m3ter_sdk/resources/plan_group_links.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_group_link_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_group_link.py">PlanGroupLink</a></code>
- <code title="get /organizations/{orgId}/plangrouplinks/{id}">client.plan_group_links.<a href="./src/m3ter_sdk/resources/plan_group_links.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan_group_link.py">PlanGroupLink</a></code>
- <code title="put /organizations/{orgId}/plangrouplinks/{id}">client.plan_group_links.<a href="./src/m3ter_sdk/resources/plan_group_links.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_group_link_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_group_link.py">PlanGroupLink</a></code>
- <code title="get /organizations/{orgId}/plangrouplinks">client.plan_group_links.<a href="./src/m3ter_sdk/resources/plan_group_links.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_group_link_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_group_link.py">SyncCursor[PlanGroupLink]</a></code>
- <code title="delete /organizations/{orgId}/plangrouplinks/{id}">client.plan_group_links.<a href="./src/m3ter_sdk/resources/plan_group_links.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan_group_link.py">PlanGroupLink</a></code>

# PlanTemplates

Types:

```python
from m3ter_sdk.types import PlanTemplate
```

Methods:

- <code title="post /organizations/{orgId}/plantemplates">client.plan_templates.<a href="./src/m3ter_sdk/resources/plan_templates.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_template_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_template.py">PlanTemplate</a></code>
- <code title="get /organizations/{orgId}/plantemplates/{id}">client.plan_templates.<a href="./src/m3ter_sdk/resources/plan_templates.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan_template.py">PlanTemplate</a></code>
- <code title="put /organizations/{orgId}/plantemplates/{id}">client.plan_templates.<a href="./src/m3ter_sdk/resources/plan_templates.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_template_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_template.py">PlanTemplate</a></code>
- <code title="get /organizations/{orgId}/plantemplates">client.plan_templates.<a href="./src/m3ter_sdk/resources/plan_templates.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_template_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_template.py">SyncCursor[PlanTemplate]</a></code>
- <code title="delete /organizations/{orgId}/plantemplates/{id}">client.plan_templates.<a href="./src/m3ter_sdk/resources/plan_templates.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan_template.py">PlanTemplate</a></code>

# Pricings

Types:

```python
from m3ter_sdk.types import Pricing
```

Methods:

- <code title="post /organizations/{orgId}/pricings">client.pricings.<a href="./src/m3ter_sdk/resources/pricings.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/pricing_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/pricing.py">Pricing</a></code>
- <code title="get /organizations/{orgId}/pricings/{id}">client.pricings.<a href="./src/m3ter_sdk/resources/pricings.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/pricing.py">Pricing</a></code>
- <code title="put /organizations/{orgId}/pricings/{id}">client.pricings.<a href="./src/m3ter_sdk/resources/pricings.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/pricing_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/pricing.py">Pricing</a></code>
- <code title="get /organizations/{orgId}/pricings">client.pricings.<a href="./src/m3ter_sdk/resources/pricings.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/pricing_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/pricing.py">SyncCursor[Pricing]</a></code>
- <code title="delete /organizations/{orgId}/pricings/{id}">client.pricings.<a href="./src/m3ter_sdk/resources/pricings.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/pricing.py">Pricing</a></code>

# Products

Types:

```python
from m3ter_sdk.types import Product
```

Methods:

- <code title="post /organizations/{orgId}/products">client.products.<a href="./src/m3ter_sdk/resources/products.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/product_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/product.py">Product</a></code>
- <code title="get /organizations/{orgId}/products/{id}">client.products.<a href="./src/m3ter_sdk/resources/products.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/product.py">Product</a></code>
- <code title="put /organizations/{orgId}/products/{id}">client.products.<a href="./src/m3ter_sdk/resources/products.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/product_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/product.py">Product</a></code>
- <code title="get /organizations/{orgId}/products">client.products.<a href="./src/m3ter_sdk/resources/products.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/product_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/product.py">SyncCursor[Product]</a></code>
- <code title="delete /organizations/{orgId}/products/{id}">client.products.<a href="./src/m3ter_sdk/resources/products.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/product.py">Product</a></code>

# ResourceGroups

Types:

```python
from m3ter_sdk.types import ResourceGroup, ResourceGroupListContentsResponse
```

Methods:

- <code title="post /organizations/{orgId}/resourcegroups/{type}">client.resource_groups.<a href="./src/m3ter_sdk/resources/resource_groups.py">create</a>(type, \*, org_id, \*\*<a href="src/m3ter_sdk/types/resource_group_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/resource_group.py">ResourceGroup</a></code>
- <code title="get /organizations/{orgId}/resourcegroups/{type}/{id}">client.resource_groups.<a href="./src/m3ter_sdk/resources/resource_groups.py">retrieve</a>(id, \*, org_id, type) -> <a href="./src/m3ter_sdk/types/resource_group.py">ResourceGroup</a></code>
- <code title="put /organizations/{orgId}/resourcegroups/{type}/{id}">client.resource_groups.<a href="./src/m3ter_sdk/resources/resource_groups.py">update</a>(id, \*, org_id, type, \*\*<a href="src/m3ter_sdk/types/resource_group_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/resource_group.py">ResourceGroup</a></code>
- <code title="get /organizations/{orgId}/resourcegroups/{type}">client.resource_groups.<a href="./src/m3ter_sdk/resources/resource_groups.py">list</a>(type, \*, org_id, \*\*<a href="src/m3ter_sdk/types/resource_group_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/resource_group.py">SyncCursor[ResourceGroup]</a></code>
- <code title="delete /organizations/{orgId}/resourcegroups/{type}/{id}">client.resource_groups.<a href="./src/m3ter_sdk/resources/resource_groups.py">delete</a>(id, \*, org_id, type) -> <a href="./src/m3ter_sdk/types/resource_group.py">ResourceGroup</a></code>
- <code title="post /organizations/{orgId}/resourcegroups/{type}/{resourceGroupId}/addresource">client.resource_groups.<a href="./src/m3ter_sdk/resources/resource_groups.py">add_resource</a>(resource_group_id, \*, org_id, type, \*\*<a href="src/m3ter_sdk/types/resource_group_add_resource_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/resource_group.py">ResourceGroup</a></code>
- <code title="post /organizations/{orgId}/resourcegroups/{type}/{resourceGroupId}/contents">client.resource_groups.<a href="./src/m3ter_sdk/resources/resource_groups.py">list_contents</a>(resource_group_id, \*, org_id, type, \*\*<a href="src/m3ter_sdk/types/resource_group_list_contents_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/resource_group_list_contents_response.py">SyncCursor[ResourceGroupListContentsResponse]</a></code>
- <code title="get /organizations/{orgId}/resourcegroups/{type}/{resourceGroupId}/permissions">client.resource_groups.<a href="./src/m3ter_sdk/resources/resource_groups.py">list_permissions</a>(resource_group_id, \*, org_id, type, \*\*<a href="src/m3ter_sdk/types/resource_group_list_permissions_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/permission_policy.py">SyncCursor[PermissionPolicy]</a></code>
- <code title="post /organizations/{orgId}/resourcegroups/{type}/{resourceGroupId}/removeresource">client.resource_groups.<a href="./src/m3ter_sdk/resources/resource_groups.py">remove_resource</a>(resource_group_id, \*, org_id, type, \*\*<a href="src/m3ter_sdk/types/resource_group_remove_resource_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/resource_group.py">ResourceGroup</a></code>

# ScheduledEventConfigurations

Types:

```python
from m3ter_sdk.types import ScheduledEventConfiguration
```

Methods:

- <code title="post /organizations/{orgId}/scheduledevents/configurations">client.scheduled_event_configurations.<a href="./src/m3ter_sdk/resources/scheduled_event_configurations.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/scheduled_event_configuration_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/scheduled_event_configuration.py">ScheduledEventConfiguration</a></code>
- <code title="get /organizations/{orgId}/scheduledevents/configurations/{id}">client.scheduled_event_configurations.<a href="./src/m3ter_sdk/resources/scheduled_event_configurations.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/scheduled_event_configuration.py">ScheduledEventConfiguration</a></code>
- <code title="put /organizations/{orgId}/scheduledevents/configurations/{id}">client.scheduled_event_configurations.<a href="./src/m3ter_sdk/resources/scheduled_event_configurations.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/scheduled_event_configuration_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/scheduled_event_configuration.py">ScheduledEventConfiguration</a></code>
- <code title="get /organizations/{orgId}/scheduledevents/configurations">client.scheduled_event_configurations.<a href="./src/m3ter_sdk/resources/scheduled_event_configurations.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/scheduled_event_configuration_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/scheduled_event_configuration.py">SyncCursor[ScheduledEventConfiguration]</a></code>
- <code title="delete /organizations/{orgId}/scheduledevents/configurations/{id}">client.scheduled_event_configurations.<a href="./src/m3ter_sdk/resources/scheduled_event_configurations.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/scheduled_event_configuration.py">ScheduledEventConfiguration</a></code>

# TransactionTypes

Types:

```python
from m3ter_sdk.types import TransactionType
```

Methods:

- <code title="post /organizations/{orgId}/picklists/transactiontypes">client.transaction_types.<a href="./src/m3ter_sdk/resources/transaction_types.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/transaction_type_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/transaction_type.py">TransactionType</a></code>
- <code title="get /organizations/{orgId}/picklists/transactiontypes/{id}">client.transaction_types.<a href="./src/m3ter_sdk/resources/transaction_types.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/transaction_type.py">TransactionType</a></code>
- <code title="put /organizations/{orgId}/picklists/transactiontypes/{id}">client.transaction_types.<a href="./src/m3ter_sdk/resources/transaction_types.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/transaction_type_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/transaction_type.py">TransactionType</a></code>
- <code title="get /organizations/{orgId}/picklists/transactiontypes">client.transaction_types.<a href="./src/m3ter_sdk/resources/transaction_types.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/transaction_type_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/transaction_type.py">SyncCursor[TransactionType]</a></code>
- <code title="delete /organizations/{orgId}/picklists/transactiontypes/{id}">client.transaction_types.<a href="./src/m3ter_sdk/resources/transaction_types.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/transaction_type.py">TransactionType</a></code>

# Usage

Types:

```python
from m3ter_sdk.types import DownloadURLResponse, SubmitMeasurementsResponse, UsageQueryResponse
```

Methods:

- <code title="get /organizations/{orgId}/measurements/failedIngest/getDownloadUrl">client.usage.<a href="./src/m3ter_sdk/resources/usage/usage.py">get_failed_ingest_download_url</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/usage_get_failed_ingest_download_url_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/download_url_response.py">DownloadURLResponse</a></code>
- <code title="post /organizations/{orgId}/usage/query">client.usage.<a href="./src/m3ter_sdk/resources/usage/usage.py">query</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/usage_query_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/usage_query_response.py">UsageQueryResponse</a></code>
- <code title="post /organizations/{orgId}/measurements">client.usage.<a href="./src/m3ter_sdk/resources/usage/usage.py">submit</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/usage_submit_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/submit_measurements_response.py">SubmitMeasurementsResponse</a></code>

## FileUploads

Types:

```python
from m3ter_sdk.types.usage import FileUploadGenerateUploadURLResponse
```

Methods:

- <code title="post /organizations/{orgId}/fileuploads/measurements/generateUploadUrl">client.usage.file_uploads.<a href="./src/m3ter_sdk/resources/usage/file_uploads/file_uploads.py">generate_upload_url</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/usage/file_upload_generate_upload_url_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/usage/file_upload_generate_upload_url_response.py">FileUploadGenerateUploadURLResponse</a></code>

### Jobs

Types:

```python
from m3ter_sdk.types.usage.file_uploads import FileUploadJob, JobGetOriginalDownloadURLResponse
```

Methods:

- <code title="get /organizations/{orgId}/fileuploads/measurements/jobs/{id}">client.usage.file_uploads.jobs.<a href="./src/m3ter_sdk/resources/usage/file_uploads/jobs.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/usage/file_uploads/file_upload_job.py">FileUploadJob</a></code>
- <code title="get /organizations/{orgId}/fileuploads/measurements/jobs">client.usage.file_uploads.jobs.<a href="./src/m3ter_sdk/resources/usage/file_uploads/jobs.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/usage/file_uploads/job_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/usage/file_uploads/file_upload_job.py">SyncCursor[FileUploadJob]</a></code>
- <code title="get /organizations/{orgId}/fileuploads/measurements/jobs/{id}/original">client.usage.file_uploads.jobs.<a href="./src/m3ter_sdk/resources/usage/file_uploads/jobs.py">get_original_download_url</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/usage/file_uploads/job_get_original_download_url_response.py">JobGetOriginalDownloadURLResponse</a></code>

# Users

Types:

```python
from m3ter_sdk.types import User, UserMeResponse
```

Methods:

- <code title="get /organizations/{orgId}/users/{id}">client.users.<a href="./src/m3ter_sdk/resources/users/users.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/user.py">User</a></code>
- <code title="put /organizations/{orgId}/users/{id}">client.users.<a href="./src/m3ter_sdk/resources/users/users.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/user_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/user.py">User</a></code>
- <code title="get /organizations/{orgId}/users">client.users.<a href="./src/m3ter_sdk/resources/users/users.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/user_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/user.py">SyncCursor[User]</a></code>
- <code title="get /organizations/{orgId}/users/{id}/permissions">client.users.<a href="./src/m3ter_sdk/resources/users/users.py">get_permissions</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/user_get_permissions_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/permission_policy.py">PermissionPolicy</a></code>
- <code title="get /organizations/{orgId}/users/{id}/usergroups">client.users.<a href="./src/m3ter_sdk/resources/users/users.py">get_user_groups</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/user_get_user_groups_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/resource_group.py">ResourceGroup</a></code>
- <code title="get /organizations/{orgId}/users/me">client.users.<a href="./src/m3ter_sdk/resources/users/users.py">me</a>(\*, org_id) -> <a href="./src/m3ter_sdk/types/user_me_response.py">UserMeResponse</a></code>
- <code title="put /organizations/{orgId}/users/{id}/password/resend">client.users.<a href="./src/m3ter_sdk/resources/users/users.py">resend_password</a>(id, \*, org_id) -> None</code>

## Invitations

Types:

```python
from m3ter_sdk.types.users import Invitation
```

Methods:

- <code title="post /organizations/{orgId}/invitations">client.users.invitations.<a href="./src/m3ter_sdk/resources/users/invitations.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/users/invitation_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/users/invitation.py">Invitation</a></code>
- <code title="get /organizations/{orgId}/invitations/{id}">client.users.invitations.<a href="./src/m3ter_sdk/resources/users/invitations.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/users/invitation.py">Invitation</a></code>
- <code title="get /organizations/{orgId}/invitations">client.users.invitations.<a href="./src/m3ter_sdk/resources/users/invitations.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/users/invitation_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/users/invitation.py">SyncCursor[Invitation]</a></code>

# Webhooks

Types:

```python
from m3ter_sdk.types import (
    M3terSignedCredentialsReq,
    M3terSignedCredentialsResp,
    Webhook,
    WebhookCreateResponse,
    WebhookUpdateResponse,
    WebhookSetActiveResponse,
)
```

Methods:

- <code title="post /organizations/{orgId}/integrationdestinations/webhooks">client.webhooks.<a href="./src/m3ter_sdk/resources/webhooks.py">create</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/webhook_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /organizations/{orgId}/integrationdestinations/webhooks/{id}">client.webhooks.<a href="./src/m3ter_sdk/resources/webhooks.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/webhook.py">Webhook</a></code>
- <code title="put /organizations/{orgId}/integrationdestinations/webhooks/{id}">client.webhooks.<a href="./src/m3ter_sdk/resources/webhooks.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/webhook_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /organizations/{orgId}/integrationdestinations/webhooks">client.webhooks.<a href="./src/m3ter_sdk/resources/webhooks.py">list</a>(\*, org_id, \*\*<a href="src/m3ter_sdk/types/webhook_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/webhook.py">SyncCursor[Webhook]</a></code>
- <code title="delete /organizations/{orgId}/integrationdestinations/webhooks/{id}">client.webhooks.<a href="./src/m3ter_sdk/resources/webhooks.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/webhook.py">Webhook</a></code>
- <code title="put /organizations/{orgId}/integrationdestinations/webhooks/{id}/active">client.webhooks.<a href="./src/m3ter_sdk/resources/webhooks.py">set_active</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/webhook_set_active_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/webhook_set_active_response.py">WebhookSetActiveResponse</a></code>
