# Setup Instructions: AI Model for Python Competence Assessment

## Prerequisites

### System Requirements
- **Operating System**: Linux, macOS, or Windows 10/11
- **RAM**: Minimum 16GB, Recommended 24GB
- **Storage**: 15GB free space for model and dependencies
- **GPU**: Optional but recommended (CUDA-compatible with 8GB+ VRAM)
- **Python**: Version 3.8 or higher

### Software Dependencies
- Git (for repository cloning)
- Python package manager (pip)
- Virtual environment tool (venv or conda)

## Installation Guide

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/ai_competence_assessment.git
cd ai_competence_assessment
```

### Step 2: Create Virtual Environment
```bash
# Using venv
python -m venv ai_assessment_env
source ai_assessment_env/bin/activate  # Linux/macOS
# ai_assessment_env\Scripts\activate   # Windows

# Or using conda
conda create -n ai_assessment python=3.9
conda activate ai_assessment
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Download CodeLlama Model
```bash
# Using Hugging Face Hub
python -c "
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

print('Downloading CodeLlama-7B-Instruct...')
tokenizer = AutoTokenizer.from_pretrained('codellama/CodeLlama-7b-Instruct-hf')
model = AutoModelForCausalLM.from_pretrained(
    'codellama/CodeLlama-7b-Instruct-hf',
    torch_dtype=torch.float16,
    device_map='auto' if torch.cuda.is_available() else 'cpu'
)
print('Model downloaded successfully!')
"
```

## Configuration

### Environment Variables
Create a `.env` file in the project root:
```bash
# .env file
MODEL_NAME=codellama/CodeLlama-7b-Instruct-hf
MAX_LENGTH=512
TEMPERATURE=0.7
TOP_P=0.95
DEVICE=auto
CACHE_DIR=./model_cache
```

### Configuration File
Edit `config.yaml` to customize assessment parameters:
```yaml
# config.yaml
model:
  name: "codellama/CodeLlama-7b-Instruct-hf"
  max_tokens: 512
  temperature: 0.7
  
assessment:
  skill_levels: ["beginner", "intermediate", "advanced"]
  max_response_time: 10
  min_confidence_threshold: 0.8
  
evaluation:
  batch_size: 4
  num_samples_per_level: 10
  output_dir: "./results"
```

## Usage Examples

### Basic Code Assessment
```python
from ai_assessment import CodeAssessment

# Initialize the assessment system
assessor = CodeAssessment()

# Sample student code
student_code = """
def calculate_factorial(n):
    result = 1
    for i in range(n):
        result *= i
    return result

print(calculate_factorial(5))
"""

# Generate assessment
assessment = assessor.evaluate_code(
    code=student_code,
    student_level="intermediate",
    focus_areas=["correctness", "efficiency", "style"]
)

print("Assessment Results:")
print(f"Issues Identified: {assessment['issues']}")
print(f"Learning Prompts: {assessment['prompts']}")
print(f"Competence Score: {assessment['score']}/100")
```

### Batch Processing
```python
from ai_assessment import BatchProcessor

# Process multiple code submissions
processor = BatchProcessor()

# Load code samples from directory
code_samples = processor.load_from_directory("./code_samples/")

# Run batch assessment
results = processor.evaluate_batch(
    samples=code_samples,
    output_file="batch_results.json",
    parallel_processing=True
)

print(f"Processed {len(results)} code samples")
```

### Interactive Assessment Mode
```python
from ai_assessment import InteractiveAssessor

# Start interactive session
interactive = InteractiveAssessor()
interactive.start_session()

# This will prompt for:
# 1. Student code input
# 2. Skill level selection
# 3. Assessment type preferences
# 4. Real-time feedback display
```

## Testing the Setup

### Verification Script
Run the verification script to ensure everything is working:
```bash
python verify_setup.py
```

Expected output:
```
✓ Python version check passed
✓ Dependencies installed correctly
✓ Model loaded successfully
✓ GPU acceleration available (if applicable)
✓ Test assessment completed
✓ All systems operational
```

