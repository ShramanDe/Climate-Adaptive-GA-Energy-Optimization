def objective_function(solution, model, weather_condition):
    """
    Adaptive objective function for climate-based optimization
    """

    heating_load, cooling_load = model.predict(solution)

    if weather_condition == "hot":
        # Prioritize minimizing cooling
        return cooling_load - 0.3 * heating_load

    elif weather_condition == "cold":
        # Prioritize maximizing heating
        return -heating_load + 0.3 * cooling_load

    else:
        # Balanced optimization
        return heating_load + cooling_load
