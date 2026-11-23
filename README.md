# tiny-chess-01 entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/khoirulr3331/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/khoirulr3331/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4 KB chess engine in a single `main.py` (LZMA-packed, stdlib only).

- 0x88 board, pseudo-legal move generation with lazy legality checks
- Negamax alpha-beta with iterative deepening to a fixed node budget
  (100,000 nodes), transposition table, killer moves, MVV-LVA ordering
- Quiescence search (captures, promotions; all evasions when in check)
- Null-move pruning, threefold-repetition detection from game history
- Tapered evaluation: material + piece-square tables, endgame king table
  that takes over as material leaves the board
- Fully deterministic: no wall clock, no unseeded randomness, so replayed
  trials play the same moves.

Local practice trials (kit's sealed scorer, manual env runs):
trial-0 Elo 1451 (4W 0D 2L), trial-1 Elo 1451 (4W 0D 2L),
trial-2 Elo 1364 (3W 1D 2L). Re-running trial-0 reproduces its
transcript byte-for-byte (deterministic).
