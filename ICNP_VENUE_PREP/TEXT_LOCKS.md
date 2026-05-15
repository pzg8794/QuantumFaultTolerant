# Text Locks

Use this file as the source of truth for locked non-caption prose during the ICNP venue draft cleanup.

## Locked conclusion paragraph

Locked on May 15 after transcript-based conclusion feedback. Requirements:

- Keep as one paragraph.
- No future-work sentence.
- Use plain-English takeaway language.
- Include numeric evidence only where it proves the main claims.
- End with the quantified external-testbed comparison.

```tex
This work shows that robust quantum entanglement routing under adversarial
conditions requires joint control of path selection, qubit allocation, replay
capacity, and threat response. The matched evaluation identifies
\texttt{iCPursuitNeuralUCB} as the strongest context-aware neural routing model:
it reaches 90.9\% internal average efficiency, clears the 90\% model-family
threshold, and outperforms the closest internal alternatives, which remain below
that mark. Under harder threats, adversarial-first exploration remains less
reliable: \texttt{EXPNeuralUCB} falls to an 18.0\% robustness floor, while the
strongest contextual baselines maintain floors near 77--81\%. The capacity
paradox shows why deployment tuning matters: replay capacity must be matched to
the active threat, and allocator choice directly shapes routing robustness. When
the threat is unknown, a fixed pursuit--neural deployment baseline provides a
strong starting point; when the threat is detected, allocator and replay settings
should be adapted to the threat regime. The external-testbed comparison shows
why the proposed approach is stronger than a topology-specific result:
\texttt{iCPursuitNeuralUCB} leads average efficiency on \paperTwo{} (74.5\%,
95/300 wins), \paperSeven{} (78.0\%, 245/300 wins), \paperTwelve{} (44.1\%,
97/300 wins), and \paperEight{} (67.9\%). The advantage is clearest on the dense
50-node \paperSeven{} setting, where it reaches 78.0\% versus 70.8\% for the
next strongest models, and it still remains best on the larger \paperTwelve{}
fusion topology, where all methods compress tightly at 44.1\% versus 43.8\%.
```
