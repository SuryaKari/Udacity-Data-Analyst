# Surya's Cheat Sheet to everything

The idea of this cheatsheet is to add anything to this that I might use as a reference in the future. 

## Conda Terminal CheatSheet

1. To install a package, type conda install package_name in your terminal.  **conda install numpy**
  
2. You can install multiple packages at the same time. **conda install numpy scipy pandas**

3. To uninstall, use **conda remove package_name**

4. To update a package **conda update package_name**

5. update all packages in an environment, which is often useful, **conda update --all**

6. you can try searching with **conda search search_term**  
  * Example : If you want to install Beautiful Soup, but you are not sure of the exact package name. So, you can try **conda search beautifulsoup**
  
7. To create an environment, use **conda create -n env_name list of packages** in your terminal
  * Example : **conda create -n my_env numpy**
  
8. You can specify which version of Python to install in the environment. This is useful when you're working with code in both Python 2.x and Python 3.x. To create an environment with a specific Python version, do something like **conda create -n py3 python=3** or **conda create -n py2 python=2**
  * Example : **conda create -n py python=3.3**

9. Once you have an environment created, use **source activate my_env**

10. When you're in the environment, you'll see the environment name in the terminal prompt. Something like **(my_env) ~ $**. The environment has only a few packages installed by default, plus the ones you installed when creating it. You can check this out with **conda list**. Installing packages in the environment is the same as before: **conda install package_name**. Only this time, the specific packages you install will only be available when you're in the environment. To leave the environment, type **source deactivate** (on OSX/Linux).

11. **Saving and loading environments**  
A really useful feature is sharing environments so others can install all the packages used in your code, with the correct versions. You can save the packages to a **YAML** file with **conda env export > environment.yaml**. The first part conda env export writes out all the packages in the environment, including the Python version.  
The second part of the export command, **> environment.yaml** writes the exported text to a YAML file environment.yaml. This file can now be shared and others will be able to create the same environment you used for the project.
  * Example : **conda env create -f environment.yaml**
  
12. If you forget what your environments are named, use **conda env list**

13. If there are environments you don't use anymore, **conda env remove -n env_name** will remove the specified environment

## MARKDOWN Shortcuts

1. Math expressions
You can create math expressions in Markdown cells using [LaTeX](http://data-blog.udacity.com/posts/2016/10/latex-primer/)   symbols. Notebooks use MathJax to render the LaTeX symbols as math symbols. To start math mode, wrap the LaTeX in dollar signs $y = mx + b$ for inline math. For a math block, use double dollar signs.  


**$$
y = \frac{a}{b+c}
$$**
  
This is a really useful feature, so if you don't have experience with [LaTeX](http://data-blog.udacity.com/posts/2016/10/latex-primer/)   please read this primer on using it to create math expressions.


## Jupyter Notebook Terminal Commands

After you have installed Anaconda and created a conda environment, you can use this to create a Jupyter notebook session 

1) To start a notebook server, enter **jupyter notebook** in your terminal or console. This will start the server in the directory you ran the command in. 

