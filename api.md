# Authentication

Types:

```python
from m3ter_sdk.types import AuthenticationGetBearerTokenResponse
```

Methods:

- <code title="post /oauth/token">client.authentication.<a href="./src/m3ter_sdk/resources/authentication.py">get_bearer_token</a>(\*\*<a href="src/m3ter_sdk/types/authentication_get_bearer_token_params.py">params</a>) -> <a href="./src/m3ter_sdk/types/authentication_get_bearer_token_response.py">AuthenticationGetBearerTokenResponse</a></code>

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
