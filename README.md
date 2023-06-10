Note: This work is contributed to the community by implementing a solution and
sharing it, long term maintainership is uncertain.

# tox-rye

Tox plugin to allow discovery of versions through [Rye][rye] - which can
supply an installed version or fetch if missing.

Currently supports version specs like: py39, cpython39, pypy39.

[rye]: https://rye-up.com

The main logic of the plugin is supplied by [virtualenv-rye-discovery](https://github.com/bluss/virtualenv-rye-discovery),
while this particular package makes sure the "rye_discovery" config is added to
tox to enable it all.

You need to **opt-in** to rye discovery per project by setting `rye_discovery = true`
in `tox.ini`.

## Example

Test the example in this repository. The rye project here has tox as a
dev-dependency for this demo. It will pull down the required versions
from Rye (see `tox.ini`).

1. Install Rye
2. `rye sync`
3. `rye run tox`

`tox.ini` includes the required `rye_discovery = true` config, which can be set
both in the `[tox]` section or per testenv.
