# Twitter Data Pipeline Using Apache Airflow

## Overview
This project builds an end-to-end Twitter data pipeline using **Apache Airflow**. The pipeline extracts data from Twitter, processes it, and stores it in a database for further analysis. It demonstrates the use of **ETL (Extract, Transform, Load)** principles and workflow orchestration with **Airflow**.

## Features
- **Data Extraction**: Fetches tweets from the Twitter API.
- **Data Processing**: Cleans and transforms raw tweet data.
- **Storage**: Loads processed data into a PostgreSQL database.
- **Automation**: Uses Apache Airflow to schedule and monitor pipeline tasks.
- **Logging & Monitoring**: Tracks pipeline execution and logs errors for debugging.

## Technologies Used
- **Apache Airflow**: Workflow orchestration and task scheduling.
- **Python**: Scripting for data extraction, transformation, and loading.
- **Twitter API**: Fetching real-time tweet data.
- **PostgreSQL**: Storing processed tweet data.
- **Docker**: Containerized execution of Airflow.

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Docker & Docker Compose
- Python 3.11
- PostgreSQL

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/PrajwalaMugajjiShambulingappa/TwitterDataPipelineUsingAirflow.git
   cd TwitterDataPipelineUsingAirflow
   ```
2. Set up the virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your Twitter API credentials in a `.env` file:
   ```
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET=your_api_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_SECRET=your_access_secret
   ```
5. Start the Airflow services using Docker:
   ```bash
   docker-compose up -d
   ```
6. Access the Airflow UI at: `http://localhost:8080`

## Usage
- Modify `dags/twitter_etl.py` to adjust API parameters or processing logic.
- Run the Airflow scheduler and trigger the DAG manually in the UI.
- Query the PostgreSQL database to analyze stored tweets.

## License
This project is licensed under the MIT License.
