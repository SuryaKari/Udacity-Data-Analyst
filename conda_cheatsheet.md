# Conda Terminal CheatSheet

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
