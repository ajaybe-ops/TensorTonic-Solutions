def promote_model(models: list) -> str:
    """Return the name of the model selected for production."""
    #sorting by highest frequency, then lowest latency and timestamp
    best_model = max(
        models,
        key=lambda m: (m["accuracy"],
-m["latency"], m["timestamp"])
    )
    return best_model["name"]