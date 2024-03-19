# Challenge: Product Sales Analysis - ETL with Pandas, JSON and Parquet

### Goal:
- Given a JSON file containing product sales data, the challenge is to read the data, process it into a dictionary for analysis, and finally calculate and report total sales by product category.

- In this project we will add a logging treatment with Loguru

- 


### Flow:
![flow](/challenges/read_csv_json_with_quality/pics/flow.png)

## Thanks and Recommendation

I discovered this challenge through [Luciano Vasconcelos Filho](https://www.linkedin.com/in/lucianovasconcelosf/) bootcamp, I recommend the bootcamp to everyone who wants to learn more about Python and Data Engineering.

And this is his [repository](https://github.com/lvgalvao/One-Billion-Row-Challenge-Python) with the challenges

## How to run from Scratch
1. Configure the correct Python version with `pyenv`:

```bash
pyenv 3.11.5 installation
pyenv local 3.11.5
```

2. Configure poetry for Python version 3.11.5 and activate the virtual environment:

```bash
poetry env use 3.11.5
poetry shell
```

4. Install project dependencies:

```bash
poetry installation

or

pip freeze install requirements.txt
```