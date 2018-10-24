{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Prime numbers up to  5\n",
      "2\n",
      "3\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "#print first prime numbers in range between 2 and any number I wont .\n",
    "number = int(input(\"  Prime numbers up to  \")) \n",
    "for num in range(2,number + 1):\n",
    "       if num > 1:\n",
    "            for i in range(2,num):\n",
    "                if (num % i) == 0:\n",
    "                     break\n",
    "            else:\n",
    "                print(num)\n",
    "                \n",
    "                "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
