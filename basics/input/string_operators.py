# Program that monitors Beep's health

def run():
  
  print("What is Beep's health status?")
  print()
  print("Please enter the number of lives.")
  lives = int(input())
  print()
  print("Please enter the energy level.")
  energy = int(input())
  print()
  print("Please enter the shield level.")
  shield = int(input())
  print()
  print("Health has been set.")
  print()
  print("Lives:","♥" * lives)
  print("Energy:","♦" * energy)
  print("Shield:","♦" * shield)