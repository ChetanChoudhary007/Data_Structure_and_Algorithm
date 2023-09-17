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


Problem 1: [countBits](countBits)
   - Description: Given an integer n, return an array of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
   - Difficulty: Easy.
   - Platform: `Leetcode`
   - Tags: `Array`
   - [Solution:1](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Arary_Easy/countBits.py)

Problem 2: [NextPermutation](NextPermutation)
   - Description: A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`
   - [Solution:2](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/next_permutation.py)

Problem 3: [RevreseInteger](reverseInteger)
   - Description: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^(31 - 1)],    then return 0.
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`
   - [Solution:3](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/reverse_number.py)
     
Problem 4: [MaximumSubarray](maximumSubarray)
   - Description: Given an integer array nums, find the subarray with the largest sum, and return its sum.
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`Kadane's Algorithm`
   - [Solution:4](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/maximum_subarray.py)

Problem 5: [SuperiorElements](superiorElements)
   - Description: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array
   - Difficulty: Easy
   - Platform: `Coding ninja`
   - Tags: `Array`,`Basic`
   - [Solution:5](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Arary_Easy/Superior_elements.py)


Problem 6: [3Sum](3Sum)
   - Description: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`Two pointer approach`
   - [Solution:6](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/3Sum.py)

Problem 7: [4Sum](4Sum)
   - Description:Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
a).0 <= a, b, c, d < n
b). a, b, c, and d are distinct.
c). nums[a] + nums[b] + nums[c] + nums[d] == target
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`Two pointer approach`
   - [Solution:7](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/4Sum.py)

Problem 8: [Search_2D_matrix](Search_2D_matrix)
   - Description: Given an integer target, return true if target is in matrix or false otherwise.
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`matrix undertanding`
   - [Solution:8](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/search2D_matrix.py)

Problem 9: [RotateMatrix](RotateMatrix)
   - Description: You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
      You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`matrix undertanding`
   - [Solution:9](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/Rotate_matrix.py)

Problem 10: [SpiralMatrix](SpiralMatrix)
   - Description: Given an m x n matrix, return all elements of the matrix in spiral order.

      eg: Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

          Output: [1,2,3,6,9,8,7,4,5]
     
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`
   - [Solution:10](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/Spiral_matrix.py)

Problem 11: [GenerateMatrix](GenerateMatrix)
   - Description: Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
     
     eg: Input: n = 3
     
         Output: [[1,2,3],[8,9,4],[7,6,5]]
     
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`Spiral matrix`
   - [Solution:11](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/Spiral_matrix_level2.py)


Problem 12: [setMatrixZeros](setMatrixZeros)
   - Description:Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
   You must do it in place.
     
   eg: Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
     
         Output: [[1,0,1],[0,0,0],[1,0,1]]
     
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`
   - [Solution:12](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/Set_matrix_0.py)

Problem 13: [SubarraySumEqualK](SubarraySumEqualK)
   - Description:Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
   A subarray is a contiguous non-empty sequence of elements within an array.
     
   
   eg: Input: nums = [1,1,1], k = 2
     
         Output: 2
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`,`presum concept`
   - [Solution:13](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/subarray_sum_equal_k.py)

Problem 14: [pascal'sTriangle](pascal'sTriangle)
   - Description: Given an integer numRows, return the first numRows of Pascal's triangle.
   
   
   eg: Input: numRows = 5
     
         Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
     
   - Difficulty: Easy
   - Platform: `Leetcode`,`Coding ninja`
   - Tags: `Array`,`Pascal's Triangle`,`Binomial coefficient concept`
   - [Solution:14](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Arary_Easy/pascalsTriangle.py)

Problem 15: [majorityElementII](majorityElementII)
   - Description: Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

   eg: Input: nums = [3,2,3]
     
         Output:[3]
   - Difficulty: Medium
   - Platform: `Leetcode`,`Coding ninja`
   - Tags: `Array`
   - [Solution:15](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/Majority_Element_II.py)

Problem 16: [twoSum](twoSum)
   - Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

   eg: Input: nums = [2,7,11,15], target = 9
     
         Output:[0,1]
         
   - Difficulty: Easy
   - Platform: `Leetcode`,`Coding ninja`
   - Tags: `Array`
   - [Solution:16](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Arary_Easy/TwoSum.py)

Problem 17: [container_With_Maximum_water](container_With_Maximum_water)
   - Description: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
              Return the maximum amount of water a container can store.

   eg: height = [1,8,6,2,5,4,8,3,7]
     
         Output: 49
         
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`
   - [Solution:17](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Array_medium/Container_with_maximum_water.py)

Problem 18: [rotateArray](rotateArray)

   - Description: Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


   eg: nums = [1,2,3,4,5,6,7], k = 3
     
         Output:[5,6,7,1,2,3,4]
         
   - Difficulty: Easy
   - Platform: `Leetcode`
   - Tags: `Array`
   - [Solution:18](https://github.com/ChetanChoudhary007/Data_Structure_and_Algorithm/blob/main/Arary_Easy/Rotate_array.py)

Problem 19: [sort_array_0,1,2](sort_array_0,1,2)

   - Description: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
     
   eg:    height = [1,8,6,2,5,4,8,3,7]

         Output:   49
     
   - Difficulty: Medium
   - Platform: `Leetcode`
   - Tags: `Array`
   - [Solution:19]



     
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
