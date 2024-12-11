# Ising Model Repository
Connie Yang, Thomas Leishner, Thida Lay-Sok

## Installation
To install dependencies, run the following command:
```
pip install -r requirements.txt
```
The main Jupyter Notebook is the file titled “project_ideas.ipynb”, which users can go through and run the cells after installing the requirements.

## Overview 
The **Ising model** is a mathematical model used in statistical mechanics to study ferromagnetism, phase transitions, and critical phenomena in condensed matter physics. It describes how individual spins, representing magnetic moments, interact in a lattice structure. 

To study the system’s behavior, we use the **Metropolis Algorithm**, which employs a **Monte Carlo** method to simulate spin configurations at a given temperature.

### Key Features of the Ising Model
**Lattice Structure:**
Spins are arranged on a lattice, which can be one-dimensional (1D), two-dimensional (2D), or three-dimensional (3D).
Each spin, Si, can take one of two values: +1 (up) or -1 (down).

**Hamiltonian (Energy Function):**
The energy of the system is defined by the Hamiltonian in the general form: 

<img width="196" alt="image2" src="https://github.com/user-attachments/assets/d157f41b-89d7-4cbc-80df-4e4f74f57157">

Where S_i is the orientation of each spin, J is the interaction strength between nearest-neighbor spins, and H is the strength of an external magnetic field.
**Interactions:**
Spins tend to align in the same direction if J>0 (ferromagnetic interaction) or in opposite directions if J<0 (antiferromagnetic interaction)

**Phase Transitions:**
In 2D and higher dimensions, the model exhibits a phase transition at a critical temperature $T_c$​

Below $T_c$​, the system shows spontaneous magnetization (ordered phase)


Above $T_c$​, the spins are disordered due to thermal fluctuations

### Implementing the Metropolis Model
The **Monte Carlo method** is a broad class of computational algorithms that rely on randomness to solve problems, particularly those involving the simulation of systems with many degrees of freedom. The **Metropolis method** is a specific implementation of the Monte Carlo method, tailored for sampling configurations in statistical mechanics.

**Metropolis Method as a Specialization:**
* The Metropolis method refines the Monte Carlo approach by introducing a systematic way to accept or reject sampled configurations based on their energy.
* It ensures that the sampled configurations follow the Boltzmann distribution, where lower-energy states are more probable but higher-energy states can occur with decreasing likelihood proportional to $e^{−ΔE/k_{BT}}$.

In summary, the Metropolis method is a Monte Carlo technique designed specifically for systems in equilibrium statistical mechanics, making it ideal for studying models like the Ising model. It combines the randomness of Monte Carlo with the selective acceptance of configurations based on physical principles, such as the Boltzmann distribution.
	
 We used the following steps to implement the model:
1. Build lattice and assign spins
2. Select random particle

   a) Instead of selecting a random particle, we updated all the particles during each step

4. Calculate the change in energy if particle is flipped

