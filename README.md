#Chrome Extention Link : https://github.com/chuabingquan/ext
# A.I. Blocker
* Ang Ming Liang, New Jun Jie, Chua Bing Quan, Toh Bing Cheng
### Applies adversarial patches and noise to reduce effectiveness of public machine learning scrapers and fight against modern invasion of data privacy.
## Problem
If you use social media, you should know about the 10-year challenge, where people compare profile pictures from 10 years ago and now. All these data, YOUR DATA, could be mined to train facial recognition algorithms on age progression and age recognition. Think of the mass data extraction of over 70 million US Facebook users during the Cambridge Analytica scandal. This is a major concern of data privacy.

## Solution
Our solution to this social problem is an A.I. Blocker, to trick the algorithms into thinking your photos mean something else. We present a Chrome extension that “masks” your photos, so that machine learning algorithms classify them wrongly, yet appear completely the same to the human eye.

## Technical Description
The user is given 2 choices: apply an Adversarial Patch to his/her image or evenly distribute Adversarial Noise across the image. For the Adversarial Patch, the extension adds a patch on the image provided that causes a general object recognition classifier to misclassify an image.[2] The patch is made by applying expectation over transformation, over a random area of the image. For the Adversarial Noise, the extension makes quasi-imperceptible changes to the image such that a machine learning model classifies it incorrectly by using a single gradient ascent step, also know as a "fast gradient sign method".[3] While both approaches typically require a known existing neural network architecture to compute their adversarial attacks, a.k.a. a white box attack, they have been shown to work well on black box neural network architectures as well.[3]

## Future Work
Our A.I. Blocker performs less effectively against some adversarial defenses, e.g. Robust Optimization and certificates.[4] To overcome this, we can apply 2nd-order gradient information in our future work to generate better-performing adversaries against these defenses. One feature that we did not manage to fully implement was a Universal Adversarial Attack to pre-compute and transform the images in a O(1) constant-time operation for the adversarial step.[1] However, this comes at the expense of less robust A.I. Blocker. Other than improvements to the Adversarial Noise approach, there is also room for improvement for the Adversarial Patch approach. One such improvement can be the use of clever geometry to blend the patch into the image more seamlessly, such as an Adversarial Frame around text. There are also better software engineering practices to implement the backend to reduce the number of times that TensorFlow, VGG and DenseNet are loaded in.

## Instructions
```
git clone https://github.com/bingcheng45/hnr-extension.git
cd ./hnr-extension
docker build -t Dockerfile .
```
## Results
![ai blocker examples](https://user-images.githubusercontent.com/27071473/51434321-0e7a9780-1c99-11e9-93ee-48b866c292d9.png)

## References
1. "Universal Adversarial Perturbations." 9 Mar. 2017, https://arxiv.org/abs/1610.08401v3.
2. "Adversarial Patch." 27 Dec. 2017, https://arxiv.org/abs/1712.09665.
3. "Explaining and Harnessing Adversarial Examples." 20 Mar. 2015, https://arxiv.org/abs/1412.6572.
4. "Towards Deep Learning Models Resistant to Adversarial Attacks." 9 Nov. 2017, https://arxiv.org/abs/1706.06083.
