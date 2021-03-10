task_allocator.py: 

- Generates a report of list tasks a given iteration has.
- Randomly choses two names for each tasks.
- Prints the report to terminal and also sends group members an e-mail of the report.
- Pops the iteration ran from "remainig_iterations" and updates the "tdd_done" list with names of the new testers in a config file.

Disclaimer: Script was created to make it easy for group members to dynamically change roles for each iteration i.e: 
it made sure that we always had two new testers for each iteration. After all iterations are complete the config file will need to be updated with the new project iterations and group member names, 'tdd_done' will need to be cleared. 

With Thanks