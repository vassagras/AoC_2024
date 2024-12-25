import time
import os
import re

def logic_gate_compute(wr_1, wr_2, op):
    """

    :param wr_1: wire 1 input
    :param wr_2: wire 2 input
    :param op: a bitwise operator i.e. AND (&), OR (|) or XOR (^)
    :return:
    """
    if op == "XOR":
        return wr_1 ^ wr_2
    elif op == "OR":
        return wr_1 | wr_2
    elif op == "AND":
        return wr_1 & wr_2
    return None

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 24"), 'r')

wire_values = {}
z_gate_values = {}
gate_operations = {}
for line in file:
    # Input wires
    if ":" in line:
        elements = line.replace("\n", "").split(":")
        wire_values[elements[0]] = int(elements[1])
    # Gates and wires connected to them
    elif "->" in line:
        elements = line.replace("\n", "").split("->")
        new_gate = elements[1].strip()
        ops = re.findall(r"(.*) (OR|AND|XOR) (.*)", elements[0].strip())[0]
        wire_1, operator, wire_2 = ops

        # if both gate wires start with either x or y, then the wire values are part of the inputs
        if (wire_1.startswith("x") or wire_1.startswith("y")) and (wire_2.startswith("x") or wire_2.startswith("y")):
            w1 = int(wire_values[wire_1])
            w2 = int(wire_values[wire_2])
            wire_values[new_gate] = logic_gate_compute(w1, w2, operator)
            # if a z-gate value is possible to be calculated while reading the input data, then store the value
            if new_gate.startswith("z"):
                z_gate_values[int(new_gate[1:])] = logic_gate_compute(w1, w2, operator)
        else:
            gate_operations[elements[1].strip()] = ([wire_1, wire_2], operator)

# keep a list of all the gates for which the value is not calculated yet
to_compute = list(gate_operations.keys())
while to_compute:
    for gate, v in gate_operations.items():
        # calculate the value of a gate only if both input wires values are available
        if v[0][0] in wire_values and v[0][1] in wire_values and gate in to_compute:
            w1 = int(wire_values[v[0][0]])
            w2 = int(wire_values[v[0][1]])
            operator = v[1]
            wire_values[gate] = logic_gate_compute(w1, w2, operator)
            # if a z-gate value is possible to be calculated while reading the input data, then store the value
            if gate.startswith("z"):
                z_gate_values[int(gate[1:])] = logic_gate_compute(w1, w2, operator)
            # Remove gate from the list of the ones to be computed
            to_compute.remove(gate)

digits = []
for i in range(len(z_gate_values) - 1, -1, -1):
    digits.append(str(z_gate_values[i]))
n = "".join(digits)
nn = int(n, 2)

end = time.time()
print("Part 1 result: {}".format(nn))
print("The time of execution of above program is :", (end - start) * 10 ** 3, "ms")
print()