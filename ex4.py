{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "There are 100 cars available.\n",
      "There are only 30 drivers available.\n",
      "There will be 70 empty cars today.\n",
      "We can transport 120.0 people today.\n",
      "We have 90 to carpool today.\n",
      "We need to put about 3.0 in each car.\n"
     ]
    }
   ],
   "source": [
    "cars = 100 #input 100 as cars \n",
    "space_in_a_car = 4.0#input 4.0 as space_in_a_car\n",
    "drivers = 30  #input 30 as drivers\n",
    "passengers = 90  #input 4.0 as space_in_a_car\n",
    "cars_not_driven = cars - drivers # input diffrerence of the cars - drivers as cars_not_driven\n",
    "cars_driven = drivers # input drivers as cars_driven \n",
    "carpool_capacity = cars_driven * space_in_a_car # input carpool_capacity as cars_driven* space_in_a_car\n",
    "average_passengers_per_car = passengers / cars_driven # input the average _passagers_per_cars as passengers over cars_drivers\n",
    "\n",
    "\n",
    "print(\"There are\", cars, \"cars available.\") #Print that # number of cars in middle of senstence.\n",
    "print(\"There are only\", drivers, \"drivers available.\") #Print that # number of drivers in middle of senstence.\n",
    "print(\"There will be\", cars_not_driven, \"empty cars today.\") #Print that # cars_not_drivens in middle of senstence.\n",
    "print(\"We can transport\", carpool_capacity, \"people today.\")  #Print that # cars_not_drivens in middle of senstence.\n",
    "print(\"We have\", passengers, \"to carpool today.\")  #Print that # passensers in middle of senstence.\n",
    "print(\"We need to put about\", average_passengers_per_car,\n",
    "      \"in each car.\")  #Print that # average_passengers_per_car in middle of senstence."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Study Drill\n",
    "# car_pool_capacity was not correct name."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "carpool_capacity is 120.0\n"
     ]
    }
   ],
   "source": [
    "#(1) \n",
    "cars = 100 #input 100 as cars \n",
    "space_in_a_car = 4.#input 4 as space_in_a_car\n",
    "drivers = 30  #input 30 as drivers\n",
    "passengers = 90  #input 4.0 as space_in_a_car\n",
    "cars_not_driven = cars - drivers # input diffrerence of the cars - drivers as cars_not_driven\n",
    "cars_driven = drivers # input drivers as cars_driven \n",
    "carpool_capacity = cars_driven * space_in_a_car # input carpool_capacity as cars_driven* space_in_a_car\n",
    "\n",
    "print (\"carpool_capacity is\",carpool_capacity)\n",
    "\n",
    "# Answer \n",
    "# No difference between 4 and 4.0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "i*j is 0.01\n"
     ]
    }
   ],
   "source": [
    "# (6)\n",
    "i = 1000\n",
    "j = 0.00001\n",
    "\n",
    "print(\"i*j is\", i*j )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
