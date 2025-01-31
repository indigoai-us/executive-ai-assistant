import os
import sys

# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from eaia.gmail import get_credentials

if __name__ == "__main__":
    get_credentials()
