import requests
import sys
import json
from datetime import datetime

class CodeGenerationAPITester:
    def __init__(self, base_url="https://smart-code-llm.preview.emergentagent.com"):
        self.base_url = base_url
        self.api_url = f"{base_url}/api"
        self.tests_run = 0
        self.tests_passed = 0
        self.test_results = []

    def log_test(self, name, success, details=""):
        """Log test result"""
        self.tests_run += 1
        if success:
            self.tests_passed += 1
            print(f"✅ {name} - PASSED")
        else:
            print(f"❌ {name} - FAILED: {details}")
        
        self.test_results.append({
            "test": name,
            "success": success,
            "details": details
        })

    def test_api_root(self):
        """Test API root endpoint"""
        try:
            response = requests.get(f"{self.api_url}/", timeout=10)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            if success:
                data = response.json()
                details += f", Response: {data}"
            self.log_test("API Root Endpoint", success, details)
            return success
        except Exception as e:
            self.log_test("API Root Endpoint", False, str(e))
            return False

    def test_documentation_endpoint(self):
        """Test documentation endpoint"""
        try:
            response = requests.get(f"{self.api_url}/documentation", timeout=10)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            
            if success:
                data = response.json()
                sections = data.get('sections', [])
                expected_sections = [
                    "Abstract", "Introduction", "Objectives", "Literature Review",
                    "Methodology", "System Architecture", "Tools and Technologies",
                    "Implementation", "Advantages and Limitations", "Future Scope", "Conclusion"
                ]
                
                section_titles = [section.get('title', '') for section in sections]
                missing_sections = [title for title in expected_sections if title not in section_titles]
                
                if len(sections) >= 10 and not missing_sections:
                    details += f", Found {len(sections)} sections"
                else:
                    success = False
                    details += f", Expected 11 sections, got {len(sections)}. Missing: {missing_sections}"
            
            self.log_test("Documentation Endpoint", success, details)
            return success
        except Exception as e:
            self.log_test("Documentation Endpoint", False, str(e))
            return False

    def test_code_generation_python(self):
        """Test code generation with Python"""
        try:
            payload = {
                "prompt": "Create a Python function to calculate factorial of a number",
                "language": "python"
            }
            response = requests.post(f"{self.api_url}/generate-code", json=payload, timeout=30)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            
            if success:
                data = response.json()
                required_fields = ['id', 'prompt', 'language', 'generated_code', 'explanation', 'timestamp']
                missing_fields = [field for field in required_fields if field not in data]
                
                if not missing_fields and data.get('generated_code') and data.get('explanation'):
                    details += f", Generated {len(data['generated_code'])} chars of code"
                else:
                    success = False
                    details += f", Missing fields: {missing_fields}"
            
            self.log_test("Code Generation (Python)", success, details)
            return success, response.json() if success else {}
        except Exception as e:
            self.log_test("Code Generation (Python)", False, str(e))
            return False, {}

    def test_code_generation_javascript(self):
        """Test code generation with JavaScript"""
        try:
            payload = {
                "prompt": "Create a JavaScript function to validate email format",
                "language": "javascript"
            }
            response = requests.post(f"{self.api_url}/generate-code", json=payload, timeout=30)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            
            if success:
                data = response.json()
                if data.get('generated_code') and data.get('language') == 'javascript':
                    details += f", Generated JavaScript code"
                else:
                    success = False
                    details += f", Invalid response structure"
            
            self.log_test("Code Generation (JavaScript)", success, details)
            return success
        except Exception as e:
            self.log_test("Code Generation (JavaScript)", False, str(e))
            return False

    def test_code_generation_java(self):
        """Test code generation with Java"""
        try:
            payload = {
                "prompt": "Create a Java method to sort an array",
                "language": "java"
            }
            response = requests.post(f"{self.api_url}/generate-code", json=payload, timeout=30)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            
            if success:
                data = response.json()
                if data.get('generated_code') and data.get('language') == 'java':
                    details += f", Generated Java code"
                else:
                    success = False
                    details += f", Invalid response structure"
            
            self.log_test("Code Generation (Java)", success, details)
            return success
        except Exception as e:
            self.log_test("Code Generation (Java)", False, str(e))
            return False

    def test_code_generation_cpp(self):
        """Test code generation with C++"""
        try:
            payload = {
                "prompt": "Create a C++ function for binary search",
                "language": "cpp"
            }
            response = requests.post(f"{self.api_url}/generate-code", json=payload, timeout=30)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            
            if success:
                data = response.json()
                if data.get('generated_code') and data.get('language') == 'cpp':
                    details += f", Generated C++ code"
                else:
                    success = False
                    details += f", Invalid response structure"
            
            self.log_test("Code Generation (C++)", success, details)
            return success
        except Exception as e:
            self.log_test("Code Generation (C++)", False, str(e))
            return False

    def test_history_endpoint(self):
        """Test history endpoint"""
        try:
            response = requests.get(f"{self.api_url}/history", timeout=10)
            success = response.status_code == 200
            details = f"Status: {response.status_code}"
            
            if success:
                data = response.json()
                if isinstance(data, list):
                    details += f", Found {len(data)} history items"
                else:
                    success = False
                    details += f", Expected list, got {type(data)}"
            
            self.log_test("History Endpoint", success, details)
            return success
        except Exception as e:
            self.log_test("History Endpoint", False, str(e))
            return False

    def test_invalid_request(self):
        """Test error handling with invalid request"""
        try:
            payload = {
                "prompt": "",  # Empty prompt
                "language": "python"
            }
            response = requests.post(f"{self.api_url}/generate-code", json=payload, timeout=10)
            # Should handle gracefully, either 400 or 422 or still 200 with error message
            success = response.status_code in [200, 400, 422]
            details = f"Status: {response.status_code}"
            
            self.log_test("Error Handling (Empty Prompt)", success, details)
            return success
        except Exception as e:
            self.log_test("Error Handling (Empty Prompt)", False, str(e))
            return False

    def run_all_tests(self):
        """Run all backend API tests"""
        print("🚀 Starting Code Generation API Tests")
        print("=" * 50)
        
        # Test basic connectivity
        if not self.test_api_root():
            print("❌ API not accessible, stopping tests")
            return False
        
        # Test documentation
        self.test_documentation_endpoint()
        
        # Test code generation for all languages
        success, _ = self.test_code_generation_python()
        self.test_code_generation_javascript()
        self.test_code_generation_java()
        self.test_code_generation_cpp()
        
        # Test history
        self.test_history_endpoint()
        
        # Test error handling
        self.test_invalid_request()
        
        # Print summary
        print("\n" + "=" * 50)
        print(f"📊 Test Summary: {self.tests_passed}/{self.tests_run} tests passed")
        print(f"Success Rate: {(self.tests_passed/self.tests_run)*100:.1f}%")
        
        if self.tests_passed == self.tests_run:
            print("🎉 All tests passed!")
            return True
        else:
            print("⚠️  Some tests failed. Check details above.")
            return False

def main():
    tester = CodeGenerationAPITester()
    success = tester.run_all_tests()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())