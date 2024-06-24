def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
    assert 0 <= index < len(self.__indexed_dataset), "Index out of range"

    data = []
    current_index = index
    next_index = index
    items_returned = 0

    while items_returned < page_size and current_index < len(self.__indexed_dataset):
        item = self.__indexed_dataset.get(current_index)
        if item is not None:
            data.append(item)
            items_returned += 1
        next_index += 1
        current_index += 1

    return {
        "index": index,
        "next_index": next_index,
        "page_size": len(data),
        "data": data
    }
