# AI Fashion Design Generator

## Overview

AI Fashion Design Generator is an intelligent fashion generation system that combines prompt engineering, ControlNet, CLIP evaluation, semantic retrieval, and brand-aware style generation.

## Features

### Week 1

* Fashion dataset exploration
* Dataset preprocessing

### Week 2

* Prompt engineering
* Stable Diffusion image generation
* CLIP similarity evaluation

### Week 3

* ControlNet integration
* Sketch-to-design generation
* Pose-guided generation
* Depth-guided generation
* Controlled vs uncontrolled comparison

### Week 4

* Brand-aware prompt generation
* Multiple fashion brand styles
* Luxury, athletic and casual fashion presets
* CLIP quality evaluation

### Week 5

* Fashion knowledge base
* Sentence Transformer embeddings
* ChromaDB vector storage
* Semantic similarity search
* Intelligent fashion recommendations

## Tech Stack

* Python
* Hugging Face Inference API
* FLUX.1-schnell
* Sentence Transformers
* ChromaDB
* CLIP
* ControlNet
* Stable Diffusion

## Project Structure

```
fashion/
│
├── image_generator.py
├── prompt_builder.py
├── clip_scorer.py
├── embeddings.py
├── vector_store.py
├── controlnet_demo.py
├── sketch_extractor.py
├── fashion_data.py
├── generated_jacket_navy.png
├── controlled.png
├── uncontrolled.png
├── README.md
├── week3_report.md
├── week4_report.md
└── week5_report.md
```

## Future Improvements

* LoRA fine-tuning on custom fashion datasets
* Larger fashion recommendation database
* User wardrobe personalization
* Interactive Gradio interface
* Trend forecasting module
