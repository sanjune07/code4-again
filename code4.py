{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4ff00470",
   "metadata": {},
   "outputs": [],
   "source": [
    "# celsius to fahrenheit\n",
    "def celsius_to_fahrenheit(celsius):\n",
    "    return (celsius * 9/5) + 32\n",
    "# fahrenheit to celsius\n",
    "def fahrenheit_to_celsius(fahrenheit):\n",
    "    return (fahrenheit - 32) * 5/9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c24a5896",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "choose the conversion direction.\n",
      "put C for celsius to fahrenheit or F for fahrenheit to celsius\n",
      "enter your choice: f\n",
      "enter the temperature: 120\n",
      "120.0 degrees fahrenheit is 48.888888888888886 degrees celsius\n"
     ]
    }
   ],
   "source": [
    "# setting dictionary to mapping the user input to the function\n",
    "conversion_features = {\n",
    "    'c': celsius_to_fahrenheit,\n",
    "    'f': fahrenheit_to_celsius\n",
    "}\n",
    "print(\"choose the conversion direction.\")\n",
    "print(\"put C for celsius to fahrenheit or F for fahrenheit to celsius\")\n",
    "choice = input(\"enter your choice: \").strip().lower()\n",
    "\n",
    "if choice in conversion_features: \n",
    "    temperature = float(input(\"enter the temperature: \"))\n",
    "    \n",
    "    # conversion\n",
    "    converted_temperature = conversion_features[choice](temperature)\n",
    "    \n",
    "    print(f\"{temperature} degrees {'celsius' if choice == 'c' else 'fahrenheit'} is {converted_temperature} degrees {'fahrenheit' if choice == 'c' else 'celsius'}\")\n",
    "else:\n",
    "          print(\"this was not a valid input. please enter a c or a f.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf4b17df",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
