class Tasit:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def bilgileri_goster(self):
        return f"Tasit: {self.marka} {self.model}"

