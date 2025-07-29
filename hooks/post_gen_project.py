#!/usr/bin/env python3
"""Post-generation hook for cookiecutter template."""

import os
import subprocess
import sys


def run_command(command: str) -> bool:
    """Run a shell command and return success status.
    
    Args:
        command: Shell command to execute
        
    Returns:
        True if command succeeded, False otherwise
    """
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def main() -> None:
    """Main post-generation hook function."""
    print("🚀 Setting up your new project...")
    
    # Initialize git repository if requested
    if "{{ cookiecutter.use_git }}" == "y":
        print("📁 Initializing git repository...")
        if run_command("git init"):
            print("✅ Git repository initialized")
            
            # Create initial commit
            run_command("git add .")
            run_command('git commit -m "Initial commit from cookiecutter template"')
            
            # Create dev branch if requested
            if "{{ cookiecutter.create_dev_branch }}" == "y":
                print("🌿 Creating development branch...")
                if run_command("git checkout -b dev"):
                    print("✅ Development branch created")
                    run_command("git checkout main")
        else:
            print("❌ Failed to initialize git repository")
    
    print("\n🎉 Project setup complete!")
    print("\n📝 Next steps:")
    print("1. cd {{ cookiecutter.project_slug }}")
    print("2. uv venv")
    print("3. source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate")
    print("4. uv add --dev black isort")
    print("5. Start coding with your established standards! 🚀")


if __name__ == "__main__":
    main()