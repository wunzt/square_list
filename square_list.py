# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 5/9/22
# Description: Mutates list by squaring each element.

def square_list(val):
  """Mutates list by squaring each element."""
  i = 0
  while i < len(val):
    val[i] *= val[i]
    i += 1