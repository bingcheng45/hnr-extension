# A.I. Blocker
* Ang Ming Liang, New Jun Jie, Chua Bing Quan, Toh Bing Cheng
### Applies adversarial patches and noise to reduce effectiveness of public machine learning scrapers and fight against modern invasion of data privacy.
## Problem
If you use social media, you should know about the 10-year challenge, where people compare profile pictures from 10 years ago and now. All these data, YOUR DATA, could be mined to train facial recognition algorithms on age progression and age recognition. Think of the mass data extraction of over 70 million US Facebook users during the Cambridge Analytica scandal. This is a major concern of data privacy.

## Solution
Our solution to this social problem is an A.I. Blocker, to trick the algorithms into thinking your photos mean something else. We present a Chrome extension that “masks” your photos, so that machine learning algorithms classify them wrongly, yet appear completely the same to the human eye.

## Technical Description
The user is given 2 choices: apply an Adversarial Patch to his/her image or evenly distribute Adversarial Noise across the image. The adversary makes minimal changes to the image such that it is classified wrongly by the model.

## Future Work
Our A.I. Blocker performs less effectively against some adversarial defenses, e.g. Robust Optimization. We intend to use 2nd-order information in our future work to generate better-performing adversaries against these defenses.

## Instructions
```
git clone https://github.com/bingcheng45/hnr-extension.git
cd ./hnr-extension
docker build -t Dockerfile .
```

## References
* "Universal Adversarial Perturbations." 9 Mar. 2017, https://arxiv.org/abs/1610.08401v3.
* "Adversarial Patch." 27 Dec. 2017, https://arxiv.org/abs/1712.09665.
* "Explaining and Harnessing Adversarial Examples." 20 Mar. 2015, https://arxiv.org/abs/1412.6572.
* "Towards Deep Learning Models Resistant to Adversarial Attacks." 9 Nov. 2017, https://arxiv.org/abs/1706.06083.
