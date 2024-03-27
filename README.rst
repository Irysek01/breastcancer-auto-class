.. raw:: html

   <table>
   <tr>
   <td>
   <img src="https://img.shields.io/github/languages/top/AstraBert/SacCerML" alt="GitHub top language">
   </td>
   <td>
   <img src="https://img.shields.io/github/commit-activity/t/AstraBert/simON-reads" alt="GitHub commit activity">
   </td>
   <td>
   <img src="https://img.shields.io/badge/Kaggle_Leaderboard-1st_place-green" alt="Static Badge">
   </td>
   <td>
   <img src="https://img.shields.io/badge/Test_evaluation-80_percent-orange" alt="Static Badge">
   </td>
   </tr>
   </table>


=======================
breastcancer-auto-class
=======================


Overview
========

This is BertGrisNald team's official repository for project building in the context of the academic code competition that is part of IUSS course *Machine Learning in Health Care* (a.y. 2023/24).

The goal of this project is to build a reliable, safe and scalable ML, DL or AI-based tool that is able to classify malignant and bening breast cancer images.

Find the Kaggle competition `at this link <https://www.kaggle.com/competitions/iuss-23-24-automatic-diagnosis-breast-cancer>`_.

Also find a more informal guide to this repository at `WELCOME.md <https://github.com/AstraBert/breastcancer-auto-class/blob/main/WELCOME.md>`

Repository structure
====================

- In `complete_set <https://github.com/AstraBert/breastcancer-auto-class/blob/main/complete_set>`_ you will find the complete sets of images, both the training and test
- In `scripts <https://github.com/AstraBert/breastcancer-auto-class/blob/main/scripts>`_ you will find *our* python scripts to build and finetune *our original* model
- In `foundation_model <https://github.com/AstraBert/breastcancer-auto-class/blob/main/foundation_model>`_ you will find *our* foundation model in :code:`-h5` format, which is an unsopported file type for GitHub or for any normal text editor, so you won't be able to see it
- In `proposed_models <https://github.com/AstraBert/breastcancer-auto-class/blob/main/proposed_models>`_ you will find a list of proposed models (based on IUSS course itself) with the scripts used to generate them, along with some other metadata


First steps
===========

Never or rarely coded in your life? There's absolutely no problem! 

You will be able to contribute to this repository just by following these steps:

1. Go to :menuselection:`Code<> > Codespaces`
2. Click on :guilabel:`Create codespace on main`
3. Patiently wait... This will take a while!

In the end, a development environment will show up: it will be identical to VSCode + Linux, so you will be able to do **literally everything**.

Try, for example, running a prediction with our DeepLearning foundation model, by opening your terminal with :command:`Ctrl + ò`: you will see a space on the bottom, where usually there is something like :code:`AstraBert@/workspace/breastcancer-auto-class$`.

Now type this instruction in the terminal, pressing :command:`Enter` afterwards. 

.. code-block:: bash

    python3 scripts/process.py -i P003.png


You should get out that the predicted class is :dfn:`Benign` (find out more `at this link <https://www.nationalbreastcancer.org/breast-tumors/>`_)

From this development environment, you could potentially do everything, but you should be careful with modifying files, adding things or deleting other stuff, because you need to know how to :guilabel:`Push` and :guilabel:`Pull` to a GitHub repository from a Codespace, which is not so easy, especially if you are a beginner!

Nevertheless, if you want to learn how to push and pull from Codespaces, please refer to `this link <https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace>`_.


Building the project
====================

Ok, now, what do we need in order to build the **"perfect"** model?

- Good data and code; we will have to experiment with several different models and build from there:
  1. :code:`scikit-learn` classical models: Decision Tree, Random Forest, SVM, KNN
  2. :code:`scikit-learn` neural network: :abbreviation:`MLP` (Multi Layers Perceptron)
  3. :code:`tensorflow-keras` neural network for image processing as suggested by Nicholas Renotte in his `youtube video <https://youtu.be/jztwpsIzEGc?feature=shared>`_
  4. :code:`huggingface-transformers`: we will be finetuning an Artificial Intelligence-based zero-shot image classifier provided by OpenAI named :guilabel:`clip-vit-base-patch16` (see it `here <https://huggingface.co/openai/clip-vit-base-patch16>`_)
- **BENCHMARKS**: benchmarking is essential to our puporses. We need to find the best ways to test and evaluate our models, in order to choose and submit the best ones
- Human assessment of test data (optional, but would be nice): it will be super useful if we were able to pre-classify test images as malignant or benign, in order to know how good our models are.

Contributors
============

- `Astra Bertelli <https://astrabert.vercel.app>`_: TBD
- `Claudio Grisorio <https://github.com/Clagriso>`_: TBD
- `Irene Naldoni <https://github.com/Irenenal>`_: TBD


Last dispositions
=================

Please, support this repository by leaving a ⭐!

Moreover, feel free to look at `Astra's GitHub account <https://github.com/AstraBert>`_ to explore what you can do with GitHub, and also to leave a ⭐ on her repositories, if you find any of them useful or interesting!


License and rights of usage 
===========================

This repository is hereby provided under MIT license (more at `LICENSE <https://github.com/AstraBert/breastcancer-auto-class/blob/main/LICENSE>_`).

If you use this work for your projects, please cite the authors (see under Contributors).

Model statistics
================
+---------------------------------------+-----------------------------+
|                                       | Eval on 25% of test dataset |
+=======================================+=============================+
| **DecisionTree Classifier**           | 0.80                        |
+---------------------------------------+-----------------------------+
| **Multi-Layer Perceptron Classifier** | 0.43                        |
+---------------------------------------+-----------------------------+
| **Deep Learning Classifier**          | 0.79                        |
+---------------------------------------+-----------------------------+
| **clip-vit-finetuned-breastcancer**   | 0.55                        |
+---------------------------------------+-----------------------------+
| **vit-base-finetuned-breastcancer**   | 0.71                        |
+---------------------------------------+-----------------------------+

References
==========

Christian Salvatore. (2024). Automatic Diagnosis of Breast Cancer | IUSS 23-24. Kaggle. https://kaggle.com/competitions/iuss-23-24-automatic-diagnosis-breast-cancer

