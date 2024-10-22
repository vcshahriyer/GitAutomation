# GitHub Automation Script

This is a Python script to automate The boring stuff 🚀.

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/vcshahriyer/GitAutomation) ![npm (scoped)](https://img.shields.io/npm/v/@shahriyer/gitautomation) [![GitHub license](https://img.shields.io/github/license/vcshahriyer/GitAutomation)](https://github.com/vcshahriyer/GitAutomation/blob/master/LICENSE)

## Installation

You may need the package [click](https://pypi.org/project/click/) to install click.

```bash
pip install click
```

## Alter Configurations

> In gitAutomate.py you can setup default variable at top starting with "\_"

```python
_remote = "your remote name"
```

## Usage

> Add gitAutomate.py at your project root and Update your gitignore

```
__pycache__
gitAutomate.py
```

> Run the gitAutomate.py from your project root ( **python -u .\gitAutomate.py** )

> You can run the script with choice & argument (remote)

```
python .\gitAutomate.py --choice=npr origin
```

![Commands](./assets/Annotation.jpg)

### <span style="color:#FFCC00">"Normal Push" includes 'git add' and 'git commit'<span></span>

## NPM package @shahriyer/gitautomation

`npm i @shahriyer/gitautomation`
install this package with npm and add a script command in your package.json file

```
"scripts": {
    "automate": "python .\\node_modules\\@shahriyer\\gitautomation\\gitAutomate.py"
  }
```

### and now you can run **" npm run automate "**

## Upcoming

Commands without changes (Clean working Dir) :

- ✅ Just create new Branch and pull-request.
- ✅ Just create pull-request.
- ✅ Prune local branches with the selected remote.
