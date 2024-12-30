class Process:
    def __init__(self) -> None:
        self.result = []
    def sum(self, arr):
        for i in range(len(arr)):
            self.result.append(arr[i] * arr[i])
            
