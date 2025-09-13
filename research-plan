# Research Plan: AI Models for Python Competence Assessment

## Research Objective

To evaluate the capability of open-source AI models to analyze student-written Python code and generate meaningful educational prompts that assess conceptual understanding, identify reasoning gaps, and encourage deeper learning without revealing complete solutions.

## Methodology

### Model Selection Criteria

**Primary Evaluation Target: CodeLlama-7B-Instruct**

Selected for evaluation based on:
- **Code Understanding**: Trained specifically on code datasets with strong Python representation
- **Instruction Following**: Fine-tuned for following educational prompts and generating appropriate responses
- **Open Source**: Fully available for research and educational use
- **Reasonable Resource Requirements**: 7B parameters allow deployment on standard hardware
- **Educational Alignment**: Designed to provide helpful responses without being overly prescriptive

### Evaluation Framework

**Dataset Construction**
- **100 Python code samples** stratified across competency levels:
  - Beginner (30): Basic syntax, variables, simple loops
  - Intermediate (40): Functions, data structures, file handling
  - Advanced (30): OOP, algorithms, design patterns
- **Ground Truth Annotations**: Expert-validated competency assessments and learning objectives
- **Diverse Coding Styles**: Multiple approaches to same problems to test model flexibility

**Assessment Dimensions**
1. **Code Analysis Accuracy**: Ability to identify logical errors, inefficiencies, and misconceptions
2. **Conceptual Gap Detection**: Recognition of missing fundamental understanding
3. **Prompt Generation Quality**: Educational value and appropriateness of generated questions
4. **Solution Preservation**: Ability to guide learning without revealing answers
5. **Scaffolding Effectiveness**: Generation of progressive hints and learning pathways

### Testing Protocol

**Phase 1: Automated Assessment (Weeks 1-2)**
```python
def evaluate_code_understanding(model, code_sample):
    """Test model's ability to analyze Python code"""
    
    prompts = [
        "Identify potential issues in this Python code without providing solutions:",
        "What concepts should this student review based on their code?",
        "Generate 3 guiding questions to help this student improve their approach:",
        "Assess the depth of programming understanding demonstrated:"
    ]
    
    responses = []
    for prompt in prompts:
        response = model.generate(f"{prompt}\n\n{code_sample}")
        responses.append(analyze_response_quality(response))
    
    return aggregate_scores(responses)
```

**Phase 2: Expert Validation (Weeks 3-4)**
- 5 experienced Python instructors evaluate model outputs
- Blind comparison against human-generated assessments
- Standardized rubrics for pedagogical effectiveness

**Phase 3: Student Testing (Weeks 5-6)**
- A/B test with 20 computer science students
- Measure learning outcomes and engagement with AI-generated prompts
- Collect feedback on usefulness and clarity

### Validation Metrics

**Quantitative Measures**
- **Accuracy Score**: Correct identification of code issues (target >80%)
- **Conceptual Coverage**: Percentage of learning objectives addressed (target >75%)
- **Non-Solution Rate**: Prompts that avoid giving away answers (target >90%)
- **Response Time**: Model inference speed (target <3 seconds)

**Qualitative Assessment**
- **Pedagogical Appropriateness**: Expert instructor ratings (1-5 scale)
- **Student Engagement**: Measured through interaction patterns
- **Learning Effectiveness**: Pre/post assessment improvements
- **Bias Detection**: Fair assessment across different coding approaches

## Implementation Approach

### Technical Setup

**Model Deployment**
```bash
# Install required dependencies
pip install torch transformers accelerate

# Load CodeLlama model
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Instruct-hf")
model = AutoModelForCausalLM.from_pretrained("codellama/CodeLlama-7b-Instruct-hf")
```

**Assessment Pipeline**
1. **Code Preprocessing**: Normalize formatting, extract key components
2. **Context Generation**: Create educational context for model prompts
3. **Response Analysis**: Parse and evaluate model outputs
4. **Feedback Synthesis**: Generate final assessment and recommendations

### Comparative Analysis

**Baseline Comparisons**
- **CodeBERT**: For semantic code understanding benchmarking
- **ChatGPT-3.5**: As commercial model comparison (where possible)
- **Rule-Based Systems**: Traditional static analysis tools (Pylint, Flake8)
- **Human Experts**: Gold standard for educational assessment quality

### Expected Challenges and Mitigation

**Challenge 1: Solution Revelation**
- *Risk*: Model may provide too much information
- *Mitigation*: Careful prompt engineering and output filtering

**Challenge 2: Conceptual Depth Assessment**
- *Risk*: Surface-level analysis missing deeper understanding gaps
- *Mitigation*: Multi-turn conversations and progressive questioning

**Challenge 3: Bias in Assessment**
- *Risk*: Model preferences for specific coding styles
- *Mitigation*: Diverse training examples and bias detection protocols

**Challenge 4: Scalability**
- *Risk*: Computational requirements for large-scale deployment
- *Mitigation*: Optimization techniques and tiered assessment approaches

## Timeline and Deliverables

### Week 1-2: Model Setup and Initial Testing
- [ ] Deploy CodeLlama-7B-Instruct locally
- [ ] Create evaluation dataset
- [ ] Implement basic assessment pipeline
- [ ] Conduct preliminary accuracy tests

### Week 3-4: Expert Validation
- [ ] Recruit instructor evaluation panel
- [ ] Conduct blind assessment studies
- [ ] Analyze pedagogical effectiveness
- [ ] Refine prompt engineering strategies

### Week 5-6: Student Testing and Analysis
- [ ] Design student interaction experiments
- [ ] Collect learning outcome data
- [ ] Perform statistical analysis
- [ ] Document findings and recommendations

### Week 7: Documentation and Reporting
- [ ] Compile comprehensive results
- [ ] Create implementation guides
- [ ] Prepare research paper draft
- [ ] Submit final evaluation report

## Success Criteria

**Technical Success**
- Model achieves >80% accuracy in identifying code issues
- Generates pedagogically appropriate prompts in >75% of cases
- Maintains <5% solution revelation rate

**Educational Success**
- Student learning improvements >15% compared to control group
- Instructor satisfaction rating >4.0/5.0
- Positive student engagement and feedback

**Practical Success**
- Deployable on standard educational hardware
- Response time suitable for interactive learning
- Clear implementation path for educational institutions

This research plan provides a systematic approach to evaluating AI models for educational Python assessment, with specific focus on maintaining pedagogical integrity while leveraging advanced AI capabilities.
