# Ghost Image Project

This repository contains the implementation of the Stanford CS106A Ghost Project. The project blends multiple images to create a "ghost" image by averaging the pixel colors at each position. The script supports two blending modes: a simple average mode and a more refined "good apple" strategy.

## Features

- Color Distance Calculation: Computes the Euclidean distance between two color tuples.
- Average Color Calculation: Computes the average color from a list of color tuples.
- Best Color Selection: Selects the best color based on the average color.
- Good Apple Strategy: Selects the best color using a more refined sorting strategy.
- Image Loading: Loads all .jpg images from a specified directory.
- Ghost Image Generation: Creates a ghost image by blending the input images based on the specified mode.

## Dependencies

- Python 3.x
- Pillow library (for image manipulation)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ghost-image-project.git
    cd ghost-image-project
    ```

2. Install the dependencies:

    ```bash
    pip install Pillow
    ```

## Usage

Run the script with a directory of images:

```bash
python ghost_image.py <directory_of_images>
