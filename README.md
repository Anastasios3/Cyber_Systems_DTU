# Cyber_Systems_DTU

# About Assignment_1

The FSMD (Finite State Machine with Datapath) project

- 1st it parses XML description files that define everything about an FSMD. (Assignment_1/fsmd-sim/test_3/double_desc.xml)

- 2nd it optionally parses also stimuli files that explain the input values over time and state for exiting simulation (Assignment_1/fsmd-sim/test_3/double_stim.xml)

- 3rd Cycle by cycle run. each cycle select the transition, execute update and advance the counter. A simpler CRUD in other words.

- 4th test folder have three different FSMD instances to verify it works properly.

#-------------------------------------------------------------------------------------------
Final report formatting

1. Intor (1/2 page)

2. FSMD model background (1/2 to 1 page)

3. The architecture of the simulator (2 to 3 pages)

4. Tests 1,2, and 3 (1_1/2 to 2 pages)

5. Discusiion on limitations and thoughts in general ( 1/2 page)

python3 fsmd-sim.py <number_of_cycles> <description_file> [stimuli_file_optional]
