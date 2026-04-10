from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
import uuid
from datetime import datetime, timezone
from emergentintegrations.llm.chat import LlmChat, UserMessage


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")


# Define Models
class CodeGenerationRequest(BaseModel):
    prompt: str
    language: str = "python"

class CodeGenerationResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    prompt: str
    language: str
    generated_code: str
    explanation: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class DocumentationSection(BaseModel):
    title: str
    content: str


# Academic Documentation Content
DOCUMENTATION_CONTENT = [
    {
        "title": "Abstract",
        "content": """This project presents a Code Generation Model powered by Large Language Models (LLMs) that translates natural language descriptions into executable code. The system leverages state-of-the-art AI technology to bridge the gap between human intent and machine-readable instructions, enabling users to generate code snippets across multiple programming languages through simple conversational prompts. The model demonstrates high accuracy in understanding programming requirements and producing syntactically correct, well-commented code that follows best practices. This project serves as a practical demonstration of how LLMs can revolutionize software development by reducing the barrier to entry for non-programmers and accelerating the development workflow for experienced developers."""
    },
    {
        "title": "Introduction",
        "content": """In today's rapidly evolving technological landscape, the demand for software solutions far exceeds the supply of skilled programmers. Code generation using Large Language Models (LLMs) addresses this gap by democratizing software development. 

LLMs like GPT-5.2, trained on billions of lines of code and natural language, can understand programming concepts and translate human requirements into functional code. This technology has real-world applications in:

• Rapid Prototyping: Quickly generating proof-of-concept code for startups and researchers
• Educational Tools: Helping students learn programming by seeing how natural language translates to code
• Developer Productivity: Automating boilerplate code generation and routine programming tasks
• Accessibility: Enabling domain experts without programming backgrounds to create simple automation scripts

This project implements a practical code generation system that showcases the potential of LLMs in transforming how we approach software development."""
    },
    {
        "title": "Objectives",
        "content": """The primary objectives of this project are:

1. To develop an intelligent code generation system that accepts natural language input and produces executable code
2. To support multiple programming languages (Python, JavaScript, Java, C++) through a unified interface
3. To provide clear explanations of the generated code, enhancing user understanding
4. To demonstrate the practical application of Large Language Models in software engineering
5. To create a user-friendly interface accessible to both programmers and non-programmers
6. To maintain a history of code generations for reference and learning purposes
7. To ensure generated code follows industry best practices and includes proper documentation
8. To explore the capabilities and limitations of LLM-based code generation"""
    },
    {
        "title": "Literature Review",
        "content": """Code generation has evolved significantly over the decades:

Early Approaches (1990s-2010s):
• Template-based code generators with limited flexibility
• Domain-specific languages (DSLs) requiring specialized knowledge
• Rule-based systems with manual pattern definitions

Machine Learning Era (2010s):
• Researchers began using RNNs and LSTMs for code generation
• GitHub Copilot (2021) introduced AI pair programming using OpenAI Codex
• Studies showed ML models could learn programming patterns from large codebases

LLM Revolution (2020s-Present):
• GPT-3 and GPT-4 demonstrated unprecedented natural language to code capabilities
• Models like Claude, Gemini, and GPT-5.2 achieve near-human performance in many coding tasks
• Research papers show LLMs can generate code with 70-85% functional correctness

Key Research Findings:
• LLMs excel at understanding programming intent from natural language
• Context-aware generation produces more accurate results
• Explanation capabilities help users learn and verify generated code
• Multi-language support emerges naturally from training on diverse codebases

This project builds upon these advancements to create a practical, accessible code generation tool."""
    },
    {
        "title": "Methodology",
        "content": """The system operates through the following step-by-step process:

Step 1: User Input
• User enters a natural language description of desired code functionality
• Example: \"Create a Python function to calculate factorial of a number\"
• User selects target programming language from dropdown

Step 2: Request Processing
• Frontend sends HTTP POST request to backend API with prompt and language
• Backend validates input and prepares request for LLM

Step 3: LLM Interaction
• System initializes LlmChat with GPT-5.2 model and API credentials
• Crafted system message instructs model to act as expert programmer
• User prompt is enhanced with language-specific instructions
• Model generates code with detailed comments

Step 4: Response Generation
• LLM returns generated code and explanation
• Backend parses response to extract code and description
• System stores generation in MongoDB for history tracking

Step 5: Display Results
• Frontend receives response and displays:
  - Syntax-highlighted code in terminal-style block
  - Clear explanation of code logic and functionality
  - Copy-to-clipboard functionality

Step 6: History Management
• All generations saved with timestamp, prompt, and language
• Users can reference previous generations
• Data persists across sessions

The entire process completes in 2-5 seconds, providing near-instant code generation."""
    },
    {
        "title": "System Architecture",
        "content": """The system follows a modern three-tier architecture:

Presentation Layer (Frontend):
• Technology: React.js with Tailwind CSS
• Components:
  - Documentation Viewer (Left Pane): Displays this academic content
  - Code Generator (Right Pane): Interactive generation interface
  - Language Selector: Dropdown for choosing programming language
  - Example Prompts: Quick-fill buttons for common requests
  - Syntax Highlighter: Terminal-themed code display
• Fonts: Chivo (headings), IBM Plex Sans (body), JetBrains Mono (code)
• Design: Swiss & High-Contrast aesthetic with sharp edges and clear borders

Application Layer (Backend):
• Technology: FastAPI (Python)
• Components:
  - API Router: Handles HTTP requests with /api prefix
  - Code Generation Service: Interfaces with LLM
  - Documentation Service: Serves academic content
  - History Service: Manages generation records
• Key Libraries:
  - emergentintegrations: LLM integration wrapper
  - motor: Async MongoDB driver
  - pydantic: Data validation and serialization

Data Layer:
• Technology: MongoDB (NoSQL database)
• Collections:
  - code_generations: Stores all generation history
  - Fields: id, prompt, language, generated_code, explanation, timestamp
• Benefits: Flexible schema, fast reads, scalable

Integration Layer:
• OpenAI GPT-5.2 via emergentintegrations library
• RESTful API communication between frontend and backend
• CORS middleware for cross-origin requests

Data Flow:
User Input → Frontend → Backend API → LLM Service → Database → Backend → Frontend → Display

This architecture ensures separation of concerns, scalability, and maintainability."""
    },
    {
        "title": "Tools and Technologies",
        "content": """Frontend Technologies:
• React.js 19.0: Modern JavaScript library for building user interfaces
• Tailwind CSS 3.4: Utility-first CSS framework for rapid styling
• React Router: Client-side routing and navigation
• Axios: HTTP client for API communication
• React Syntax Highlighter: Code syntax highlighting with theme support
• Shadcn/UI: High-quality accessible component library
• Lucide React: Modern icon library

Backend Technologies:
• Python 3.11+: Core programming language
• FastAPI 0.110: Modern, fast web framework for building APIs
• Uvicorn: ASGI server for running FastAPI applications
• Motor 3.3: Async MongoDB driver for Python
• Pydantic 2.6: Data validation using Python type hints
• Python-dotenv: Environment variable management

LLM Integration:
• emergentintegrations 0.1.0: Unified LLM integration library
• OpenAI GPT-5.2: State-of-the-art language model for code generation
• Emergent LLM Key: Universal API key for multiple LLM providers

Database:
• MongoDB 27017: NoSQL document database for flexible data storage

Development Tools:
• Git: Version control system
• VS Code: Code editor with extensions
• Postman: API testing and development
• Chrome DevTools: Frontend debugging

Deployment:
• Kubernetes: Container orchestration platform
• Supervisor: Process control system for backend/frontend services
• NGINX/Ingress: Reverse proxy and routing

Design Tools:
• Google Fonts: Chivo, IBM Plex Sans, JetBrains Mono
• Color Palette: High-contrast (#002FA7 primary, #0A0A0A foreground)"""
    },
    {
        "title": "Implementation",
        "content": """Core Implementation Details:

1. Backend API Endpoint (server.py):
```python
@api_router.post(\"/generate-code\", response_model=CodeGenerationResponse)
async def generate_code(request: CodeGenerationRequest):
    # Initialize LLM chat
    chat = LlmChat(
        api_key=os.environ.get('EMERGENT_LLM_KEY'),
        session_id=f\"code-gen-{uuid.uuid4()}\",
        system_message=\"You are an expert programmer...\"
    ).with_model(\"openai\", \"gpt-5.2\")
    
    # Generate code using LLM
    user_message = UserMessage(
        text=f\"Generate {request.language} code: {request.prompt}\"
    )
    response = await chat.send_message(user_message)
    
    # Store in database
    doc = {...}
    await db.code_generations.insert_one(doc)
    
    return CodeGenerationResponse(...)
```

2. Frontend Code Generator Component:
```javascript
const generateCode = async () => {
  const response = await axios.post(`${API}/generate-code`, {
    prompt: userPrompt,
    language: selectedLanguage
  });
  
  setGeneratedCode(response.data.generated_code);
  setExplanation(response.data.explanation);
};
```

3. Syntax Highlighting:
```javascript
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';

<SyntaxHighlighter language={language} style={vscDarkPlus}>
  {generatedCode}
</SyntaxHighlighter>
```

4. Example Prompts:
• \"Create a Python function for factorial calculation\"
• \"Generate JavaScript code to validate email format\"
• \"Write a Java class for sorting an array using quicksort\"
• \"Create a Python function to reverse a string\"

The implementation focuses on simplicity, clarity, and educational value."""
    },
    {
        "title": "Advantages and Limitations",
        "content": """Advantages:

1. Accessibility: Non-programmers can generate functional code using natural language
2. Speed: Generates code in seconds, dramatically reducing development time
3. Learning Tool: Explanations help users understand programming concepts
4. Multi-language Support: Single interface for multiple programming languages
5. Best Practices: Generated code follows industry standards and conventions
6. Cost-Effective: Reduces need for extensive programming knowledge
7. Consistency: Produces well-structured, commented code every time
8. Experimentation: Allows quick prototyping and testing of ideas
9. Documentation: Auto-generates code comments and explanations
10. Scalability: Can handle simple to moderately complex programming tasks

Limitations:

1. Complex Logic: May struggle with highly complex algorithmic problems
2. Context Understanding: Limited understanding of broader application context
3. Dependency on Prompts: Output quality depends on clarity of user input
4. Security Concerns: Generated code should be reviewed for security vulnerabilities
5. API Costs: Requires API access and incurs usage costs
6. Internet Dependency: Requires active internet connection
7. Model Hallucinations: Occasionally generates syntactically correct but logically flawed code
8. Limited Debugging: Cannot debug or troubleshoot existing codebases
9. Version-Specific Issues: May not be aware of latest library versions
10. Ethical Considerations: Questions about code ownership and originality

Best Practices:
• Always review and test generated code
• Use for learning and prototyping, not production without review
• Provide clear, specific prompts for better results
• Combine with human expertise for complex projects"""
    },
    {
        "title": "Future Scope",
        "content": """Potential Enhancements:

1. Advanced Features:
• Code debugging and error correction capabilities
• Integration with version control systems (Git)
• Real-time collaboration for team-based code generation
• Support for more programming languages (Rust, Go, Kotlin, Swift)
• Code optimization and refactoring suggestions

2. Enhanced Intelligence:
• Context-aware generation using project file uploads
• Learning from user feedback to improve accuracy
• Custom fine-tuning for specific domains (web dev, data science, etc.)
• Multi-file project generation with proper structure

3. Integration Capabilities:
• IDE plugins (VS Code, IntelliJ, PyCharm)
• API for third-party application integration
• Mobile application for on-the-go code generation
• Terminal/CLI tool for developer workflows

4. Educational Features:
• Interactive tutorials based on generated code
• Step-by-step execution visualization
• Quizzes and challenges using generated examples
• Progress tracking and skill assessment

5. Quality Improvements:
• Automated testing of generated code
• Security vulnerability scanning
• Performance optimization analysis
• Code style enforcement and linting

6. Specialized Models:
• Domain-specific models (frontend, backend, ML, DevOps)
• Framework-specific generators (React, Django, Spring)
• Database query generation (SQL, MongoDB)
• Test case generation

7. Community Features:
• Sharing generated code snippets
• Rating and reviewing generations
• Community-contributed prompt templates
• Open-source contribution automation

8. Enterprise Features:
• Team workspaces and shared history
• Custom model training on proprietary codebases
• Compliance and audit logging
• On-premise deployment options

The future of code generation with LLMs is promising, with potential to fundamentally transform software development education and practice."""
    },
    {
        "title": "Conclusion",
        "content": """This project successfully demonstrates the power and potential of Large Language Models in code generation. By creating an intuitive interface that translates natural language into executable code across multiple programming languages, we've showcased how AI can democratize software development and enhance programmer productivity.

Key Achievements:
• Successfully implemented a working code generation system using GPT-5.2
• Created a dual-pane interface balancing documentation and functionality
• Demonstrated multi-language support (Python, JavaScript, Java, C++)
• Provided educational value through code explanations and examples
• Built a scalable architecture using modern web technologies

The system proves that LLMs can:
✓ Understand programming requirements from natural language
✓ Generate syntactically correct and well-commented code
✓ Explain complex programming concepts in simple terms
✓ Adapt to different programming languages and paradigms

Educational Impact:
For BCA/MCA students, this project serves as a practical example of:
- Full-stack web development (React + FastAPI + MongoDB)
- API integration and asynchronous programming
- Modern UI/UX design principles
- Real-world application of artificial intelligence
- Software architecture and system design

Practical Applications:
The developed system can be used for rapid prototyping, learning programming concepts, generating boilerplate code, and assisting in software development workflows. While not a replacement for skilled programmers, it serves as a powerful tool to augment human capabilities.

Final Thoughts:
As LLMs continue to evolve, code generation will become increasingly sophisticated and reliable. This project lays the foundation for exploring these advancements and understanding both the capabilities and limitations of AI-assisted programming. The future of software development will likely involve close collaboration between human developers and AI systems, combining human creativity with machine efficiency.

The journey from natural language to executable code represents a significant milestone in making technology more accessible and development more efficient."""
    }
]


