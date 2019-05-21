import sys
import os
import traceback


def get_size_file_in_directory(path):
  size = 0
  for dir__path, dir__names, file__names in os.walk(path):

    for f in file__names:
        try:
            fp = os.path.join(dir__path, f)
            size += os.path.getsize(fp)
        except:
            None
    for dir in dir__names:
        size += os.path.getsize(os.path.join(dir__path, dir))
  return round(size / 1024 / 1024, 2)


try:

    path = sys.argv[1]
    dirs = os.listdir(path)

    for d in dirs:
        full_path = os.path.join(path, d)

        mb = get_size_file_in_directory(full_path)
        gb = round(mb / 1024, 2)
        print(d, "\n", mb, " mb", "\t", gb, "gb")
        print('-----------------------')


except Exception:
    print('Error:\n', traceback.format_exc())