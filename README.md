-# Shady Meadows Bed And Breakfast

This is automation tests projects

**To run allure report use terminal:** 


pytest --alluredir=/tmp/my_allure_results
or
pytest --alluredir=${HOME}/tmp/tmp_allure_dir_1
pytest --alluredir=${HOME}/tmp/tmp_allure_dir_1 --env="edge, chrome, firefox"
python -m pytest --alluredir=${HOME}/tmp/tmp_allure_dir_1


allure serve /tmp/my_allure_results
or 
allure serve ${HOME}/tmp/tmp_allure_dir_1
