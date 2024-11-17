import numpy as np
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# AES Encryption and Decryption Functions
def aes_encrypt(key, data):
    # Pad the data to be 16-byte aligned if necessary
    pad = 16 - len(data) % 16
    data += bytes([pad]) * pad  # Padding data

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

def aes_decrypt(key, encrypted_data):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remove padding after decryption
    pad = decrypted_data[-1]
    return decrypted_data[:-pad]

# Quantum-Inspired Key Generation Function
def generate_key():
    # Generate Gaussian distribution (mean=0, std=1)
    gaussian_values = np.random.normal(0, 1, 16)  # 16 bytes from Gaussian distribution
    
    # Generate Uniform distribution (values between 0 and 1)
    uniform_values = np.random.uniform(0, 1, 16)  # 16 bytes from Uniform distribution
    
    # Combine both to form the key (adding element-wise)
    key = gaussian_values + uniform_values
    key = (key * 255).astype(np.uint8)  # Scale and convert to 8-bit values
    
    return key.tobytes()  # Convert to bytes for AES key

# XOR Encryption/Decryption Function
def xor_encrypt(data, xor_key):
    return bytes([b ^ xor_key[i % len(xor_key)] for i, b in enumerate(data)])

# Demo Function to Showcase the Encryption Flow
def keyGen_algo():
    print("Starting Quantum-Inspired Encryption Demo\n")
    
    # Step 1: Generate a quantum-inspired key
    key = generate_key()
    print(f"Generated Key: {key.hex()}\n")
    
    # Step 2: Encrypt data with AES
    data = b"Hello, Quantum World!"
    print(f"Original Data: {data}\n")
    
    encrypted_data = aes_encrypt(key, data)
    print(f"Encrypted Data (AES): {encrypted_data.hex()}\n")
    
    # Step 3: Apply XOR encryption after AES
    xor_key = np.random.bytes(16)  # Generate XOR key
    encrypted_data_xor = xor_encrypt(encrypted_data, xor_key)
    print(f"Encrypted with XOR: {encrypted_data_xor.hex()}\n")
    
    # Step 4: Decrypt XOR before AES
    decrypted_data_xor = xor_encrypt(encrypted_data_xor, xor_key)
    decrypted_data = aes_decrypt(key, decrypted_data_xor)
    print(f"Decrypted Data: {decrypted_data}\n")
    
# Run the demo
keyGen_algo()