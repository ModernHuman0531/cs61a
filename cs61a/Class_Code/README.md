# Effiency
* Take fibonacci sequence as example, you need to recalculate the same stuff over and over again.For example, if we want to calculate Fib(5), we need to calculate fib(4) and fib(3), but we already
  count Fib(3) when we count Fib(4), it's kind of waste time to calculate itagain.
* So we may right a helper function that will do the following:
  * If we have not calculte the Fib(n), calculate the corresponding number and store it into the dictionary.
  * If it the we have already calculated Fib(n), then we don't need to calculate it, just take the value from the dictionary.
  * Code:
    ```python
    def memo(f):#f is the function that we need remember it's value
      ans_dict = {}
      def memorized(n):#Use key in the dictionary to find the corresponding value
        if n nor in ans_dict:
          ans_dict[n] = f(n)# dict[Key value] = corresponding value of that key
        return ans_dict[n]
      return memorized
    ```
# Order of growth
* The growth of the time as the **amount of input** increase
* Common type:
    * Exponetial growth(ex.fib):formula => $`a*b^{n+1}`$(Time for input n+1) =  $`a*b^{n}*b`$(Tiem for input n)
    * Quadratic growth(ex.overlap of the sequence)=> $`a*(n+1)^2`$(Time for input n+1) =  $`a*n^2+a*(2n+1)`$(Tiem for input n)
    * Linear growth(slow exponetial)=> $`a*(n+1)`$(Time for input n+1) =  $`a*n+a`$(Tiem for input n)
    * Logarithmic growth(ex.exp_fact)=> $`a*ln(2n)`$(Time for input 2n) =  $`a*ln(n)+a*ln(2)`$(Tiem for input n)
    * Constant growth(Increasing of the input doesn't affect time)
          
