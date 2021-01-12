# Running Cypress
* open _cyp\cypress\integration\google.spec.js_
  * change value of _SRCH_STR_ to desired search item
* from root folder, cd into cyp
  * type _npx cypress open_
  * click on _google.spec.js_

# Running Pylenium
* from command line in root folder, type _python -m pytest pyl/tests/test_search.py -s_