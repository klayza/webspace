import os
import glob

def concatenate_readmes():
    """
    Concatenates all markdown files from the awesome_readmes directory
    into a single readme.md file in the root directory.
    """
    output_filename = 'readme.md'
    input_directory = 'awesome_readmes'
    
    # Get a list of all .md files in the directory, sorted alphabetically
    md_files = sorted(glob.glob(os.path.join(input_directory, '*.md')))
    
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for filename in md_files:
            # Add a header indicating the source file
            header = f"# From {os.path.basename(filename)}\n\n"
            outfile.write(header)
            
            with open(filename, 'r', encoding='utf-8', errors='ignore') as infile:
                content = infile.read()
                outfile.write(content)
                outfile.write('\n\n---\n\n') # Add a separator
                
    print(f"Successfully concatenated {len(md_files)} files into {output_filename}")

if __name__ == "__main__":
    concatenate_readmes()

