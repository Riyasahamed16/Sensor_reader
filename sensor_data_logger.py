import csv
import time
from datetime import datetime

# Simulated sensor class (replace with your actual sensor library)
class Sensor:
    def read_acceleration(self):
        return {"x": 0.01, "y": 0.02, "z": 9.81}  # Simulated accel data

    def read_gyroscope(self):
        return {"x": 0.1, "y": 0.2, "z": 0.3}  # Simulated gyro data

# Initialize the sensor
sensor = Sensor()

# CSV file path
csv_file = "sensor_data.csv"

# Function to append data to CSV file
def log_sensor_data():
    file_exists = False

    try:
        # Open file in append mode, creating it if it doesn't exist
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            
            # Add the header if the file is newly created
            if not file_exists:
                writer.writerow(["Timestamp", "Accel_X", "Accel_Y", "Accel_Z", "Gyro_X", "Gyro_Y", "Gyro_Z"])
                file_exists = True
            
            print("Logging sensor data... Press Ctrl+C to stop.")
            while True:
                # Read sensor data
                accel = sensor.read_acceleration()
                gyro = sensor.read_gyroscope()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Append data to the CSV file
                writer.writerow([timestamp, accel["x"], accel["y"], accel["z"], gyro["x"], gyro["y"], gyro["z"]])
                
                # Display logged data in the console
                print(f"{timestamp} - Accel: {accel}, Gyro: {gyro}")
                time.sleep(1)  # Delay for 1 second
    except KeyboardInterrupt:
        print("\nData logging stopped.")
    except Exception as e:
        print(f"Error: {e}")

# Run the data logger
if __name__ == "__main__":
    log_sensor_data()
