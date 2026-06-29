# Week 4 Report – LoRA Fine-Tuning for Brand Style

## Objective

The objective of Week 4 was to incorporate brand-specific fashion styles into the image generation pipeline and generate garments following different brand aesthetics.

## Work Completed

### 1. Brand Style Presets

Created brand-specific style mappings for multiple fashion brands:

* Nike
* Gucci
* Zara
* H&M

Each brand was assigned unique style keywords and prompt modifiers.

### 2. Prompt Engineering

Extended the prompt generation pipeline by incorporating brand-specific descriptors into Stable Diffusion prompts.

Example:

**Input**

Brand: Gucci

Garment: Jacket

Color: Navy

Season: Autumn

**Generated Prompt**

A luxury designer navy jacket for women, autumn, premium fabric, embroidery, luxury editorial, flat lay product photography, overhead shot, clean white background, commercial fashion, garment only, highly detailed, high quality

### 3. Image Generation

Generated fashion images using the Hugging Face Inference API with the FLUX.1-schnell model.

### 4. Image Evaluation

Used CLIP similarity scoring to evaluate prompt-image alignment.

Result:

* CLIP Score: 33.73
* Quality: Good

## Technologies Used

* Python
* Hugging Face Inference API
* FLUX.1-schnell
* Prompt Engineering
* CLIP

## Outcome

Successfully generated brand-specific fashion images with improved prompt quality and evaluated them using CLIP similarity scores.