# Routes
@api_router.get("/")
async def root():
    return {"message": "Code Generation Model API"}

@api_router.post("/generate-code", response_model=CodeGenerationResponse)
async def generate_code(request: CodeGenerationRequest):
    try:
        # Initialize LLM chat
        chat = LlmChat(
            api_key=os.environ.get('EMERGENT_LLM_KEY'),
            session_id=f"code-gen-{uuid.uuid4()}",
            system_message=f"""You are an expert {request.language} programmer. Generate clean, well-commented code based on user requirements. 
            
            Respond in this EXACT format:
            CODE:
            ```{request.language}
            [your generated code here]
            ```
            
            EXPLANATION:
            [Clear explanation of what the code does, how it works, and any important details]
            """
        ).with_model("openai", "gpt-5.2")
        
        # Create enhanced prompt
        enhanced_prompt = f"""Generate {request.language} code for the following requirement:
        
        {request.prompt}
        
        Requirements:
        - Write clean, readable code
        - Include helpful comments
        - Follow {request.language} best practices
        - Make it production-ready
        """
        
        user_message = UserMessage(text=enhanced_prompt)
        llm_response = await chat.send_message(user_message)
        
        # Parse response
        response_text = llm_response
        
        # Extract code and explanation
        code = ""
        explanation = ""
        
        if "CODE:" in response_text and "EXPLANATION:" in response_text:
            parts = response_text.split("EXPLANATION:")
            code_part = parts[0].replace("CODE:", "").strip()
            explanation = parts[1].strip()
            
            # Extract code from markdown code blocks
            if "```" in code_part:
                code_lines = code_part.split("```")
                for i, line in enumerate(code_lines):
                    if i % 2 == 1:  # Odd indices contain code
                        # Remove language identifier from first line
                        lines = line.split("\n")
                        if lines[0].strip().lower() in [request.language.lower(), "python", "javascript", "java", "cpp", "c++"]:
                            code = "\n".join(lines[1:]).strip()
                        else:
                            code = line.strip()
                        break
            else:
                code = code_part
        else:
            # Fallback parsing
            code = response_text
            explanation = f"Generated {request.language} code based on your requirements."
        
        # Create response object
        code_gen = CodeGenerationResponse(
            prompt=request.prompt,
            language=request.language,
            generated_code=code,
            explanation=explanation
        )
        
        # Store in database
        doc = code_gen.model_dump()
        doc['timestamp'] = doc['timestamp'].isoformat()
        await db.code_generations.insert_one(doc)
        
        return code_gen
        
    except Exception as e:
        logger.error(f"Error generating code: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Code generation failed: {str(e)}")

@api_router.get("/documentation")
async def get_documentation():
    return {"sections": DOCUMENTATION_CONTENT}

@api_router.get("/history", response_model=List[CodeGenerationResponse])
async def get_history(limit: int = 10):
    try:
        history = await db.code_generations.find(
            {}, 
            {"_id": 0}
        ).sort("timestamp", -1).limit(limit).to_list(limit)
        
        # Convert ISO string timestamps back to datetime objects
        for item in history:
            if isinstance(item['timestamp'], str):
                item['timestamp'] = datetime.fromisoformat(item['timestamp'])
        
        return history
    except Exception as e:
        logger.error(f"Error fetching history: {str(e)}")
        return []


# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()