# Metaheuristics

This repository contains code and resources for a university course on Metaheuristics and stochastic search algorithms.

### Author: Ahmed Samady
### Supervised by: Pr. Khalid Jebari

## Overview

The purpose of this repository is to provide implementations of various metaheuristic algorithms in Python and C++. It covers topics such as Genetic Algorithms, Simulated Annealing, Multi-Verse Optimizer, and more.
## Note

The Python implementations in this repository for GWO [[1]](#1)[[2]](#2), MVO [[3]](#3)[[4]](#4), and ALO [[5]](#5)[[6]](#6) are adapted from the MATLAB implementations by Dr. Seyedali Mirjalili.
### Hashing Algorithms

|       Algorithm       |       Python       |        C++         |
|-----------------------|--------------------|--------------------|
| Genetic Algorithms    |        :x:         | :white_check_mark: |
| Tabu Search           |        :x:         | :white_check_mark: |
| Simulated Annealing   | :white_check_mark: |        :x:         |
| Multi-Verse Optimizer | :white_check_mark: |        :x:         |
| Ant Lion Optimizer    | :white_check_mark: |        :x:         |

## Getting Started
To get started with this repository, follow these steps:
Clone the repository:
```bash
git clone -b main --single-branch [https://github.com/Samashi47/Metaheuristics]
```
Navigate to the directory of the cloned repository:
```bash
cd Metaheuristics
```
### Python
Create a virtual environment in the repository by typing the followwing command:
```bash
python -m venv /path/to/repo/on/your/local/machine
```
After cloning the project and creating your venv, activate the venv by:

```bash
.venv\Scripts\activate
```
You can run the following command to install the dependencies:
```bash
pip3 install -r requirements.txt
```
### C++
Compile the C++ files. For example, to run the `Simulated Annealing` implementation, you can compile the `sa.cpp` file in the `Simulated Annealing` folder using g++:
```bash
g++ -o sa sa.cpp
```
Run the compiled file:
```bash
./sa
```
## Contributing

Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Contact

For any questions or inquiries, please contact the owner of this repository or open an issue.

Happy coding!

## References

<a id="1">[1]</a> Seyedali Mirjalili (2024). Grey Wolf Optimizer (GWO) [MATLAB Central File Exchange](https://www.mathworks.com/matlabcentral/fileexchange/44974-grey-wolf-optimizer-gwo). Retrieved April 22, 2024. \
<a id="2">[2]</a> Mirjalili, S., Mirjalili, S. M., & Lewis, A. (2014). Grey Wolf Optimizer. Advances in Engineering Software, 69, 46–61. doi:10.1016/j.advengsoft.2013.12.007 \
<a id="3">[3]</a> Seyedali Mirjalili (2024). Multi-Verse Optimizer (MVO) [MATLAB Central File Exchange](https://www.mathworks.com/matlabcentral/fileexchange/50112-multi-verse-optimizer-mvo). Retrieved April 22, 2024. \
<a id="4">[4]</a> Mirjalili, S., Mirjalili, S. M., & Hatamlou, A. (2015). Multi-Verse Optimizer: a nature-inspired algorithm for global optimization. Neural Computing and Applications, 27(2), 495–513. doi:10.1007/s00521-015-1870-7 \
<a id="5">[5]</a> Seyedali Mirjalili (2024). Ant Lion Optimizer (ALO) [MATLAB Central File Exchange](https://www.mathworks.com/matlabcentral/fileexchange/49920-ant-lion-optimizer-alo). Retrieved April 22, 2024. \
<a id="6">[6]</a> Mirjalili, S. (2015). The Ant Lion Optimizer. Advances in Engineering Software, 83, 80–98. doi:10.1016/j.advengsoft.2015.01.010 \