# Contributing to Code Generation Model using LLM

First off, thank you for considering contributing to this project! It's people like you that make this project such a great learning tool for BCA/MCA students.

## Code of Conduct

This project and everyone participating in it is governed by respect, professionalism, and a commitment to learning. By participating, you are expected to uphold these values.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (code snippets, screenshots)
- **Describe the behavior you observed and expected**
- **Include your environment details** (OS, Python version, Node version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **List any alternatives** you've considered

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Write clear commit messages**
6. **Submit a pull request**

## Development Process

### Setting Up Development Environment

```bash
# Fork and clone the repository
git clone https://github.com/your-username/code-generation-llm.git
cd code-generation-llm

# Set up backend
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Set up frontend
cd ../frontend
yarn install
```

### Making Changes

#### Backend (Python/FastAPI)

- Follow PEP 8 style guide
- Use type hints for function parameters and return values
- Write docstrings for all functions and classes
- Keep functions focused and modular
- Handle errors gracefully with proper HTTP status codes

```python
# Good example
async def generate_code(request: CodeGenerationRequest) -> CodeGenerationResponse:
    """Generate code from natural language prompt using LLM.
    
    Args:
        request: Code generation request containing prompt and language
        
    Returns:
        CodeGenerationResponse with generated code and explanation
        
    Raises:
        HTTPException: If code generation fails
    """
    try:
        # Implementation
        pass
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
```

#### Frontend (React/JavaScript)

- Use functional components with hooks
- Follow the existing design system (Swiss & High-Contrast)
- Add `data-testid` attributes to all interactive elements
- Keep components small and reusable
- Use meaningful variable and function names

```javascript
// Good example
const CodeGenerator = () => {
  const [code, setCode] = useState("");
  
  const handleGenerate = async () => {
    try {
      const response = await axios.post(`${API}/generate-code`, data);
      setCode(response.data.generated_code);
    } catch (error) {
      console.error("Generation failed:", error);
      toast.error("Failed to generate code");
    }
  };
  
  return (
    <button 
      onClick={handleGenerate}
      data-testid="generate-button"
    >
      Generate Code
    </button>
  );
};
```

### Testing

#### Backend Tests

```bash
cd backend
pytest tests/ -v --cov=. --cov-report=html
```

#### Frontend Tests

```bash
cd frontend
yarn test --coverage
```

All new features should include appropriate tests.

### Commit Messages

Follow the conventional commits specification:

```
feat: add support for C++ code generation
fix: resolve syntax highlighting issue for Java
docs: update API documentation
style: improve button hover states
refactor: simplify code generation logic
test: add tests for code history API
chore: update dependencies
```

## Areas for Contribution

### High Priority

- [ ] Add support for more programming languages (Rust, Go, Kotlin)
- [ ] Implement code testing/validation
- [ ] Add user authentication
- [ ] Create mobile-responsive design
- [ ] Add dark mode toggle

### Medium Priority

- [ ] Improve error messages and user feedback
- [ ] Add code formatting options
- [ ] Implement search in documentation
- [ ] Add export options (PDF, DOCX)
- [ ] Create tutorial/walkthrough

### Low Priority

- [ ] Add internationalization (i18n)
- [ ] Create keyboard shortcuts
- [ ] Add code snippets library
- [ ] Implement user preferences
- [ ] Add analytics/usage tracking

### Documentation

- [ ] Add video tutorials
- [ ] Create API examples in multiple languages
- [ ] Write troubleshooting guides
- [ ] Add architecture diagrams
- [ ] Create contribution examples

## Style Guides

### Python Style Guide

- Use Black for code formatting: `black .`
- Use isort for import sorting: `isort .`
- Use flake8 for linting: `flake8 .`
- Maximum line length: 100 characters
- Use descriptive variable names

### JavaScript Style Guide

- Use ESLint for linting
- Use Prettier for formatting
- Use camelCase for variables and functions
- Use PascalCase for components
- Maximum line length: 100 characters

### CSS/Tailwind Style Guide

- Follow existing design tokens
- Use design system colors and spacing
- Avoid custom CSS when Tailwind utilities exist
- Keep styles consistent with Swiss & High-Contrast theme

## Design Guidelines

### Colors

- Primary: `#002FA7` (Blue)
- Foreground: `#0A0A0A` (Near Black)
- Background: `#FFFFFF` (White)
- Surface: `#F8F9FA` (Light Gray)
- Border: `#E5E7EB` (Medium Gray)

### Typography

- Headings: Chivo (font-black, font-bold)
- Body: IBM Plex Sans
- Code: JetBrains Mono

### Components

- Sharp edges (rounded-none or rounded-sm)
- High contrast
- Clear borders (1px solid)
- Flat design (no shadows except subtle ones)

## Review Process

1. **Automated checks** must pass (linting, tests)
2. **Code review** by maintainers
3. **Documentation** review if applicable
4. **Testing** verification
5. **Approval** and merge

## Recognition

Contributors will be:
- Listed in the project README
- Credited in release notes
- Mentioned in documentation updates

## Questions?

Feel free to:
- Open an issue for discussion
- Ask questions in pull requests
- Reach out to maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Code Generation Model using LLM! 🎉