# Architecture Overview

HiveMind OS is structured as a set of microservices communicating via REST APIs.
Each service (Architect, CodeGen, Review, Debugger, Tests) is built with FastAPI.
The services are containerized with Docker and can be orchestrated using Docker Compose or Kubernetes.

## Components

- **Architect:** Generates project blueprints.
- **CodeGen:** Generates code stubs based on blueprints.
- **Review:** Analyzes code for best practice-projects-projectss.
- **Debugger:** Applies debugging fixes to code.
- **Tests:** Generates basic test cases for the codebase.
- **Dashboard:** Frontend to visualize and control the system.

## Next Steps

- Integrate asynchronous processing (Celery/Redis).
- Extend UI components.
- Enhance error handling and logging.

