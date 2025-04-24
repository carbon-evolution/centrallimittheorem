# Central Limit Theorem Demonstration

An interactive visualization tool to demonstrate the Central Limit Theorem using Python and Matplotlib.

## Overview

This program provides an interactive demonstration of the Central Limit Theorem (CLT), one of the most important concepts in statistics. The Central Limit Theorem states that, regardless of the original distribution's shape, the sampling distribution of the mean approaches a normal distribution as the sample size increases.

## Features

- Interactive visualization showing:
  - The original population distribution (which is non-normal)
  - Random sample from the population
  - Sampling distribution of means
- Adjustable parameters:
  - Population mean
  - Population standard deviation
- Real-time updates to see how changes affect the distributions

## Requirements

- Python 3.6+
- NumPy
- Matplotlib

## Usage

Run the program with:

```
python centrallimittheorem.py
```

## How It Works

1. The program generates a population with a non-normal distribution (mixture of normal and exponential)
2. It draws multiple random samples from this population
3. It calculates the mean of each sample
4. It plots the distribution of these sample means, which demonstrates the Central Limit Theorem

![image](https://github.com/user-attachments/assets/19147be4-afa5-45ad-a563-8ee0697fdb22)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
