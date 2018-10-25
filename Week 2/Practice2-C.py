{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "28.22222222222222\n",
      "10.0\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "module 'numpy' has no attribute 'stdev'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-f9297fab3b2b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m \u001b[0ma\u001b[0m \u001b[1;33m=\u001b[0m\u001b[0mnumpy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mstdev\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mexample_list\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     12\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mAttributeError\u001b[0m: module 'numpy' has no attribute 'stdev'"
     ]
    }
   ],
   "source": [
    "import numpy\n",
    "\n",
    "example_list = [23,76,97,28,10,8,2,4,6]\n",
    "\n",
    "x = numpy.mean(example_list)\n",
    "print(x)\n",
    "\n",
    "y = numpy.median(example_list)\n",
    "print(y)\n",
    "\n",
    "a =numpy.stdev(example_list)\n",
    "print(a)\n",
    "\n"
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
