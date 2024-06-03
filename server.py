
from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

app = Flask(__name__)

def generate_daily_report():
    # Placeholder for the logic to generate daily report
    print("Generating daily report...")

def create_dataset():
    # Placeholder for the logic to create dataset
    print("Creating dataset...")

@app.route('/generate_report', methods=['POST'])
def handle_generate_report():
    generate_daily_report()
    return jsonify({"message": "Report generation started"}), 202

@app.route('/create_dataset', methods=['POST'])
def handle_create_dataset():
    create_dataset()
    return jsonify({"message": "Dataset creation started"}), 202

scheduler = BackgroundScheduler()
scheduler.add_job(func=generate_daily_report, trigger="cron", hour=0)  # Schedules at midnight every day
scheduler.add_job(func=create_dataset, trigger="cron", hour=0)         # Schedules at midnight every day
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
