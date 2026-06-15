# Week 3 Report – Style Control & Workflow Exploration

## Objective

Explore style-control techniques for fashion image generation and evaluate their impact using CLIP-based scoring.

---

## Tasks Completed

### Sketch Extraction

Generated an edge-map sketch from a fashion image using OpenCV Canny edge detection.

Output:

* `jacket_sketch.png`

### Depth Map Generation

Generated a depth-style representation of the garment image.

Output:

* `jacket_depth.png`

### Pose Map Generation

Generated a contour-based pose representation.

Output:

* `jacket_pose.png`

### Controlled Generation

Created multiple guided image generation strategies:

* Uncontrolled
* Controlled Prompt
* Sketch-guided
* Depth-guided
* Pose-guided

### Evaluation

Used CLIP to measure image-text alignment.

---

## Results

| Method        | Score | Rating  |
| ------------- | ----: | ------- |
| Uncontrolled  | 22.80 | Poor    |
| Controlled    | 30.14 | Good    |
| Sketch-guided | 25.79 | Average |
| Depth-guided  | 27.84 | Average |
| Pose-guided   | 31.38 | Good    |

### Improvements

* Controlled vs Uncontrolled: +7.34
* Sketch-guided vs Uncontrolled: +2.99
* Depth-guided vs Uncontrolled: +5.05
* Pose-guided vs Uncontrolled: +8.58

---

## Key Findings

Guided generation methods consistently outperformed uncontrolled generation.

Among all approaches, pose-guided generation achieved the highest CLIP score, indicating stronger alignment with the target fashion prompt.

---

## Limitations

The project generated sketch, depth, and pose control maps but did not perform full ControlNet conditioning or ControlNet fine-tuning due hardware limitations.

---

## Conclusion

The experiments demonstrate that introducing structural guidance improves fashion image generation quality and prompt alignment.

The developed workflow provides a foundation for future ControlNet integration and fashion-specific model training.
