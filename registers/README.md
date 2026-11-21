# Registers

A register is a structured table for anything you will look up twice. Recall becomes a file lookup instead of a re-audit, which is what keeps an assistant from guessing or forgetting.

## When to make one

- The same question keeps coming back (What do I own? What did I post? What is still open?)
- The data has rows and fields, not stories
- Being wrong about it would cost time or money

## Rules

- One register per subject, CSV so anything can read it.
- Every row carries an identifier and a status.
- When the underlying work changes, update the register the same day.
- The core memory file holds a pointer to each register, not its contents.

## Template columns

See `register-template.csv`. Adapt the columns to the subject; keep `id` and `status` whatever you build.
