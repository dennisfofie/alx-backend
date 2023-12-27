#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
         Retrieve a page data
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start, end = self.index_range(page, page_size)

        data = self.dataset()

        if (start > len(data)):
            return []
        return data[start:end]


    
    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
         Discription - return range to paginate
        """
        if type(page) and type(page_size) != int:
            return "<page> and <page_size> must be of type int"

        start = (page - 1) * page_size
        
        if type(start) != int:
            return "First index must be of type int"
        
        end = start + page_size

        if type(start) != int:
            return "Last index must be of type int"
        
        return (start, end)
