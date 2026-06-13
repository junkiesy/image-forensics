# AI Image Forensics Lab

A local web application for studying, comparing, and detecting AI-generated images.

## Project Purpose

This project is a local AI image forensics lab. It helps users compare real and AI-generated images, inspect visual and pixel-level differences, extract useful forensic features, and eventually train an AI-vs-real image identifier.

## Main Modules

### 1. Forensic Comparison Lab

Compare real and AI images side by side. Inspect visual differences, zoom into image regions, and analyze possible forensic clues.

### 2. Feature and Training Builder

Convert discovered forensic patterns into labeled data, extracted features, and training inputs for an AI-real image identifier.

### 3. AI-Real Detector

Upload an image and receive a prediction showing whether the image is likely real or AI-generated, with a confidence score and supporting indicators.

## Tech Stack

- Frontend: React, TypeScript, Vite
- Backend: Python, FastAPI
- Image Processing: Pillow, OpenCV, NumPy, scikit-image
- Machine Learning: scikit-learn, PyTorch or TensorFlow later
- Testing: pytest

## Dataset Policy

Datasets are stored locally in:

- `datasets/real/`
- `datasets/ai/`

Large image datasets should not be committed to GitHub.

## Development Status

Initial project setup.