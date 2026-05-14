class Perceptron:
    def __init__(self, filename: str, features: int, threshold: float):
        with open(filename) as f:
            self.weights = []
            for i in range(features):
                self.weights.append(float(f.readline().split(':')[1].strip()))
            self.bias = float(f.readline().split(':')[1].strip())
        self.threshold = threshold
        self.features = features

    def activation(self, x: float) -> bool:
        return True if x > self.threshold else False
    
    def predict(self, input: list[float]) -> bool:
        total = self.bias
        for i in range(self.features):
            total += self.weights[i] * input[i]
        return self.activation(total)

if __name__ == "__main__":

    p = Perceptron(filename='weights.txt', features=5, threshold=0.5)

    print('Inserisci i dati:')

    inp = []
    inp.append(int(input('Artista famoso? (1=Si, 0=No): ')))
    inp.append(int(input('Bel meteo? (1=Si, 0=No): ')))
    inp.append(int(input('Amici presenti? (1=Si, 0=No): ')))
    inp.append(int(input('Cibo buono? (1=Si, 0=No): ')))
    inp.append(int(input('Alcool disponibile? (1=Si, 0=No): ')))

    if p.predict(inp):
        print('Vai al concerto!')
    else:
        print('Resta a casa!')