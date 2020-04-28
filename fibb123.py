# running this code as __main__ module
# __main__ means the current script file
def fib(n): 
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b
   return result

if __name__ == "__main__":
   f = fib(100)
   print(f)