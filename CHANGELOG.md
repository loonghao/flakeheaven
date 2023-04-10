## 3.3.0 (2023-04-10)

### Feat

- Change default cache dir to workdir

## 3.2.1 (2022-11-04)

### Fix

- disable plugin execution when '-*' is used as exception

## 3.2.0 (2022-10-26)

### Feat

- **lint**: enable flag to check for missing plugins

## 3.1.0 (2022-10-25)

### Feat

- **logic**: Allow `base` config to use "~" (HOME)

## 3.0.0 (2022-08-01)

### Fix

- **plugins/pylint**: forward max_line_length to pylint plugin

### BREAKING CHANGE

- E0001 is no longer ignored

## 2.1.3 (2022-07-27)

### Fix

- **logic**: use deep update to ensure proper value overrides

## 2.1.2 (2022-07-26)

### Fix

- **logic/snapshot**: avoid file existence errors when preparing cache

## 2.1.1 (2022-07-25)

### Fix

- **patched**: use same config fields as tox

## 2.1.0 (2022-07-25)

### Feat

- **config**: config command

## 2.0.0 (2022-06-23)

### Fix

- **logic**: properly merge configs to avoid creating empty values

### BREAKING CHANGE

- Default plugins will now run when pyproject.toml exists without [tool.flakeheaven.plugins] section.

## 1.0.2 (2022-06-21)

### Fix

- add severity property to GitLab formatter output

## 1.0.1 (2022-05-25)

### Fix

- **exceptions-config**: flakeheaven/flakeheaven#74: fix exceptions ordering

## 1.0.0 (2022-05-24)

### Perf

- **import**: Import urllib3 only if needed (#81)

### Fix

- importlib-metadata requirement
- **patched**: re-enable --config cli arg
- **formatters**: use another plugin name colour
- **plugins**: increase max violation code length

### Feat

- Configurable cache timeout (#46)
- Use relative path (#41)

### Refactor

- drop support for flake8-strict

### BREAKING CHANGE

- Users should replace flake-strict rules with flake8-black

## 0.11.1 (2022-01-26)

### Fix

- **plugins**: use new pylint api
