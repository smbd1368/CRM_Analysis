#!/usr/bin/env python

"""Tests for `CRMAnalytics` class."""
import pytest
import numpy as np
from datetime import datetime, timedelta
from CRM_Analysis import CRMAnalytics

@pytest.fixture
def sample_data():
    np.random.seed(42)
    num_customers = 100
    num_transactions = 500

    customer_ids = np.random.randint(1, num_customers + 1, num_transactions)
    purchase_amounts = np.random.uniform(10, 1000, num_transactions)
    start_date = datetime(2020, 1, 1)
    purchase_dates = [start_date + timedelta(days=int(x)) for x in np.random.uniform(0, 365*2, num_transactions)]
    acquisition_costs = np.random.uniform(50, 200, num_transactions)
    product_categories = np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'], num_transactions)
    interaction_channels = np.random.choice(['Web', 'Mobile', 'Store', 'Phone'], num_transactions)

    return np.column_stack((customer_ids, purchase_amounts, purchase_dates, 
                            acquisition_costs, product_categories, interaction_channels))

@pytest.fixture
def crm_analytics(sample_data):
    return CRMAnalytics(sample_data)

def test_calculate_customer_lifetime_value(crm_analytics):
    clv = crm_analytics.calculate_customer_lifetime_value()
    assert isinstance(clv, dict)
    assert all(isinstance(value, float) for value in clv.values())

def test_segment_customers(crm_analytics):
    segmentation = crm_analytics.segment_customers()
    assert isinstance(segmentation, dict)
    assert all(1 <= segment <= 3 for segment in segmentation.values())

def test_calculate_retention_rate(crm_analytics):
    retention_rate = crm_analytics.calculate_retention_rate(np.datetime64('2020-01-01'), np.datetime64('2021-01-01'))
    assert isinstance(retention_rate, float)
    assert 0 <= retention_rate <= 100

def test_identify_top_customers(crm_analytics):
    top_customers = crm_analytics.identify_top_customers(5)
    assert isinstance(top_customers, list)
    assert len(top_customers) == 5

def test_personalize_recommendations(crm_analytics):
    recommendations = crm_analytics.personalize_recommendations(1)
    assert isinstance(recommendations, list)
    assert all(isinstance(category, str) for category in recommendations)

def test_analyze_customer_behavior(crm_analytics):
    behavior = crm_analytics.analyze_customer_behavior(1)
    assert isinstance(behavior, dict)
    assert 'total_purchases' in behavior
    assert 'total_spend' in behavior

def test_identify_cross_selling_opportunities(crm_analytics):
    cross_sell = crm_analytics.identify_cross_selling_opportunities(1)
    assert isinstance(cross_sell, list)
    assert all(isinstance(category, str) for category in cross_sell)

def test_segment_by_behavior(crm_analytics):
    behavioral_segments = crm_analytics.segment_by_behavior()
    assert isinstance(behavioral_segments, dict)
    assert all(0 <= segment <= 2 for segment in behavioral_segments.values())
