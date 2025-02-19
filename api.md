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
from m3ter_sdk.types import Account, AccountSearchResponse
```

Methods:

- <code title="post /organizations/{orgId}/accounts">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/account_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account.py">Account</a></code>
- <code title="get /organizations/{orgId}/accounts/{id}">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/account.py">Account</a></code>
- <code title="put /organizations/{orgId}/accounts/{id}">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/account_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account.py">Account</a></code>
- <code title="get /organizations/{orgId}/accounts">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/account_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account.py">SyncCursor[Account]</a></code>
- <code title="delete /organizations/{orgId}/accounts/{id}">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/account.py">Account</a></code>
- <code title="get /organizations/{orgId}/accounts/{id}/children">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">list_children</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/account_list_children_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account.py">Account</a></code>
- <code title="get /organizations/{orgId}/accounts/search">client.accounts.<a href="./src/m3ter_sdk/resources/accounts.py">search</a>(org_id, \*\*<a href="src/m3ter_sdk/types/account_search_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account_search_response.py">AccountSearchResponse</a></code>

# AccountPlans

Types:

```python
from m3ter_sdk.types import AccountPlan
```

Methods:

- <code title="post /organizations/{orgId}/accountplans">client.account_plans.<a href="./src/m3ter_sdk/resources/account_plans.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/account_plan_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account_plan.py">AccountPlan</a></code>
- <code title="get /organizations/{orgId}/accountplans/{id}">client.account_plans.<a href="./src/m3ter_sdk/resources/account_plans.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/account_plan.py">AccountPlan</a></code>
- <code title="put /organizations/{orgId}/accountplans/{id}">client.account_plans.<a href="./src/m3ter_sdk/resources/account_plans.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/account_plan_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account_plan.py">AccountPlan</a></code>
- <code title="get /organizations/{orgId}/accountplans">client.account_plans.<a href="./src/m3ter_sdk/resources/account_plans.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/account_plan_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/account_plan.py">SyncCursor[AccountPlan]</a></code>
- <code title="delete /organizations/{orgId}/accountplans/{id}">client.account_plans.<a href="./src/m3ter_sdk/resources/account_plans.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/account_plan.py">AccountPlan</a></code>

# Aggregations

Types:

```python
from m3ter_sdk.types import Aggregation
```

Methods:

- <code title="post /organizations/{orgId}/aggregations">client.aggregations.<a href="./src/m3ter_sdk/resources/aggregations.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/aggregation_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/aggregation.py">Aggregation</a></code>
- <code title="get /organizations/{orgId}/aggregations/{id}">client.aggregations.<a href="./src/m3ter_sdk/resources/aggregations.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/aggregation.py">Aggregation</a></code>
- <code title="put /organizations/{orgId}/aggregations/{id}">client.aggregations.<a href="./src/m3ter_sdk/resources/aggregations.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/aggregation_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/aggregation.py">Aggregation</a></code>
- <code title="get /organizations/{orgId}/aggregations">client.aggregations.<a href="./src/m3ter_sdk/resources/aggregations.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/aggregation_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/aggregation.py">SyncCursor[Aggregation]</a></code>
- <code title="delete /organizations/{orgId}/aggregations/{id}">client.aggregations.<a href="./src/m3ter_sdk/resources/aggregations.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/aggregation.py">Aggregation</a></code>

# Balances

Types:

```python
from m3ter_sdk.types import Balance
```

Methods:

- <code title="post /organizations/{orgId}/balances">client.balances.<a href="./src/m3ter_sdk/resources/balances/balances.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/balance_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/balance.py">Balance</a></code>
- <code title="get /organizations/{orgId}/balances/{id}">client.balances.<a href="./src/m3ter_sdk/resources/balances/balances.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/balance.py">Balance</a></code>
- <code title="put /organizations/{orgId}/balances/{id}">client.balances.<a href="./src/m3ter_sdk/resources/balances/balances.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/balance_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/balance.py">Balance</a></code>
- <code title="get /organizations/{orgId}/balances">client.balances.<a href="./src/m3ter_sdk/resources/balances/balances.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/balance_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/balance.py">SyncCursor[Balance]</a></code>
- <code title="delete /organizations/{orgId}/balances/{id}">client.balances.<a href="./src/m3ter_sdk/resources/balances/balances.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/balance.py">Balance</a></code>

## Transactions

Types:

```python
from m3ter_sdk.types.balances import Transaction
```

Methods:

- <code title="post /organizations/{orgId}/balances/{balanceId}/transactions">client.balances.transactions.<a href="./src/m3ter_sdk/resources/balances/transactions.py">create</a>(balance_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/balances/transaction_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/balances/transaction.py">Transaction</a></code>
- <code title="get /organizations/{orgId}/balances/{balanceId}/transactions">client.balances.transactions.<a href="./src/m3ter_sdk/resources/balances/transactions.py">list</a>(balance_id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/balances/transaction_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/balances/transaction.py">SyncCursor[Transaction]</a></code>

# BillConfig

Types:

```python
from m3ter_sdk.types import BillConfig
```

Methods:

- <code title="get /organizations/{orgId}/billconfig">client.bill_config.<a href="./src/m3ter_sdk/resources/bill_config.py">retrieve</a>(org_id) -> <a href="./src/m3ter_sdk/types/bill_config.py">BillConfig</a></code>
- <code title="put /organizations/{orgId}/billconfig">client.bill_config.<a href="./src/m3ter_sdk/resources/bill_config.py">update</a>(org_id, \*\*<a href="src/m3ter_sdk/types/bill_config_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/bill_config.py">BillConfig</a></code>

# Commitments

Types:

```python
from m3ter_sdk.types import Commitment, CommitmentSearchResponse
```

Methods:

- <code title="post /organizations/{orgId}/commitments">client.commitments.<a href="./src/m3ter_sdk/resources/commitments.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/commitment_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/commitment.py">Commitment</a></code>
- <code title="get /organizations/{orgId}/commitments/{id}">client.commitments.<a href="./src/m3ter_sdk/resources/commitments.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/commitment.py">Commitment</a></code>
- <code title="put /organizations/{orgId}/commitments/{id}">client.commitments.<a href="./src/m3ter_sdk/resources/commitments.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/commitment_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/commitment.py">Commitment</a></code>
- <code title="get /organizations/{orgId}/commitments">client.commitments.<a href="./src/m3ter_sdk/resources/commitments.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/commitment_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/commitment.py">SyncCursor[Commitment]</a></code>
- <code title="delete /organizations/{orgId}/commitments/{id}">client.commitments.<a href="./src/m3ter_sdk/resources/commitments.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/commitment.py">Commitment</a></code>
- <code title="get /organizations/{orgId}/commitments/search">client.commitments.<a href="./src/m3ter_sdk/resources/commitments.py">search</a>(org_id, \*\*<a href="src/m3ter_sdk/types/commitment_search_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/commitment_search_response.py">CommitmentSearchResponse</a></code>

# CompoundAggregations

Types:

```python
from m3ter_sdk.types import CompoundAggregation
```

Methods:

- <code title="post /organizations/{orgId}/compoundaggregations">client.compound_aggregations.<a href="./src/m3ter_sdk/resources/compound_aggregations.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/compound_aggregation_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/aggregation.py">Aggregation</a></code>
- <code title="get /organizations/{orgId}/compoundaggregations/{id}">client.compound_aggregations.<a href="./src/m3ter_sdk/resources/compound_aggregations.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/compound_aggregation.py">CompoundAggregation</a></code>
- <code title="put /organizations/{orgId}/compoundaggregations/{id}">client.compound_aggregations.<a href="./src/m3ter_sdk/resources/compound_aggregations.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/compound_aggregation_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/aggregation.py">Aggregation</a></code>
- <code title="get /organizations/{orgId}/compoundaggregations">client.compound_aggregations.<a href="./src/m3ter_sdk/resources/compound_aggregations.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/compound_aggregation_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/compound_aggregation.py">SyncCursor[CompoundAggregation]</a></code>
- <code title="delete /organizations/{orgId}/compoundaggregations/{id}">client.compound_aggregations.<a href="./src/m3ter_sdk/resources/compound_aggregations.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/compound_aggregation.py">CompoundAggregation</a></code>

# Contracts

Types:

```python
from m3ter_sdk.types import Contract
```

Methods:

- <code title="post /organizations/{orgId}/contracts">client.contracts.<a href="./src/m3ter_sdk/resources/contracts.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/contract_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/contract.py">Contract</a></code>
- <code title="get /organizations/{orgId}/contracts/{id}">client.contracts.<a href="./src/m3ter_sdk/resources/contracts.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/contract.py">Contract</a></code>
- <code title="put /organizations/{orgId}/contracts/{id}">client.contracts.<a href="./src/m3ter_sdk/resources/contracts.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/contract_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/contract.py">Contract</a></code>
- <code title="get /organizations/{orgId}/contracts">client.contracts.<a href="./src/m3ter_sdk/resources/contracts.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/contract_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/contract.py">SyncCursor[Contract]</a></code>
- <code title="delete /organizations/{orgId}/contracts/{id}">client.contracts.<a href="./src/m3ter_sdk/resources/contracts.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/contract.py">Contract</a></code>

# Counters

Types:

```python
from m3ter_sdk.types import Counter
```

Methods:

- <code title="post /organizations/{orgId}/counters">client.counters.<a href="./src/m3ter_sdk/resources/counters.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/counter_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter.py">Counter</a></code>
- <code title="get /organizations/{orgId}/counters/{id}">client.counters.<a href="./src/m3ter_sdk/resources/counters.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/counter.py">Counter</a></code>
- <code title="put /organizations/{orgId}/counters/{id}">client.counters.<a href="./src/m3ter_sdk/resources/counters.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/counter_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter.py">Counter</a></code>
- <code title="get /organizations/{orgId}/counters">client.counters.<a href="./src/m3ter_sdk/resources/counters.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/counter_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter.py">SyncCursor[Counter]</a></code>
- <code title="delete /organizations/{orgId}/counters/{id}">client.counters.<a href="./src/m3ter_sdk/resources/counters.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/counter.py">Counter</a></code>

# CounterAdjustments

Types:

```python
from m3ter_sdk.types import CounterAdjustment
```

Methods:

- <code title="post /organizations/{orgId}/counteradjustments">client.counter_adjustments.<a href="./src/m3ter_sdk/resources/counter_adjustments.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/counter_adjustment_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter_adjustment.py">CounterAdjustment</a></code>
- <code title="get /organizations/{orgId}/counteradjustments/{id}">client.counter_adjustments.<a href="./src/m3ter_sdk/resources/counter_adjustments.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/counter_adjustment.py">CounterAdjustment</a></code>
- <code title="put /organizations/{orgId}/counteradjustments/{id}">client.counter_adjustments.<a href="./src/m3ter_sdk/resources/counter_adjustments.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/counter_adjustment_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter_adjustment.py">CounterAdjustment</a></code>
- <code title="get /organizations/{orgId}/counteradjustments">client.counter_adjustments.<a href="./src/m3ter_sdk/resources/counter_adjustments.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/counter_adjustment_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter_adjustment.py">SyncCursor[CounterAdjustment]</a></code>
- <code title="delete /organizations/{orgId}/counteradjustments/{id}">client.counter_adjustments.<a href="./src/m3ter_sdk/resources/counter_adjustments.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/counter_adjustment.py">CounterAdjustment</a></code>

# CounterPricings

Types:

```python
from m3ter_sdk.types import CounterPricing
```

Methods:

- <code title="post /organizations/{orgId}/counterpricings">client.counter_pricings.<a href="./src/m3ter_sdk/resources/counter_pricings.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/counter_pricing_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter_pricing.py">CounterPricing</a></code>
- <code title="get /organizations/{orgId}/counterpricings/{id}">client.counter_pricings.<a href="./src/m3ter_sdk/resources/counter_pricings.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/counter_pricing.py">CounterPricing</a></code>
- <code title="put /organizations/{orgId}/counterpricings/{id}">client.counter_pricings.<a href="./src/m3ter_sdk/resources/counter_pricings.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/counter_pricing_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter_pricing.py">CounterPricing</a></code>
- <code title="get /organizations/{orgId}/counterpricings">client.counter_pricings.<a href="./src/m3ter_sdk/resources/counter_pricings.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/counter_pricing_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/counter_pricing.py">SyncCursor[CounterPricing]</a></code>
- <code title="delete /organizations/{orgId}/counterpricings/{id}">client.counter_pricings.<a href="./src/m3ter_sdk/resources/counter_pricings.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/counter_pricing.py">CounterPricing</a></code>

# CreditReasons

Types:

```python
from m3ter_sdk.types import CreditReason
```

Methods:

- <code title="post /organizations/{orgId}/picklists/creditreasons">client.credit_reasons.<a href="./src/m3ter_sdk/resources/credit_reasons.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/credit_reason_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/credit_reason.py">CreditReason</a></code>
- <code title="get /organizations/{orgId}/picklists/creditreasons/{id}">client.credit_reasons.<a href="./src/m3ter_sdk/resources/credit_reasons.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/credit_reason.py">CreditReason</a></code>
- <code title="put /organizations/{orgId}/picklists/creditreasons/{id}">client.credit_reasons.<a href="./src/m3ter_sdk/resources/credit_reasons.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/credit_reason_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/credit_reason.py">CreditReason</a></code>
- <code title="get /organizations/{orgId}/picklists/creditreasons">client.credit_reasons.<a href="./src/m3ter_sdk/resources/credit_reasons.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/credit_reason_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/credit_reason.py">SyncCursor[CreditReason]</a></code>
- <code title="delete /organizations/{orgId}/picklists/creditreasons/{id}">client.credit_reasons.<a href="./src/m3ter_sdk/resources/credit_reasons.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/credit_reason.py">CreditReason</a></code>

# Currencies

Types:

```python
from m3ter_sdk.types import Currency
```

Methods:

- <code title="post /organizations/{orgId}/picklists/currency">client.currencies.<a href="./src/m3ter_sdk/resources/currencies.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/currency_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/currency.py">Currency</a></code>
- <code title="get /organizations/{orgId}/picklists/currency/{id}">client.currencies.<a href="./src/m3ter_sdk/resources/currencies.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/currency.py">Currency</a></code>
- <code title="put /organizations/{orgId}/picklists/currency/{id}">client.currencies.<a href="./src/m3ter_sdk/resources/currencies.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/currency_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/currency.py">Currency</a></code>
- <code title="get /organizations/{orgId}/picklists/currency">client.currencies.<a href="./src/m3ter_sdk/resources/currencies.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/currency_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/currency.py">SyncCursor[Currency]</a></code>
- <code title="delete /organizations/{orgId}/picklists/currency/{id}">client.currencies.<a href="./src/m3ter_sdk/resources/currencies.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/currency.py">Currency</a></code>

# DebitReasons

Types:

```python
from m3ter_sdk.types import DebitReason
```

Methods:

- <code title="post /organizations/{orgId}/picklists/debitreasons">client.debit_reasons.<a href="./src/m3ter_sdk/resources/debit_reasons.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/debit_reason_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/debit_reason.py">DebitReason</a></code>
- <code title="get /organizations/{orgId}/picklists/debitreasons/{id}">client.debit_reasons.<a href="./src/m3ter_sdk/resources/debit_reasons.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/debit_reason.py">DebitReason</a></code>
- <code title="put /organizations/{orgId}/picklists/debitreasons/{id}">client.debit_reasons.<a href="./src/m3ter_sdk/resources/debit_reasons.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/debit_reason_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/debit_reason.py">DebitReason</a></code>
- <code title="get /organizations/{orgId}/picklists/debitreasons">client.debit_reasons.<a href="./src/m3ter_sdk/resources/debit_reasons.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/debit_reason_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/debit_reason.py">SyncCursor[DebitReason]</a></code>
- <code title="delete /organizations/{orgId}/picklists/debitreasons/{id}">client.debit_reasons.<a href="./src/m3ter_sdk/resources/debit_reasons.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/debit_reason.py">DebitReason</a></code>

# Meters

Types:

```python
from m3ter_sdk.types import Meter
```

Methods:

- <code title="post /organizations/{orgId}/meters">client.meters.<a href="./src/m3ter_sdk/resources/meters.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/meter_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/meter.py">Meter</a></code>
- <code title="get /organizations/{orgId}/meters/{id}">client.meters.<a href="./src/m3ter_sdk/resources/meters.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/meter.py">Meter</a></code>
- <code title="put /organizations/{orgId}/meters/{id}">client.meters.<a href="./src/m3ter_sdk/resources/meters.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/meter_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/meter.py">Meter</a></code>
- <code title="get /organizations/{orgId}/meters">client.meters.<a href="./src/m3ter_sdk/resources/meters.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/meter_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/meter.py">SyncCursor[Meter]</a></code>
- <code title="delete /organizations/{orgId}/meters/{id}">client.meters.<a href="./src/m3ter_sdk/resources/meters.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/meter.py">Meter</a></code>

# OrganizationConfig

Types:

```python
from m3ter_sdk.types import OrganizationConfig
```

Methods:

- <code title="get /organizations/{orgId}/organizationconfig">client.organization_config.<a href="./src/m3ter_sdk/resources/organization_config.py">retrieve</a>(org_id) -> <a href="./src/m3ter_sdk/types/organization_config.py">OrganizationConfig</a></code>
- <code title="put /organizations/{orgId}/organizationconfig">client.organization_config.<a href="./src/m3ter_sdk/resources/organization_config.py">update</a>(org_id, \*\*<a href="src/m3ter_sdk/types/organization_config_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/organization_config.py">OrganizationConfig</a></code>

# Plans

Types:

```python
from m3ter_sdk.types import Plan
```

Methods:

- <code title="post /organizations/{orgId}/plans">client.plans.<a href="./src/m3ter_sdk/resources/plans.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/plan_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan.py">Plan</a></code>
- <code title="get /organizations/{orgId}/plans/{id}">client.plans.<a href="./src/m3ter_sdk/resources/plans.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan.py">Plan</a></code>
- <code title="put /organizations/{orgId}/plans/{id}">client.plans.<a href="./src/m3ter_sdk/resources/plans.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan.py">Plan</a></code>
- <code title="get /organizations/{orgId}/plans">client.plans.<a href="./src/m3ter_sdk/resources/plans.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/plan_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan.py">SyncCursor[Plan]</a></code>
- <code title="delete /organizations/{orgId}/plans/{id}">client.plans.<a href="./src/m3ter_sdk/resources/plans.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan.py">Plan</a></code>

# PlanGroups

Types:

```python
from m3ter_sdk.types import PlanGroup
```

Methods:

- <code title="post /organizations/{orgId}/plangroups">client.plan_groups.<a href="./src/m3ter_sdk/resources/plan_groups.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/plan_group_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_group.py">PlanGroup</a></code>
- <code title="get /organizations/{orgId}/plangroups/{id}">client.plan_groups.<a href="./src/m3ter_sdk/resources/plan_groups.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan_group.py">PlanGroup</a></code>
- <code title="put /organizations/{orgId}/plangroups/{id}">client.plan_groups.<a href="./src/m3ter_sdk/resources/plan_groups.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_group_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_group.py">PlanGroup</a></code>
- <code title="get /organizations/{orgId}/plangroups">client.plan_groups.<a href="./src/m3ter_sdk/resources/plan_groups.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/plan_group_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_group.py">SyncCursor[PlanGroup]</a></code>
- <code title="delete /organizations/{orgId}/plangroups/{id}">client.plan_groups.<a href="./src/m3ter_sdk/resources/plan_groups.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan_group.py">PlanGroup</a></code>

# PlanGroupLinks

Types:

```python
from m3ter_sdk.types import PlanGroupLink
```

Methods:

- <code title="post /organizations/{orgId}/plangrouplinks">client.plan_group_links.<a href="./src/m3ter_sdk/resources/plan_group_links.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/plan_group_link_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_group_link.py">PlanGroupLink</a></code>
- <code title="get /organizations/{orgId}/plangrouplinks/{id}">client.plan_group_links.<a href="./src/m3ter_sdk/resources/plan_group_links.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan_group_link.py">PlanGroupLink</a></code>
- <code title="put /organizations/{orgId}/plangrouplinks/{id}">client.plan_group_links.<a href="./src/m3ter_sdk/resources/plan_group_links.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_group_link_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_group_link.py">PlanGroupLink</a></code>
- <code title="get /organizations/{orgId}/plangrouplinks">client.plan_group_links.<a href="./src/m3ter_sdk/resources/plan_group_links.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/plan_group_link_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_group_link.py">SyncCursor[PlanGroupLink]</a></code>
- <code title="delete /organizations/{orgId}/plangrouplinks/{id}">client.plan_group_links.<a href="./src/m3ter_sdk/resources/plan_group_links.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan_group_link.py">PlanGroupLink</a></code>

# PlanTemplates

Types:

```python
from m3ter_sdk.types import PlanTemplate
```

Methods:

- <code title="post /organizations/{orgId}/plantemplates">client.plan_templates.<a href="./src/m3ter_sdk/resources/plan_templates.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/plan_template_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_template.py">PlanTemplate</a></code>
- <code title="get /organizations/{orgId}/plantemplates/{id}">client.plan_templates.<a href="./src/m3ter_sdk/resources/plan_templates.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan_template.py">PlanTemplate</a></code>
- <code title="put /organizations/{orgId}/plantemplates/{id}">client.plan_templates.<a href="./src/m3ter_sdk/resources/plan_templates.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/plan_template_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_template.py">PlanTemplate</a></code>
- <code title="get /organizations/{orgId}/plantemplates">client.plan_templates.<a href="./src/m3ter_sdk/resources/plan_templates.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/plan_template_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/plan_template.py">SyncCursor[PlanTemplate]</a></code>
- <code title="delete /organizations/{orgId}/plantemplates/{id}">client.plan_templates.<a href="./src/m3ter_sdk/resources/plan_templates.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/plan_template.py">PlanTemplate</a></code>

# Pricings

Types:

```python
from m3ter_sdk.types import Pricing
```

Methods:

- <code title="post /organizations/{orgId}/pricings">client.pricings.<a href="./src/m3ter_sdk/resources/pricings.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/pricing_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/pricing.py">Pricing</a></code>
- <code title="get /organizations/{orgId}/pricings/{id}">client.pricings.<a href="./src/m3ter_sdk/resources/pricings.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/pricing.py">Pricing</a></code>
- <code title="put /organizations/{orgId}/pricings/{id}">client.pricings.<a href="./src/m3ter_sdk/resources/pricings.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/pricing_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/pricing.py">Pricing</a></code>
- <code title="get /organizations/{orgId}/pricings">client.pricings.<a href="./src/m3ter_sdk/resources/pricings.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/pricing_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/pricing.py">SyncCursor[Pricing]</a></code>
- <code title="delete /organizations/{orgId}/pricings/{id}">client.pricings.<a href="./src/m3ter_sdk/resources/pricings.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/pricing.py">Pricing</a></code>

# Products

Types:

```python
from m3ter_sdk.types import Product
```

Methods:

- <code title="post /organizations/{orgId}/products">client.products.<a href="./src/m3ter_sdk/resources/products.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/product_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/product.py">Product</a></code>
- <code title="get /organizations/{orgId}/products/{id}">client.products.<a href="./src/m3ter_sdk/resources/products.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/product.py">Product</a></code>
- <code title="put /organizations/{orgId}/products/{id}">client.products.<a href="./src/m3ter_sdk/resources/products.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/product_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/product.py">Product</a></code>
- <code title="get /organizations/{orgId}/products">client.products.<a href="./src/m3ter_sdk/resources/products.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/product_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/product.py">SyncCursor[Product]</a></code>
- <code title="delete /organizations/{orgId}/products/{id}">client.products.<a href="./src/m3ter_sdk/resources/products.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/product.py">Product</a></code>

# TransactionTypes

Types:

```python
from m3ter_sdk.types import TransactionType
```

Methods:

- <code title="post /organizations/{orgId}/picklists/transactiontypes">client.transaction_types.<a href="./src/m3ter_sdk/resources/transaction_types.py">create</a>(org_id, \*\*<a href="src/m3ter_sdk/types/transaction_type_create_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/transaction_type.py">TransactionType</a></code>
- <code title="get /organizations/{orgId}/picklists/transactiontypes/{id}">client.transaction_types.<a href="./src/m3ter_sdk/resources/transaction_types.py">retrieve</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/transaction_type.py">TransactionType</a></code>
- <code title="put /organizations/{orgId}/picklists/transactiontypes/{id}">client.transaction_types.<a href="./src/m3ter_sdk/resources/transaction_types.py">update</a>(id, \*, org_id, \*\*<a href="src/m3ter_sdk/types/transaction_type_update_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/transaction_type.py">TransactionType</a></code>
- <code title="get /organizations/{orgId}/picklists/transactiontypes">client.transaction_types.<a href="./src/m3ter_sdk/resources/transaction_types.py">list</a>(org_id, \*\*<a href="src/m3ter_sdk/types/transaction_type_list_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/transaction_type.py">SyncCursor[TransactionType]</a></code>
- <code title="delete /organizations/{orgId}/picklists/transactiontypes/{id}">client.transaction_types.<a href="./src/m3ter_sdk/resources/transaction_types.py">delete</a>(id, \*, org_id) -> <a href="./src/m3ter_sdk/types/transaction_type.py">TransactionType</a></code>

# DataExports

Types:

```python
from m3ter_sdk.types import AdhocExport, AdHocOperationalDataRequest, AdHocUsageDataRequest
```

Methods:

- <code title="post /organizations/{orgId}/dataexports/adhoc">client.data_exports.<a href="./src/m3ter_sdk/resources/data_exports.py">create_adhoc</a>(org_id, \*\*<a href="src/m3ter_sdk/types/data_export_create_adhoc_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/adhoc_export.py">AdhocExport</a></code>
