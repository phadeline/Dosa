


def read_file(file):
    parser = argparse.ArgumentParser(description="Read a file and print its contents.")
    parser.add_argument("file", type=str, help="Name or path of the file to read")
    args = parser.parse_args()

# Open and read the file manually using a context manager
    try:
        with open(args.file, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


