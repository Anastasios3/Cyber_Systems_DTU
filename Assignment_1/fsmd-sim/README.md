The FSMD (Finite State Machine with Datapath) project

- 1st it parses XML description files that define everything about an FSMD. (Assignment_1/fsmd-sim/test_3/double_desc.xml)

- 2nd it optionally parses also stimuli files that explain the input values over time and state for exiting simulation (Assignment_1/fsmd-sim/test_3/double_stim.xml)

- 3rd Cycle by cycle run. each cycle select the transition, execute update and advance the counter. A simpler CRUD in other words.

- 4th test folder have three different FSMD instances to verify it works properly.

python3 fsmd-sim.py <number_of_cycles> <description_file> [stimuli_file_optional]
