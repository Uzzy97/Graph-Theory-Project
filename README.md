# Graph Theory

It is a program in the Python programming language that can build a non-deterministic finite automaton (NFA) from a regular expression, and can use the NFA to check if the regular expression matches any given string of text.

## Thompson's Construction

* Algorithm made by ken thompson in 1960’s.
* Convert regular expressions into a Non-Deterministic Finite Automaton.
* This is one way to convert a regular expression into an NFA.
* Thompson's Construction is a simple and systematic method. It guarantees that the resulting NFA will have exactly one final state and one start state.
* Thompson's Construction works on fragments of NFA.
* Make bigger NFA from smaller ones.
* Normal characters push fragments to the stack.
* Special characters pop from and push to the stack.

  ### Example
  ![WhatsApp Image 2019-03-31 at 15 56 06](https://user-images.githubusercontent.com/26766158/55290763-32600500-53cf-11e9-9505-f4e99a4d3218.jpeg)


  ### Research

  Research conducted for Thompson's Construction

  ```
  https://www.youtube.com/watch?v=62JAy4oH6lU
  ```

### Installing
