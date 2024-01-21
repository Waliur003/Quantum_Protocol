from qiskit import *

circuit = QuantumCircuit(3, 3)

circuit.x(0)
circuit.barrier()

circuit.h(1)
circuit.cx(1, 2)

circuit.cx(0, 1)
circuit.h(0)

circuit.barrier()
circuit.measure([0, 1], [0, 1])

circuit.barrier()
circuit.cx(1, 2)
circuit.cz(0, 2)
circuit.draw(output='mpl', style = 'iqp')

#now measure it by initaitilizing simulator and visualize it plot_histogram
circuit.measure(2, 2)
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots =1024).result()
counts = result.get_counts()
from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)