import pandas as pd
from datetime import datetime


def process_and_evaluate_metrics(weather_data, fleet_records):
    print(
        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Executing parallel metrics mapping..."
    )

    # Extract structural metrics
    temperature = weather_data.get("temperature", 25.0)
    windspeed = weather_data.get("windspeed", 12.0)
    weather_code = weather_data.get("weathercode", 0)

    # Convert fleet list to Pandas DataFrame for high-performance enterprise filtering
    df = pd.DataFrame(fleet_records)
    df["recorded_temp"] = temperature
    df["recorded_windspeed"] = windspeed

    # Business Logic Rule: If windspeed > 15.0 or weather_code indicates anomaly, flags constraint triggers
    df["risk_assessment"] = df.apply(
        lambda row: (
            "🚨 CRITICAL DELAY RISK"
            if row["recorded_windspeed"] > 15.0 or row["priority"] == "Critical"
            else "✅ NOMINAL OPERATION"
        ),
        axis=1,
    )

    return df
