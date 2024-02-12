import json

# returnerer om verdien er et tall og om tallet er et partall, for å unngå feil i koden om det skulle snike seg inn noe annet i flen
def is_even_num(value):
    return isinstance(value, int) and (value % 2) == 0

def filter_num(file_path):

    file = open(file_path)
    data = json.load(file)
    even_num = []

    for i in data:
        if is_even_num(i):
                even_num.append(i)

    return (even_num)

even_num_list = filter_num("array.json")
print(f"Sum av partall: {sum(even_num_list)}")