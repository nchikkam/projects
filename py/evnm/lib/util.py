import os
import functools

def get_size(_path):
    @functools.lru_cache(maxsize=4096)
    def get_dir_size(start_path = '.'):
        """
            get the size of the directory by memoization
        :param start_path:
        :return:
        """
        total_size = 0
        for entry in os.scandir(start_path):
            if entry.is_dir(follow_symlinks = False):
                total_size += get_dir_size(entry.path)
            elif entry.is_file(follow_symlinks = False):
                total_size += entry.stat().st_size
        return total_size

    return get_dir_size(_path)

def get_bucket_list(_path):
    """
        get all the files in a directory
    :param _path:
    :return:
    """
    ret = []
    try:
        for entry in os.scandir(_path):
            if entry.is_file(follow_symlinks = False):
                ret.append(entry)
    except Exception as e:
        #raise Exception("Error reading "+ _path)
        pass
    return ret

def get_buckets(_path):
    """
        get all directories of path - recursively
    :param _path:
    :return:
    """
    @functools.lru_cache(maxsize=4096)
    def get_dirs(start):
        dirs = [start]
        try:
            for entry in os.scandir(start):
                if entry.is_dir(follow_symlinks = False):
                    dirs.append(get_dirs(entry.name))
            return dirs
        except Exception as e:
            pass
        return dirs
    return get_dirs(_path)