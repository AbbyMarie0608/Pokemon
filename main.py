from pokemon import PokemonTree
def main():
    file_name = input('Input a file: ')
    tree = PokemonTree()
    tree.read_file(file_name)
    tree.main()

if __name__ == "__main__":
    main()