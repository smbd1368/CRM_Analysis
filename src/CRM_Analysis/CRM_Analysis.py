import numpy as np
from typing import Dict, List
from collections import Counter
from datetime import datetime, timedelta
from sklearn.cluster import KMeans

class CRMAnalytics:
    def __init__(self, customer_data: np.ndarray):
        self.data = customer_data
        self.customer_ids = self.data[:, 0]
        self.purchase_amounts = self.data[:, 1].astype(float)
        self.purchase_dates = self.data[:, 2].astype('datetime64')
        self.acquisition_costs = self.data[:, 3].astype(float)
        self.product_categories = self.data[:, 4]
        self.interaction_channels = self.data[:, 5]

    def calculate_customer_lifetime_value(self, time_period: int = 365) -> Dict[int, float]:
        current_date = np.max(self.purchase_dates)
        mask = (current_date - self.purchase_dates).astype(int) <= time_period
        clv = {}
        for customer_id in np.unique(self.customer_ids):
            customer_mask = (self.customer_ids == customer_id) & mask
            total_revenue = np.sum(self.purchase_amounts[customer_mask])
            acquisition_cost = self.acquisition_costs[self.customer_ids == customer_id][0]
            clv[customer_id] = total_revenue - acquisition_cost
        return clv

    def segment_customers(self, num_segments: int = 3) -> Dict[int, int]:
        total_purchases = {}
        for customer_id in np.unique(self.customer_ids):
            total_purchases[customer_id] = np.sum(self.purchase_amounts[self.customer_ids == customer_id])
        
        sorted_customers = sorted(total_purchases.items(), key=lambda x: x[1], reverse=True)
        segment_size = len(sorted_customers) // num_segments
        
        segmentation = {}
        for i, (customer_id, _) in enumerate(sorted_customers):
            segmentation[customer_id] = i // segment_size + 1
        return segmentation
    
    def calculate_retention_rate(self, start_date: np.datetime64, end_date: np.datetime64) -> float:
        customers_start = set(self.customer_ids[(self.purchase_dates <= start_date)])
        customers_end = set(self.customer_ids[(self.purchase_dates > start_date) & (self.purchase_dates <= end_date)])
        retained_customers = len(customers_start.intersection(customers_end))
        return float((retained_customers / len(customers_start)) * 100 if customers_start else 0)

    def identify_top_customers(self, top_n: int = 10) -> List[int]:
        total_purchases = {}
        for customer_id in np.unique(self.customer_ids):
            total_purchases[customer_id] = np.sum(self.purchase_amounts[self.customer_ids == customer_id])
        
        sorted_customers = sorted(total_purchases.items(), key=lambda x: x[1], reverse=True)
        return [customer_id for customer_id, _ in sorted_customers[:top_n]]

    def personalize_recommendations(self, customer_id: int, top_n: int = 3) -> List[str]:
        customer_purchases = self.product_categories[self.customer_ids == customer_id]
        if len(customer_purchases) == 0:
            return []
        
        category_counts = Counter(customer_purchases)
        return [category for category, _ in category_counts.most_common(top_n)]

    def analyze_customer_behavior(self, customer_id: int) -> Dict[str, any]:
        customer_mask = self.customer_ids == customer_id
        customer_purchases = self.purchase_amounts[customer_mask]
        customer_dates = self.purchase_dates[customer_mask]
        customer_channels = self.interaction_channels[customer_mask]

        if len(customer_purchases) == 0:
            return {"error": "No data available for this customer"}

        return {
            "total_purchases": len(customer_purchases),
            "total_spend": np.sum(customer_purchases),
            "average_purchase_value": np.mean(customer_purchases),
            "first_purchase_date": np.min(customer_dates),
            "last_purchase_date": np.max(customer_dates),
            "preferred_channel": Counter(customer_channels).most_common(1)[0][0],
            "purchase_frequency": self.calculate_purchase_frequency(customer_dates)
        }

    def calculate_purchase_frequency(self, purchase_dates: np.ndarray) -> float:
        if len(purchase_dates) < 2:
            return 0
        sorted_dates = np.sort(purchase_dates)
        days_between_purchases = np.diff(sorted_dates).astype(int)
        return np.mean(days_between_purchases)

    def identify_cross_selling_opportunities(self, customer_id: int) -> List[str]:
        customer_categories = set(self.product_categories[self.customer_ids == customer_id])
        all_categories = set(self.product_categories)
        return list(all_categories - customer_categories)

    def segment_by_behavior(self, num_segments: int = 3) -> Dict[int, int]:
        customer_metrics = {}
        for customer_id in np.unique(self.customer_ids):
            behavior = self.analyze_customer_behavior(customer_id)
            customer_metrics[customer_id] = (behavior['total_spend'], behavior['purchase_frequency'])
        
        kmeans = KMeans(n_clusters=num_segments, n_init=10, random_state=42)
        segments = kmeans.fit_predict(list(customer_metrics.values()))
        
        return {customer_id: segment for customer_id, segment in zip(customer_metrics.keys(), segments)}

