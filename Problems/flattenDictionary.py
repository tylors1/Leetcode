def flatten_dictionary(dictionary, parent_key = ""):
  
  items = []
  for k, v in dictionary.items():
    new_key = parent_key + "." + k if parent_key else k
    if isinstance(v, dict):
      items.extend(flatten_dictionary(v, new_key).items())
    else:
      items.append((new_key, v))
                   
  return dict(items)
      
