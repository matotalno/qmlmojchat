import os
from pathlib import Path

def generate_directory_structure(startpath, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(startpath):
            # Preskače .git, __pycache__ i venv direktorijume
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'venv']]
            
            level = root.replace(startpath, '').count(os.sep)
            indent = '    ' * level
            f.write(f'{indent}{os.path.basename(root)}/\n')
            subindent = '    ' * (level + 1)
            for file in sorted(files):
                if not file.endswith('.pyc'):
                    f.write(f'{subindent}{file}\n')

if __name__ == "__main__":
    # Uzima trenutni direktorijum
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(current_dir, 'current_structure.txt')
    
    print(f"Generating structure in: {output_file}")
    generate_directory_structure(current_dir, output_file)
    print("Done! Check current_structure.txt")
