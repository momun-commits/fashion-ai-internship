# Fashion AI Design System

## Overview

This project explores AI-assisted fashion design workflows using image generation, prompt engineering, CLIP evaluation, and style-control techniques.

The system generates fashion product images from text prompts and evaluates image-text alignment using CLIP scores.

---

## Technologies Used

* Python
* Hugging Face Inference API
* FLUX.1-schnell
* OpenCV
* Transformers
* CLIP
* PIL

---

## Week 1: Data & Embeddings

* Fashion data exploration
* Embedding generation
* Vector storage concepts

---

## Week 2: Image Generation & Evaluation

* Fashion image generation using FLUX
* Prompt engineering
* CLIP-based image evaluation

---

## Week 3: Style Control & Workflow Exploration

### Implemented

* Sketch extraction using OpenCV
* Depth map extraction
* Pose map extraction
* Controlled image generation
* CLIP-based comparison

### Results

| Method        | CLIP Score |
| ------------- | ---------: |
| Uncontrolled  |      22.80 |
| Controlled    |      30.14 |
| Sketch-guided |      25.79 |
| Depth-guided  |      27.84 |
| Pose-guided   |      31.38 |

Best result: **Pose-guided generation (31.38)**

---

## Project Files

* `controlnet_demo.py`
* `sketch_extractor.py`
* `week3_comparison.py`
* `clip_scorer.py`

---

## Future Work

* Full ControlNet integration
* Fashion sketch conditioning
* ControlNet fine-tuning on fashion datasets
* Real-time designer workflow support
