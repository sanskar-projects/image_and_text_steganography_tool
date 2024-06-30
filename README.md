### Project Description

#### Overview

This Python project implements a simple steganography tool using the Pillow library. The project allows users to hide one image inside another (cover image) and then retrieve the hidden image. The project features a command-line user interface for ease of use.

#### Features

1. **Hide Image**:
    - **Input**: Cover image path, secret image path, and output image path.
    - **Process**: The secret image is hidden inside the cover image by modifying the least significant bits (LSBs) of the cover image's pixels to store the secret image's pixel data.
    - **Output**: A new image file with the hidden image embedded.

2. **Reveal Image**:
    - **Input**: Stego image path (image with the hidden content), output image path, and the size of the hidden image.
    - **Process**: The hidden image is extracted from the stego image by retrieving the least significant bits (LSBs) of the stego image's pixels.
    - **Output**: The revealed hidden image saved as a new file.

#### Functions

1. **hide_image(cover_path, secret_path, output_path)**:
    - This function takes the path of the cover image, the path of the secret image, and the path where the output image will be saved.
    - It ensures that the cover image is large enough to contain the secret image.
    - It then hides the secret image in the cover image by manipulating the LSBs of the cover image's pixels.
    - Finally, it saves the modified cover image as the output image.

2. **reveal_image(stego_image_path, output_path, size)**:
    - This function takes the path of the stego image (cover image with the hidden content), the path where the revealed image will be saved, and the size of the hidden image.
    - It extracts the hidden image from the stego image by reading the LSBs of the stego image's pixels.
    - The revealed image is then saved as a new file.

3. **get_image_dimensions(image_path)**:
    - This helper function takes the path of an image file and returns its width and height.

#### User Interface

The user interface is a simple command-line menu that allows users to choose between hiding an image, revealing an image, or exiting the program. It prompts the user for the necessary file paths and then calls the appropriate function to perform the requested operation.

#### Usage

1. **Run the Program**:
   - Execute the script to start the command-line interface.
   
2. **Choose an Option**:
   - `1`: Hide an image
   - `2`: Reveal an image
   - `3`: Exit

3. **Follow Prompts**:
   - For hiding an image, provide the cover image path, secret image path, and output image path.
   - For revealing an image, provide the stego image path and output image path. The script will determine the size of the hidden image.

This project has been developed with the help of artificial intelligence.
