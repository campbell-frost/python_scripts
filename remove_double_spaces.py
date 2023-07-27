# Define the input file path
file_path = "C:\Users\Campbell\Documents\input.txt"

# Define the output file path
output_path = "C:\Users\Campbell\Documents\output.txt"


file_path = "C:\Users\Campbell
# Open the input file for reading
with open(file_path, "r") as file:
    # Read the contents of the file
    text = file.read()

# Process the text
processed_text = ""
previous_char = ""

for char in text:
    if char == "." and previous_char == " ":
        # Remove one of the spaces
        processed_text = processed_text[:-1] + char
    else:
        processed_text += char

    previous_char = char

# Write the processed text to the output file
with open(output_path, "w") as file:
    file.write(processed_text)

print("Processing complete. Result saved to output.txt.")
