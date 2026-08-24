def retraining_policy(daily_stats: list, config: dict) -> list:
    retraining_days = []

    remaining_budget = config["budget"]
    last_retrain_day = -config["cooldown"]
    days_since_retrain = 0

    for stats in daily_stats:
        day = stats["day"]

        # Increment before checking conditions
        days_since_retrain += 1

        # Check whether at least one trigger condition holds
        needs_retraining = (
            stats["drift_score"] > config["drift_threshold"]
            or stats["performance"] < config["performance_threshold"]
            or days_since_retrain >= config["max_staleness"]
        )

        # Check cooldown and budget
        cooldown_satisfied = (
            day - last_retrain_day >= config["cooldown"]
        )

        budget_sufficient = (
            remaining_budget >= config["retrain_cost"]
        )

        # Retrain only if all required conditions are satisfied
        if needs_retraining and cooldown_satisfied and budget_sufficient:
            retraining_days.append(day)

            remaining_budget -= config["retrain_cost"]
            last_retrain_day = day
            days_since_retrain = 0

    return retraining_days