## 🧠 AI-Based Invention vs Prior Art Similarity & Coverage Analyzer

### 📌 Overview

This project is an **AI-assisted analysis tool** designed to evaluate how well a given **prior art document (patent or research paper)** covers the **key features of an invention**. Instead of performing full patentability analysis or automatically discovering prior art, the system focuses on a **more controlled and reliable task**: measuring **semantic similarity and feature-level coverage** between two inputs.

The goal is to provide a **transparent, explainable, and measurable comparison** that helps users understand:

* Which parts of an invention are already disclosed
* Which features are missing
* How strong the overlap is between the invention and the prior art

---

### ⚙️ Key Functionalities

* **Feature Extraction from Invention**
  The system processes the input invention and breaks it down into **individual features or elements** for structured comparison.

* **Semantic Similarity Analysis**
  Using embedding-based techniques, the system computes:

  * Overall similarity between invention and prior art
  * Feature-level similarity scores

* **Feature-wise Coverage Mapping (Core Component)**
  Each invention feature is mapped against the prior art and classified as:

  * **Covered** (strong match)
  * **Partially Covered** (moderate match)
  * **Not Covered** (weak or no match)

* **Coverage Score Calculation**
  A quantitative metric representing how much of the invention is disclosed:

  ```
  Coverage (%) = (Number of matched features / Total features) × 100
  ```

* **Missing Feature Identification**
  Clearly highlights which elements of the invention are **not present** in the prior art.

* **Explainable Output (LLM-Assisted)**
  Generates concise explanations based strictly on similarity results, ensuring **minimal hallucination** and improved interpretability.

---

### 📄 Output Structure

The system generates a structured report containing:

* **Overall Similarity Score**
* **Coverage Percentage**
* **Feature-wise Mapping Table**
* **List of Missing Features**
* **Short Explanation of Overlap and Gaps**

---

### 🚀 Motivation

Traditional patent analysis is **time-consuming and highly manual**, requiring detailed comparison of technical features across documents. This project aims to:

* Assist in **faster preliminary analysis**
* Provide **data-driven similarity insights**
* Enable **feature-level transparency** in comparisons
* Serve as a supporting tool for researchers, analysts, and students

---

### 🛠️ Tech Stack

* **Language:** Python
* **Embeddings:** Sentence Transformers
* **Vector Search (Optional):** FAISS
* **LLM (for explanation):** OpenAI / Groq / similar APIs
* **Frontend (Optional):** Streamlit

---

### ⚠️ Limitations

* This system **does NOT perform legal patentability analysis**
* It **does NOT automatically determine novelty or inventive step**
* Results are based on **semantic similarity**, not legal standards
* Intended for **assistance and exploration**, not final decision-making

---

### 💡 Key Highlights

* Focuses on a **well-defined, solvable problem**
* Emphasizes **explainability over black-box AI**
* Avoids unreliable “AI guessing” by grounding outputs in similarity scores
* Designed to be **practical, testable, and interview-ready**

---

### 🎯 Use Cases

* Preliminary prior art comparison
* Research and academic analysis
* Learning tool for patent feature mapping
* AI-assisted document comparison workflows

---

This project demonstrates how **AI can be applied in a controlled and reliable way** to support complex technical analysis tasks without overclaiming capabilities.
