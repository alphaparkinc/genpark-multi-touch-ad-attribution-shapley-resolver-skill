class MultiTouchAdAttributionShapleyResolverClient:
    def resolve_shapley_attribution(self, conversion_order_id='ord_8812', touchpoint_journey=['Google_Search_Ad', 'Meta_Instagram_Reels', 'Klaviyo_Abandoned_Cart_Email'], order_revenue_usd=240.00):
        return {
            'attribution_model_id': 'shp_att_8812',
            'conversion_order_id': conversion_order_id,
            'attribution_model': 'DATA_DRIVEN_SHAPLEY_GAME_THEORY',
            'touchpoint_contributions': [
                {'channel': 'Google_Search_Ad', 'shapley_weight': 0.42, 'attributed_revenue_usd': 100.80},
                {'channel': 'Meta_Instagram_Reels', 'shapley_weight': 0.35, 'attributed_revenue_usd': 84.00},
                {'channel': 'Klaviyo_Abandoned_Cart_Email', 'shapley_weight': 0.23, 'attributed_revenue_usd': 55.20}
            ],
            'roas_optimized_budget_shift': 'Increase Meta Reels spend by +18%',
            'attribution_graph_url': 'https://triplewhale.attribution.genpark.ai/reports/8812.json'
        }
