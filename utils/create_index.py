import os

def generate_index_md(root_folder):

    output_file = os.path.join(root_folder, "index.md")

    with open(output_file, 'w', encoding='utf-8') as f:
        def write_folder_contents(folder_path, depth=2):
            # Get the folder name
            folder_name = os.path.basename(folder_path)
            # Write the folder name as a heading
            f.write(f"{'##'} {folder_name}\n")
            
            # List the contents of the folder
            contents = sorted(os.listdir(folder_path))
            for item in contents:
                item_path = os.path.join(folder_path, item)
                if os.path.isdir(item_path):
                    write_folder_contents(item_path, depth + 1)
                elif item.endswith(".md"):
                    # Write the markdown file link
                    f.write(f"[[{item}]]\n\n")
        
        # Start the recursive writing from the root folder
        write_folder_contents(root_folder)

# Specify the root folder
root_folder = r"D:\007_Projects\007_Programming\obsidian-publish\my_wiki\content"
# Call the function to generate index.md
generate_index_md(root_folder)
