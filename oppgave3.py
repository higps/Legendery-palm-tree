import os
# kan spesifisere path valgfritt, om ikke noen path er gitt så går den bare ut ifra der .py filen ligger
def get_all_files(directory):

    files_list = []
    # bruker os.walk til å gjennom alle mapper og undermapper, tar så pathen og legger til i en liste, her inneholder pathen file extension også
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            
            path = os.path.join(root, file_name)
            files_list.append(path)

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
folder = "Oppgave 3"

files = get_all_files(directory=folder)
result = find_pattern_in_files(files, pattern, extension)

print(f"Filer som matcher mønster {pattern}: {len(result[pattern])}")
print(f"Filer av typen .{extension}: {len(result[extension])}")