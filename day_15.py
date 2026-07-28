
import itertools

import numpy as np
import pandas as pd
from scipy.optimize import minimize


def data_prep(data):
    data = pd.DataFrame(data)

    # data prep
    data = data[0].str.split(expand=True)
    data[0] = data[0].str.replace(":", "")
    data = data.drop([1, 3, 5, 7, 9], axis=1)
    data[2] = data[2].str.replace(",", "")
    data[4] = data[4].str.replace(",", "")
    data[6] = data[6].str.replace(",", "")
    data[8] = data[8].str.replace(",", "")
    data.columns = ["Ingredient", "Capacity", "Durability", 
                    "Flavor", "Texture", "Calories"]

    data[data.columns[1:]] = data[data.columns[1:]].astype(int)

    # 1. Define ingredients properties
    df_partial = data[data.columns[1:]]
    matrix = df_partial.to_numpy()

    return matrix


def optimize_recipe(matrix, total_spoons=100, calories=None):
    """Optimizes ingredient ratios to maximize 
        (Capacity * Durability * Flavor * Texture).

    Parameters:
      matrix : np.ndarray
          Input array where rows are ingredients and columns are
          [Capacity, Durability, Flavor, Texture, Calories].
      total_spoons : int
          Target sum of ingredients (default 100).
      calories : int or float, optional
          Target of total calories. Defaults to None (no limit).

    Returns:
      best_score : int
          Maximized product score.
      actual_calories : int
          Total calories for the chosen combination.
    """
    props = matrix[:, :4]
    calories_per_unit = matrix[:, 4]
    num_ingredients = len(matrix)

    # 1. Define objective function
    def get_score(x):
        totals = np.dot(x, props)
        totals = np.maximum(0, totals)
        return np.prod(totals)

    def loss(x):
        return -get_score(x)

    # 2. Base constraint: sum(x) == total_spoons
    constraints = [{"type": "eq", "fun": lambda x: np.sum(x) - total_spoons}]

    bounds = [(0, total_spoons) for _ in range(num_ingredients)]
    x0 = [total_spoons / num_ingredients] * num_ingredients

    # 3. Optional calorie target
    if calories is not None:
        constraints.append(
            {
                "type": "eq",
                "fun": lambda x, target=calories: np.dot(x, calories_per_unit)
                - target,
            }
        )

    # 4. Continuous optimization
    res = minimize(
        loss, x0, method="SLSQP", bounds=bounds, constraints=constraints
    )

    # 5. Integer neighborhood refinement around the continuous optimum
    center = np.round(res.x).astype(int)

    best_score = -1
    best_quantities = None

    delta_range = range(-3, 4)
    for deltas in itertools.product(delta_range, repeat=num_ingredients):
        candidate = center + np.array(deltas)

        # Basic constraints check
        if np.sum(candidate) != total_spoons or np.any(candidate < 0):
            continue

        # Calorie check (if active)
        tot_calories = np.dot(candidate, calories_per_unit)
        if calories is not None and tot_calories != calories:
            continue

        score = get_score(candidate)
        if score > best_score:
            best_score = score
            best_quantities = candidate

    actual_calories = int(np.dot(best_quantities, calories_per_unit))
    return int(best_score), actual_calories


if __name__ == "__main__":

    # DATA
    with open("./data/data_15.txt") as file:
        data = file.read().splitlines()

    matrix = data_prep(data)
    score_unlimited, cal_unlimited = optimize_recipe(matrix, 100)
    print(f"Part 1: {score_unlimited}")
    score_limited, cal_limited = optimize_recipe(matrix, 100, 500)
    print(f"Part 2: {score_limited}")


