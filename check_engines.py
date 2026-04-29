import vertexai
import google.auth
from vertexai.agent_engines import AgentEngine

try:
    _, project = google.auth.default()
    vertexai.init(project=project, location="us-central1")
    engines = AgentEngine.list()
    for engine in engines:
        print(f"Name: {engine.resource_name}, Display Name: {engine.display_name}")
except Exception as e:
    print(f"Error: {e}")
