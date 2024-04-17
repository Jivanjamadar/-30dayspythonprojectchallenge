import random

def ascii_to_binary(data):
    """Convert ASCII characters to binary representation."""
    return ''.join(format(ord(char), '08b') for char in data)

def compute_checksum(data):
    """Compute a simple checksum for error detection."""
    checksum = 0
    for bit in data:
        checksum += int(bit)
    checksum %= 2      #checksum check(%2)
    return checksum

def add_checksum(data):
    """Add a checksum to the data for error detection."""
    checksum = compute_checksum(data)
    return data + str(checksum)

def simulate_noise(data, error_prob):
    """Simulate noise by randomly flipping bits with a given error probability."""
    noisy_data = ''
    for bit in data:
        if random.random() < error_prob:
            noisy_data += '1' if bit == '0' else '0'  #noise creation(bit flip)
        else:
            noisy_data += bit
    return noisy_data

def check_checksum(data):
    """Check the checksum for error detection."""
    return compute_checksum(data[:-1]) == int(data[-1])

#simulate data transmission
def simulate_transmission(message, error_prob):
    print("Original Message:", message)

    #binary conversion & checksum add
    binary_message = ascii_to_binary(message)
    encoded_message = add_checksum(binary_message)

    #stimulate noise in transmission
    noisy_message = simulate_noise(encoded_message, error_prob)

    #check checksum
    error_detected = not check_checksum(noisy_message)

    if error_detected:
        print("Received Message (with Error):", noisy_message)
        print("Error Detected!")
    else:
        print("Received Message (without Error):", noisy_message)
        print("No Error Detected.")

#sample message & error probability
if __name__ == "__main__":
    message ="Hello Friends !"
    error_probability = 0.5 # Increase error probability

    simulate_transmission(message, error_probability)

