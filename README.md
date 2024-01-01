# CAPTCHA Solver

`captchasolver` is a utility package designed to solve simple image-based CAPTCHAs given a trained model.

The trained model is based off of this [tutorial](https://keras.io/examples/vision/captcha_ocr/).

## Features

- Decode base64 encoded CAPTCHA images.
- Split CAPTCHA into individual characters.
- Predict characters using a pre-trained machine learning model.
- Easy-to-use interface for solving CAPTCHAs.

## Installation

```bash
git clone 
cd captchasolver
pip install.
```

## Usage

First import the package:

```python
from captchasolver import CAPTCHASolver
```

Then, create an instance of `CAPTCHASolver` and use it to solve CAPTCHAs:

```python
solver = CAPTCHASolver(model_path='path_to_your_model')
captcha_answer = solver.solve(encoded_image)
print("CAPTCHA Answer:", captcha_answer)
```

Here, `encoded_image` is a string containing the Base64 encoded CAPTCHA image.
