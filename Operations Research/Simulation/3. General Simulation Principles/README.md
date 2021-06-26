## Steps in a Simulation Study
1. Problem Formulation - problem statement
2. Objectives & Planning
3. Model Building - M/M/k model? Equations/Random variates involved
4. Data Collection - — what kinds of data, how much? Continuous? Discrete?
5. Coding
6. Verification - is the code ok? If no, go back to 5.
7. Validation - is the model ok? If no, go back to 3. and 4.
8. Experimental Design - What experiments need to be run? Statistical consideration? Time/budget?
9. Run Experiments
10. Output Analysis - statistical analysis, relevant measures of performance, often iterative with 8 and 9.
11. Write Reports, convince management, implement.

## Definitions:
* <ins>A system</ins> is a collection of entities (people, machines, etc.) that interact together to accomplish a goal.
* <ins>A model</ins> is an abstract representation of a system, usually containing math/logical relationships describing the system in terms of states, entities, sets, events, etc.
* <ins>System state:</ins> A set of variables that contains enough information to describe the system. Think of the state as a system “snapshot.” E.g., in a single-server queue, all you might need to describe the state are: LQ(t) = number of people in queue at time t, and B(t) = 1 [0] if server is busy [idle] at time t.
* <ins>Entities</ins> can be permanent (e.g., a machine) or temporary (e.g., customers), and can have various properties or attributes (e.g., priority of a customer or average speed of a server)
* <ins> A list (or queue) </ins> is an ordered list of associated entities (e.g., a
linked list, or a line of people).
* <ins>An event</ins> is a point in time at which the system state changes (and which can’t be predicted with certainty beforehand). E.g., an arrival event, a departure event, a machine breakdown event. “Event” technically means the time that the thing happens, but loosely refers to “what” happens (e.g., an arrival)
* <ins>An activity</ins> is a duration of time of specified length (aka an unconditional wait). E.g., an exponential customer interarrival time or a constant service time (since we can explicitly generate those).
* <ins>A conditional wait</ins> is a duration of time of unspecified length. E.g., a customer waiting time — we don’t know that directly (we just know arrival and service times).

## Time Advance Mechanisms
* The simulation clock is a variable whose value represents simulated time (which doesn’t equal real time)
* Time-Advance Mechanisms — how does the clock move?
    * Always moves forward (never goes back in time). Two ways:
    * Fixed-Increment Time Advance: Update the state of the system at fixed times, nh, n = 0, 1, 2, . . ., where h is chosen appropriately. This is used in continuous-time models (e.g., differential equations) and models where data are only available at fixed times
    * Next-Event Time Advance: The simulation clock is initialized at 0. Times of all known future events are determined and placed in the future events list (FEL), ordered by time. The clock advances to the most imminent event, then to the next most imminent event, etc. At each event, the system state is updated, and the FEL is updated. 
    * Any time there’s an event, the simulation may update the chronological order of the FEL’s events by inserting new events, deleting events, moving them around, or doing nothing

## Modelling Approaches:
* There are 2 main modelling approaches to simulation:
    1. Event-scheduling Approach - Concentrate on the events and how they affect the system state. Help the simulation evolve over time by keeping track of every event in increasing order of time of occurrence.
    2. Process-Interaction Approach. Concentrate on a generic customer (entity) and the sequence of events and activities it undergoes as it progresses through the system. At any time, the system may have many customers interacting with each other as they compete for resources