def count_sort_letters(list, size, col, base, max_len, sorting_column):
  output   = [0] * size
  count    = [0] * (base + 1) 
  min_base = ord('a') - 1 

  for item in list: 
    letter = ord(item[sorting_column][col]) - min_base if col < len(item) else 0
    count[letter] += 1

  for i in range(len(count)-1): 
      count[i + 1] += count[i]

  for item in reversed(list):
    letter = ord(item[sorting_column][col]) - min_base if col < len(item) else 0
    output[count[letter] - 1] = item
    count[letter] -= 1

  return output

def sort_strings(list, sorting_column, max_col = None):
  if not max_col:
    max_col = len(max(list, key = len)) 

  for col in range(max_col-1, -1, -1): 
    list = count_sort_letters(list, len(list), col, 36, max_col, sorting_column)

  return list