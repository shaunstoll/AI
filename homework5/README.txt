Uriel (Shaun) Stoll
uds2104
homework5

Linear Regression:
Choice of 7 iterations with alpha = 0.58

First, I ran experimental values between 0.5 and 1 to find a learning rate that with a strictly decreaing R value. Since, through 100 iterations, 0.5 had a strictily decreasing R value, but 1 did not, I knew that there was a learning rate with 100 iterations that had a strictly decreasing R value between 0.5 and 1.
Next, I printed the R values after each iteration for alpha = 0.58 :

9.223372036854776e+18
0.5027097421665327
0.08755200770467643
0.015562643927093021
0.0028299132503184824
0.0005596818192365148
0.0001419398534522661

After just 7 iterations, the R value was already practically zero. So I decided to only keep 7 iterations.




Clustering:
The 3 k values that standout most are k=2, k=4, and k=9

With only 2 clusters, the image is roughly outlined between dark and light colors. Perhaps only the center tree is truly visible to someone who has never seen the original picture.
At k=4, we really begin to see color distinction besides different grays. The blue water versus the brown trees. 
By around k=9, the main details of the picture are  nearly fully formed. The ground is distinguishable from the trees and we can see grass and leaves.

I have attached 3 pdfs of the pictures for k=2, k=4, and k=9
