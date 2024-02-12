import os

# kan spesifisere path valgfritt, om ikke noen path er gitt så går den bare ut ifra der .py filen ligger
def get_all_files(directory=None):

    if directory is None:
        directory = os.path.dirname(os.path.abspath(__file__))

    files_list = []

    for root, dirs, files in os.walk(directory):
        for file_name in files:

            # bruker relative path så det ikke har noe å si hvor koden kjører fra
            relative_path = os.path.relpath(os.path.join(root, file_name), directory)
            files_list.append(relative_path)

    return files_list

# ser igjennom listen med filer og ser etter mønster
def find_pattern_in_files(files, pattern, extension):
    
    pattern_list = []
    extension_list = []
    result_dict = {}
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            if pattern in content:
                pattern_list.append(file)

            # splitter fil navnet slik at vi får extensions for seg selv, i tilfelle noen filer inneholder txt strengen i filnavnet
            directory, filename_with_extension = os.path.split(file)
            filename, found_extension = os.path.splitext(filename_with_extension)

            if extension in found_extension:
                extension_list.append(filename_with_extension)

    # bruker dictionary i tilfelle koden må utvides i fremtiden med flere parameter
    result_dict[pattern] = pattern_list
    result_dict[extension] = extension_list
    return result_dict


pattern = "Sommer"
extension = 'txt'
files = get_all_files()

result = find_pattern_in_files(files, pattern, extension)

print(f"Filer som matcher mønster: {len(result[pattern])}")
print(f"Filer av typen .{extension}: {len(result[extension])}")