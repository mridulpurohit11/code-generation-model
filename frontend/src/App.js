import { useState, useEffect } from "react";
import "@/App.css";
import axios from "axios";
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Textarea } from "@/components/ui/textarea";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Code, Copy, Check, Download, Sparkles, ChevronRight } from "lucide-react";
import { toast } from "sonner";
import { Toaster } from "@/components/ui/sonner";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const EXAMPLE_PROMPTS = [
  "Create a Python function to calculate factorial of a number",
  "Generate JavaScript code to validate email format using regex",
  "Write a Python function to check if a string is palindrome",
  "Create a JavaScript function to sort an array of objects by a property",
  "Generate Python code for binary search algorithm",
  "Write a JavaScript function to debounce another function"
];

const LANGUAGES = [
  { value: "python", label: "Python" },
  { value: "javascript", label: "JavaScript" },
  { value: "java", label: "Java" },
  { value: "cpp", label: "C++" }
];

function App() {
  const [documentation, setDocumentation] = useState([]);
  const [prompt, setPrompt] = useState("");
  const [language, setLanguage] = useState("python");
  const [generatedCode, setGeneratedCode] = useState("");
  const [explanation, setExplanation] = useState("");
  const [isGenerating, setIsGenerating] = useState(false);
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    fetchDocumentation();
  }, []);

  const fetchDocumentation = async () => {
    try {
      const response = await axios.get(`${API}/documentation`);
      setDocumentation(response.data.sections);
    } catch (e) {
      console.error("Error fetching documentation:", e);
    }
  };

  const handleGenerate = async () => {
    if (!prompt.trim()) {
      toast.error("Please enter a prompt");
      return;
    }

    setIsGenerating(true);
    setGeneratedCode("");
    setExplanation("");

    try {
      const response = await axios.post(`${API}/generate-code`, {
        prompt: prompt,
        language: language
      });

      setGeneratedCode(response.data.generated_code);
      setExplanation(response.data.explanation);
      toast.success("Code generated successfully!");
    } catch (e) {
      console.error("Error generating code:", e);
      toast.error("Failed to generate code. Please try again.");
    } finally {
      setIsGenerating(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(generatedCode);
    setCopied(true);
    toast.success("Code copied to clipboard!");
    setTimeout(() => setCopied(false), 2000);
  };

  const handleExampleClick = (example) => {
    setPrompt(example);
    // Auto-detect language from example
    if (example.toLowerCase().includes("python")) {
      setLanguage("python");
    } else if (example.toLowerCase().includes("javascript")) {
      setLanguage("javascript");
    } else if (example.toLowerCase().includes("java")) {
      setLanguage("java");
    }
  };

  const handleDownloadDoc = () => {
    // Create text content from documentation
    let content = "CODE GENERATION MODEL USING LLM - PROJECT DOCUMENTATION\n\n";
    documentation.forEach(section => {
      content += `\n${section.title.toUpperCase()}\n`;
      content += "=".repeat(section.title.length) + "\n\n";
      content += section.content + "\n";
    });

    // Create blob and download
    const blob = new Blob([content], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'Code_Generation_LLM_Project_Documentation.txt';
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
    document.body.removeChild(a);
    toast.success("Documentation downloaded!");
  };

  return (
    <div className="flex flex-col lg:flex-row h-screen w-full overflow-hidden bg-white text-[#0A0A0A]">
      <Toaster position="top-center" />
      
      {/* LEFT PANE - Documentation */}
      <div className="w-full lg:w-5/12 h-full overflow-y-auto border-r border-[#E5E7EB] bg-[#F8F9FA] p-6 lg:p-12" data-testid="documentation-pane">
        <div className="max-w-3xl">
          {/* Header */}
          <div className="mb-8">
            <div className="flex items-center gap-3 mb-4">
              <Code className="w-8 h-8" strokeWidth={2} />
              <h1 className="text-4xl sm:text-5xl tracking-tight font-black" style={{ fontFamily: 'Chivo, sans-serif' }}>
                Code Generation Model
              </h1>
            </div>
            <p className="text-xs tracking-[0.2em] uppercase font-bold mb-6" style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}>
              Using Large Language Models
            </p>
            <button 
              onClick={handleDownloadDoc}
              className="border border-[#0A0A0A] text-[#0A0A0A] hover:bg-[#F8F9FA] px-4 py-2 text-sm font-bold transition-colors duration-200 ease-in-out flex items-center gap-2"
              data-testid="download-doc-button"
              style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}
            >
              <Download className="w-4 h-4" />
              DOWNLOAD DOCUMENTATION
            </button>
          </div>

          {/* Hero Image */}
          <div className="mb-8">
            <img 
              src="https://static.prod-images.emergentagent.com/jobs/1f943d2f-3ffc-439a-9e29-6c4d4f0888f7/images/7fe2f73e875788c1208606d5f711160eaceaaeb0d623f89555818bc96584b3ec.png" 
              alt="AI Architecture" 
              className="w-full h-auto border border-[#E5E7EB]"
            />
          </div>

          {/* Documentation Accordion */}
          <Accordion type="single" collapsible className="space-y-1" data-testid="documentation-accordion">
            {documentation.map((section, index) => (
              <AccordionItem key={index} value={`item-${index}`} className="border-b border-[#E5E7EB]">
                <AccordionTrigger className="text-left font-bold hover:no-underline py-4" style={{ fontFamily: 'Chivo, sans-serif' }} data-testid={`doc-section-${section.title.toLowerCase().replace(/\s+/g, '-')}`}>
                  {section.title}
                </AccordionTrigger>
                <AccordionContent className="text-base leading-relaxed pb-4 whitespace-pre-line" style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}>
                  {section.content}
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </div>

      {/* RIGHT PANE - Code Generator */}
      <div className="w-full lg:w-7/12 h-full flex flex-col overflow-y-auto bg-white p-6 lg:p-12" data-testid="code-generator-pane">
        <div className="max-w-5xl w-full mx-auto">
          {/* Header */}
          <div className="mb-8">
            <div className="flex items-center gap-3 mb-2">
              <Sparkles className="w-6 h-6 text-[#002FA7]" strokeWidth={2} />
              <h2 className="text-2xl sm:text-3xl tracking-tight font-bold" style={{ fontFamily: 'Chivo, sans-serif' }}>
                Interactive Code Generator
              </h2>
            </div>
            <p className="text-base leading-relaxed text-[#0A0A0A]/70" style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}>
              Transform natural language into executable code
            </p>
          </div>

          {/* Language Selector */}
          <div className="mb-6">
            <label className="text-xs tracking-[0.2em] uppercase font-bold mb-2 block" style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}>
              Programming Language
            </label>
            <Select value={language} onValueChange={setLanguage}>
              <SelectTrigger className="w-full border border-[#E5E7EB] focus:ring-2 focus:ring-[#002FA7] focus:border-transparent" data-testid="language-selector" style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}>
                <SelectValue />
              </SelectTrigger>
              <SelectContent>
                {LANGUAGES.map(lang => (
                  <SelectItem key={lang.value} value={lang.value}>
                    {lang.label}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>

          {/* Prompt Input */}
          <div className="mb-6">
            <label className="text-xs tracking-[0.2em] uppercase font-bold mb-2 block" style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}>
              Describe what code you need
            </label>
            <Textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="e.g., Create a function that calculates the factorial of a number"
              className="min-h-[120px] border border-[#E5E7EB] focus:ring-2 focus:ring-[#002FA7] focus:border-transparent resize-none"
              data-testid="prompt-input"
              style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}
            />
          </div>

          {/* Example Prompts */}
          <div className="mb-6">
            <label className="text-xs tracking-[0.2em] uppercase font-bold mb-3 block" style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}>
              Example Prompts
            </label>
            <div className="flex flex-wrap gap-2">
              {EXAMPLE_PROMPTS.map((example, index) => (
                <button
                  key={index}
                  onClick={() => handleExampleClick(example)}
                  className="border border-[#E5E7EB] text-xs uppercase tracking-wider bg-white hover:bg-[#F8F9FA] cursor-pointer px-3 py-2 transition-colors duration-200 ease-in-out text-left"
                  data-testid={`example-prompt-${index}`}
                  style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}
                >
                  {example.length > 50 ? example.substring(0, 50) + '...' : example}
                </button>
              ))}
            </div>
          </div>

          {/* Generate Button */}
          <button
            onClick={handleGenerate}
            disabled={isGenerating || !prompt.trim()}
            className="bg-[#002FA7] text-white hover:bg-[#0A0A0A] px-8 py-3 font-bold transition-colors duration-200 ease-in-out disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2 mb-8"
            data-testid="generate-code-button"
            style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}
          >
            {isGenerating ? (
              <>
                <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                GENERATING...
              </>
            ) : (
              <>
                <ChevronRight className="w-4 h-4" />
                GENERATE CODE
              </>
            )}
          </button>

          {/* Generated Code Display */}
          {generatedCode && (
            <div className="space-y-6" data-testid="generated-code-section">
              {/* Code Block */}
              <div>
                <div className="flex items-center justify-between mb-2">
                  <label className="text-xs tracking-[0.2em] uppercase font-bold" style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}>
                    Generated Code
                  </label>
                  <button
                    onClick={handleCopy}
                    className="border border-[#0A0A0A] text-[#0A0A0A] hover:bg-[#F8F9FA] px-3 py-1 text-xs font-bold transition-colors duration-200 ease-in-out flex items-center gap-2"
                    data-testid="copy-code-button"
                    style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}
                  >
                    {copied ? <Check className="w-3 h-3" /> : <Copy className="w-3 h-3" />}
                    {copied ? 'COPIED' : 'COPY'}
                  </button>
                </div>
                <div className="bg-[#0A0A0A] border border-[#E5E7EB] overflow-hidden">
                  <SyntaxHighlighter 
                    language={language} 
                    style={vscDarkPlus}
                    customStyle={{
                      margin: 0,
                      padding: '1.5rem',
                      background: '#0A0A0A',
                      fontSize: '0.875rem',
                      fontFamily: 'JetBrains Mono, monospace'
                    }}
                    data-testid="syntax-highlighter"
                  >
                    {generatedCode}
                  </SyntaxHighlighter>
                </div>
              </div>

              {/* Explanation */}
              {explanation && (
                <div data-testid="code-explanation-section">
                  <label className="text-xs tracking-[0.2em] uppercase font-bold mb-2 block" style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}>
                    Code Explanation
                  </label>
                  <div className="border border-[#E5E7EB] bg-white p-6">
                    <p className="text-base leading-relaxed whitespace-pre-line" style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}>
                      {explanation}
                    </p>
                  </div>
                </div>
              )}
            </div>
          )}

          {/* Empty State */}
          {!generatedCode && !isGenerating && (
            <div className="border border-[#E5E7EB] bg-[#F8F9FA] p-12 text-center" data-testid="empty-state">
              <div className="max-w-md mx-auto">
                <img 
                  src="https://images.unsplash.com/photo-1741795990628-7ec99d7d2044?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2Mzl8MHwxfHNlYXJjaHwyfHxhYnN0cmFjdCUyMGNvZGUlMjBtYXRyaXh8ZW58MHx8fHwxNzc1ODE5NzMzfDA&ixlib=rb-4.1.0&q=85" 
                  alt="Code Matrix" 
                  className="w-full h-48 object-cover mb-6 opacity-50"
                />
                <p className="text-base leading-relaxed text-[#0A0A0A]/70" style={{ fontFamily: 'IBM Plex Sans, sans-serif' }}>
                  Enter a description above and click "Generate Code" to see AI-powered code generation in action.
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;