def feature_store_lookup(feature_store: dict, requests: list, defaults: dict) -> list:
    result = []

    for request in requests:
        user_id = request["user_id"]

        # Get stored offline features, or defaults if user is unknown
        offline_features = feature_store.get(user_id, defaults)

        # Get the online features inside the request
        online_features = request["online_features"]

        # Merge offline + online features
        combined = {**offline_features, **online_features}

        result.append(combined)

    return result