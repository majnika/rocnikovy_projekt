class Pattern:
    
    _pattern: dict

    @property
    def name(self) -> str:
        return self._pattern["name"]

    # TODO(5)
    def __init__(self, pattern: dict) -> None:
        self._pattern = pattern

    # TODO(5)
    def set(self, pattern: dict) -> None:
        self._pattern = pattern

    def get(self) -> dict:
        return self._pattern


    # TODO(7)
    def is_valid(self, size: int) -> bool:
        
        checksum: int = size

        # TODO(4)
        for field in self._pattern["pattern"]["data"]:
            checksum -= int(field["size"]) + len(field["name"])

        return checksum >= 0
    