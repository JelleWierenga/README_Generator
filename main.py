import tkinter as tk
from tkinter import filedialog
import openai

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    return file_path

def read_python_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    return code

def generate_readme(code):
    openai.api_key = 'YOUR_API_KEY'

    prompt = f"Generate README for code:\n\n```python\n{code}\n```"

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        temperature=0.8,
        n=1,
        stop=None,
        timeout=10
    )

    readme = response.choices[0].text.strip()

    return readme

def save_readme_as_markdown(readme, filename):
    with open(filename, 'w') as file:
        file.write(readme)

    print(f"README saved as {filename}")

file_path = open_file_dialog()

if file_path:
    code = read_python_file(file_path)

    readme = generate_readme(code)

    save_readme_as_markdown(readme, 'README.md')

    print("README generated and saved successfully.")
else:
    print("No file selected.")
