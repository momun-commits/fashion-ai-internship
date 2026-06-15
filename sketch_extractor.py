import cv2
import numpy as np
from PIL import Image

def extract_edges(image_path: str, output_path: str) -> str:
    """Extract edge map (sketch) from an image using Canny edge detection."""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, threshold1=30, threshold2=100)
    sketch = cv2.bitwise_not(edges)
    cv2.imwrite(output_path, sketch)
    print(f"✅ saved {output_path}")
    return output_path

def extract_depth(image_path: str, output_path: str) -> str:
    """Simulate depth map using Laplacian gradient (dark=far, bright=near)."""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Blur heavily — depth maps are smooth
    depth = cv2.GaussianBlur(gray, (21, 21), 0)
    
    # Normalize to full 0-255 range
    depth = cv2.normalize(depth, None, 0, 255, cv2.NORM_MINMAX)
    
    # Apply colormap — blue=far, red=near (standard depth visualization)
    depth_colored = cv2.applyColorMap(depth.astype(np.uint8), cv2.COLORMAP_MAGMA)
    
    cv2.imwrite(output_path, depth_colored)
    print(f"✅ saved {output_path}")
    return output_path

def extract_pose(image_path: str, output_path: str) -> str:
    """Simulate pose map using contour detection (approximates body structure)."""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Threshold to isolate garment shape
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours — approximates pose/body outline
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw on black background (standard pose map style)
    pose_map = np.zeros_like(img)
    cv2.drawContours(pose_map, contours, -1, (0, 255, 0), 2)
    
    cv2.imwrite(output_path, pose_map)
    print(f"✅ saved {output_path}")
    return output_path

if __name__ == "__main__":
    print("Extracting all control maps...")
    extract_edges("generated_jacket_navy.png", "jacket_sketch.png")
    extract_depth("generated_jacket_navy.png", "jacket_depth.png")
    extract_pose("generated_jacket_navy.png", "jacket_pose.png")
    print("\n✅ All control maps extracted")