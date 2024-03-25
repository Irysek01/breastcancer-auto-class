# breastcanc-auto-class

## Table of Contents
- [Overview](#overview)
- [Play around](#play-around)
- [Don't forget](#dont-forget)
- [Useful practices](#usefuls-practices)
- [PS](#ps)

## Overview

This repository serves as a checkpoint for code dumping and project building in the context of the academic code competition that is part of IUSS course _Machine Learning in Health Care_.

In [scripts](./scripts/) you will find:

- the [foundation model](./scripts/image_ml.py) we will use to build our perfect breast cancer automatic classifier:sunglasses:
- the [prediction script](./scripts/process.py) you can already use to play around a little bit with predictions

In [complete_set](./complete_set/) you will find training and test data.

In [models](./models/) you will find the model binary: it is an unsupported file format for visualization, so don't be worried if GitHub tells you it can't show it!

:warning: To be able to do **literally anything**, you need Linux! Don't have Linux? Take it easy and see how to enable Linux on your Windows PC [here](https://learn.microsoft.com/it-it/windows/wsl/install):coffee:

## Play around 
Wanna give the foundation model a try?

First of all, ensure to be in a Linux-like env (Debian or Ubuntu, preferably), than install git:

```bash
sudo apt-get update && sudo apt-get install git
```

After that, clone this repository:

```bash
git clone https://github.com/AstraBert/breastcanc-auto-class

cd breastcanc-auto-class
```

Install necessary dependencies (it will take a while and up to 1GB disk space... Brace yourself):

```bash
python3 -m pip install -r requirements.txt
```

And then run the prediction script like this:

```bash
python3 scripts/process.py -i P003.png
```

The predicted class should be "Malignant"... Did it work?:heart_eyes::grin:

## Don't forget
There are three rules while team-programming:

- **Always** share ideas: no matter how stupid they may sound in your head, your ideas can always be a valuable contribution to the project!
- Keep your teammates updated on your work
- Don't be afraid to ask if something is not clear or does not make sense!

Also, make sure to support this repository be living a little :star:!

Thanks:heart:

## Usefuls practices
There are two rules of common practice:

- Use Issues to flag problems or proposals when you can't speak to your mates face2face
- If you are working from remote, **always** PULL the repository before PUSHING any changes

## PS

- **Want to know how to write documents like this README?** Check out the [markdown cheat sheet](https://www.markdownguide.org/cheat-sheet/)
- **Feel free to take a look to [Astra's account](https://github.com/AstraBert) and repos and take inspiration!!!** (and maybe leave some stars to her repositories, please:kissing_smiling_eyes:)
- **Wanna see what was the inspiration for the foundation model?** Check out [Nicholas Renotte's video on YouTube](https://youtu.be/jztwpsIzEGc?feature=shared) or his repository [here on GitHub](https://github.com/nicknochnack/ImageClassification)
