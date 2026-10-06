# IntelliResolve – AI-Powered Customer Complaint Intelligence

## Batch F NLP Capstone Project

**Name:** Nikhil Krishna  
**Registration Number:** `23FE10CDS00409`  
**Branch:** B.Tech Computer Science and Data Science  
**Batch:** F  
**Project Title:** IntelliResolve – AI-Powered Customer Complaint Intelligence  
**GitHub Username:** nikhligit2604
**Registration Number:** 23FE10CDS00409  
**Training Program:** Batch F – NLP Capstone Project

---

## 1. Project Overview

IntelliResolve is an NLP and Generative AI based customer complaint intelligence system. It combines traditional NLP and machine learning with a Gemini LLM API to classify, prioritize and analyze customer complaints.

The system can classify complaints, detect sentiment, determine urgency, extract keywords, generate root-cause analysis, recommend actions, draft customer responses, identify escalation needs, identify missing information, store complaint history, process CSV batches and provide analytics through Streamlit.

---

## 2. Problem Statement

Customer support teams receive large numbers of complaints. Manually reviewing every complaint can be time-consuming and can lead to inconsistent prioritization and responses.

IntelliResolve automates the initial analysis so support teams can quickly understand the complaint type, customer sentiment, urgency, important information, likely root cause, recommended action and appropriate response.

---

## 3. Objectives

- Build an NLP-based complaint classification system.
- Apply TF-IDF for text feature extraction.
- Use Logistic Regression for complaint classification.
- Perform sentiment analysis using VADER.
- Detect urgency using rule-based priority detection.
- Extract relevant complaint keywords.
- Integrate the Google Gemini API.
- Use prompt engineering for structured complaint analysis.
- Store complaint records using SQLite.
- Provide an interactive Streamlit interface.
- Support batch CSV analysis.
- Provide complaint analytics and history.
- Maintain the project using Git and GitHub.

---

## 4. System Architecture

```text
Customer Complaint
       |
       v
Text Preprocessing
       |
       +----------------------+----------------------+
       |                      |                      |
       v                      v                      v
   TF-IDF +              VADER              Urgency Rules
   Classifier            Sentiment              Priority
       |                      |                      |
       +----------------------+----------------------+
                              |
                              v
                         Gemini LLM
                              |
              +---------------+----------------+
              |               |                |
          Root Cause      Recommended      Customer
                           Action           Response
              |               |                |
              +---------------+----------------+
                              |
                              v
                    IntelliResolve Result
                              |
             +----------------+----------------+
             |                |                |
             v                v                v
         Streamlit         SQLite          Analytics
             UI             History          Dashboard
```

---

## 5. NLP Pipeline

### Text Preprocessing
- Lowercase conversion
- URL removal
- Non-alphabetic character removal
- Whitespace normalization

### Complaint Classification

TF-IDF features are combined with Logistic Regression.

Current categories include:

- Billing
- Delivery
- Product
- Account
- Technical
- Refund
- Service
- Other

### Sentiment Analysis

VADER produces a compound sentiment score and classifies complaints as:

- Positive
- Neutral
- Negative

### Urgency Detection

Rule-based detection identifies terms such as:

- urgent
- immediately
- blocked
- fraud
- unauthorized
- security
- stolen
- charged twice

Priority levels:

- Normal
- High
- Critical

### Keyword Extraction

TF-IDF is used to identify important words and phrases from individual complaints.

---

## 6. Generative AI Integration

IntelliResolve integrates the Google Gemini API.

The LLM receives:

- Original complaint
- Predicted category
- Sentiment
- Priority
- Extracted keywords

It generates:

- Root cause
- Recommended action
- Professional customer response
- Escalation decision and explanation
- Missing information

The prompt instructs the model not to invent facts, promise refunds or compensation, claim that an action has already been completed, or assume information that was not provided.

---

## 7. Technology Stack

| Component | Technology |
|---|---|
| Language | Python |
| UI | Streamlit |
| Data Processing | Pandas |
| NLP/ML | Scikit-learn |
| Features | TF-IDF |
| Classification | Logistic Regression |
| Sentiment | VADER |
| Generative AI | Google Gemini API |
| LLM SDK | Google GenAI |
| Database | SQLite |
| Configuration | YAML |
| Environment Variables | python-dotenv |
| Visualization | Plotly |
| Model Serialization | Joblib |
| Version Control | Git + GitHub |

---

## 8. Repository Structure

