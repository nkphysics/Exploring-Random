from . import howRandom

def run():
	random_benchmark(10, 1e5 + 10, 10)
	random_benchmark(10, 1e5 + 10, 10, "random")
	random_benchmark(10, 1e5 + 10, 10, "numpy")
