use rand::Rng;
use pyo3::prelude::*;

#[pyfunction]
fn rand_rust_func(low: i8, high: i8) -> PyResult<i8> {
	let num: i8 = rand::thread_rng().gen_range(low..high);
	Ok(num)
}

#[pymodule]
fn rust_rand(_py: Python<'_>, m: &PyModule) -> PyResult<()>{
	m.add_function(wrap_pyfunction!(rand_rust_func, m)?)?;
	Ok(())
}
