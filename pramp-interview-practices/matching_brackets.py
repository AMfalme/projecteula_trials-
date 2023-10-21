def bracket_match(text):
  open_needed =  0 
  closed_needed =  0 
  for index, bracket in enumerate(text):
    if bracket == '(':
      closed_needed += 1
    
    elif bracket == ')':
      if closed_needed > 0:
        closed_needed -= 1
      else:
        open_needed += 1  
    print('index ', index,)
    print('closed_needed ', closed_needed,)
    print('open_needed ', open_needed,)
    return open_needed + closed_needed
  

text = '(())'



print(bracket_match(text='(())'))