```text
MUJ-DS-23FE10CDS00409/
├── README.md
├── app.py
├── config.yaml
├── requirements.txt
├── train_model.py
├── predict.py
├── assignments/
├── notebooks/
├── code/
├── resources/
│   ├── screenshots/
│   └── results/
├── presentations/
├── data/
├── models/
├── prompts/
├── src/
└── tests/
```

The repository structure follows the Batch F capstone guideline requiring README, assignments, notebooks, code, resources, presentations and capstone/project materials.

---

## 9. Installation

### Prerequisites

- Python 3.9+
- Git
- GitHub account
- Google Gemini API key

### Clone

```bash
git clone https://github.com/nikhligit2604/MUJ-DS-23FE10CDS00409.git
cd MUJ-DS-RegNo
```

The personal repository name is `MUJ-DS-23FE10CDS00409`.

### Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Dependencies

```bash
pip install -r requirements.txt
```

---

## 10. Environment Configuration

Create `.env` in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

Never commit `.env` to GitHub. The repository includes `.env.example` as a safe template.

---

## 11. Train the Model

```bash
python train_model.py
```

The trained classifier is stored locally as:

```text
models/complaint_classifier.pkl
```

---

## 12. Run the Application

```bash
streamlit run app.py
```

The application contains:

### Analyze Complaint
Analyze an individual complaint using the hybrid NLP + Gemini pipeline.

### Batch Analysis
Upload a CSV containing a `text` or `complaint` column and analyze multiple complaints.

### Complaint History
Review complaints stored in SQLite.

### Analytics
View category, sentiment and priority patterns.

---

## 13. Example

```text
My package has been delayed for five days.
The tracking information has not been updated
and customer support has not responded.
I am extremely frustrated.
```

The system analyzes category, sentiment, priority and keywords, then uses Gemini to provide root cause, recommended action, customer response, escalation guidance and missing information.

---

## 14. Testing

Run the available tests:

```bash
python test_setup.py
python test_sentiment.py
python test_urgency.py
python test_keywords.py
python test_analyzer.py
python test_database.py
python test_llm.py
```

Check application syntax with:

```bash
python -m py_compile app.py
```

---

## 15. Results and Evaluation

The classification model can be evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Classification report

Operational outputs include:

- Complaint category
- Sentiment
- Priority
- Keywords
- AI-generated analysis
- Complaint history
- Batch results
- Analytics

Final numerical results should be updated after the final training run.

---

## 16. Screenshots and Results

Store project screenshots under:

```text
resources/screenshots/
```

Recommended screenshots:

1. Analyze Complaint page
2. Individual analysis result
3. Batch Analysis
4. Complaint History
5. Analytics Dashboard
6. GitHub repository
7. Successful application execution

Store final evaluation outputs under:

```text
resources/results/
```

---

## 17. GitHub Workflow

The project uses Git and GitHub throughout development.

Recommended workflow:

```text
Feature Branch
      |
Development
      |
Commit
      |
Push
      |
Pull Request
      |
Review
      |
Merge into main
```

GitHub Issues can track:

- Dataset Collection
- Model Development
- Testing
- Documentation
- Deployment

---

## 18. Limitations

- Classification performance depends on dataset quality and size.
- Rule-based urgency detection may not capture every urgent case.
- VADER may not capture every domain-specific sentiment expression.
- Gemini responses depend on API availability and model behavior.
- AI-generated outputs should be reviewed by humans before consequential customer actions.

---

## 19. Future Enhancements

- Larger and more diverse datasets
- Transformer-based classification
- Multilingual complaint support
- Email/ticket integration
- RAG using company policies
- Complaint trend forecasting
- Human-in-the-loop approval
- Authentication and role-based access
- Cloud deployment
- Advanced LLM response evaluation

---

## 20. Deliverables

The repository is intended to contain:

- Source code
- NLP/ML implementation
- Gemini API integration
- Prompt configuration
- Tests
- Dataset
- Documentation
- Screenshots
- Results
- Presentation materials
- Installation and execution instructions

---

## 21. Academic Information

**University:** Manipal University Jaipur  
**Program:** B.Tech Computer Science and Data Science  
**Batch:** F  
**Project:** IntelliResolve – AI-Powered Customer Complaint Intelligence  
**GitHub Username:** nikhligit2604
**Registration Number:** 23FE10CDS00409

---

## 22. Acknowledgement

This project was developed as part of the Batch F NLP Capstone Project and demonstrates the integration of traditional NLP, machine learning, database storage, web application development and Generative AI.
