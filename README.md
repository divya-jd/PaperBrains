# 🧾 PaperBrains – Intelligent Multimodal Document Understanding

PaperBrains is an AI-driven **document intelligence system** that combines the power of **OCR, Vision Transformers, and Large Language Models (LLMs)** to read, interpret, and summarize complex business documents such as **invoices, claim forms, and financial reports**.

It transforms unstructured visual data into structured insights — automating what traditionally required manual review.

## Project Overview

PaperBrains mimics how humans read documents:

**Sees the document** — using Vision Transformers and CLIP to understand layout and visual cues.

**Reads the text** — using OCR (Tesseract) to extract text accurately from PDFs or images.

**Thinks and summarizes** — using an LLM (like GPT-4 or Claude) to generate structured summaries, key entities, or responses to queries.

This architecture enables multimodal reasoning — where both text and visuals contribute to understanding the document holistically.

## Features

> **OCR-based text extraction** via pytesseract

> **Vision-Language embeddings** using CLIP or BLIP

> **LLM-powered contextual understanding** for summaries & Q&A

> **FastAPI backend** for real-time document intelligence API

> **Batch pipeline support** for processing multiple documents

> **Evaluation framework** for extraction accuracy and latency

## Setup & Installation

git clone https://github.com/divya-jd/PaperBrains.git
cd PaperBrains

python3 -m venv venv
source venv/bin/activate    (for macOS/Linux)
venv\Scripts\activate (for windows)

pip install -r requirements.txt

## Architecture Diagram

Document Image
      
 [ OCR - Tesseract ] -> [ CLIP - Visual Embeddings ] -> [ LLM (GPT-4) Summarizer ] -> Structured Insights (JSON)

## Tech Stack

| Category            | Tools                           |
| ------------------- | ------------------------------- |
| **OCR**             | Tesseract, pytesseract          |
| **Vision Models**   | CLIP, BLIP, Vision Transformers |
| **LLM Integration** | OpenAI GPT, LangChain           |
| **Backend**         | FastAPI                         |
| **Data**            | PNG, JPG, PDF                   |
| **Deployment**      | Docker, AWS Lambda (optional)   |

## Example API Response
{
  "entities": {
    "invoice_number": "INV-2025-0043",
    "client": "TechNova Inc",
    "total": "$5,120"
  },
  "summary": "Invoice INV-2025-0043 for TechNova Inc. Total billed amount: $5,120 due within 30 days.",
  "confidence_score": 0.96
}

## Future Improvements

> Add table structure extraction using LayoutLMv3

> Fine-tune multimodal models for document-specific datasets

> Deploy scalable inference via AWS Lambda + S3

> Integrate human feedback loops for continual learning

**AUTHOR**
Velankani Joise Divya G C
