class Gateau:
    def __init__(self):
        self.ingredients = []
        self.tempo_cuissao = 0

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def mistura(self):
        if not self.ingredients:
            raise ValueError("Nenhum ingredient adicionado.")
        return "Misturar ingrediente : " + ", ".join(self.ingredients)

    def cozinhar(self, tempo):
        self.temps_cuisson = tempo #aqui está errado
        return f"Gâteau pronto até {self.temps_cuisson} minutos."

    def fritar(self, tempo):
        self.tempo_cuissao = tempo
        return f"Gâteau pronto até {self.temps_cuisson} minutos."