# Project Overview
## Scenario
1. This project aims at forecasting Airbnb Taipei house listing price in future month.
2. When a new listing is created on the website, the model will forecast its listing price. The reasons for such a forecast are 2 fold:
    1. If user's listing price is higher or lower than the predicted listing price, certain campaign or action can be set for renter or property owner to facilitate transaction.
    2. If price is way off the predicted value, then anomolies happen. A special agent will be assigned to invetigate potential legal issue.

## Dataset
1. Data Download: [http://insideairbnb.com/get-the-data.html](http://insideairbnb.com/get-the-data.html)
2. Upon forecast, you may use all feature except the price feature belonging to the month of forecast (i.e. the only endogenous feature is pricing, while the rest can be freely treated as endogenous or exogenous depending on developer's own judgement).

# Devloper Guide
1. Refer [here](develop.md) for how to setup environment and continue development.
2. Refer to [project issues](https://github.com/schwannden/airbnb-taipei/issues) for idea bank, done trial and errors, and future todos.
    1. To know what's more urgent and needed to be done, view issue based on [milestone filter](https://github.com/schwannden/airbnb-taipei/milestones)
    2. To know what optimizations are still available, view issue based on [ds label](https://github.com/schwannden/airbnb-taipei/labels/ds)
3. Refer to [project wiki](https://github.com/schwannden/airbnb-taipei/wiki/Project-Insight) for insights obtained from done experiment. We have decided to use wiki to record project insight, as it does not require commit and pr, so is more light weight in document process.
