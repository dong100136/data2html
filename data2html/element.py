class DElement:
    pass


class DText(DElement):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return f'Text(path="{self.path}")'


class DImage(DElement):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return f'Image(path="{self.path}")'
