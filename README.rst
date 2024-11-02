============
CRM_Analysis
============

CRM_Analysis is a Python package for Customer Relationship Management (CRM) analytics. It provides tools for analyzing customer data, segmenting customers, calculating customer lifetime value, and more.

Features
--------

* Calculate Customer Lifetime Value
* Segment customers based on purchase behavior
* Calculate retention rates
* Identify top customers
* Generate personalized product recommendations
* Analyze customer behavior
* Identify cross-selling opportunities
* Perform behavioral segmentation

Installation
------------

You can install CRM_Analysis using pip:

.. code-block:: console

    $ pip install CRM_Analysis

Usage
-----

Here's a quick example of how to use the CRMAnalytics class:

.. code-block:: python

    import numpy as np
    from datetime import datetime, timedelta
    from CRM_Analysis import CRMAnalytics

    # Generate sample data (in a real scenario, you'd load this from your database)
    np.random.seed(42)
    num_customers = 1000
    num_transactions = 5000

    customer_ids = np.random.randint(1, num_customers + 1, num_transactions)
    purchase_amounts = np.random.uniform(10, 1000, num_transactions)
    start_date = datetime(2020, 1, 1)
    purchase_dates = [start_date + timedelta(days=int(x)) for x in np.random.uniform(0, 365*2, num_transactions)]
    acquisition_costs = np.random.uniform(50, 200, num_transactions)
    product_categories = np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'], num_transactions)
    interaction_channels = np.random.choice(['Web', 'Mobile', 'Store', 'Phone'], num_transactions)

    customer_data = np.column_stack((customer_ids, purchase_amounts, purchase_dates, 
                                     acquisition_costs, product_categories, interaction_channels))

    # Create CRMAnalytics instance
    crm = CRMAnalytics(customer_data)

    # Calculate Customer Lifetime Value
    clv = crm.calculate_customer_lifetime_value()
    print("Customer Lifetime Value for first 5 customers:")
    for customer_id in sorted(list(clv.keys()))[:5]:
        print(f"Customer {customer_id}: ${clv[customer_id]:.2f}")

    # Segment customers
    segmentation = crm.segment_customers()
    print("\nCustomer Segmentation:")
    for segment, count in Counter(segmentation.values()).items():
        print(f"Segment {segment}: {count} customers")

    # Identify top customers
    top_customers = crm.identify_top_customers(5)
    print(f"\nTop 5 customer IDs: {top_customers}")

    # Get personalized recommendations
    recommendations = crm.personalize_recommendations(1)
    print(f"\nRecommended categories for Customer 1: {recommendations}")

Documentation
-------------

For detailed documentation on each method and its parameters, please refer to the docstrings in the source code.

Contributing
------------

Contributions are welcome! Please feel free to submit a Pull Request.

