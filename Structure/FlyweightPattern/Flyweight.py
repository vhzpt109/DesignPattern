class DogBreedDNA:
    def __init__(self, breed, DNA):
        self.breed = breed
        self.DNA = DNA

    def __repr__(self):
        return f'{self.DNA}'


class Dog:
    DNA_Table = {}  # {key,DogBreedDNA}

    @staticmethod
    def addDNA(breed, DNA):
        breed_DNA = DogBreedDNA(breed, DNA)
        Dog.DNA_Table[breed] = breed_DNA

    def __init__(self, name, age, gender, breed):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        if breed not in Dog.DNA_Table:
            raise RuntimeError(f"{breed} is not in DNA_Table")

    def __repr__(self):
        return f'{self.name},{self.age},{Dog.DNA_Table[self.breed]}'


if __name__ == "__main__":
    Dog.addDNA('shihTzu', 'ATAGGCTTACCGATGG...')
    Dog.addDNA('jinDo', 'ATAGGCTTACCGATGA...')

    choco = Dog('choco', 2, 'male', 'shihTzu')
    baduk = Dog('baduk', 3, 'female', 'jinDo')

    print(choco)
    print(baduk)
