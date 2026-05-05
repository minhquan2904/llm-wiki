---
title: "Llama 3.2 3B Instruct Architecture and Specifications"
source: "Google Vertex Search Summary"
date_added: 2026-05-05
tags: [autoresearch, Llama-3.2-3B-Instruct, LLM]
aliases: []
status: draft
summary: "Tổng quan về thông số kỹ thuật, kiến trúc và khả năng của mô hình Llama 3.2 3B Instruct."
confidence: high
---

# Llama 3.2 3B Instruct architecture and specifications

*   **Model Size (Parameters):** Approximately 3 billion parameters.
*   **Architecture:** Auto-regressive transformer model utilizing optimized transformer architecture. It employs **Grouped-Query Attention (GQA)** to enhance inference scalability and performance.
*   **Context Window:** Supports a context length of **128,000 tokens**.
*   **Training & Alignment:**
    *   Pre-trained on up to 9 trillion tokens of data.
    *   Utilized knowledge distillation from larger Llama 3.1 models (8B and 70B) during pre-training to recover performance after pruning.
    *   Instruction-tuned using supervised fine-tuning (SFT) and reinforcement learning with human feedback (RLHF) to align with human preferences for safety and helpfulness.
*   **Intended Use:** Optimized for edge and mobile device deployment, suitable for assistant-like chat, agentic applications, knowledge retrieval, summarization, and prompt rewriting.
*   **Languages:** Officially supports English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai.
