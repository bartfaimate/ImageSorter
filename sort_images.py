#! /usr/bin/python3

import os
import sys
import argparse
from pathlib import Path
from typing import Union, List
import shutil

# get the filenames without extension
# get parent of files (jpeg)
# get the sibling folder(raw)
# get differencfrom the raw stem-s and the jpg-stems

class ImageSorter:
    def __init__(self, base_path:Union[str, Path], input_list : List[str] = None):
        self.base_path = Path(base_path) if isinstance(base_path, str) else base_path
        self.input_list = input_list
            
    def get_files(self, folder: Union[str, Path]) -> set:
        _folder = Path(folder) if isinstance(folder, str) else folder
        
        filenames = {Path(file).stem for file in os.listdir(_folder)}
        return filenames

    def files_to_remove(self, files:List[str], folder_to_cleanup, suffix=".ARW"):
        print(f'There are {len(files)} differences')
        for file in files:
            to_remove = self.base_path.joinpath(f'{folder_to_cleanup}/{file}').with_suffix(suffix)
            print(to_remove)
            os.remove(to_remove)

    def move_selected_to_dest(self, selected_images, output):
        for selected in selected_images:
            print(f"Moving {selected} to {output}")
            shutil.move(selected.as_posix(), output.as_posix())

    def select(self, fromf):
        folder = self.base_path.joinpath(fromf)
        files = [Path(f).name for f in os.listdir(folder)]
        with_suffix =  "." in self.input_list[0]

        # print(files)
        selecteds = set()
        for image_name in self.input_list:
            for file in files:
                if ( with_suffix and file.lower().endswith(image_name.lower()) or
                    not with_suffix and Path(file).stem.endswith(image_name)
                   ):
                    selecteds.add(folder.joinpath(file))
        # print("Selected files: ")
        # print(selecteds)
        return selecteds

def parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-b", "--base-path", required=True, help="The base path of the images")
    arg_parser.add_argument("-i", "--inputs", nargs="+", help="The name of images or numbering of images")
    arg_parser.add_argument("-d", "--delete", help="Delete from folder")
    arg_parser.add_argument("-f", "--fromf", help="The folder from delete")
    arg_parser.add_argument("-m", "--move", help="Select switch. Use this if you want to select the [inputs] as better images and move to this")
    arg_parser.add_argument("-o", "--output", help="Destination folder where to move the selected images")
    # arg_parser.add_help()
    return arg_parser

def main():
    arg_parser = parser()
    args = arg_parser.parse_args()
    # return
    # get jpegs
    base_path = Path(args.base_path)
    image_sorter = ImageSorter(base_path)
    print(f"base path is: {base_path}")
    if args.inputs:
        input_images = args.inputs
        image_sorter.input_list = input_images
        if not args.output:
            arg_parser.print_help()
            raise OSError("No Destination folder is given")
        dest_folder = Path(args.output)
        print(f"input images: {input_images}")
        print(f"output folder: {dest_folder}")
        # create folder
        if not dest_folder.is_dir():
            dest_folder.mkdir(parents=True)
        if args.move:
            # select from this fodler and move to destination folder
            fromf = args.move
            selected_images = image_sorter.select(fromf)
            image_sorter.move_selected_to_dest(selected_images, dest_folder)
            pass
        elif args.delete :
            fromf = args.delete
            selected_images = image_sorter.select(fromf)
            for selected in selected_images:
                print(f"Deleting {selected}")
            pass

    # jpegs = image_sorter.get_files(base_path.joinpath('jpeg'))

    # raws = image_sorter.get_files(base_path.joinpath('raw'))
    # print(len(jpegs))
    # print(len(raws))

    # diffs = raws.difference(jpegs)
    # folder_to_cleanup = "raw"
    # image_sorter.files_to_remove(diffs, folder_to_cleanup)






if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\n')
        exit(0)
