def calculate_risk_of_sequela(age: int, lg: int, ka: int, bleeding: int, charlsone: int, es: float, sequela: bool,
                              dindo: int, access: bool, joint: bool):
    is_bleeding = bleeding >= 1000
    return 0.80806 + 0.04355 * age - 0.07624 * lg + 0.0245 * ka - 1.366 * int(is_bleeding) - 1.4601 * charlsone - 0.30636 * es - 1.37319 * int(
        sequela) - 0.34939 * dindo - 0.94 * int(access) - 1.46815 * int(joint)
