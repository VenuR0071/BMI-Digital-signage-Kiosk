# BMI Digital Signage Kiosk

The BMI Digital Signage Kiosk is an interactive health monitoring system designed to measure users' weight and height, calculate their Body Mass Index (BMI), and provide personalized health tips. It features facial recognition and voice input for user authentication, leveraging OpenCV, DLIB, and Google Speech API. Weight and height data are collected via ESP32 microcontrollers with load cells and ultrasonic sensors, communicated through MQTT to a Raspberry Pi-based backend. The system aims to integrate a VPS-hosted content system for digital signage and store user data in MongoDB (planned but not implemented in current code). This project is ideal for health-focused environments like gyms, clinics, or public kiosks.

## Project Goals

- Authenticate users via facial recognition or voice input, registering new users with photos and IDs.
- Measure weight and height using ESP32-based sensors and calculate BMI.
- Display BMI results with health tips on a user-friendly interface.
- Communicate sensor data securely via MQTT to a Raspberry Pi backend.
- (Planned) Deliver dynamic digital signage content via a VPS-hosted system and store user profiles in MongoDB.

## Tech Stack

### Hardware
- **ESP32 Microcontroller**: Interfaces with load cells for weight and ultrasonic sensors for height, publishing data via MQTT.
- **Raspberry Pi**: Runs the Python backend and MQTT broker, coordinating data processing.
- **Webcam**: Captures images for facial recognition.
- **Microphone**: Captures voice input for authentication.
- **Load Cells & Ultrasonic Sensors**: Measure weight and height (simulated with dummy data in current code).

