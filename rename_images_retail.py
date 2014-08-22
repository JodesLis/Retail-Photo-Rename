"""
Copies and renames image files for retail website, using list
of codes + titles.
 -Jody 21-08-2014
"""

import csv
import os
import shutil


def read_codes_and_titles(filename):
    """
    reads in csv file, and creates a list
    input csv of form:
    code,website title
    """
    with open(filename, "r") as file_in:
        code_titles = list(csv.reader(file_in))
    return code_titles


def generate_title(code_titles):
    """
    converts website title to concatenated
    version, and adds to dictionary
    """
    full_titles = {}
    for line in code_titles:
        code = line[0].lower()
        if code not in full_titles:
            new_title = ""
            temp_title = line[1].lower()
            temp_title = temp_title.split(" ")
            for word in temp_title:
                new_title += word + "-"
            full_titles[code] = new_title
    return full_titles


def read_images(new_title, image_path, out_path):
    """
    copies images in image directory into
    a new directory, based on if they are
    in code dictionary
    """
    os.chdir(image_path)
    for target_file in os.listdir(image_path):
        if target_file[:7] in new_title:
            new_file = out_path + target_file
            if not os.path.isfile(new_file):
                shutil.copyfile(target_file, new_file)
    rename_images(new_title, out_path)


def rename_images(new_title, out_path):
    """
    renames files
    """
    os.chdir(out_path)
    for target_file in os.listdir(out_path):
        if target_file[:7] in new_title:
            code = target_file.split(".")[0]
            new_filename = new_title[target_file[:7]] + code + ".jpg"
            if not os.path.isfile(new_filename):
                os.rename(target_file, new_filename)
            else:
                os.remove(target_file)
    print "\nDone! Check", str(out_path), "for files!"


def main():
    """
    the bit that does all the work!
    """
    filename = raw_input("Enter filename of codes list, in csv: ")
    while not os.path.isfile(filename):
        print "\nFile not found - please try again."
        filename = raw_input("Enter filename of codes list, in csv: ")
    code_titles = read_codes_and_titles(filename)
    new_title = generate_title(code_titles)
    starting_path = os.getcwd()
    image_path = "P:/users/RETAIL/Web Selling/Retail Product Photos/Code filenamed images/"
    out_path = "p:/users/RETAIL/joseF/New images/"
    read_images(new_title, image_path, out_path)
    os.chdir(starting_path)


if __name__ == "__main__":
    main()
