# brain_age

This code comes from a RAMP challenge aiming to predict age from brain grey matter .
Aging is associated with is grey matter (GM) atrophy, each year, an adult lose
0.1% of GM. We try to learn a predictor of the chronological age (true age)
using GM measurements on the brain on a population of healthy control participants.

Such a predictor provides the expected **brain age** of a subject. Deviation from
this expected brain age indicates acceleration or slowdown of the aging process
which may be associated with a pathological neurobiological process or protective factor of aging.

## Installation

To ensure an isolated development environment, we recommend using a virtual environment (venv). Follow these steps to create your virtual environment and install the project dependencies:
1. Clone the repository
   ```bash
   git@github.com:samuel-LP/Predict-Age-From-Brain-Images.git
   cd Predict-Age-From-Brain-Images
   ```
2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate the virtual environment
  - On Windows : 
    ```bash
     \venv\Scripts\Activate
    ```
- On Linux/Mac
    ```bash
  source venv/bin/activate
    ```
4. Install the dependencies

```bash
pip install -r requirements.txt
```

## Project Structure
- **scripts**: The python script for downloading the datas
- **notebooks**: This folder contains Jupyter notebooks used for exploratory data analysis and all the models used in this project.
- **submissions**: This folder includes all the models we used for the submissions.
- **requirements**: The list of project dependencies.


## Authors

- [Samuel Launay Pariente](https://github.com/samuel-LP)
- [Samuel Baheux](https://github.com/SamuelBaheux)
- [Axel Fritz](https://github.com/AxelFritz1)
