def read_dob_file(file_path):
    """
    Read the contents of a file and return the lines.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    list: A list of lines from the file.
    """
    # Open the file and read its contents
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def split_names_and_birthdates(lines):
    """
    Split lines into names and birthdates.

    Parameters:
    lines (list): A list of lines from the file.

    Returns:
    tuple: Two lists, one with names and the other with birthdates.
    """
    names = []
    birthdates = []

    # Process each line to extract names and birthdates
    for line in lines:
        name, birthdate = line.strip().split(', ')
        names.append(name)
        birthdates.append(birthdate)
    return names, birthdates


def print_names_and_birthdates(names, birthdates):
    """
    Print names and birthdates in a formatted manner.

    Parameters:
    names (list): A list of names.
    birthdates (list): A list of birthdates.
    """
    # Print the names
    print("Name")
    for name in names:
        print(name)

    # Print the birthdates
    print("\nBirthdate")
    for birthdate in birthdates:
        print(birthdate)


if __name__ == "__main__":
    file_path = 'DOB.txt'

    # Read the lines from the file
    lines = read_dob_file(file_path)

    # Split the lines into names and birthdates
    names, birthdates = split_names_and_birthdates(lines)

    # Print the names and birthdates
    print_names_and_birthdates(names, birthdates)