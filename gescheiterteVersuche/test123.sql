INSERT INTO bsdbneu (
    date,
    station,
    count,
    wind_speed,
    precipitation,
    snowfall,
    snow_depth,
    mean_temperature,
    max_temperature,
    min_temperature)
VALUES (
    :date,
    :station,
    :count,
    :wind_speed,
    :precipitation,
    :snowfall,
    :snow_depth,
    :mean_temperature,
    :max_temperature,
    :min_temperature)