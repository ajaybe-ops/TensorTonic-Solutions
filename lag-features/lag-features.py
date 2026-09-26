def lag_features(series: list, lags: list) -> list:
    max_lag = max(lags)
    result = []

    for i in range(max_lag, len(series)):
        row = []

        for lag in lags:
            row.append(series[i - lag])

        result.append(row)

    return result