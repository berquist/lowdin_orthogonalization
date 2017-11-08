double_real_cpp: double_real.cpp
	g++ -larmadillo -o double_real.x double_real.cpp
	./double_real.x

double_real_python: double_real.py
	python double_real.py
