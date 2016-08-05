import os
import shutil
import logging
from lib.util import (
    get_size,
    get_bucket_list,
    get_buckets
)

logging.basicConfig(level=logging.FATAL)
logger = logging.getLogger(__name__)

class FSS:

    def __init__(self, id, token):
        pass

    def create_directory(self, current_dir, directory):
        try:
            dir = os.path.join(current_dir, directory)
            os.mkdir(dir)
        except Exception as e:
            logger.error(e)

    def remove_directory(self, current_dir, directory):
        try:
            _path = os.path.join(current_dir, directory)
            shutil.rmtree(_path)
        except Exception as e:
            logger.error(e)

    def create_file(self, directory, source_file, destination_file):
        try:
            src_path = source_file
            dst_path = os.path.join(directory, destination_file)

            logger.info(src_path)
            logger.info(dst_path)

            src = open(src_path, "r")

            dst = open(dst_path, "w")
            shutil.copyfileobj(src, dst)

            src.close()
            dst.close()
        except Exception as e:
            logger.error(e)

    def remove_file(self, directory, file_name):
        try:
            file = os.path.join(directory, file_name)
            os.remove(file)
        except Exception as e:
            logger.error(e)

    def directory_exists(self, directory):
        return os.path.exists(directory)

    def file_exists(self, directory, file_name):
        try:
            file_name = os.path.join(directory, file_name)
            logger.info(file_name)
            return os.path.isfile(file_name)
        except Exception as e:
            logger.error(e)

    def get_file_handle(self, directory, file_name):
        """
            return a handle if it exists else null handle
        :param directory:
        :param file_name:
        :return:
        """
        try:
            _path = os.path.join(directory, file_name)
            file = open(_path, "r")
            return file
        except Exception as e:
            logger.info(e)
        return None

    def close_file_handle(self, file_handle):
        try:
            file_handle.close()
        except Exception as e:
            logger.error(e)

    def get_directory_contents(self, directory):
        return get_bucket_list(directory)

    def get_directories(self, directory):
        return get_buckets(directory)

    def get_directory_size(self, directory):
        return get_size(directory)