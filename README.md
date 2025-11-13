## Representing periodic systems with one-electron integral matrices
<p align="center">
  <img src="images/image_1.png" width="700" />
</p>

### Welcome! 👋
This repository supports the research paper of the same name, where we investigate how one-electron integrals can be used as an effective and robust materials representation. Here you’ll find the code, data, and tools used to develop and validate the approach. 

The code in this repository allows you to generate the TM, VM, and SM representations.
Notably, for the QMOF dataset and the prediction of the PBE band gap, the TM representation demonstrates the strongest performance compared to the others.

### ❓ Why This Project?
There are many ways to represent materials—everything from simple text-based formats to computer-vision-style features and physics-inspired descriptors. But unlike the molecular world, materials science rarely uses quantum-inspired electronic information as part of the representation.
A big reason for this is that generating such data has traditionally been slow, complex, and not very practical for large datasets. Still, if we want a complete picture of a material, we shouldn’t ignore its electronic structure. In some cases, combining electronic information with geometry can make a big difference—and even become essential for predicting certain properties. 

Apart from that, traditional representations are often extremely large, making them difficult to handle and challenging to use as input for machine learning models.
The table below illustrates this for several widely used representations, showing the number of features and the memory required to load or store these arrays for 2,000 randomly selected compounds from the QMOF dataset.

<div align="center">

<table>
  <tr>
    <th>Representations</th>
    <th>Dimensions</th>
    <th>Memory [MB]</th>
  </tr>
  <tr>
    <td>MBTR</td>
    <td><img src="https://img.shields.io/badge/28800-green"></td>
    <td><img src="https://img.shields.io/badge/439.54-green"></td>
  </tr>
  <tr>
    <td>LMBTR</td>
    <td><img src="https://img.shields.io/badge/384000-yellow"></td>
    <td><img src="https://img.shields.io/badge/5859.46-yellow"></td>
  </tr>
  <tr>
    <td>SM</td>
    <td><img src="https://img.shields.io/badge/250000-yellow"></td>
    <td><img src="https://img.shields.io/badge/3814.79-yellow"></td>
  </tr>
  <tr>
    <td>ESM</td>
    <td><img src="https://img.shields.io/badge/250000-yellow"></td>
    <td><img src="https://img.shields.io/badge/3814.79-yellow"></td>
  </tr>
  <tr>
    <td>SOAP</td>
    <td><img src="https://img.shields.io/badge/5362560-red"></td>
    <td><img src="https://img.shields.io/badge/81826.26-red"></td>
  </tr>
  <tr>
    <td>TM, VM, SM</td>
    <td><img src="https://img.shields.io/badge/34992-green"></td>
    <td><img src="https://img.shields.io/badge/534.02-green"></td>
  </tr>
</table>

</div>

## 🔧 Installation

To generate the representations based on one-electron integrals, install the package using:

```bash
pip install one_electron_matrices
```
The code depends on the following packages: [NumPy](https://numpy.org/), [Pandas](https://pandas.pydata.org/), [ASE](https://ase-lib.org/), and [ASE](https://pyscf.org/).
