import time
from api_client import EnterpriseAPIClient
from analytics_processor import process_and_evaluate_metrics
from apscheduler.schedulers.background import BackgroundScheduler


def run_master_pipeline():
    client = EnterpriseAPIClient()

    # Ingest from endpoints
    weather = client.fetch_live_weather()
    fleet = client.fetch_logistics_routes()

    # Transform via dataframe engine
    final_registry_df = process_and_evaluate_metrics(weather, fleet)

    # Display inside operational terminal console
    print("\n--- ENTERPRISE PIPELINE RUN LOG ---")
    print(final_registry_df[["fleet_id", "route", "priority", "risk_assessment"]])
    print("------------------------------------\n")

    # Save localized checkpoint state
    final_registry_df.to_csv("active_pipeline_snapshot.csv", index=False)


if __name__ == "__main__":
    print("🤖 Initializing Multi-Source Enterprise API Pipeline Scheduler...")

    scheduler = BackgroundScheduler()
    # Runs the pipeline every 10 seconds for real-time validation testing
    scheduler.add_job(run_master_pipeline, "interval", seconds=10)
    scheduler.start()

    print("⚡ Pipeline is actively listening. Press Ctrl+C to terminate.")

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("\n❌ Scheduler terminated safely.")
