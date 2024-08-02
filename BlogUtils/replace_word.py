import re

# Directory containing the .md files
directory = "/Users/lyk/Documents/LYK-love.github.io/source/_posts"

# Import os module to work with the filesystem
import os

# Loop through all files in the specified directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):  # Check if the file is a Markdown file
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Find the first occurrence of "<!--more-->" and split the content
        parts = content.split("<!--more-->", 1)
        if len(parts) > 1:
            # Replace "Source" with "Spurces" in the part before "<!--more-->"
            parts[0] = re.sub(r"\bSource\b", "Sources", parts[0], flags=re.IGNORECASE)
            # Combine the parts back together
            content = "<!--more-->".join(parts)

            # Write the modified content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
