Enhusiast's intro to Probabilistic Programming <p>5th June 2014</p><p>Laszlo Fogas</p>
===============================================================================

---

Probabilistic?
==============

---

<s>"Works on my machine"</s>
============================

---

It is deterministic
===================

---

What is it used for?
====================

---

Predicting the probabilities of future outcomes
===============================================

---

Just like machine learning algoritmhs
=====================================

---

Unlike machine learning algorithms
==================================

---

Telling a plausible story is almost as important as being right
===============================================================


---

Random Forest
<img src="pics/tree.gif" alt="Drawing" style="width: 20%"/>

SVM
<img src="pics/svm.jpg" alt="Drawing" style="width: 20%"/>

Deep learning
<img src="pics/neurocat.jpg" alt="Drawing" style="width: 20%"/>

---

White box, we build probabilistic models of real world phenomenons
==================================================================

---

What is a probabilistic model?
==============================

---

Probability distribution of dice roll outcomes
==============================================
<img src="pics/dice.png" alt="Drawing" style="width: 80%"/>

---

Uniform distribtion
===================
<img src="pics/uniform.png" alt="Drawing" style="width: 80%"/>

---

Normal distribtion
==================
<img src="pics/normal.png" alt="Drawing" style="width: 80%"/>

---

An example 
==========

<img src="pics/texting.png" alt="Drawing" style="width: 90%"/>

---

The model
=========

<img src="pics/texting.png" alt="Drawing" style="width: 60%"/>

<img src="pics/poisson.png" alt="Drawing" style="width: 60%"/>

number of texts per day ~ Poisson(lambda)

switchpoint: tau ~ DiscreteUniform(1,70)

if t < tau: Poisson(lambda1)

if t > tau: Poisson(lambda2)

---

The model...
============

We don't know lambda1 or lambda2, we have only beliefs we have an idea about: continuous variable with expected value at the avg of all values

<img src="pics/exp.png" alt="Drawing" style="width: 60%"/>

lambda 1 ~ Exp(alfa)

lambda 2 ~ Exp(alfa)

---

Pymc
====

<img src="pics/pymc1.png" alt="Drawing" style="width: 80%"/>

<img src="pics/pymc2.png" alt="Drawing" style="width: 80%"/>

<img src="pics/pymc3.png" alt="Drawing" style="width: 80%"/>

<img src="pics/pymc4.png" alt="Drawing" style="width: 80%"/>

---

Posterior
=========

<img src="pics/posterior.png" alt="Drawing" style="width: 50%"/>

<img src="pics/posterior3.png" alt="Drawing" style="width: 50%"/>

---

Model as predictor
==================

<img src="pics/prediction.png" alt="Drawing" style="width: 80%"/>

---

Football model
==============

"Bayesian hierarchical model for the prediction of
football results" - Baio, Blangiardo

goals scored per team on a match ~ Poisson(teta)

home team goals ~ home + att_home + def_away

away team goals ~ att_away + def_home


home ~ Normal(0, 0.0001) att* ~ Normal(mu_att, tau_att) def* ~ Normal(mu_def, tau_def)
<br/>
mu_att ~ Normal(0, 0.0001) mu_def ~ Normal(0, 0.0001) tau_att ~ Gamma(0.1, 0.1) tau_def ~ Gamma(0.1, 0.1)

<img src="pics/hierarhical.png" alt="Drawing" style="width: 60%"/>

---

Football model...
=================

<img src="pics/goals.png" alt="Drawing" style="width: 80%"/>

http://discovery.ucl.ac.uk/16040/1/16040.pdf

---

Further reads
=============

Cam Davidson-Pilon: Probabilistic Programming & Bayesian Methods for Hackers
http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/
<img src="pics/bays.png" alt="Drawing" style="width: 10%"/>

John K. Kruschke: Doing Bayesian Data Analysis
<img src="pics/dogs.jpg" alt="Drawing" style="width: 10%"/>

Nate Silver: The signal and the noise
<img src="pics/signal.jpg" alt="Drawing" style="width: 10%"/>


