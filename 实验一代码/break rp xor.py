

def hamming_distance(bytes1, bytes2):
    # Calculate the Hamming distance between two bytes objects
    distance = 0
    for b1, b2 in zip(bytes1, bytes2):
        xor_result = b1 ^ b2
        distance += bin(xor_result).count('1')
    return distance

def find_keysize(data, max_keysize, num_keysizes):
    # Try different key sizes and find the specified number of smallest normalized Hamming distances
    distances = []

    for keysize in range(2, max_keysize + 1):
        blocks = [data[i:i + keysize] for i in range(0, len(data), keysize)]
        total_distance = 0

        # Calculate Hamming distance between adjacent blocks
        for block1, block2 in zip(blocks, blocks[1:]):
            distance = hamming_distance(block1, block2)
            total_distance += distance

        # Calculate normalized Hamming distance
        normalized_distance = total_distance / (len(blocks) - 1) / keysize
        distances.append((keysize, normalized_distance))

    # Sort the distances and return the smallest num_keysizes
    sorted_distances = sorted(distances, key=operator.itemgetter(1))
    return [keysize for keysize, _ in sorted_distances[:num_keysizes]]

# Usage example
if __name__ == '__main__':
    # Replace 'data' with your actual data
    data = bytes.fromhex("...")  # Input your hexadecimal data

    max_keysize = 40  # Maximum keysize to try
    num_keysizes = 3  # Number of smallest key sizes to find

    smallest_keysizes = find_keysize(data, max_keysize, num_keysizes)
    print(f"Smallest key sizes: {smallest_keysizes}")