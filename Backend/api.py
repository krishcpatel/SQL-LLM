from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import os
import pyodbc
from langchain_community.utilities import SQLDatabase
from sqlalchemy.engine import URL
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain import hub
from langgraph.prebuilt import create_react_agent

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:8080"])

@app.route('/date', methods=['GET'])
def get_date():
    result = subprocess.check_output(['date']).decode('utf-8')
    return jsonify({'date': result.strip()})

@app.route('/llmresp', methods=['POST'])
def get_llmresp():
    gmni_api_key = request.json['gmni_api_key']
    lngchn_api_key = request.json['lngchn_api_key']
    username = request.json['username']
    password = request.json['password']
    host = request.json['host']
    port = request.json['port']
    database = request.json['database']
    llmprompt = request.json['prompt']

    os.environ["GOOGLE_API_KEY"] = gmni_api_key
    os.environ["LANGCHAIN_API_KEY"] = lngchn_api_key

    connection_url = URL.create(
        "mssql+pyodbc",
        username=username,
        password=password,
        host=host,
        port=port,
        database=database,
        query={
            "driver": "ODBC Driver 18 for SQL Server",
            "TrustServerCertificate": "yes",
        },
    )

    db = SQLDatabase.from_uri(connection_url)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    prompt_template = hub.pull("langchain-ai/sql-agent-system-prompt")
    assert len(prompt_template.messages) == 1

    system_message = prompt_template.format(dialect="SQL", top_k=5)

    agent_executor = create_react_agent(
        llm, toolkit.get_tools(), state_modifier=system_message
    )

    query = llmprompt

    events = agent_executor.stream(
        {"messages": [("user", query)]},
        stream_mode="values",
    )

    final_response = None  # Initialize a variable to store the final response

    for event in events:
        final_response = event["messages"][-1]  # Update with the latest event's message

    # Return the final response
    return jsonify({'response': final_response.pretty_repr()})

if __name__ == '__main__':
    app.run(port=3030)