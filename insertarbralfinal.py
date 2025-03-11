def add_line_breaks(text):
    """
    Adds HTML line break tags (<br>) at the end of each line in a text paragraph.
    
    Parameters:
    text (str): The input text to process
    
    Returns:
    str: Text with <br> tags added at the end of each line
    """
    # Check if input is empty or None
    if not text:
        return ""
    
    # Split the text into lines
    lines = text.split('\n')
    
    # Add <br> tag to each line except the last one
    modified_lines = []
    for i, line in enumerate(lines):
        if i < len(lines) - 1:
            modified_lines.append(line.strip() + " <br>")
        else:
            modified_lines.append(line.strip())
    
    # Join the lines back together
    return '\n'.join(modified_lines)

def main():
    # Get input from user
    print("Enter your text (press Enter twice to finish):")
    
    # Collect lines until empty line is entered
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    
    # Join lines into a single text
    text = '\n'.join(lines)
    
    # Process the text
    result = add_line_breaks(text)
    
    # Print the result
    print("\nModified text:")
    print(result)

if __name__ == "__main__":
    main()