

def directory_search(dirname):
    import os
    file_list = []
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        file_list.append(full_filename)

    return file_list
