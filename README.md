# truiz-salesforce-agent

Simple ReAct agent
Agent generated with [`googleCloudPlatform/agent-starter-pack`](https://github.com/GoogleCloudPlatform/agent-starter-pack) version `0.37.0`

## Project Structure

```
truiz-salesforce-agent/

├── app/         # Core agent code
│   ├── agent.py               # Main agent logic
│   ├── agent_engine_app.py    # Agent Engine application logic
│   └── app_utils/             # App utilities and helpers
├── tests/                     # Unit, integration, and load tests
├── GEMINI.md                  # AI-assisted development guide
├── Makefile                   # Development commands
└── pyproject.toml             # Project dependencies
```

> 💡 **Tip:** Use [Gemini CLI](https://github.com/google-gemini/gemini-cli) for AI-assisted development - project context is pre-configured in `GEMINI.md`.

## Setup Instructions

Follow these steps to set up the project locally:

### 1. Prerequisites

Before you begin, ensure you have:
- **uv**: Python package manager (used for all dependency management in this project) - [Install](https://docs.astral.sh/uv/getting-started/installation/)
- **Google Cloud SDK**: For GCP services - [Install](https://cloud.google.com/sdk/docs/install)
- **make**: Build automation tool - [Install](https://www.gnu.org/software/make/) (pre-installed on most Unix-based systems)

### 2. Google Cloud Platform (GCP) Project Setup

1. Create a new GCP project or select an existing one in the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the required APIs for this project, such as Vertex AI API.
3. Authenticate with Google Cloud using the SDK:
   ```bash
   gcloud auth login
   gcloud auth application-default login
   gcloud config set project <your-project-id>
   ```

### 3. Environment Configuration

Create a `.env` file in the `app/` directory:

```bash
touch app/.env
```

Populate the `.env` file with your specific configurations. For example:
```env
PROJECT_ID="your-gcp-project-id"
LOCATION="us-central1"
# Add other necessary variables (like Salesforce credentials, API keys, etc.)
```

### 4. Install Dependencies & Launch

Install required packages and launch the local development environment:

```bash
make install && make playground
```

## Architecture Decisions

When developing and deploying this agent, consider the following architectural opinions and best practices:

*   **ADK Starter Pack:** This project utilizes the ADK Starter Pack, which provides essential scaffolding and enforces best practices for Agent Developer Kit (ADK) development. It is recommended to adhere to its structure to ensure maintainability and compatibility with GCP tooling.
*   **Integration Strategy:** For robust, fully-managed integrations, **Application Integration** is the recommended service. However, for simpler or custom tool execution directly within the agent's context, you have the flexibility to utilize the `MCP Toolset` class provided by the ADK framework.
*   **Deployment Target:** Deploying to **Agent Engine** provides a fully managed runtime optimized for AI agents out-of-the-box. As an alternative, you can also deploy the agent to **Cloud Run** if you require more granular control over the container environment or need to fit into existing Cloud Run architectures.

## Commands

| Command              | Description                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------- |
| `make install`       | Install dependencies using uv                                                               |
| `make playground`    | Launch local development environment                                                        |
| `make lint`          | Run code quality checks                                                                     |
| `make test`          | Run unit and integration tests                                                              |
| `make deploy`        | Deploy agent to Agent Engine                                                                |
| `make register-gemini-enterprise` | Register deployed agent to Gemini Enterprise                                  |

For full command options and usage, refer to the [Makefile](Makefile).

## 🛠️ Project Management

| Command | What It Does |
|---------|--------------|
| `uvx agent-starter-pack enhance` | Add CI/CD pipelines and Terraform infrastructure |
| `uvx agent-starter-pack setup-cicd` | One-command setup of entire CI/CD pipeline + infrastructure |
| `uvx agent-starter-pack upgrade` | Auto-upgrade to latest version while preserving customizations |
| `uvx agent-starter-pack extract` | Extract minimal, shareable version of your agent |

---

## Development

Edit your agent logic in `app/agent.py` and test with `make playground` - it auto-reloads on save.
See the [development guide](https://googlecloudplatform.github.io/agent-starter-pack/guide/development-guide) for the full workflow.

## Deployment

```bash
gcloud config set project <your-project-id>
make deploy
```

To add CI/CD and Terraform, run `uvx agent-starter-pack enhance`.
To set up your production infrastructure, run `uvx agent-starter-pack setup-cicd`.
See the [deployment guide](https://googlecloudplatform.github.io/agent-starter-pack/guide/deployment) for details.

## Observability

Built-in telemetry exports to Cloud Trace, BigQuery, and Cloud Logging.
See the [observability guide](https://googlecloudplatform.github.io/agent-starter-pack/guide/observability) for queries and dashboards.
