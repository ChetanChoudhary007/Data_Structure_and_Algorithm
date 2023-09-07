# Data Structures and Algorithms Problems

This repository contains a collection of data structure and algorithm (DSA) problems, solutions, and explanations. It's designed to help you practice and improve your DSA skills.

## Table of Contents

- [Introduction](#introduction)
- [Problem List](#problem-list)
- [Solutions](#solutions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In this repository, you'll find a variety of DSA problems, including popular coding interview questions, algorithm challenges, and more. Each problem includes:

- A clear problem statement.
- Sample input and output.
- One or more solutions in various programming languages.

Feel free to explore the problems, attempt them on your own, and compare your solutions with the provided ones. This repository is a valuable resource for anyone preparing for technical interviews, competitive programming, or simply looking to strengthen their DSA skills.

## Problem List

Below is a list of DSA problems available in this repository:

1. Problem 1: [countBits](countBits)
   - Description: Given an integer n, return an array of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
   - Difficulty: Easy.
   - Platform: `Leetcode`
   - Tags: `Array`
   - [Solution:1](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Arary_Easy/countBits.py)

2. Problem 2: [NextPermutation](NextPermutation)
   - Description: A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`
   - [Solution:2](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/next_permutation.py)

3. Problem 3: [RevreseInteger](reverseInteger)
   - Description: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^(31 - 1)],    then return 0.
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`
   - [Solution:3](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/reverse_number.py)
     
4. Problem 4: [MaximumSubarray](maximumSubarray)
   - Description: Given an integer array nums, find the subarray with the largest sum, and return its sum.
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`Kadane's Algorithm`
   - [Solution:4](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/maximum_subarray.py)

5. Problem 5: [SuperiorElements](superiorElements)
   - Description: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array
   - Difficulty: Easy
   - Platform: `Coding ninja`
   - Tags: `Array`,`Basic`
   - [Solution:5](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Arary_Easy/Superior_elements.py)


6. Problem 6: [3Sum](3Sum)
   - Description: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`Two pointer approach`
   - [Solution:6](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/3Sum.py)

7. Problem 7: [4Sum](4Sum)
   - Description:Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
a).0 <= a, b, c, d < n
b). a, b, c, and d are distinct.
c). nums[a] + nums[b] + nums[c] + nums[d] == target
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`Two pointer approach`
   - [Solution:7](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/4Sum.py)

8. Problem 8: [Search_2D_matrix](Search_2D_matrix)
   - Description: Given an integer target, return true if target is in matrix or false otherwise.
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`matrix undertanding`
   - [Solution:8](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/search2D_matrix.py)

9. Problem 9: [RotateMatrix](RotateMatrix)
   - Description: You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
      You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`matrix undertanding`
   - [Solution:9](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/Rotate_matrix.py)

10. Problem 10: [SpiralMatrix](SpiralMatrix)
   - Description: Given an m x n matrix, return all elements of the matrix in spiral order.

      eg: Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

          Output: [1,2,3,6,9,8,7,4,5]
     
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`
   - [Solution:10](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/Spiral_matrix.py)

11. Problem 11: [GenerateMatrix](GenerateMatrix)
   - Description: Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
     
     eg: Input: n = 3
     
         Output: [[1,2,3],[8,9,4],[7,6,5]]
     
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`Spiral matrix`
   - [Solution:9](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/Spiral_matrix_level2.py)
     
<!-- Add more problems as needed -->

## Solutions

You can find solutions to the problems in this repository organized by programming language:

- [Python](python/) [for now only in this particular language]
- [Java](java/)
- [C++](cpp/)

Each language directory contains solutions to the problems in that language. Feel free to contribute your own solutions or improve existing ones.


## Contributing

Contributions are welcome! If you have additional problems, better solutions, or improvements to the existing content, please follow these guidelines:

1. Fork this repository.
2. Create a new branch for your changes.
3. Make your changes, ensuring code quality and documentation.
4. Test your solutions if applicable.
5. Commit your changes and push them to your fork.
6. Create a pull request to this repository's main branch.

## License