### Software
- **Python**: Primary language for backend logic, BMI calculation, and sensor communication.
- **OpenCV & DLIB**: Enable facial recognition with the `face_recognition` library.[](https://pypi.org/project/face-recognition/)
- **Google Speech API (`speech_recognition`)**: Processes voice input for user authentication.
- **Paho MQTT**: Facilitates communication between ESP32 sensors and Raspberry Pi backend.[](https://www.hivemq.com/blog/mqtt-raspberrypi-part03-sending-sensor-data-hivemqcloud-pico/)
- **NumPy**: Handles numerical computations for image processing and BMI calculation.
- **Imutils**: Simplifies image processing tasks for facial recognition.
- **MongoDB** (planned): Intended for storing user profiles and BMI data.
- **VPS-Hosted Content System** (planned): For managing digital signage content.

### Frontend
- **Text-Based Interface**: Displays BMI results and health tips via `display.py` (potential for GUI enhancement).

### Backend
- **Python Scripts**: Handle facial recognition (`frontend.py`), BMI calculation (`functions.py`), and MQTT communication (`weightpublish.py`, `weightsubscribe.py`, `heightpublish.py`, `heightsubscribe.py`).

## Prerequisites

- **Hardware**:
  - ESP32 with load cells and ultrasonic sensors (HC-SR04 recommended).
  - Raspberry Pi (e.g., Pi 4) with Raspbian OS.
  - Webcam and microphone connected to the host machine.
- **Software**:
  - Python 3.8+ on the host machine (Windows, as per hardcoded paths).
  - MQTT broker (e.g., Mosquitto) running on Raspberry Pi or external server (IP: `68.178.163.199` used in code).
  - MongoDB (optional, for future implementation).
- **Development Tools**:
  - Git for cloning the repository.
  - pip for installing Python dependencies.
  - IDE (e.g., VSCode) for editing scripts.
- **ESP32 Setup**:
  - MicroPython or Arduino IDE for programming ESP32 to read sensor data and publish to MQTT topics.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/VenuR0071/BMI-Digital-signage-Kiosk.git
   cd "BMI Kiosk"
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

3. **Install Python Dependencies**
   Create a `requirements.txt` with the following content:
   ```text
   paho-mqtt==1.6.1
   opencv-python==4.9.0
   dlib==19.24.2
   face_recognition==1.3.0
   speech_recognition==3.10.0
   numpy==1.24.3
   imutils==0.5.4
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Dataset Directory**
   - Create a directory at `D:\dataset\` for storing user images (or modify paths in `frontend.py` for portability).
   - Organize images in subfolders named with user IDs (e.g., `D:\dataset\1\user1.jpg`).

5. **Set Up MQTT Broker**
   - Install Mosquitto on Raspberry Pi or use the external broker at `68.178.163.199:1883` (ensure accessibility).
   - Configure ESP32 to publish weight to `esp32/weight` and height to `esp32/height` topics.

6. **Program ESP32**
   - Flash MicroPython on ESP32 using Thonny or esptool.py.[](https://www.scribd.com/document/534887016/EXPLORE-ESP32-MICROPYTHON-Python-Coding-Arduino-Coding-Raspberry-Pi-ESP8266-IoT-Projects-Android-Application-Projects)
   - Write scripts to read load cell (weight) and ultrasonic sensor (height) data, publishing JSON payloads (e.g., `{"weight": 84}`) to MQTT topics.
   - Example libraries: `adafruit_hcsr04` for ultrasonic sensors, HX711 library for load cells.

7. **Update File Paths**
   - Modify hardcoded paths in `bmi.py` (e.g., `D:\\MiniProject\\bmi\\`) to match your system.
   - Rename misnamed files: `import paho.mqtt.py` to `weightpublish_test.py` and `jssonsubb.py` to `heightpublish_test.py`.

8. **Provide show_text.py (Missing)**
   Create `show_text.py` with health tip strings, e.g.:
   ```python
   a = "Eat nutrient-rich foods to gain healthy weight."
   b = "Maintain balanced diet and regular exercise."
   c = "Reduce calorie intake and increase physical activity."
   d = "Consult a healthcare provider for weight management."
   ```

## Running the Kiosk

1. **Start the MQTT Broker**
   On Raspberry Pi:
   ```bash
   sudo systemctl start mosquitto
   ```

2. **Run ESP32 Scripts**
   - Deploy weight and height measurement scripts on ESP32, ensuring they publish to `esp32/weight` and `esp32/height`.

3. **Run the BMI Kiosk**
   - Ensure webcam and microphone are connected.
   - Run the main script:
     ```bash
     python bmi.py
     ```
   - The system will:
     - Authenticate users via facial recognition or voice input (`frontend.py`).
     - Trigger weight and height measurements via MQTT (currently dummy data).
     - Calculate BMI and display results with health tips (`display.py`, `functions.py`).

## Usage

1. **User Authentication**
   - Stand in front of the webcam for facial recognition.
   - If recognized, confirm identity by saying "yes" or "no" via microphone.
   - If not recognized or "no," provide your name via voice and capture a new photo for registration.

2. **BMI Measurement**
   - Step on the load cell platform for weight measurement.
   - Stand under the ultrasonic sensor for height measurement.
   - The system retrieves data via MQTT and calculates BMI.

3. **View Results**
   - Results display user name, ID, height, weight, BMI, BMI category, and health tips (e.g., water intake).

## Limitations and Future Improvements

- **Current Limitations**:
  - Uses dummy MQTT data (weight = 84 kg, height trigger = 1); ESP32 sensor integration is incomplete.
  - Hardcoded Windows paths reduce portability.
  - MongoDB and VPS-hosted signage are not implemented.
  - Limited error handling for MQTT disconnections or recognition failures.
  - Missing `show_text.py` requires user implementation.

- **Future Improvements**:
  - Integrate real ESP32 sensor data for weight and height.
  - Implement MongoDB for user data storage.
  - Develop a VPS-hosted content system for digital signage (e.g., Flask-based CMS).
  - Add a GUI (e.g., Tkinter or Streamlit) for enhanced user interaction.
  - Improve portability by using relative paths and environment variables.
  - Enhance error handling and add logging for debugging.

## Troubleshooting

- **Facial Recognition Fails**:
  - Ensure webcam is connected and dataset images are in `D:\dataset\`.
  - Update DLIB and `face_recognition` to latest versions.[](https://pypi.org/project/face-recognition/)
- **MQTT Connection Issues**:
  - Verify broker IP (`68.178.163.199`) is accessible or use a local Mosquitto broker.
  - Check ESP32 is publishing to correct topics.
- **Voice Input Errors**:
  - Test microphone and internet connection for Google Speech API.
- **Path Errors**:
  - Update hardcoded paths in `bmi.py` and `frontend.py` to match your system.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

MIT License. See [LICENSE](LICENSE) for details.

## Contact

For questions or feedback, open an issue on GitHub or contact the repository owner.

## Acknowledgments

- OpenCV and DLIB for facial recognition capabilities.[](https://dlib.net/)
- Paho MQTT for efficient sensor communication.[](https://www.hivemq.com/blog/mqtt-raspberrypi-part03-sending-sensor-data-hivemqcloud-pico/)
- Google Speech API for voice input processing.
