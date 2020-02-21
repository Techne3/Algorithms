#!/usr/bin/python

import math


# 	recipe    { 'milk': 100, 'butter': 50, 'flour': 5 }
# ingredients  { 'milk': 138, 'butter': 60, 'flour': 51 }

def recipe_batches(recipe, ingredients):
  batches = []
  # Check to make sure that ingredients in both lists match.
  if ingredients.keys() != recipe.keys():
    return 0
  else:
    # Divide available ingredients by required ingredients, append to list.
    for key in recipe.items():
      batches.append(ingredients[key] // recipe[key])
      return min(batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 488, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))