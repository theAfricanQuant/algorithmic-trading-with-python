def calculate_return_series(prices: List[float]) -> List[float]:
    """
    Calculates return series as a parallel list of returns on prices
    """
    return_series = [None]
    return_series.extend(
        (prices[i] / prices[i - 1]) - 1 for i in range(1, len(prices))
    )
    return return_series