## Project Description: Image and Text Steganography Tool

### Overview
This project provides a set of Python scripts that enable users to hide and reveal secret images and text within cover images using steganography techniques. Steganography is the practice of concealing messages or information within other non-secret text or data. The tool leverages the Python Imaging Library (PIL) to manipulate image pixels and embed secret data in an imperceptible way.

### Features
1. **Hide an Image within Another Image:**
   - Embed a secret image within a cover image.
   - Ensure the cover image is large enough to accommodate the secret image.
   - Modify the least significant bits (LSBs) of the cover image's pixels to encode the secret image's pixels.

2. **Reveal an Image from a Stego Image:**
   - Extract a hidden image from a stego image.
   - Use the size of the original secret image to correctly interpret and reconstruct the hidden image.

3. **Hide Text within an Image:**
   - Convert text to binary format and embed it within a cover image.
   - Use LSB modification to store text data in the cover image's pixel values.
   - Append a delimiter "###" to mark the end of the hidden text.

4. **Unhide Text from an Image:**
   - Extract and decode hidden text from a stego image.
   - Identify the end of the hidden text using the delimiter "###".
   - Return an appropriate message if no hidden text is found.

### Functions
- `hide_image(cover_path, secret_path, output_path)`: Embeds a secret image within a cover image and saves the output.
- `reveal_image(stego_image_path, output_path, size)`: Extracts a hidden image from a stego image and saves the revealed image.
- `hide_text_in_image(cover_path, text, output_path)`: Converts text to binary and embeds it within a cover image, saving the output.
- `unhide_text_in_image(stego_image_path)`: Extracts and decodes hidden text from a stego image, returning the text or an error message.
- `get_image_dimensions(image_path)`: Returns the dimensions (width, height) of an image.
- `main()`: Provides a command-line interface for users to choose between the available options: hide an image, reveal an image, hide text in an image, unhide text from an image, or exit the program.

### Usage
Upon running the script, the user is prompted to select an option from the main menu. Depending on the chosen option, the user will be asked to provide the necessary file paths and text inputs. The tool then performs the corresponding steganographic operation and provides feedback on the process completion.

### Example
- **Hide an Image:**
  - Input: Paths to cover image, secret image, and output image.
  - Process: Embeds the secret image into the cover image and saves the result.

- **Reveal an Image:**
  - Input: Path to stego image and output image.
  - Process: Extracts and saves the hidden image from the stego image.

- **Hide Text:**
  - Input: Path to cover image, text to hide, and output image.
  - Process: Embeds the text into the cover image and saves the result.

- **Unhide Text:**
  - Input: Path to stego image.
  - Process: Extracts and displays the hidden text or an error message if no text is found.

### Conclusion
This steganography tool is a practical implementation for hiding and revealing secret data within images. It serves as a useful demonstration of steganographic techniques and provides a hands-on approach for exploring data concealment within digital images.

This project has been developed with the help of generative artificial intelligence.
