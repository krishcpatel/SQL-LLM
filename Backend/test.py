import os


gmni_api_key = 'AIzaSyD6sktIyUrVgeVUXoMjLve5wJqZ0T8Nga0'
lngchn_api_key = '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'
username = 'sa'
password = 'KP493159#c'
host = 'localhost'
port = '1433'
database = 'StackOverflowMini'

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