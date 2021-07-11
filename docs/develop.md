# Setup Dev Env
* install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)
* `conda create -y -n airbnb python=3.8`
* `conda activate airbnb`
* `pip install -r requirements.txt`
* (optional) `conda install nb_conda`
* `jupyter lab`
    * this should open your browser to jupyter lab page.
* refer to [Project Structure] about the purpose of each file.
* each notebook should be self explanatory, as they are all well commented and annotated within notebook.

# Project Structure
* `data`
    * `holsout`: this contains summary listing for 2021/03, which will be used to evaluate performance score.
    * `summary`: this contains summary listing before 2021/03, and can be merged to form our final training data.
* `merge_files.ipynb`: as downloaded raw data are multiple files, this notebook is for properly merging all dataset. It is a good idea to have this notebook separate from various training, and different method of training usual share from the same data source.
* `baseline.ipynb`: trains our baseline model with minimal feature engineering, perform cv grid search, and give holdout score.
* `betterFE.ipynb`: adding feature engineering concerning text processing and neighboring price effect. Model is trained similarly to baseline model
* `multi_model.ipynb`: trains multiple model based on segment, to facilitate insight and and optimization.
* `model`
    * `baseline_*.json`: this is the trained baseline model with minimal feature engineering
    * `betterfe_*.json`: this is the trained model based on more feature engineering concerning text and neighborhood effect.
    * `wordFreq.json`: this is a meta file used to accelerate feature engineering.
    * `multimodel_*`: this is a folder containiner a more advanced approach of training which will generate multiple models.

# gochas
* I was able to read all csv file for individual month successfully, but after merging them and writing the file, and reading the file back, pandas conplains about wrong csv format. The issue is solved by adding `quoting=csv.QUOTE_ALL` when I write the merged df to csv. The issue is most likely cause by text field and Chinese charater in name, host_name field.
* The reason why I choose not to containerize develop environment is that it gives me easy access to GPU, I was able to get GPU for xgb working easily this way. If develop does not have GPU enabled, plz remove the tree_method and gpu_id parameter to XGBRegressor parameter.
