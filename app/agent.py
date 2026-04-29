# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import google.auth
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.agents.llm_agent import LlmAgent
from .tools import connector_tool

# Initialize project configuration
try:
    _, project_id = google.auth.default()
except Exception:
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

if project_id:
    os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)

os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

# Define the root agent
root_agent = LlmAgent(
    model='gemini-3-flash-preview',
    name='salesforce_connector_agent',
    instruction="""
    Help the user by leveraging your access to Salesforce data via the provided tools.
    Always use the tools to interact with Salesforce. 
    Do not speculate or make up information. If you don't know the answer, state that clearly. 
    Be professional and concise in your responses.
    """,
    tools=[connector_tool],
)

# Initialize the ADK App
app = App(
    root_agent=root_agent,
    name="app",
)
