## AV DataHack Slides using Jupyter Notebook + Reveal.js

__NOTE: These slides are prepared using [Dat Tran's](http://www.dat-tran.com/) github repo: [datitran/jupyter2slides](https://github.com/datitran/jupyter2slides). Visit the link to know more how to create those.__

### How to run the slides:
***
- Setup the conda environment using the `datahack.yml` file: `conda env create -f datahack.yml`
- `cd slides`
- Run the command: `python run.py --file ./static/datahack_slides_first_draft.slides.html`
- The `html slides` would be served at `localhost:9099`.
- And you are done with the above steps!

### If the above thing doesn't work:
- Open up the html file directly, there's still an issue related to cache when you continue to render it via Flask.
