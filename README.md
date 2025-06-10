# HiveMind OS

## Overview
HiveMind OS is an AI-driven system for generating, reviewing, debugging, and testing code at scale. The platform consists of multiple microservices built with FastAPI, a React-based dashboard, and infrastructure templates for deployment.

## Architecture

The system is composed of the following microservices:

- **Architect** (Port 8001): Generates project blueprints and architecture designs
- **CodeGen** (Port 8002): Converts blueprints into executable code
- **Review** (Port 8003): Performs code review and quality analysis
- **Debugger** (Port 8004): Identifies and fixes code issues
- **Tests** (Port 8005): Generates and runs test suites
- **Dashboard** (Port 3000): React-based web interface for system interaction

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+ (for frontend development)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/HiveMind-OS.git
   cd HiveMind-OS
   ```

2. **Set up Python virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Install backend dependencies
   pip install -r requirements.txt
   ```

3. **Set up frontend:**
   ```bash
   cd frontend/dashboard
   npm install
   cd ../..
   ```

### Running the Services

1. **Start Backend Services**

   Open separate terminal windows for each service:

   ```bash
   # Terminal 1 - Architect
   cd backend/architect
   uvicorn main:app --reload --port 8001

   # Terminal 2 - CodeGen
   cd backend/codegen
   uvicorn main:app --reload --port 8002

   # Terminal 3 - Review
   cd backend/review
   uvicorn main:app --reload --port 8003

   # Terminal 4 - Debugger
   cd backend/debugger
   uvicorn main:app --reload --port 8004

   # Terminal 5 - Tests
   cd backend/tests
   uvicorn main:app --reload --port 8005
   ```

2. **Start Frontend Dashboard**
   ```bash
   cd frontend/dashboard
   npm start
   ```

### Accessing Services

Once running, access the services at:
- Architect: http://localhost:8001
- CodeGen: http://localhost:8002
- Review: http://localhost:8003
- Debugger: http://localhost:8004
- Tests: http://localhost:8005
- Dashboard: http://localhost:3000

## API Documentation

### Architect Service
- **Endpoint**: POST `/architect/generate`
- **Input**: 
  ```json
  {
    "project_description": "Your project description"
  }
  ```
- **Output**: Project blueprint with modules and tech stack

### CodeGen Service
- **Endpoint**: POST `/codegen/generate`
- **Input**: Blueprint from Architect service
- **Output**: Generated code for each module

### Review Service
- **Endpoint**: POST `/review/analyze`
- **Input**: Generated code from CodeGen service
- **Output**: Code review with suggestions

### Debugger Service
- **Endpoint**: POST `/debugger/analyze`
- **Input**: Generated code from CodeGen service
- **Output**: Debugged code and analysis logs

### Tests Service
- **Endpoint**: POST `/tests/generate`
- **Input**: Generated code from CodeGen service
- **Output**: Test suites including:
  - Basic functionality tests
  - Edge case tests
  - Integration tests

## Development

### Project Structure
```
HiveMind-OS/
├── backend/           # Microservices
│   ├── architect/    # Architecture generation service
│   ├── codegen/      # Code generation service
│   ├── review/       # Code review service
│   ├── debugger/     # Debugging service
│   └── tests/        # Testing service
├── frontend/         # React dashboard
├── infrastructure/   # Deployment configs
├── docs/            # Documentation
└── .github/         # GitHub workflows
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Future Improvements

### Planned Features
- Enhanced error handling and logging across all microservices
- Integration of Celery with Redis for asynchronous task processing
- Improved scalability and performance optimizations
- Extended API documentation and examples
- Additional test coverage and quality metrics
- More sophisticated code analysis in Debugger service
- Additional test types in Tests service

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
For support, please open an issue in the GitHub repository or contact the maintainers.