5. If energy < 0, the flip is accepted
6. If random.random() < np.exp(-delta_E / T), flip spin
7. Repeat for number of steps
![image18](https://github.com/user-attachments/assets/591509c7-a232-42fb-9361-ea5952d90841)



### Ising Model
In the 1D model, each spin interacts only with its nearest neighbors on either side (left and right), forming a single linear chain. Spins in a chain might look something like this:

	↑↓↑↑↓↑

Where each arrow represents a spin, which evolves depending on temperature and the neighboring interactions. 
**Behavior:**
* The 1D Ising model **does not exhibit a phase transition** at finite temperatures.
* At any nonzero temperature, thermal fluctuations dominate, preventing long-range magnetic order
* Only at absolute zero (T=0) does the system achieve full alignment of spins (ferromagnetic order).

### 2D Ising Model
In the 2D model, spins are arranged on a lattice (typically square or rectangular) where each spin interacts with its nearest neighbors in the horizontal and vertical direction. 

Spins on a 2D grid might look like this:
```
  ↑↑↓↑
  ↓↑↑↓
  ↑↓↓↑
  ↑↑↑↓
```
The arrangement evolves based on temperature and interaction strength

**Behavior:**
The 2D Ising model exhibits a phase transition at a critical temperature $T_c$.
* Below $T_c$: Spins align to create long-range magnetic order (ferromagnetic phase).
* Above $T_c$: Thermal fluctuations dominate, and the system becomes disordered (paramagnetic phase).

![image11](https://github.com/user-attachments/assets/2958c74d-7f8e-4d98-82d2-00267b2d114c)
J=1, T=0.1, H=0

The ferromagnetic phase is characterized by a spontaneous magnetization developing below $T_c$, even without an external field (h=0). The paramagnetic phase is characterized by the random alignment of spins above $T_c$, in which the average magnetization is 0. The critical temperature at which the phase transition occurs can be seen where the two phases intersect in the plots of average magnetization vs temperature.

![image6](https://github.com/user-attachments/assets/36215f92-b4e4-4513-859e-0b132a78561a)
![image13](https://github.com/user-attachments/assets/808e28d6-6134-4ef7-8095-457ae28ccf2b)
![image12](https://github.com/user-attachments/assets/b9d41920-8d98-427d-87e6-f3da5ea4cc0f)


The phase transition can be visualized in plots of average magnetization, energy, and heat capacity as functions of temperature. In these plots, the critical temperature corresponds to the steep jumps in average magnetization and energy and the sharp peaks in average heat capacity.

For our project, we extended the generic Ising model by incorporating different interaction types and implementing the model on Cayley graphs.
### Different Interaction Types
**Next Nearest Neighbor:**
This adds another term to the Hamiltonian with interaction strength $J_2$. This adds extra complexity to the phase and introduces frustration to the system. 

<img width="452" alt="image8" src="https://github.com/user-attachments/assets/88c593f3-050e-4655-b8ec-16065a936a44">
<img width="452" alt="image14" src="https://github.com/user-attachments/assets/58590b93-b922-4716-afeb-87da34d4b30b">
<img width="452" alt="image9" src="https://github.com/user-attachments/assets/39583aa9-160c-49f8-b1c0-9cc2d4f06c19">

$J_1$ = 0.5 and $J_2$ = -0.5

Frustration is when there are competing interactions between spins that prevent the system from minimizing its energy. Can occur when $J_1$ > 0 and $J_2$ < 0 

![image19](https://github.com/user-attachments/assets/00da932b-37a1-4e63-a18f-ee36ba8d91a4)


Represented by the Hamiltonian: 

![image21](https://github.com/user-attachments/assets/90773eeb-6a92-4085-9f49-73b698c2d2c4)


**Non-Reciprocal Interactions:**
This is when the interaction strength between two spins are not the same both ways. This interaction changes the Hamiltonian of the Ising model to become the equation below: 

![image15](https://github.com/user-attachments/assets/29bc5459-1bc7-4bda-a2f6-917aefa5a568)

To implement this, we had to compute the summation of the product between neighbors and the interaction strength associated with their relative position. Frustration can also be present in this system due to the possibility of competing interaction strengths.

<img width="452" alt="image8" src="https://github.com/user-attachments/assets/6ec3a53d-79ea-4f82-bcc3-383b0e013893">

<img width="452" alt="image20" src="https://github.com/user-attachments/assets/bef31206-bdc8-4e1a-b1e7-96bea4adc919">

<img width="452" alt="image16" src="https://github.com/user-attachments/assets/38892a54-63c6-42fd-abe2-0d66a82322ad">

<img width="452" alt="image3" src="https://github.com/user-attachments/assets/77e0d09d-b68c-4bbc-ae1e-068f0cf0b9ac">


$J_{top}= 1.0, J_{bottom} = 0.5, J_{left} = 1.2, J_{right}  = 0.8$

### Cayley Tree
In addition to different types of interactions, we also wanted to test the behavior of the Ising model on systems with different geometries. To do so, we implemented the generic Ising model Hamiltonian, with only nearest neighbor interactions, on a closed Cayley tree. A Cayley tree is a tree where all nodes (i.e. vertices) except the root and leaf nodes have the same number of edges. To create a closed system with periodic boundary conditions, we connected 2 identical open trees at the leaf nodes. Our implementation can also be extended to explore Ising models on any other type of graph.
![image1](https://github.com/user-attachments/assets/fe6d00b1-1a1b-414d-a691-9cacb7027e37)
![image5](https://github.com/user-attachments/assets/66808254-a464-4251-b531-d1926b18558b)
k=2, J=1, H=0

![image4](https://github.com/user-attachments/assets/2c3a311a-a964-4f02-9fa1-646c82435e2f)



![image17](https://github.com/user-attachments/assets/93d6dec9-f861-490e-8f76-13d69fef9340)

![image10](https://github.com/user-attachments/assets/5b788288-1a09-4305-9809-80a2d5b8dcd9)

k=2, J=1, initially 75% down, 100 MC iterations

The plots of average magnetization, energy, and heat capacity are smooth functions of temperature (with some jaggedness due to statistical fluctuations), indicating the absence of a phase transition. The plots exhibit very similar shapes for double Cayley trees with other branching ratios k. It can be inferred that the presence of minimal cycles significantly reduces the ability of the system to exhibit collective behavior, even if each spin has a large number of neighbors. We can also see that the ferromagnetic character of the system is enhanced, as higher values of temperature and external field strength were needed to see noticeable trends in these plots.

## Resources
https://arxiv.org/pdf/2105.00841v1
https://www.sciencedirect.com/science/article/pii/0378437179901341 
https://journals.aps.org/prb/pdf/10.1103/PhysRevB.109.064422 
https://www.lapasserelle.com/statistical_mechanics/lesson_9.pdf
https://arxiv.org/abs/2403.06875
https://arxiv.org/pdf/2311.05471

## Credits
Special thanks to Dr. William Gilpin (wgilpin@utexas.edu), Aditi Pujar (aditiajithpujar@utexas.edu), Carson McVay (carsonmcvay@utexas.edu), and Anish Pandya (apandya@utexas.edu) for teaching the course!
