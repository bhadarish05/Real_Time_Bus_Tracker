# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import os

app = Flask(__name__)

# Allow Vite dev server origin
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}})

# Mongo connection
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
client = MongoClient(MONGODB_URI)
db = client.get_database(os.getenv("MONGODB_DB", "bus_tracker"))

def to_safe_doc(doc):
    if not doc:
        return doc
    doc = dict(doc)
    if "_id" in doc and isinstance(doc["_id"], ObjectId):
        doc["_id"] = str(doc["_id"])
    return doc

@app.route("/")
def index():
    return "Bus Tracker API is running!"

@app.route("/test_db")
def test_db():
    try:
        collections = db.list_collection_names()
        return jsonify({"status": "success", "collections": collections}), 200
    except Exception as e:
        return jsonify({"status": "failed", "error": str(e)}), 500

@app.route("/api/buses", methods=["GET"])
def get_buses():
    try:
        buses = [to_safe_doc(b) for b in db.buses.find({})]
        return jsonify({"status": "success", "buses": buses}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/buses/<bus_id>/location", methods=["POST"])
def update_bus_location(bus_id):
    try:
        location_data = request.get_json(force=True) or {}
        db.buses.update_one(
            {"bus_id": bus_id},
            {"$set": {"location": location_data, "last_updated": datetime.utcnow()}},
            upsert=True
        )
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/routes", methods=["GET"])
def get_routes():
    try:
        routes = [to_safe_doc(r) for r in db.routes.find({})]
        return jsonify({"status": "success", "routes": routes}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    # For local dev
    app.run(debug=True, port=5000)
