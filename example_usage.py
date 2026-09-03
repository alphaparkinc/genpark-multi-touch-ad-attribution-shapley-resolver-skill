from client import MultiTouchAdAttributionShapleyResolverClient

def main():
    client = MultiTouchAdAttributionShapleyResolverClient()
    res = client.resolve_shapley_attribution('ord_01', ['Search', 'Social'], 100.00)
    print('Multi-Touch Shapley Attribution: ' + res['attribution_model_id'])
    print('Model: ' + res['attribution_model'])
    print('Top Contribution: ' + res['touchpoint_contributions'][0]['channel'] + ' ($' + str(res['touchpoint_contributions'][0]['attributed_revenue_usd']) + ')')
    print('Attribution Graph URL: ' + res['attribution_graph_url'])

if __name__ == '__main__':
    main()
