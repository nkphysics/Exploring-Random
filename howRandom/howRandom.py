import numpy as np
from random import randrange
import matplotlib.pyplot as plt
from time import perf_counter
import rust_rand
import pandas as pd

	
def gen_bin(min_val, max_val, total, src="rust"):
	ints = []
	for i in range(0, total):
		if src == "numpy":
			ints.append(np.random.randint(min_val, max_val, dtype=np.int8))
		elif src == "random":
			ints.append(randrange(min_val, max_val))
		elif src == "rust":
			ints.append(rust_rand.rand_rust_func(min_val, max_val))
	hist, edges = np.histogram(ints, np.arange(min_val, max_val + 1, 1))
	return hist, edges
	
def opt_genbin(min_val, max_val, total, src="rust"):
	ints = 0
	if src == "rust":
		ints = rust_rand.rand_opt(min_val, max_val, total, "fill")
	elif src == "numpy":
		ints = np.random.randint(min_val, max_val, total)
	hist, edges = np.histogram(ints, np.arange(min_val, max_val + 1, 1))
	return hist, edges
	
def nump_genbin(min_val, max_val, total, src="rust"):
	ints = np.zeros(total)
	for i in range(0, total):
		if src == "numpy":
			ints[i] = np.random.randint(min_val, max_val, dtype=np.int8)
		elif src == "random":
			ints[i] = randrange(min_val, max_val)
		elif src == "rust":
			ints[i] = rust_rand.rand_rust_func(min_val, max_val)
	hist, edges = np.histogram(ints, np.arange(min_val, max_val + 1, 1))
	return hist, edges
	
def runtime_plot(data_files, labels, title, filename):
	plt.style.use("dark_background")
	fig, ax = plt.subplots(sharey=True)
	ax.set_ylabel("Time (s)")
	ax.set_xlabel("# of Random Ints Generated")
	# ax.set_yscale("log")
	# ax.set_xscale("log")
	dcnt = 0
	fig.suptitle(title)
	colors = ["orangered", "aqua", "gold", "fuchsia", "lime", "ivory"]
	for i in data_files:
		din = pd.read_csv(i)
		src = labels[dcnt]
		ax.plot(din["Total Numbers"], din["Runtime"], label=src, color=colors[dcnt])
		dcnt += 1
	plt.legend()
	plt.grid(which="minor")
	plt.savefig(f"{filename}.jpg", format="jpg")
		
def random_benchmark(s_gen, e_gen, gen_step, src= "rust", mode="std"):
	errors = []
	iter_times = []
	trials = np.arange(s_gen, int(e_gen), int(gen_step))
	s = perf_counter()
	for i in trials:
		if mode == "std":
			s1 = perf_counter()
			hist1, edges1 = gen_bin(1, 11, int(i), src)
			e1 = perf_counter()
			iter_time = str(e1 - s1)
			iter_times.append(iter_time)
			print(f"{src} Rand Runtime Total#{i} {iter_time} s")
			err = abs((hist1/(e_gen - gen_step)) - (1/len(hist1)))
			errors.append(sum(err)/10)
		elif mode == "nump":
			s1 = perf_counter()
			hist1, edges1 = nump_genbin(1, 11, int(i), src)
			e1 = perf_counter()
			iter_time = str(e1 - s1)
			iter_times.append(iter_time)
			print(f"{src} Rand Runtime Total#{i} {iter_time} s")
			err = abs((hist1/(e_gen - gen_step)) - (1/len(hist1)))
			errors.append(sum(err)/10)
		else: 
			s1 = perf_counter()
			hist1, edges1 = opt_genbin(1, 11, int(i), src)
			e1 = perf_counter()
			iter_time = str(e1 - s1)
			iter_times.append(iter_time)
			print(f"{src} Rand Runtime Total#{i} {iter_time} s")
			err = abs((hist1/(e_gen - gen_step)) - (1/len(hist1)))
			errors.append(sum(err)/10)
	e = perf_counter()
	print(f"Total Rand Runtime: {e - s} s")
	final = pd.DataFrame({"Total Numbers": trials, "Avg. Error": errors, "Runtime": iter_times})
	final.to_csv(f"{mode}-{src}_test_{e_gen-gen_step}.csv", index=False)
	
if __name__ == "__main__":
	runtime_plot(["std-rust_test_100000.0.csv", "nump-rust_test_100000.0.csv", "fill-opt-rust_test_100000.0.csv", "push-opt-rust_test_100000.0.csv"], ["python array", "np.array", "rust vector filled", "rust vector push"], "Runtime for Generating Random Ints w/ Rust", "rust-runtime")
	

