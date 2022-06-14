import numpy as np
from random import randrange
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import perf_counter
import rust_rand
import pandas as pd

	
def gen_bin(min_val, max_val, total, src="rust"):
	ints = []
	for i in range(0, total):
		if src == "numpy":
			ints.append(np.random.randint(min_val, max_val))
		elif src == "random":
			ints.append(randrange(min_val, max_val))
		elif src == "rust":
			ints.append(rust_rand.rand_rust_func(min_val, max_val))
	hist, edges = np.histogram(ints, np.arange(min_val, max_val + 1, 1))
	return hist, edges
	
def avg_error_plot(hist, edges, title):
	fig, ax = plt.subplots(nrows=1, ncols=3, sharex=True, figsize=(9, 5))
	ax.bar(edges1[:-1], hist1/sum(hist1), label="Actual Rust")
	ax.set_yscale("log")
	ax.set_ylabel(f"Probability of Generation (log)")
	ay.set_xlabel(f"Number Generated")
	ax.set_title(f"{sum(hist1)} Term Randomness Test")
	plt.show()
		
def random_benchmark(s_gen, e_gen, gen_step, src= "rust"):
	errors = []
	iter_times = []
	trials = np.arange(s_gen, int(e_gen), int(gen_step))
	s = perf_counter()
	for i in trials:
		s1 = perf_counter()
		hist1, edges1 = gen_bin(1, 11, int(i), src)
		e1 = perf_counter()
		iter_time = str(e1 - s1)
		iter_times.append(iter_time)
		print(f"Rust Rand Runtime Total#{i} {iter_time} s")
		err = abs(hist1/sum(hist1) - (1/10))
		errors.append(sum(err)/10)		
	e = perf_counter()
	print(f"Rust Rand Runtime: {e - s} s")
	final = pd.DataFrame({"Total Numbers": trials, "Avg. Error": errors, "Runtime": iter_times})
	final.to_csv(f"{src}_test_{len(trials)}.csv", index=False)
	
if __name__ == "__main__":
	# random_benchmark(10, 1e5 + 10, 10)
	# random_benchmark(10, 1e5 + 10, 10, "random")
	random_benchmark(10, 1e5 + 10, 10, "numpy")
	
	

