---
title: "Phi-3.5-Mini-Instruct: Specs, Architecture, and Evolution"
source: "Web Search Synthesis"
date_added: 2026-05-05
tags: [autoresearch, phi-3.5-mini, slm, microsoft]
aliases: []
status: draft
summary: "Tổng hợp thông số kỹ thuật, kiến trúc và sự khác biệt giữa Phi-3.5-Mini và Phi-3-Mini."
confidence: high
---

### Phi-3.5-Mini-Instruct Overview
Phi-3.5-Mini-Instruct is a lightweight, high-performance small language model developed by Microsoft, designed for efficient deployment in resource-constrained environments while maintaining competitive reasoning and generation capabilities.

### Technical Specifications
*   **Architecture:** Dense decoder-only Transformer.
*   **Parameters:** 3.8 Billion.
*   **Context Length:** 128K tokens (supports long-context tasks like document/meeting summarization and long-document QA).
*   **Training Data:** High-quality, reasoning-dense synthetic data ("textbook-quality") and filtered publicly available websites.
*   **Training Techniques:** Supervised fine-tuning (SFT), proximal policy optimization (PPO), and direct preference optimization (DPO) for improved instruction adherence and safety.
*   **License:** MIT License.

### Key Capabilities & Performance
*   **Reasoning & Coding:** Optimized for complex reasoning, mathematical problem-solving, and code generation. It demonstrates significant advancements over the previous Phi-3 generation.
*   **Multilingual Support:** Enhanced capabilities across more than 20 languages.
*   **Competitive Benchmarking:** Despite its small size, it frequently outperforms or matches significantly larger models (such as Llama-3.1-8B-Instruct or Mistral-7B-Instruct-v0.3) on various benchmarks, particularly in long-context understanding tasks (e.g., RepoQA).
*   **Efficiency:** Designed for edge deployment, requiring minimal RAM (approx. 3.5GB+) and providing low-latency inference.
*Note: Some sources may reference a 4K context window depending on specific quantization or hardware-optimized deployment configurations, but the base model architecture supports up to 128K tokens.*

### Evolution: Phi-3.5-Mini vs Phi-3-Mini
Phi-3.5-Mini represents an evolution over the original Phi-3-Mini, primarily driven by enhancements in its training methodology and data rather than a fundamental change in architecture. The core differences are:
*   **Additional Continual Pre-training:** Phi-3.5-Mini underwent further continual pre-training beyond what was used for Phi-3-Mini, specifically utilizing additional multilingual synthetic data and high-quality filtered datasets.
*   **Enhanced Post-Training:** A significant differentiator is the rigorous post-training process. This involved a combination of Supervised Fine-Tuning (SFT), Proximal Policy Optimization (PPO), and Direct Preference Optimization (DPO). These steps utilized a mix of human-labeled, synthetic, and translated datasets designed to improve instruction adherence, multi-turn conversation quality, and safety.
*   **Focus on Multilingualism and Reasoning:** While both models are built upon the foundational "textbook-quality" synthetic data and filtered public websites, Phi-3.5-Mini was explicitly optimized to improve multilingual performance and reasoning capabilities. This effort resulted in significant performance boosts across languages like Arabic, Dutch, Finnish, Polish, Thai, and Ukrainian.
*   **Consistency in Foundation:** Both models are dense decoder-only Transformer models with 3.8B parameters and use the same tokenizer. They share the underlying philosophy of prioritizing "reasoning-dense" data to maximize the capability of a smaller model.
