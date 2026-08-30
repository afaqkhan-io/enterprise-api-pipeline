# 🌐 API Data Pipeline & Scheduler

A Python automation project that fetches data from an external REST API, transforms the response with Pandas, writes a CSV snapshot, and repeats the workflow on a configurable schedule.

`Python 3.x` · `Requests` · `Pandas` · `APScheduler` · `MIT License`

## 🚀 Features

- **REST API ingestion:** Retrieves structured JSON data from an external API.
- **Data transformation:** Converts API responses into Pandas DataFrames for filtering and analysis.
- **CSV snapshots:** Saves processed results for later inspection.
- **Scheduled execution:** Uses APScheduler to run the workflow repeatedly in the background.
- **Modular design:** Keeps API communication, data processing, and orchestration in separate modules.

## 🧩 Project Structure

- `api_client.py` — API request and response handling.
- `analytics_processor.py` — Pandas transformation and filtering.
- `main.py` — scheduler and workflow orchestration.
- `requirements.txt` — dependencies.

## 📋 Setup

```bash
git clone https://github.com/afaqkhan-io/enterprise-api-pipeline.git
cd enterprise-api-pipeline
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run

```bash
python main.py
```

The workflow will run on its configured interval and write its processed snapshot to the project output file.

> **Note:** API availability and response formats can change. Review the configured endpoint and scheduling interval before using the project in a long-running environment.

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.
