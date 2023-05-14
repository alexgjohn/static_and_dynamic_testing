### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
  #equality operator must be ==
  # else statement is missing colon  

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  # def misspelt as dif, meaning method will not run. 
  # missing comma between parameters
  # missing indentation from if statement onwards
  # 'return card' - card is not one of the parameters
  # Also, I would call this get_highest_card()
  


def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
# method is not indented, so 'self' will not be recognised for class.
# total not defined as any data type, so cannot be added to or included as return concatenation.
# Also, lack of space means the return concatenation will be poorly presented.
# the return statement is inside the for loop, so will interrupt the loop upon the first iteration
```
