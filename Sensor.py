from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import datetime

app = FastAPI()

# CORS (if running frontend separately)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLite setup
conn = sqlite3.connect("robot_data.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
                    id INTEGER PRIMARY KEY,
                    value REAL,
                    timestamp TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS robot_status (
                    id INTEGER PRIMARY KEY,
                    status TEXT,
                    speed INTEGER)''')
# Ensure a default status row exists
cursor.execute("INSERT OR IGNORE INTO robot_status (id, status, speed) VALUES (1, 'stopped', 0)")
conn.commit()

# Models
class SensorData(BaseModel):
    value: float

class Command(BaseModel):
    action: str  # start or stop
    speed: int

@app.post("/log_sensor_data")
async def log_sensor_data(data: SensorData):
    timestamp = datetime.datetime.now().isoformat()
    cursor.execute("INSERT INTO sensor_data (value, timestamp) VALUES (?, ?)", (data.value, timestamp))
    conn.commit()
    return {"message": "Sensor data logged"}

@app.get("/get_sensor_data")
async def get_sensor_data():
    cursor.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    return [{"value": r[1], "timestamp": r[2]} for r in rows[::-1]]  # Return in ascending time order

@app.post("/command")
async def command_robot(cmd: Command):
    cursor.execute("UPDATE robot_status SET status = ?, speed = ? WHERE id = 1", (cmd.action, cmd.speed))
    conn.commit()
    return {"message": f"Robot set to {cmd.action} with speed {cmd.speed}"}

@app.get("/status")
async def get_status():
    cursor.execute("SELECT status, speed FROM robot_status WHERE id = 1")
    status, speed = cursor.fetchone()
    return {"status": status, "speed": speed}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Sensor:app", host="127.0.0.1", port=8000, reload=True)
