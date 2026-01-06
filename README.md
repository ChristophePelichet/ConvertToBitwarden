# 🔐 ConvertToBitwarden

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![PEP 8](https://img.shields.io/badge/code%20style-PEP%208-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> 🚀 A simple and efficient tool to convert your password manager exports to Bitwarden format!

## 📖 Description

This Python script reads a password manager export file (CSV format) and converts it to Bitwarden-compatible CSV format. It automatically handles the following fields:
- 🌐 Website URLs
- 👤 Usernames
- 🔑 Passwords
- 📝 Titles/Names
- 💬 Notes/Comments

## ✨ Features

- ✅ CSV to Bitwarden format conversion
- ✅ Preserves all credentials
- ✅ Maintains notes and comments
- ✅ UTF-8 encoding support
- ✅ PEP 8 compliant code

## 📦 Installation

1. **Clone or download the project**
   ```bash
   git clone <your-repo>
   cd ConvertToBitwarden
   ```

## 🎯 Usage

1. **Configure file paths** 📂
   
   Edit the `convert_to_bitwarden.py` file and set your paths:
   ```python
   source_file = r'my_src_file.csv'
   output_file = r'my_output_file.csv'
   ```

2. **Prepare your source file** 📄
   
   Make sure your CSV contains these columns:
   - `Titre` (Title)
   - `URL` (Website URL)
   - `Nom d'utilisateur` (Username)
   - `Mot de passe` (Password)
   - `Commentaire` (Comments)

3. **Run the conversion** 🚀
   ```bash
   python convert_to_bitwarden.py
   ```

4. **Import into Bitwarden** 📥
   - Open Bitwarden
   - Settings → Import Data
   - Select "Bitwarden (csv)"
   - Choose your output file
   - ✅ Done!

## 📊 Output Format

The script generates a CSV with standard Bitwarden columns:
- `folder` (Folder)
- `favorite` (Favorite)
- `type` (Entry type)
- `name` (Name)
- `notes` (Notes)
- `fields` (Custom fields)
- `reprompt` (Re-prompt for password)
- `login_uri` (URL)
- `login_username` (Username)
- `login_password` (Password)
- `login_totp` (TOTP code)

## 🛠️ Requirements

- 🐍 Python 3.6 or higher
- 📦 No external dependencies (uses standard library only)

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details.

## 📌 Version

Current version: **1.0**

---

💡 **Tip**: Remember to backup your passwords before any conversion!

🔒 **Security**: Never share CSV files containing your passwords! Delete the CSV files after a successful import for security reasons.

