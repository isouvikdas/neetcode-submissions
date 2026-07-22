class TimeMap:
    mp: dict[str, list[str]]

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            length = len(self.mp[key])
            if length > timestamp:
                self.mp[key][timestamp] = value
            elif timestamp >= length:
                idx = length
                while idx <= timestamp:
                    if idx == timestamp:
                        self.mp[key].append(value)
                    else:
                        self.mp[key].append('inf')
                    idx += 1
        else:
            self.mp[key] = []
            i = 0
            while i <= timestamp:
                if i == timestamp:
                    self.mp[key].append(value)
                else:
                    self.mp[key].append('inf')
                i += 1

    def get(self, key: str, timestamp: int) -> str:
        if key in self.mp:
            arr = self.mp[key]
            if timestamp >= len(arr):
                while timestamp >= len(arr):
                    timestamp -= 1
            if arr[timestamp] != 'inf':
                return arr[timestamp]
            else:
                idx = timestamp
                while idx >= 0:
                    if arr[idx] != "inf":
                        return arr[idx]
                    idx -= 1
        return ""




        
