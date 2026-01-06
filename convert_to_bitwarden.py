"""
Convert password export file to Bitwarden-compatible CSV format.

This script reads a password manager export file and converts it to the Bitwarden
CSV import format with the following columns: folder, favorite, type, name, notes,
fields, reprompt, login_uri, login_username, login_password, login_totp.

Version: 1.0
Author: Password Manager Converter
License: MIT
"""
import csv

__version__ = "1.0"

# Read source file
source_file = r'my_src_file.csv'
output_file = r'my_output_file.csv'

# Bitwarden structure: folder,favorite,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp

with open(source_file, 'r', encoding='utf-8') as f_in, \
     open(output_file, 'w', encoding='utf-8', newline='') as f_out:
    
    reader = csv.DictReader(f_in)
    
    # Bitwarden columns
    fieldnames = ['folder', 'favorite', 'type', 'name', 'notes', 'fields', 'reprompt', 
                  'login_uri', 'login_username', 'login_password', 'login_totp']
    
    writer = csv.DictWriter(f_out, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        # Data mapping
        bitwarden_row = {
            'folder': '',  # No folder in source file
            'favorite': '',  # No favorites in source file
            'type': 'login',  # All entries are logins
            'name': row['Titre'],
            'notes': row['Commentaire'],
            'fields': '',  # No custom fields in source file
            'reprompt': '0',  # No reprompt by default
            'login_uri': row['URL'],
            'login_username': row["Nom d'utilisateur"],
            'login_password': row['Mot de passe'],
            'login_totp': ''  # No TOTP in source file
        }
        
        writer.writerow(bitwarden_row)

print(f'✅ Conversion completed! File created: {output_file}')
print('The file is ready to be imported into Bitwarden.')
