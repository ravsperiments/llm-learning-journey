---
title: "Week 1–2: From Pixels to Perceptrons — Starting My AI Research Journey"
date: 2025-05-02
---

## 🚀 Why I'm Doing This

I've set myself a 52-week challenge: to go from working knowledge to research-level depth in AI. My goal is to clear an L1 AI researcher interview loop by May 2026. This blog tracks that journey — wins, stumbles, and everything in between.

As someone fascinated by radio astronomy, I also plan to fold that interest into AI projects over time — from detecting bursts in telescope signals to building simulations of how sensors interpret the sky.

---

## 🛠 What I Built So Far

**Week 1**: I trained a simple fully connected neural network in PyTorch to classify handwritten digits using the MNIST dataset.  
**Week 2**: I implemented a binary classifier (perceptron) using NumPy — visualizing decision boundaries and training it with sigmoid + cross-entropy loss.

Example:  
```python
z = np.dot(X, w) + b
y_pred = 1 / (1 + np.exp(-z))  # sigmoid
```

---

## 🧠 What I Learned

- Why we flatten a 28x28 image into a 784-dimensional vector
- What the weights and bias actually *do*
- Why stacking linear layers without activation functions is mathematically redundant
- How backpropagation flows gradients backward to update weights
- The role of loss functions like CrossEntropy in scoring predictions

---

## 😮 What Surprised Me

- Commenting out ReLU had little effect on accuracy in my small model — why?
- Backpropagation felt more intuitive after thinking of it as blame assignment
- Dot products suddenly made sense when I visualized how weights “listen” to input features

---

## 🔭 What’s Next

I’ll start implementing convolutional neural networks (CNNs) from scratch and then with PyTorch. I'm also planning to experiment with signal detection in radio astronomy as a side project.

If you’ve done something similar, or just enjoy watching someone slowly bend tensors to their will — follow along.

