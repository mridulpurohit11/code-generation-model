# Code Generation Model Using LLM

A comprehensive mini project demonstrating intelligent code generation powered by Large Language Models (GPT-5.2). This academic project includes complete documentation and a practical implementation that translates natural language descriptions into executable code across multiple programming languages.

![Code Generation Model](https://static.prod-images.emergentagent.com/jobs/1f943d2f-3ffc-439a-9e29-6c4d4f0888f7/images/7fe2f73e875788c1208606d5f711160eaceaaeb0d623f89555818bc96584b3ec.png)

## 🎯 Project Overview

This project bridges the gap between human intent and machine-readable instructions, enabling users to generate code snippets through simple conversational prompts. It serves as both an academic exploration of LLM capabilities and a practical tool for code generation.

### Key Features

- **Natural Language to Code**: Convert plain English descriptions into executable code
- **Multi-Language Support**: Python, JavaScript, Java, and C++
- **Syntax Highlighting**: Terminal-themed code display with professional highlighting
- **Code Explanations**: Detailed explanations of generated code logic
- **Comprehensive Documentation**: Complete academic project documentation included
- **History Tracking**: MongoDB-based storage of all code generations
- **Modern UI/UX**: Swiss & High-Contrast design optimized for desktop

## 🏗️ Architecture

### Three-Tier Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Presentation Layer                      │
│  React.js + Tailwind CSS + Syntax Highlighting         │
│  Dual-pane layout: Documentation + Code Generator       │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                  Application Layer                       │
│  FastAPI + emergentintegrations + GPT-5.2              │
│  RESTful API + Code Generation Service                  │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                    Data Layer                           │
│  MongoDB - NoSQL database for flexible storage          │
│  Collections: code_generations, history                 │
└─────────────────────────────────────────────────────────┘
```

## 🛠️ Tech Stack

### Frontend
- **React.js 19.0** - Modern JavaScript library
- **Tailwind CSS 3.4** - Utility-first CSS framework
- **React Syntax Highlighter** - Code syntax highlighting
- **Shadcn/UI** - Accessible component library
- **Lucide React** - Modern icon library
- **Axios** - HTTP client

### Backend
- **Python 3.11+** - Core programming language
- **FastAPI 0.110** - Modern, fast web framework
- **Motor 3.3** - Async MongoDB driver
- **Pydantic 2.6** - Data validation
- **emergentintegrations** - Unified LLM integration

### LLM & Database
- **OpenAI GPT-5.2** - State-of-the-art language model
- **MongoDB** - NoSQL document database

### Design System
- **Fonts**: Chivo (headings), IBM Plex Sans (body), JetBrains Mono (code)
- **Color Palette**: Swiss & High-Contrast (#002FA7 primary, #0A0A0A foreground)

## 📦 Installation

### Prerequisites
- Python 3.11 or higher
- Node.js 16+ and Yarn
- MongoDB 27017
- Emergent LLM Key or OpenAI API Key

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your EMERGENT_LLM_KEY

# Run the server
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
yarn install

# Configure environment variables
cp .env.example .env
# Edit .env and set REACT_APP_BACKEND_URL

# Start development server
yarn start
```

## 🔧 Configuration

### Backend Environment Variables (.env)

```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=test_database
CORS_ORIGINS=*
EMERGENT_LLM_KEY=your-emergent-llm-key-here
```

### Frontend Environment Variables (.env)

```env
REACT_APP_BACKEND_URL=http://localhost:8001
WDS_SOCKET_PORT=443
ENABLE_HEALTH_CHECK=false
```

## 🚀 Usage

### Basic Code Generation

1. **Select Programming Language**: Choose from Python, JavaScript, Java, or C++
2. **Enter Description**: Describe what code you need in natural language
   - Example: "Create a Python function to calculate factorial of a number"
3. **Generate Code**: Click the "Generate Code" button
4. **View Results**: See syntax-highlighted code with detailed explanation
5. **Copy Code**: Use the copy button to copy generated code to clipboard

### Example Prompts

- "Create a Python function for factorial calculation"
- "Generate JavaScript code to validate email format using regex"
- "Write a Java class for sorting an array using quicksort"
- "Create a Python function to check if a string is palindrome"
- "Generate JavaScript code for binary search algorithm"

## 📚 API Documentation

### Endpoints

#### Generate Code
```http
POST /api/generate-code
Content-Type: application/json

{
  "prompt": "Create a Python function for factorial",
  "language": "python"
}

Response:
{
  "id": "uuid",
  "prompt": "Create a Python function for factorial",
  "language": "python",
  "generated_code": "def factorial(n):\n    ...",
  "explanation": "This function calculates...",
  "timestamp": "2026-01-09T..."
}
```

#### Get Documentation
```http
GET /api/documentation

Response:
{
  "sections": [
    {
      "title": "Abstract",
      "content": "This project presents..."
    },
    ...
  ]
}
```

#### Get History
```http
GET /api/history?limit=10

Response: Array of CodeGenerationResponse objects
```

## 📖 Academic Documentation

The project includes comprehensive academic documentation covering:

1. **Abstract** - Project summary and capabilities
2. **Introduction** - Real-world relevance and applications
3. **Objectives** - Key goals and deliverables
4. **Literature Review** - Evolution of code generation
5. **Methodology** - Step-by-step system workflow
6. **System Architecture** - Technical architecture details
7. **Tools and Technologies** - Complete tech stack
8. **Implementation** - Code examples and implementation details
9. **Advantages and Limitations** - Pros, cons, and best practices
10. **Future Scope** - Potential enhancements and roadmap
11. **Conclusion** - Key achievements and impact

All documentation is accessible through the web interface and can be downloaded as a text file.

## 🎨 Design Philosophy

The project follows a **Swiss & High-Contrast** design aesthetic:

- **Sharp Edges**: Clean, geometric lines with minimal rounding
- **High Contrast**: Strong black (#0A0A0A) on white (#FFFFFF)
- **Functional Typography**: Three distinct font families for hierarchy
- **Brutalist Components**: Flat buttons, sharp borders, no shadows
- **Split-Pane Layout**: Documentation (left) and workspace (right)

## 🧪 Testing

### Run Backend Tests
```bash
cd backend
pytest tests/
```

### Run Frontend Tests
```bash
cd frontend
yarn test
```

### Manual Testing
1. Test code generation with different languages
2. Verify syntax highlighting renders correctly
3. Check MongoDB storage of generation history
4. Test documentation accordion functionality
5. Verify download documentation feature
6. Test example prompt auto-fill

## 📁 Project Structure

```
/app/
├── backend/
│   ├── server.py              # Main FastAPI application
│   ├── requirements.txt       # Python dependencies
│   └── .env                   # Environment variables
├── frontend/
│   ├── src/
│   │   ├── App.js            # Main React component
│   │   ├── App.css           # Component styles
│   │   ├── index.css         # Global styles
│   │   └── components/ui/    # Shadcn UI components
│   ├── package.json          # Node dependencies
│   ├── tailwind.config.js    # Tailwind configuration
│   └── .env                  # Frontend environment variables
├── design_guidelines.json     # UI/UX design specifications
└── README.md                 # This file
```

## 🎓 Educational Value

### For BCA/MCA Students

This project demonstrates:
- **Full-Stack Development**: React + FastAPI + MongoDB integration
- **API Design**: RESTful API principles and async programming
- **LLM Integration**: Practical AI/ML application
- **Modern UI/UX**: Professional design implementation
- **Database Management**: NoSQL with MongoDB
- **Software Architecture**: Clean, scalable system design

### Learning Outcomes

✅ Understand how LLMs process natural language  
✅ Learn async/await patterns in Python and JavaScript  
✅ Implement syntax highlighting and code parsing  
✅ Design dual-pane desktop applications  
✅ Integrate third-party AI services  
✅ Build production-ready APIs with FastAPI  
✅ Create responsive, accessible UIs with React  

## ⚡ Advantages

1. **Accessibility**: Non-programmers can generate functional code
2. **Speed**: Generates code in 2-5 seconds
3. **Learning Tool**: Explanations help understand concepts
4. **Multi-Language**: Single interface for multiple languages
5. **Best Practices**: Follows industry standards
6. **Cost-Effective**: Reduces development time
7. **Consistency**: Well-structured, commented code
8. **Experimentation**: Quick prototyping capability

## ⚠️ Limitations

1. **Complex Logic**: May struggle with highly complex algorithms
2. **Context Understanding**: Limited broader application context
3. **Prompt Dependency**: Quality depends on input clarity
4. **Security Review**: Generated code should be reviewed
5. **API Costs**: Requires API access and credits
6. **Internet Required**: Active connection needed
7. **Model Limitations**: Occasional logical errors possible

### Best Practices

- Always review and test generated code
- Use for learning and prototyping
- Provide clear, specific prompts
- Combine with human expertise for production

## 🚀 Future Enhancements

### Planned Features
- [ ] Code debugging and error correction
- [ ] Version control integration (Git)
- [ ] Multi-file project generation
- [ ] IDE plugins (VS Code, PyCharm)
- [ ] Automated testing of generated code
- [ ] Security vulnerability scanning
- [ ] Custom model fine-tuning
- [ ] Team collaboration features

### Advanced Capabilities
- Context-aware generation from uploaded files
- Real-time collaboration
- Mobile application
- Terminal/CLI tool
- Test case generation
- Database query generation

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Project Developer** - Initial work and implementation
- **Academic Advisor** - Documentation and guidance

## 🙏 Acknowledgments

- OpenAI for GPT-5.2 language model
- Emergent for LLM integration platform
- React and FastAPI communities
- MongoDB documentation team
- Shadcn/UI component library

## 📞 Support

For support and questions:
- Open an issue on GitHub
- Check the documentation section in the web interface
- Review the API documentation above

## 🔗 Links

- [OpenAI Documentation](https://platform.openai.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Emergent Platform](https://emergent.sh)

---

**Built with ❤️ for BCA/MCA students exploring AI and Full-Stack Development**

*Last Updated: January 2026*
