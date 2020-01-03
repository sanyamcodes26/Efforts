import re


def initial():
    if re.search("ape", "The ape was at the apex"):
        print(True)

    all_apes = re.findall("ape", "The ape was at the apex")
    print(all_apes)

    the_str = "The ape was at the apex"
    for i in re.finditer("ape.", the_str):
        loc_tuple = i.span()
        print(loc_tuple)
        print(the_str[loc_tuple[0]:loc_tuple[1]])

    animal_str = "cat mat rat fat bat"
    print(re.findall("[crb]at", animal_str))
    print(re.findall("[^crb]at", animal_str))

    owl_food = "rat cat mat pat"
    print(owl_food)
    regex = re.compile("[cr]at")
    owl_food = regex.sub("owl", owl_food)
    print(owl_food)

    rand_str = "Here is \\stuff"
    print(re.search("\\\\stuff", rand_str))
    print(re.search(r"\\stuff", rand_str))
    return


if __name__ == "__main__":
    initial()
