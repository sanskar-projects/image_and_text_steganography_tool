from PIL import Image
from sys import exit

def hide_image(cover_path, secret_path, output_path):
    # Load the cover and secret images
    cover_image = Image.open(cover_path)
    secret_image = Image.open(secret_path)

    # Ensure the cover image is large enough to hold the secret image
    if cover_image.size[0] < secret_image.size[0] or cover_image.size[1] < secret_image.size[1]:
        raise ValueError("Cover image is too small to hold the secret image")

    # Convert images to RGBA if they are not
    cover_image = cover_image.convert("RGBA")
    secret_image = secret_image.convert("RGBA")

    # Get pixel data
    cover_pixels = cover_image.load()
    secret_pixels = secret_image.load()

    # Hide the secret image in the cover image
    for y in range(secret_image.size[1]):
        for x in range(secret_image.size[0]):
            # Get the RGBA values of the cover and secret images
            cover_pixel = cover_pixels[x, y]
            secret_pixel = secret_pixels[x, y]

            # Modify the LSBs of the cover image's pixels to hide the secret image's pixels
            new_pixel = (
                (cover_pixel[0] & 0xFE) | (secret_pixel[0] >> 7),
                (cover_pixel[1] & 0xFE) | (secret_pixel[1] >> 7),
                (cover_pixel[2] & 0xFE) | (secret_pixel[2] >> 7),
                cover_pixel[3]  # Preserve the alpha channel
            )

            cover_pixels[x, y] = new_pixel

    # Save the output image
    cover_image.save(output_path, "PNG")

def reveal_image(stego_image_path, output_path, size):
    # Load the stego image
    stego_image = Image.open(stego_image_path)

    # Convert the image to RGBA if it's not
    stego_image = stego_image.convert("RGBA")

    # Create a new image for the revealed secret
    revealed_image = Image.new("RGBA", size)
    revealed_pixels = revealed_image.load()

    # Get pixel data
    stego_pixels = stego_image.load()

    # Extract the secret image from the stego image
    for y in range(size[1]):
        for x in range(size[0]):
            # Get the pixel from the stego image
            stego_pixel = stego_pixels[x, y]

            # Extract the hidden data
            revealed_pixel = (
                (stego_pixel[0] & 1) << 7,
                (stego_pixel[1] & 1) << 7,
                (stego_pixel[2] & 1) << 7,
                255  # Set alpha to fully opaque
            )

            revealed_pixels[x, y] = revealed_pixel

    # Save the revealed secret image
    revealed_image.save(output_path, "PNG")

def get_image_dimensions(image_path):
    # Open the image
    with Image.open(image_path) as img:
        # Get the width and height
        width, height = img.size
        return width, height

def main():
    print("Choose an option:")
    print("1. Hide an image")
    print("2. Reveal an image")
    print("3. Exit")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        cover_path = input("Enter the path to the cover image: ")
        secret_path = input("Enter the path to the secret image: ")
        output_path = input("Enter the path to save the output image: ")
        hide_image(cover_path,secret_path,output_path)
        print("Image hiding process complete.")
    elif choice == "2":
        stego_image_path = input("Enter the path to the stego image: ")
        output_path = input("Enter the path to save the revealed image: ")
        width, height = get_image_dimensions(stego_image_path)
        reveal_image(stego_image_path,output_path,(width,height))
        print("Image revealing process complete.")
    elif choice == "3":
        exit(0)
    else:
        print("Invalid choice.")
