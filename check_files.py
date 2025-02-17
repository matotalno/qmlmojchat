import os
import subprocess

def get_project_files():
    files = []
    print("Scanning project files...")
    for root, _, filenames in os.walk('.'):
        # Preskoči direktorijume koje ne želimo
        if any(skip in root for skip in ['.git', '__pycache__', 'venv']):
            continue
        for filename in filenames:
            # Preskoči fajlove koje ne želimo
            if any(skip in filename for skip in ['.pyc', '.env']):
                continue
            path = os.path.join(root, filename).replace('\\', '/')
            if path.startswith('./'):
                path = path[2:]
            files.append(path)
    return set(files)

def get_git_files():
    print("Getting git files...")
    try:
        result = subprocess.run(['git', 'ls-files'], capture_output=True, text=True, check=True)
        return set(result.stdout.splitlines())
    except subprocess.CalledProcessError:
        print("Error: Git command failed")
        return set()

if __name__ == '__main__':
    print("=== Checking Project Files ===\n")
    
    project_files = get_project_files()
    git_files = get_git_files()
    
    print(f"\nTotal project files: {len(project_files)}")
    print(f"Total git files: {len(git_files)}\n")
    
    print("Files not in git (should be added):")
    missing_files = project_files - git_files
    if missing_files:
        for f in sorted(missing_files):
            print(f"  + {f}")
    else:
        print("  None - all files are in git")
    
    print("\nFiles in git but not in project (might be deleted):")
    extra_files = git_files - project_files
    if extra_files:
        for f in sorted(extra_files):
            print(f"  - {f}")
    else:
        print("  None - no extra files in git")
    
    input("\nPress Enter to exit...")
