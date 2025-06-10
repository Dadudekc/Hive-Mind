import requests
import json

# Base URLs for all services
ARCHITECT_URL = "http://localhost:8001"
CODEGEN_URL = "http://localhost:8002"
REVIEW_URL = "http://localhost:8003"
DEBUGGER_URL = "http://localhost:8004"
TESTS_URL = "http://localhost:8005"

def test_architect():
    """Test the Architect service by generating a project blueprint"""
    print("\n1. Testing Architect Service...")
    response = requests.post(
        f"{ARCHITECT_URL}/architect/generate",
        json={"project_description": "A simple task management API with user authentication"}
    )
    if response.status_code == 200:
        blueprint = response.json()
        print("Blueprint generated successfully!")
        print(json.dumps(blueprint, indent=2))
        return blueprint
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def test_codegen(blueprint):
    """Test the CodeGen service by generating code from the blueprint"""
    print("\n2. Testing CodeGen Service...")
    response = requests.post(
        f"{CODEGEN_URL}/codegen/generate",
        json=blueprint
    )
    if response.status_code == 200:
        code = response.json()
        print("Code generated successfully!")
        print(json.dumps(code, indent=2))
        return code
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def test_review(code):
    """Test the Review service by reviewing the generated code"""
    print("\n3. Testing Review Service...")
    response = requests.post(
        f"{REVIEW_URL}/review/analyze",
        json=code
    )
    if response.status_code == 200:
        review = response.json()
        print("Code review completed!")
        print(json.dumps(review, indent=2))
        return review
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def test_debugger(code):
    """Test the Debugger service by analyzing the code for potential issues"""
    print("\n4. Testing Debugger Service...")
    response = requests.post(
        f"{DEBUGGER_URL}/debugger/analyze",
        json=code
    )
    if response.status_code == 200:
        debug = response.json()
        print("Debug analysis completed!")
        print(json.dumps(debug, indent=2))
        return debug
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def test_tests(code):
    """Test the Tests service by generating tests for the code"""
    print("\n5. Testing Tests Service...")
    response = requests.post(
        f"{TESTS_URL}/tests/generate",
        json=code
    )
    if response.status_code == 200:
        tests = response.json()
        print("Tests generated successfully!")
        print(json.dumps(tests, indent=2))
        return tests
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def main():
    """Run the complete workflow"""
    print("Starting HiveMind OS Service Test...")
    
    # Step 1: Generate blueprint
    blueprint = test_architect()
    if not blueprint:
        return
    
    # Step 2: Generate code
    code = test_codegen(blueprint)
    if not code:
        return
    
    # Step 3: Review code
    review = test_review(code)
    if not review:
        return
    
    # Step 4: Debug code
    debug = test_debugger(code)
    if not debug:
        return
    
    # Step 5: Generate tests
    tests = test_tests(code)
    if not tests:
        return
    
    print("\nAll services tested successfully!")

if __name__ == "__main__":
    main() 