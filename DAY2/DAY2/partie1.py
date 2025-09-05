def read_one_line(filename: str) -> str:
    with open(filename, "r") as f:
        first_line = f.readline()
    return first_line

ligne = read_one_line("partie1.py")
print(ligne)



 

def write_text(filename: str, text: str):
    f = open(filename, "w")
    f.write(text)
    f.close()


write_text("with.txt", "Bonjour !")
print("Texte écrit")




def copy_characters(input_file: str, output_file: str, nb: int):
    with open(input_file, "r") as f_in:
        content = f_in.read(nb)

    with open(output_file, "a") as f_out:
        f_out.write("\n" + content)

input_filename = "../../../PycharmProjects/PythonProject/requirements.txt"
output_filename = "../../../PycharmProjects/PythonProject/requirements.txt"
nombre_de_caracteres = 50

copy_characters(input_filename, output_filename, nombre_de_caracteres)
print(f"Les {nombre_de_caracteres} premiers caractères de '{input_filename}' ont été copiés dans '{output_filename}'.")





from copy import copy

def read_all_lines(filename: str) -> (list[str], list[str]):
    with open(filename, "r") as f:
        all_lines = f.readlines()  

    every_other_line = copy(all_lines)[::2] 

    return all_lines, every_other_line

filename = "partie2.py"
all_lines, every_other_line = read_all_lines(filename)

print("Toutes les lignes :")
print(all_lines)

print("\nUne ligne sur deux :")
print(every_other_line)





def write_text_better(filename: str, text: str):
    with open(filename, "a") as f:
        f.write(text + "\n")

write_text_better("texte_destination.txt", "Ceci est une ligne ajoutée avec with.")
print("Texte écrit dans 'texte_destination.txt'.")



def copy_characters_better(input_file: str, output_file: str, nb: int):
    with open(input_file, "r") as f_in:
        content = f_in.read(nb)

    with open(output_file, "a") as f_out:
        f_out.write("\n" + content)

input_filename = "texte_destination.txt"
output_filename = "texte-destination.txt"
nombre_de_caracteres = 50


copy_characters_better(input_filename, output_filename, nombre_de_caracteres)
print(f"Les {nombre_de_caracteres} premiers caractères ont été copiés de '{input_filename}' vers '{output_filename}'.")




