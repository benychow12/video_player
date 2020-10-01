import sys
import os.path

def check_file(filepath, filetype):
    if os.path.exists(filepath) and filepath[-3:] == filetype:
        print("Valid file found: ", filepath)
        return True
    else:
        print("Invalid file found: ", filepath)
        return False

vid_path = sys.argv[1]
sub_path = sys.argv[2]
local_file = os.path.join(os.getcwd(), "index.html")

if (check_file(vid_path, "mp4") and check_file(sub_path, "srt")):
    print("Opening file")

    if os.path.exists("index.html"):
        print(local_file)
        with open(local_file, "r+") as read_source:
            lines = read_source.readlines()

            read_source.seek(0)

            for line in lines:
                if "mp4" in line:
                    print(line)
                    first = line.find("src=") + 5
                    last = line.find("type=") - 2
                    old_filepath = line[first:last]
                    line = line.replace(old_filepath, vid_path)
                    print(line)

                if "srt" in line:
                    print(line)
                    first = line.find("src=") + 5
                    last = line.find("default") - 2
                    old_filepath = line[first:last]
                    line = line.replace(old_filepath, sub_path)
                    print(line)

                read_source.write(line)

            read_source.truncate()
            read_source.close()

    else:
        print("index.html not found")
        exit()

else:
    print("One or more invalid files, exiting...")
    exit()
