FROM python:3.9
COPY . /Dice_roll
WORKDIR /Dice_roll
CMD python Dice_roll.py
