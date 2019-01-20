# A.I. Blocker
* Ang Ming Liang, New Jun Jie, Chua Bing Quan, Toh Bing Cheng
### Applies adversarial patches and noise to reduce effectiveness of public machine learning scrapers and fight against modern invasion of data privacy.
## Problem
If you use social media, you should know about the 10-year challenge, where people compare profile pictures from 10 years ago and now. All these data, YOUR DATA, could be mined to train facial recognition algorithms on age progression and age recognition. Think of the mass data extraction of over 70 million US Facebook users during the Cambridge Analytica scandal. This is a major concern of data privacy.

## Solution
Our solution to this social problem is an A.I. Blocker, to trick the algorithms into thinking your photos mean something else. We present a Chrome extension that “masks” your photos, so that machine learning algorithms classify them wrongly, yet appear completely the same to the human eye.

## Technical Description
The user is given 2 choices: apply an Adversarial Patch to his/her image or evenly distribute Adversarial Noise across the image. For the first method, adversarial patch, the idea is to add a patch on the image that can cause a general object recognition classifer to misclassify an image.[2] The patch is made by applying expectation over transformation method over a random area of the image. While for adversarial noise, the extention makes qusai-impercetible changes to the image such that a machine learning model will classifiy it wrongly by using a single gradient ascent step also known as a fast signed gradient method.[3]  While both these approaches typically need a exisiting known neural network archiecture to compute their adversarial attack, they have been shown to work on black box neural networks archeictures as well. [3]

## Future Work
Our A.I. Blocker performs less effectively against some adversarial defenses, e.g. Robust Optimization and certificates.[4] To overcome this, we can apply 2nd-order gradient information in our future work to generate better-performing adversaries against these defenses. Furthermore, one feature that we did not manage to fully implement was universal adversarial defense which we can precompute and add to our images in a single constant time operation reducing our time complexity for the advsersarial step to an O(1) operation.[1] However this comes at the expense of less robust AI blocker. Besides improvements to adversarial noise approach, there are also possible improvements to be made for the adversarial patch approach. One such possible improvement can be the use of clever geometry to allow the patches to blend into the AI blocker more seemlessly such a frame around text. There are also software enginnering improvemenet to the backend that would reduce the number of times that tensorflow and VGG are loaded in. 

## Instructions
```
git clone https://github.com/bingcheng45/hnr-extension.git
cd ./hnr-extension
docker build -t Dockerfile .
```
## Examples
![ai blocker examples](https://user-images.githubusercontent.com/27071473/51434321-0e7a9780-1c99-11e9-93ee-48b866c292d9.png)

## References
1. "Universal Adversarial Perturbations." 9 Mar. 2017, https://arxiv.org/abs/1610.08401v3.
2. "Adversarial Patch." 27 Dec. 2017, https://arxiv.org/abs/1712.09665.
3. "Explaining and Harnessing Adversarial Examples." 20 Mar. 2015, https://arxiv.org/abs/1412.6572.
4. "Towards Deep Learning Models Resistant to Adversarial Attacks." 9 Nov. 2017, https://arxiv.org/abs/1706.06083.
