import os
from dotenv import load_dotenv
from google.adk.tools.application_integration_tool.application_integration_toolset import ApplicationIntegrationToolset

# Load environment variables from .env if present
load_dotenv()

# Initialize the Salesforce Integration toolset
# Project and location should ideally be set in environment variables
connector_tool = ApplicationIntegrationToolset(
    project=os.environ.get("GOOGLE_CLOUD_PROJECT"), 
    location=os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1"),
    connection="salesforce-conn3", # Update if the connection name changes
    entity_operations={
        "User": ["LIST", "CREATE", "GET", "UPDATE"],
        "Lead": ["LIST", "CREATE", "GET", "UPDATE"],
        "Campaign": ["LIST", "CREATE", "GET", "UPDATE"],
        "Opportunity": ["LIST", "CREATE", "GET", "UPDATE"],
        "Case": ["LIST", "CREATE", "GET", "UPDATE"],
        "Account": ["LIST", "CREATE", "GET", "UPDATE"],
    },
    tool_name_prefix="Salesforce Tool",
    tool_instructions="A tool for interacting with Salesforce. You can fetch user and account data, search and create Opportunities, leads, and view and create campaigns."
)
