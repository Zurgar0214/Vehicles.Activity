from Service.Loader import Loader


if __name__ == "__main__":
    loader = Loader()
    vehicles, motorcycles, cars = loader.load_data()