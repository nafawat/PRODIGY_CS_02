from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Encrypt the image by adding the key to each pixel value
    encrypted_array = img_array + key
    encrypted_array = np.clip(encrypted_array, 0, 255)  # Ensure pixel values stay within 0-255
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Decrypt the image by subtracting the key from each pixel value
    decrypted_array = img_array - key
    decrypted_array = np.clip(decrypted_array, 0, 255)  # Ensure pixel values stay within 0-255
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    print("Image Encryption Tool")
    image_path = input("Enter the path of the image to encrypt: ")
    output_encrypted_path = input("Enter the output path for the encrypted image: ")
    output_decrypted_path = input("Enter the output path for the decrypted image: ")
    key = int(input("Enter a key (integer value for pixel manipulation): "))

    # Encrypt the image
    encrypt_image(image_path, output_encrypted_path, key)  # Pass the key here

    # Decrypt the image
    decrypt_image(output_encrypted_path, output_decrypted_path, key)

if __name__ == "__main__":
    main()