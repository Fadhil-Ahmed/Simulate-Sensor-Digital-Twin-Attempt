# 🤖 Robot Control Dashboard with FastAPI, SQLite, and Chart.js

This project is a complete system for controlling and monitoring a robot using a FastAPI backend, SQLite database, a simulated Python client, and a web-based frontend dashboard.

---

## 🚀 Features

- **Start/Stop Robot** from a web dashboard  
- **Set robot speed**  
- **Real-time sensor data visualization**  
- **Sensor data logging with timestamps**  
- **SQLite persistence**  
- **CORS-enabled backend** for cross-origin frontend use  

---

## 🗂️ Project Structure

```
robot-control-dashboard/
├── Sensor.py              # FastAPI backend with database and API
├── simulate_robot.py      # Simulated robot sending sensor data
├── robot_data.db          # SQLite database (auto-created)
├── index.html             # Frontend dashboard (open in browser)
└── README.md              # This file
```

---

## 🛠️ Technologies Used

- **FastAPI** – API backend  
- **SQLite** – lightweight database  
- **Chart.js** – real-time charting library  
- **HTML/CSS/JavaScript** – frontend dashboard  
- **Python requests** – simulate sensor/robot sending data  
- **Uvicorn** – ASGI server for running FastAPI  

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/robot-control-dashboard.git
cd robot-control-dashboard
```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn pydantic requests
```

### 3. Run the Backend

```bash
uvicorn Sensor:app --reload
```

> This will start the backend at: `http://127.0.0.1:8000`

### 4. Run the Robot Simulator (Optional)

```bash
python simulate_robot.py
```

This script simulates a robot sending random sensor values to the backend every 2 seconds *only* when the robot is "started".

### 5. Open the Frontend

Open `index.html` in your browser. You’ll see the Robot Control Dashboard.

---

## 📡 API Endpoints

| Method | Endpoint            | Description                                  |
|--------|---------------------|----------------------------------------------|
| `GET`  | `/status`           | Returns current robot status and speed       |
| `POST` | `/command`          | Sets robot status (`start` or `stop`) and speed |
| `POST` | `/log_sensor_data`  | Logs sensor data with timestamp              |
| `GET`  | `/get_sensor_data`  | Returns the 10 latest sensor values          |

---

## 📊 Dashboard Features

- See **current robot status and speed**
- Control the robot: **Start/Stop**
- Set **custom speed**
- See a **live-updating chart** of recent sensor values

---

## 🔒 Notes

- Sensor values are simulated using `simulate_robot.py`
- SQLite DB (`robot_data.db`) is auto-created if it doesn't exist
- CORS is enabled to allow frontend-backend communication across origins

---

## 🧠 Future Improvements

- Add multi-robot support  
- Use WebSockets for real-time updates  
- Add user authentication  
- Export data to CSV  
- Deploy with Docker or on the cloud  

---

## 👨‍💻 Author

Made with ❤️ by Fadhil Ahmed

Feel free to fork, star ⭐, and contribute!
