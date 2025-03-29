
from flask import Blueprint, request, jsonify
from app.db import get_db_connection
from app.query_processor import convert_to_sql

routes = Blueprint("routes", __name__)

@routes.route("/query", methods=["POST"])
def query():
    
    data = request.get_json()
    user_query = data.get("query", "").lower()
    sql_query = convert_to_sql(user_query)
    
    if not sql_query:
        return jsonify({"error": "Query not understood"}), 400
    
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql_query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify({"query": user_query, "result": result})

@routes.route("/explain", methods=["POST"])
def explain():
    
    data = request.get_json()
    user_query = data.get("query", "").lower()
    sql_query = convert_to_sql(user_query)
    
    if not sql_query:
        return jsonify({"error": "Could not generate SQL translation"}), 400
    
    return jsonify({"query": user_query, "sql_translation": sql_query})

@routes.route("/validate", methods=["POST"])
def validate():
    
    data = request.get_json()
    user_query = data.get("query", "").lower()
    sql_query = convert_to_sql(user_query)
    
    return jsonify({"valid": bool(sql_query), "message": "Query is valid." if sql_query else "Query could not be processed."})
