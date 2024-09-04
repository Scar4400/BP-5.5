from apscheduler.schedulers.blocking import BlockingScheduler
from data_integration import integrate_data_and_train
import pickle
import logging

# Set up logging
logging.basicConfig(filename="model_updates.log", level=logging.INFO)

def update_model():
    try:
        model = integrate_data_and_train()

        # Save the updated model
        with open("saved_model.pkl", "wb") as f:
            pickle.dump(model, f)

        logging.info("Model updated successfully")
    except Exception as e:
        logging.error(f"Model update failed: {str(e)}")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(update_model, 'interval', hours=24)  # Update every 24 hours
    scheduler.start()
