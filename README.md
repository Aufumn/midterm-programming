# CMPSC 202 - Midterm Programming Assignment

Name: Autumn

**Instructions**: Complete the exercise below. Open book, open notes, any tools allowed (except submitting another student's work). Due tonight (10/6) at 11:59pm.

**Submission**: Fork this repository and invite your professor (username: bcmullins) to the repository. To submit, push your code to your forked repository. Make sure to include your name in the README file.

You have been provided with a starter Python file (`midterm_starter.py`). This file contains two fully implemented algorithms that solve the exact same problem: finding if an array contains duplicate values.

The file also contains a `flawed_benchmark()` function. The developer who wrote this benchmark made several severe methodological errors, making the printed timing results completely unreliable for comparing the asymptotic growth of these two algorithms.

**Your tasks**: 

1. Rewrite the `flawed_benchmark()` function to provide a robust empirical comparison of the two algorithms. List the methodological errors in the original benchmark and explain how you fixed them. Your benchmark should demonstrate the scaling behavior of the two algorithms across multiple input sizes.

*list your methodological errors and fixes here*
Error 1 data generation was being timed so it was measuring random.randint as well as the algorithim itself. Fixed by building data before calling the function.
Error 2 Each algorithim had different data. data1 and data2 were seperate lists so the comparison wasn't equal. I fixed this by making both run on the same list.
Error 3 The distribution was skewed. The range (i, 10000) shifts with i, so values weren't drawn uniformly. random.sample gives clean unique values.
Error 4 There was only one input size. You are unable to show scaling with only n = 1000. The algorithim tests more input sizes to see the scale a bit better.
Error 5 The time function was not optimal as time.perf_counter() helps to time only the performance and it does a median of 7 runs. So now the function has a better time moduole.
Error 6 Garbage collection is not paused while timing this is fixed to to help with outside interference.

2. Run the empirical comparion and plot the results using a plotting library of your choice (e.g., `matplotlib`, `seaborn`, etc.). Include the plot in your submission called `results.png`. Be sure to label your axes and include a legend.

Check 
n	    slow (s)	fast (s)	speedup
250	  0.000746	0.000011	67x
500	  0.003644	0.000026	141x
1000	0.014765	0.000050	297x
2000	0.060046	0.000119	503x
4000	0.266793	0.000221	1208x



