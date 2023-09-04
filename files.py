import pandas


class Files:
    def __init__(self, path: str):
        self.path = path

    def create(self, columns: list) -> pandas.DataFrame:
        dataset = pandas.DataFrame(columns=columns)
        self.save(dataset)

        return dataset

    def load(self, path: str) -> pandas.DataFrame:
        dataset = pandas.read_csv(path)

        return dataset

    def add(self, dataset: pandas.DataFrame, row: dict) -> pandas.DataFrame:
        row = pandas.DataFrame(row)
        dataset = pandas.concat([dataset, row], axis=0)
        
        return dataset

    def save(self, dataset: pandas.DataFrame) -> None:
        dataset.to_csv(self.path, index=False)
