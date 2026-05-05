---
title: "Ollama Architecture and Core Components"
source: "Web Search (compiled)"
date_added: 2026-05-05
tags: [autoresearch, ollama, architecture, llm]
aliases: [Ollama Architecture]
status: draft
summary: "Tổng quan về kiến trúc client-server, C++ inference engine và quản lý bộ nhớ động của Ollama."
confidence: high
---

Ollama uses a lightweight, client-server architecture designed to make running large language models (LLMs) locally as simple as possible. Its design is heavily inspired by containerization tools like Docker.

### Core Architectural Components

*   **Client-Server Model:**
    *   **Ollama Server (Daemon):** A background service (written in Go) that manages the model lifecycle, handles API requests, manages system memory, and interfaces with the inference engine.
    *   **Ollama Client:** The interface used to interact with the server. This includes the CLI (`ollama run`), language-specific SDKs (Python, JavaScript), and third-party integrations connecting via a REST API.
*   **Inference Engine (llama.cpp):** The heart of Ollama’s execution layer is a highly optimized version of `llama.cpp` (written in C/C++). Ollama acts as a wrapper that abstracts the complexity of hardware utilization.
    *   **Hardware Acceleration:** It automatically detects and utilizes appropriate compute APIs, such as Metal Performance Shaders (MPS) for Apple Silicon, CUDA for Nvidia GPUs, and ROCm for AMD GPUs.
*   **GGUF Format:** Ollama uses the GGUF (GPT-Generated Unified Format) for models. This format is optimized for fast loading (using `mmap`) and supports quantization (e.g., 4-bit, 8-bit), which significantly reduces RAM/VRAM requirements.
*   **Model Management (Modelfiles):** Similar to a Dockerfile, Ollama uses a declarative `Modelfile` to define and configure models, including system prompts and parameters.

### Key Operational Features

*   **Dynamic Memory Management:** Before loading a model, the Ollama daemon checks available VRAM and system RAM. If a model is too large for the GPU, it intelligently performs "layer offloading," sending as many layers as possible to the GPU and keeping the rest in CPU/System RAM.
*   **Layered Storage:** Ollama stores model data efficiently. If multiple models share the same base weights, the underlying file data is not duplicated on the disk.
*   **Stateless Server:** Models are loaded into memory on demand and are typically unloaded after a period of inactivity (defaulting to 5 minutes) to free up system resources.
*   **Process Isolation:** The inference engine runs in a separate process from the main server, ensuring that if an inference task crashes, it does not take down the entire Ollama service.
