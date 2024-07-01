from PIL import Image
from sys import exit

def hide_image(cover_path, secret_path, output_path):
    cover_image = Image.open(cover_path)
    secret_image = Image.open(secret_path)

    if cover_image.size[0] < secret_image.size[0] or cover_image.size[1] < secret_image.size[1]:
        raise ValueError("Cover image is too small to hold the secret image")

    cover_image = cover_image.convert("RGBA")
    secret_image = secret_image.convert("RGBA")

    cover_pixels = cover_image.load()
    secret_pixels = secret_image.load()

    for y in range(secret_image.size[1]):
        for x in range(secret_image.size[0]):
            cover_pixel = cover_pixels[x, y]
            secret_pixel = secret_pixels[x, y]

            new_pixel = (
                (cover_pixel[0] & 0xFE) | (secret_pixel[0] >> 7),
                (cover_pixel[1] & 0xFE) | (secret_pixel[1] >> 7),
                (cover_pixel[2] & 0xFE) | (secret_pixel[2] >> 7),
                cover_pixel[3]
            )

            cover_pixels[x, y] = new_pixel

    cover_image.save(output_path, "PNG")

def reveal_image(stego_image_path, output_path, size):
    stego_image = Image.open(stego_image_path)
    stego_image = stego_image.convert("RGBA")

    revealed_image = Image.new("RGBA", size)
    revealed_pixels = revealed_image.load()
    stego_pixels = stego_image.load()

    for y in range(size[1]):
        for x in range(size[0]):
            stego_pixel = stego_pixels[x, y]

            revealed_pixel = (
                (stego_pixel[0] & 1) << 7,
                (stego_pixel[1] & 1) << 7,
                (stego_pixel[2] & 1) << 7,
                255
            )

            revealed_pixels[x, y] = revealed_pixel

    revealed_image.save(output_path, "PNG")

def hide_text_in_image(cover_path, text, output_path):
    cover_image = Image.open(cover_path)
    cover_image = cover_image.convert("RGBA")
    cover_pixels = cover_image.load()

    text_binary = ''.join(format(ord(char), '08b') for char in text)
    text_len = len(text_binary)

    if cover_image.size[0] * cover_image.size[1] * 3 < text_len:
        raise ValueError("Cover image is too small to hold the secret text")

    index = 0
    for y in range(cover_image.size[1]):
        for x in range(cover_image.size[0]):
            cover_pixel = cover_pixels[x, y]

            if index < text_len:
                new_pixel = (
                    (cover_pixel[0] & 0xFE) | int(text_binary[index]),
                    cover_pixel[1],
                    cover_pixel[2],
                    cover_pixel[3]
                )
                index += 1
            else:
                new_pixel = cover_pixel

            if index < text_len:
                new_pixel = (
                    new_pixel[0],
                    (cover_pixel[1] & 0xFE) | int(text_binary[index]),
                    new_pixel[2],
                    new_pixel[3]
                )
                index += 1

            if index < text_len:
                new_pixel = (
                    new_pixel[0],
                    new_pixel[1],
                    (cover_pixel[2] & 0xFE) | int(text_binary[index]),
                    new_pixel[3]
                )
                index += 1

            cover_pixels[x, y] = new_pixel

    cover_image.save(output_path, "PNG")

def unhide_text_in_image(stego_image_path):
    stego_image = Image.open(stego_image_path)
    stego_image = stego_image.convert("RGBA")
    stego_pixels = stego_image.load()

    binary_data = ""
    for y in range(stego_image.size[1]):
        for x in range(stego_image.size[0]):
            stego_pixel = stego_pixels[x, y]
            binary_data += str(stego_pixel[0] & 1)
            binary_data += str(stego_pixel[1] & 1)
            binary_data += str(stego_pixel[2] & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_text = ""
    for byte in all_bytes:
        decoded_text += chr(int(byte, 2))
        if decoded_text.endswith("###"):
            break

    if "###" in decoded_text:
        return decoded_text.rstrip("###")
    else:
        return ""

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        return width, height

def main():
    print("-"*100)
    print("Choose an option:")
    print("1. Hide an image")
    print("2. Reveal an image")
    print("3. Hide text in image")
    print("4. Unhide hidden text in image")
    print("5. Exit")
    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
    if choice == "1":
        cover_path = input("Enter the path to the cover image: ")
        secret_path = input("Enter the path to the secret image: ")
        output_path = input("Enter the path to save the output image: ")
        hide_image(cover_path, secret_path, output_path)
        print("Image hiding process complete.")
    elif choice == "2":
        stego_image_path = input("Enter the path to the stego image: ")
        output_path = input("Enter the path to save the revealed image: ")
        width, height = get_image_dimensions(stego_image_path)
        reveal_image(stego_image_path, output_path, (width, height))
        print("Image revealing process complete.")
    elif choice == "3":
        cover_path = input("Enter the path to the cover image: ")
        text = input("Enter the text to hide: ") + "###"  # Adding delimiter to indicate end of hidden text
        output_path = input("Enter the path to save the output image: ")
        hide_text_in_image(cover_path, text, output_path)
        print("Text hiding process complete.")
    elif choice == "4":
        stego_image_path = input("Enter the path to the stego image: ")
        hidden_text = unhide_text_in_image(stego_image_path)
        if(hidden_text!=""):
            print(f"Hidden text: {hidden_text}")
        else:
            print("No hidden text found.")
    elif choice == "5":
        exit(0)
    else:
        print("Invalid choice.")

while True:
    main()
