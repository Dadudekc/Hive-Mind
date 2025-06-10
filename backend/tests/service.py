# backend/tests/service.py
from models import TestCase, TestSuite

def generate_tests(code_result: dict) -> dict:
    """
    Generates comprehensive test cases for each module.
    """
    test_suites = {}
    
    for module, code in code_result["codebase"].items():
        # Generate basic test case
        basic_test = TestCase(
            module=module,
            test_script=(
                f"def test_{module}_basic():\n"
                f"    # Basic functionality test for {module}\n"
                f"    result = {module}_module()\n"
                f"    assert result is not None\n"
            ),
            description=f"Basic functionality test for {module} module"
        )
        
        # Generate edge case test
        edge_test = TestCase(
            module=module,
            test_script=(
                f"def test_{module}_edge_cases():\n"
                f"    # Edge case test for {module}\n"
                f"    # TODO: Add specific edge cases based on module functionality\n"
                f"    pass\n"
            ),
            description=f"Edge case test for {module} module"
        )
        
        # Generate integration test
        integration_test = TestCase(
            module=module,
            test_script=(
                f"def test_{module}_integration():\n"
                f"    # Integration test for {module}\n"
                f"    # TODO: Add integration test with other modules\n"
                f"    pass\n"
            ),
            description=f"Integration test for {module} module"
        )
        
        # Create test suite for this module
        test_suite = TestSuite(tests=[basic_test, edge_test, integration_test])
        test_suites[module] = test_suite.dict()
    
    return {
        "test_suites": test_suites,
        "summary": {
            "total_modules": len(test_suites),
            "total_tests": sum(len(suite["tests"]) for suite in test_suites.values())
        }
    }
