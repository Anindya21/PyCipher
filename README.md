# PyCipher

A comprehensive Python implementation of classical cryptographic ciphers including Caesar, Affine, Playfair, and Hill ciphers with a user-friendly interface.

## ✨ Features

- **Multiple Classical Ciphers**: Implementation of Caesar, Affine, Playfair, and Hill ciphers
- **User Interface**: Interactive UI for easy cipher operations
- **Encryption & Decryption**: Support for both encryption and decryption operations
- **Modular Design**: Clean separation of cipher implementations and UI components

## 📁 Project Structure

```
crypto_project/
├── ciphers/           # Cipher implementations
├── ui/                # User interface components
├── main.py            # Main application entry point
├── LICENSE            # Project license
├── README.md          # Project documentation
├── pyproject.toml     # Project configuration and dependencies
└── uv.lock            # Dependency lock file
```

## 🔧 Prerequisites

- Python 3.8 or higher
- uv package manager (recommended) or pip

## 📥 Installation

### Option 1: Using uv (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/crypto_project.git
cd crypto_project
```

2. Install uv if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Install dependencies:
```bash
uv sync
```

### Option 2: Using pip

1. Clone the repository:
```bash
git clone https://github.com/yourusername/crypto_project.git
cd crypto_project
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

## 🚀 Usage

Run the main application:

```bash
# Using uv
uv run python main.py

# Using standard Python
python main.py
```

Follow the on-screen prompts to:
1. Select a cipher (Caesar, Affine, Playfair, or Hill)
2. Choose encryption or decryption
3. Enter your message and required keys
4. View the results

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

---

**Note:** This project is for educational purposes. Classical ciphers are not secure for modern cryptographic applications.