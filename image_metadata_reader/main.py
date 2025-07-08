# Import required modules
from PIL import Image        # Pillow module for image processing
import os                    # OS module for file handling

# Define a function to read and print metadata of an image
def read_image_metadata(file_path):
    # Check if the file actually exists
    if not os.path.isfile(file_path):
        print("❌ File does not exist. Please check the file path.")
        return

    try:
        # Open the image file using PIL's Image module
        with Image.open(file_path) as img:
            # Print a header
            print("🖼️ Image Metadata:")
            
            # Print the name of the file (just the last part of the path)
            print("📄 Filename:", os.path.basename(file_path))
            
            # Print the size of the file in bytes
            print("📦 File size:", os.path.getsize(file_path), "bytes")
            
            # Print the image format (e.g., JPEG, PNG)
            print("🗂️ Format:", img.format)
            
            # Print the color mode (e.g., RGB, L, CMYK)
            print("🎨 Mode:", img.mode)
            
            # Print the dimensions of the image as a tuple (width, height)
            print("📐 Dimensions:", img.size)

    except Exception as e:
        # Handle any error while opening or reading the image
        print("⚠️ Error reading image:", e)


# ----------------------------
# Run the function with an example image path
# You can change "sample.jpg" to any image file you have in the same folder
# ----------------------------

# Example usage
if __name__ == "__main__":
    # Ask user to enter the image file name
    file_name = input("Enter image file name (with extension): ")

    # Call the function with the file name provided by the user
    read_image_metadata(file_name)
