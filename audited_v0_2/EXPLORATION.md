# Discovery record (not mathematical evidence for upper bounds)

2026-10-22, same-assistant exploration. No existing No.32 artifacts were
modified. This note records dead ends so that timeout results are not
subsequently mistaken for impossibility proofs.

| Task | Search outcome | Use |
|---|---|---|
| C4, 4 colors | SAT; all 84 proper colorings checked | Reproduction of known small case |
| C4, 5 colors | Solver returned UNSAT | Exploratory consistency check only; no delivered nonexistence proof relies on it |
| C5, 5 colors | UNKNOWN at short time limit | No conclusion; not the chosen candidate |
| C6, 5 colors | UNKNOWN at short time limit | No conclusion |
| Diamond K4-e, 6 colors | SAT; all 480 proper colorings checked | Reproduction of known small case |
| Hourglass, 6 colors | SAT; all 2,400 proper colorings checked | Initial witness, then simplified |
| Five-vertex fan, 6 colors | SAT; all 1,920 proper colorings checked | Side observation, not a main theorem here |
| Four-rim wheel, 7 colors | UNKNOWN at short time limit | No conclusion |
| Hourglass, 7 colors | UNKNOWN at short time limit | Replaced by a direct general proof, not a computational exclusion |
| Five-vertex fan, 7 colors | UNKNOWN at short time limit | No conclusion |
| Three/four petals, 7 colors, unrestricted search | UNKNOWN at short time limits | No conclusion from those runs |
| Two petals, 6 colors, cyclic and leaf-symmetric | SAT; zero failed full colorings | Simplified final six-color witness |
| Three petals, 7 colors, cyclic | SAT; zero failed full colorings | Simplified to a six-entry table with scaling |

The delivered proof and both delivered verifiers are independent of the
exploratory SAT package. Search restrictions can prove existence when a
witness is found; they cannot prove impossibility in the unrestricted model.

The exact-choice SAT encodings and recorded exploratory logs are retained
in discovery/. They are unnecessary for checking the tables and proof
delivered in the bundle root; re-running discovery requires the optional
free python-sat package.