### Sample Test Cases
```bash
# Run basic functionality tests
python -m pytest tests/test_basic_functionality.py -v

# Run model evaluation tests
python -m pytest tests/test_model_evaluation.py -v

# Run educational assessment tests
python -m pytest tests/test_educational_features.py -v
```

## Performance Optimization

### GPU Acceleration Setup
If you have a CUDA-compatible GPU:
```bash
# Verify CUDA installation
nvidia-smi

# Install CUDA-enabled PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Memory Optimization
For systems with limited RAM:
```python
# In your configuration
model_config = {
    "torch_dtype": "float16",  # Use half precision
    "load_in_8bit": True,      # Enable 8-bit quantization
    "device_map": "auto",      # Automatic device mapping
    "max_memory": {0: "14GB"}  # Limit GPU memory usage
}
```

### CPU-Only Configuration
For systems without GPU:
```python
# config.yaml modification
model:
  device: "cpu"
  torch_dtype: "float32"
  max_batch_size: 1  # Smaller batch size for CPU
```

## Troubleshooting

### Common Issues

**1. Out of Memory Error**
```bash
# Reduce model precision
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512

# Or use CPU inference
export CUDA_VISIBLE_DEVICES=""
```

**2. Slow Inference Speed**
```python
# Enable optimizations
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_compile=True,  # PyTorch 2.0+ compilation
    attn_implementation="flash_attention_2"  # If available
)
```

**3. Model Download Issues**
```bash
# Set up Hugging Face cache directory
export HF_HOME=/path/to/large/storage
export TRANSFORMERS_CACHE=$HF_HOME/transformers

# Use offline mode if model already downloaded
export TRANSFORMERS_OFFLINE=1
```

**4. Permission Issues**
```bash
# Fix file permissions
chmod +x scripts/*.py
pip install --user -r requirements.txt
```

### Getting Help

**1. Check System Diagnostics**
```bash
python diagnostic_tool.py
```

**2. View Debug Logs**
```bash
export LOG_LEVEL=DEBUG
python your_script.py
```

**3. Community Support**
- GitHub Issues: Report bugs and get community help
- Documentation: Comprehensive guides at `/docs/`
- Example Notebooks: `/examples/jupyter_notebooks/`

## Advanced Configuration

### Custom Model Fine-tuning
```python
# For institutions wanting to customize the model
from ai_assessment.training import FineTuner

tuner = FineTuner(
    base_model="codellama/CodeLlama-7b-Instruct-hf",
    training_data="./custom_educational_data/",
    output_dir="./custom_model/"
)

tuner.train(
    epochs=3,
    learning_rate=5e-5,
    batch_size=4
)
```

### Integration with Learning Management Systems
```python
# Example LMS integration
from ai_assessment.integrations import MoodleConnector, CanvasConnector

# Configure for your LMS
moodle = MoodleConnector(
    url="https://your-moodle-site.edu",
    token="your-api-token"
)

# Automatic assessment of submissions
moodle.setup_automated_assessment(
    course_id="CS101",
    assignment_id="python-project-1"
)
```

## Security Considerations

### Data Privacy
```yaml
# privacy_config.yaml
privacy:
  anonymize_code: true
  local_processing_only: true
  log_retention_days: 30
  encryption_at_rest: true
```

### Educational Compliance
- FERPA compliance configuration available
- Student data handling protocols included
- Audit logging for educational oversight

## Deployment Options

### Single Machine Deployment
Suitable for small classes or individual instructor use.

### Institutional Deployment
```bash
# Docker deployment for institutional use
docker build -t ai-code-assessment .
docker run -p 8080:8080 ai-code-assessment
```

### Cloud Deployment
Guidelines for AWS, Google Cloud, or Azure deployment included in `/docs/cloud_deployment.md`.

This setup enables comprehensive AI-assisted Python competence assessment suitable for educational environments ranging from individual instruction to large-scale institutional deployment.
