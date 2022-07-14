use rand::Rng;
use pyo3::prelude::*;

#[pyfunction]
fn rand_rust_func(low: i8, high: i8) -> PyResult<i8> {
	let num: i8 = rand::thread_rng().gen_range(low..high);
	Ok(num)
}

#[pyfunction]
fn rand_opt(low: i8, high: i8, tot: usize, mode:String) -> PyResult<Vec<i8>> {
	if mode == "fill"{
		let mut rands:Vec<i8> = vec![0; tot];
		for i in 0..tot{
			let num: i8 = rand::thread_rng().gen_range(low..high).into();
			rands[i] = num;
		}
		Ok(rands)
	}
	else {
		let mut rands = Vec::new();
		for _ in 0..tot{
			let num: i8 = rand::thread_rng().gen_range(low..high).into();
			rands.push(num);
		}
		assert_eq!(rands.len(), tot);
		Ok(rands)
	}
}

#[pymodule]
fn rust_rand(_py: Python<'_>, m: &PyModule) -> PyResult<()>{
	m.add_function(wrap_pyfunction!(rand_rust_func, m)?)?;
	m.add_function(wrap_pyfunction!(rand_opt, m)?)?;
	Ok(())
}
