import os

folder_path = r'E:\SteamLibrary\steamapps\common\Apex Legends\cfg'
search_phrase = 'bind "4"'
replace_phrase = 'bind "["'

i = 0

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.startswith('neo'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.read()
            if search_phrase in content:
                i += 1
                updated_content = content.replace(search_phrase, replace_phrase)
                with open(file_path, 'w') as f:
                    f.write(updated_content)
                print(f"Updated {file_path} {i}")
