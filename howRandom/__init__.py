from . import howRandom

def run():
	srcs = ["rust", "numpy", "random"]
	modes = ["std", "nump"]
	for i in srcs:
		for j in modes: 
			random_benchmark(10, 1e5 + 10, 10, src=i, mode=j)
	
	opt_srcs = ["rust", "numpy"]
	for i in opt_srcs:
		random_benchmark(10, 1e5 + 10, 10, src=i, mode="opt")
			
	runtime_plot(["std-rust_test_100000.0.csv", "std-numpy_test_100000.0.csv", "std-random_test_100000.0.csv"], srcs, "Runtime for Generating Random Ints w/ lists", "std-runtime")
	runtime_plot(["nump-rust_test_100000.0.csv", "nump-numpy_test_100000.0.csv", "nump-random_test_100000.0.csv"], srcs, "Runtime for Generating Random Ints w/ numpy arrays", "nump-runtime")
	runtime_plot(["opt-rust_test_100000.0.csv", "opt-numpy_test_100000.0.csv"], opt_srcs, "Runtime for Generating Random Ints Optimized", "opt-runtime")
	runtime_plot(["std-rust_test_100000.0.csv", "nump-rust_test_100000.0.csv", "opt-rust_test_100000.0.csv"], ["python array", "np.array", "rust vector"], "Runtime for Generating Random Ints w/ Rust", "rust-runtime")
