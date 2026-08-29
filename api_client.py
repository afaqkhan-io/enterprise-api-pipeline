import requests


class EnterpriseAPIClient:
    def __init__(self):
        # We use public testing APIs that don't require strict authentication keys
        self.weather_url = "https://open-meteo.com"

    def fetch_live_weather(
        self, lat=24.8607, lon=67.0011
    ):  # Default coordinates (e.g., KarachiHub)
        params = {"latitude": lat, "longitude": lon, "current_weather": "true"}
        try:
            response = requests.get(self.weather_url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get("current_weather", {})
            return {"error": f"API responded with status {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}

    def fetch_logistics_routes(self):
        # Simulating live fleet dispatch tracking coordinates and statuses
        return [
            {
                "fleet_id": "FL-001",
                "route": "Zone-A to Hub-1",
                "lat": 24.86,
                "lon": 67.00,
                "priority": "High",
            },
            {
                "fleet_id": "FL-002",
                "route": "Zone-B to Hub-1",
                "lat": 31.52,
                "lon": 74.35,
                "priority": "Standard",
            },
            {
                "fleet_id": "FL-003",
                "route": "Zone-C to Destination",
                "lat": 33.68,
                "lon": 73.04,
                "priority": "Critical",
            },
        ]
